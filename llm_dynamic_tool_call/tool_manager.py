"""
ChromaDB Tool Manager
Stores tool descriptions in ChromaDB and retrieves relevant tools based on query similarity
"""

import chromadb
from chromadb.config import Settings
import json
from typing import List, Dict, Any
from ecommerce_tools import TOOL_REGISTRY, TOOL_CATEGORIES


class ToolManager:
    """Manages tool storage and retrieval using ChromaDB"""

    def __init__(self, collection_name: str = "ecommerce_tools", persist_directory: str = "./chroma_db"):
        """
        Initialize ChromaDB client and collection

        Args:
            collection_name: Name of the ChromaDB collection
            persist_directory: Directory to persist the database
        """
        self.client = chromadb.PersistentClient(path=persist_directory)

        # Create or get collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"description": "E-commerce platform tools"}
        )

    def convert_to_openai_schema(self, tool_name: str, pydantic_model) -> Dict[str, Any]:
        """
        Convert Pydantic model to OpenAI function calling schema

        Args:
            tool_name: Name of the tool
            pydantic_model: Pydantic model class for the tool

        Returns:
            OpenAI-compatible function schema
        """
        func, model = TOOL_REGISTRY[tool_name]

        # Get the function docstring as description
        description = func.__doc__.strip(
        ) if func.__doc__ else f"Execute {tool_name}"

        # Convert Pydantic model to JSON schema
        schema = model.model_json_schema()

        # Build OpenAI function format
        openai_schema = {
            "type": "function",
            "function": {
                "name": tool_name,
                "description": description,
                "parameters": {
                    "type": "object",
                    "properties": schema.get("properties", {}),
                    "required": schema.get("required", [])
                }
            }
        }

        return openai_schema

    def get_tool_category(self, tool_name: str) -> str:
        """Get the category of a tool"""
        for category, tools in TOOL_CATEGORIES.items():
            if tool_name in tools:
                return category
        return "uncategorized"

    def add_tools_to_chromadb(self):
        """
        Add all tools to ChromaDB with their descriptions and metadata
        This should be run once to populate the database
        """
        documents = []
        metadatas = []
        ids = []

        for tool_name in TOOL_REGISTRY.keys():
            func, model = TOOL_REGISTRY[tool_name]
            schema = self.convert_to_openai_schema(tool_name, model)

            # Create a rich text description for embedding
            # This includes function name, description, and parameter details
            description = schema["function"]["description"]
            params = schema["function"]["parameters"]["properties"]

            # Build searchable text
            param_descriptions = []
            for param_name, param_info in params.items():
                param_desc = f"{param_name}: {param_info.get('description', '')}"
                param_descriptions.append(param_desc)

            searchable_text = f"{tool_name}. {description}. Parameters: {', '.join(param_descriptions)}"

            # Store in lists for batch insertion
            documents.append(searchable_text)
            metadatas.append({
                "tool_name": tool_name,
                "category": self.get_tool_category(tool_name),
                "description": description,
                # Store full schema as JSON string
                "schema": json.dumps(schema)
            })
            ids.append(tool_name)

        # Add all tools to ChromaDB in batch
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

        print(f"✓ Added {len(documents)} tools to ChromaDB")
        return len(documents)

    def retrieve_relevant_tools(self, query: str, n_results: int = 15) -> List[Dict[str, Any]]:
        """
        Retrieve the most relevant tools for a given query

        Args:
            query: User's task/query description
            n_results: Number of tools to retrieve (default: 15)

        Returns:
            List of OpenAI-compatible function schemas for relevant tools
        """
        # Query ChromaDB for similar tools
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results
        )

        # Extract and parse tool schemas
        relevant_tools = []

        if results['ids'] and len(results['ids']) > 0:
            for metadata in results['metadatas'][0]:
                schema = json.loads(metadata['schema'])
                relevant_tools.append(schema)

        return relevant_tools

    def get_tools_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Get all tools from a specific category

        Args:
            category: Category name (inventory_management, customer_operations, etc.)

        Returns:
            List of OpenAI-compatible function schemas for tools in category
        """
        if category not in TOOL_CATEGORIES:
            raise ValueError(
                f"Category '{category}' not found. Available: {list(TOOL_CATEGORIES.keys())}")

        tool_names = TOOL_CATEGORIES[category]
        tools = []

        for tool_name in tool_names:
            schema = self.convert_to_openai_schema(
                tool_name, TOOL_REGISTRY[tool_name][1])
            tools.append(schema)

        return tools

    def get_all_tools(self) -> List[Dict[str, Any]]:
        """
        Get all tools as OpenAI-compatible schemas

        Returns:
            List of all tool schemas
        """
        tools = []
        for tool_name in TOOL_REGISTRY.keys():
            schema = self.convert_to_openai_schema(
                tool_name, TOOL_REGISTRY[tool_name][1])
            tools.append(schema)
        return tools

    def search_tools_by_name(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Search tools by name (useful for debugging)

        Args:
            search_term: Term to search in tool names

        Returns:
            List of matching tool schemas
        """
        matching_tools = []
        for tool_name in TOOL_REGISTRY.keys():
            if search_term.lower() in tool_name.lower():
                schema = self.convert_to_openai_schema(
                    tool_name, TOOL_REGISTRY[tool_name][1])
                matching_tools.append(schema)
        return matching_tools

    def get_collection_stats(self) -> Dict[str, Any]:
        """Get statistics about the tool collection"""
        count = self.collection.count()

        # Count tools per category
        category_counts = {}
        for category, tools in TOOL_CATEGORIES.items():
            category_counts[category] = len(tools)

        return {
            "total_tools": count,
            "categories": category_counts,
            "collection_name": self.collection.name
        }

    def reset_collection(self):
        """Delete and recreate the collection (useful for testing)"""
        self.client.delete_collection(name=self.collection.name)
        self.collection = self.client.get_or_create_collection(
            name=self.collection.name,
            metadata={"description": "E-commerce platform tools"}
        )
        print(f"✓ Collection '{self.collection.name}' reset")


# ============================================================================
# HELPER FUNCTIONS FOR QUICK USAGE
# ============================================================================

def initialize_tool_database(persist_directory: str = "./chroma_db") -> ToolManager:
    """
    Initialize and populate the tool database
    Run this once to set up ChromaDB with all tools

    Args:
        persist_directory: Directory to store ChromaDB data

    Returns:
        Initialized ToolManager instance
    """
    print("Initializing Tool Database...")
    manager = ToolManager(persist_directory=persist_directory)

    # Check if collection is empty
    if manager.collection.count() == 0:
        print("Populating database with tools...")
        manager.add_tools_to_chromadb()
    else:
        print(f"Database already contains {manager.collection.count()} tools")

    # Print stats
    stats = manager.get_collection_stats()
    print(f"\n📊 Database Statistics:")
    print(f"   Total tools: {stats['total_tools']}")
    print(f"   Categories:")
    for category, count in stats['categories'].items():
        print(f"      - {category}: {count} tools")

    return manager


def demo_tool_retrieval(manager: ToolManager):
    """
    Demonstrate tool retrieval with sample queries

    Args:
        manager: Initialized ToolManager instance
    """
    print("\n" + "="*70)
    print("DEMO: Tool Retrieval Examples")
    print("="*70)

    test_queries = [
        "I need to check if a product is in stock and reorder if needed",
        "A customer wants a refund for their order",
        "Show me sales analytics for last month",
        "Create a marketing campaign and send emails to customers",
        "Process a new order and calculate shipping costs"
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n{'─'*70}")
        print(f"Query {i}: {query}")
        print(f"{'─'*70}")

        relevant_tools = manager.retrieve_relevant_tools(query, n_results=5)

        print(f"Top 5 relevant tools:")
        for j, tool in enumerate(relevant_tools, 1):
            tool_name = tool['function']['name']
            tool_desc = tool['function']['description']
            category = manager.get_tool_category(tool_name)
            print(f"  {j}. {tool_name} [{category}]")
            print(f"     → {tool_desc}")


if __name__ == "__main__":
    # Initialize the tool database
    manager = initialize_tool_database()

    # Run demo
    demo_tool_retrieval(manager)

    print("\n" + "="*70)
    print("✓ Tool database ready for use!")
    print("="*70)
