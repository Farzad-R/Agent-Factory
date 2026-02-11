"""
Setup and Demo Script
Run this to initialize the database and see examples of tool retrieval
"""

from tool_manager import ToolManager, initialize_tool_database
from ecommerce_tools import TOOL_REGISTRY, TOOL_CATEGORIES
import json


def print_section(title: str):
    """Print a formatted section header"""
    print("\n" + "="*80)
    print(f"  {title}")
    print("="*80)


def display_tool_details(tool_schema: dict):
    """Pretty print a tool schema"""
    func_info = tool_schema['function']
    print(f"\n📦 Tool: {func_info['name']}")
    print(f"   Description: {func_info['description']}")
    print(f"   Parameters:")

    params = func_info['parameters']['properties']
    required = func_info['parameters'].get('required', [])

    for param_name, param_info in params.items():
        required_marker = " (required)" if param_name in required else " (optional)"
        print(
            f"      • {param_name}{required_marker}: {param_info.get('description', 'No description')}")


def main():
    """Main setup and demo function"""

    print_section("E-COMMERCE TOOL MANAGEMENT SYSTEM")
    print("\nThis demo shows how to manage 70 tools using ChromaDB for retrieval")

    # Initialize database
    print_section("STEP 1: Initialize Tool Database")
    manager = initialize_tool_database()

    # Show category breakdown
    print_section("STEP 2: Tool Categories Overview")
    for category, tools in TOOL_CATEGORIES.items():
        print(f"\n📁 {category.replace('_', ' ').title()}: {len(tools)} tools")
        print(f"   Sample tools: {', '.join(tools[:3])}")

    # Demonstrate retrieval by query
    print_section("STEP 3: Retrieve Tools by Query (Semantic Search)")

    sample_queries = [
        "I need to handle a customer refund request",
        "Check inventory levels and reorder products",
        "Generate monthly sales and revenue reports",
    ]

    for query in sample_queries:
        print(f"\n🔍 Query: '{query}'")
        relevant_tools = manager.retrieve_relevant_tools(query, n_results=3)
        print(f"   → Retrieved {len(relevant_tools)} most relevant tools:")
        for tool in relevant_tools:
            print(f"      • {tool['function']['name']}")

    # Demonstrate category-based retrieval
    print_section("STEP 4: Retrieve Tools by Category")

    category = "order_processing"
    print(f"\n📂 Getting all tools from '{category}' category...")
    category_tools = manager.get_tools_by_category(category)
    print(f"   → Found {len(category_tools)} tools")
    print(
        f"   → Tool names: {[t['function']['name'] for t in category_tools[:5]]}...")

    # Show a detailed tool example
    print_section("STEP 5: Detailed Tool Schema Example")

    print("\nExample: Let's look at the 'process_refund' tool in detail:")
    refund_tools = manager.search_tools_by_name("process_refund")
    if refund_tools:
        display_tool_details(refund_tools[0])

    # Demonstrate getting all tools (the naive approach)
    print_section("STEP 6: All Tools (Naive Approach - NOT RECOMMENDED)")

    all_tools = manager.get_all_tools()
    print(f"\n⚠️  Total tools: {len(all_tools)}")
    print(f"   This would pass ALL {len(all_tools)} tools to the LLM")
    print(f"   Token usage would be very high and tool selection poor!")

    # Show comparison
    print_section("COMPARISON: Different Approaches")

    comparison_data = [
        ("Naive (All Tools)", len(all_tools), "Poor", "Very High"),
        ("Category-Based", 15, "Good", "Medium"),
        ("Query Retrieval", 10, "Excellent", "Low"),
    ]

    print(f"\n{'Approach':<25} {'# Tools':<12} {'Selection':<12} {'Token Usage'}")
    print("-" * 70)
    for approach, num_tools, selection, tokens in comparison_data:
        print(f"{approach:<25} {num_tools:<12} {selection:<12} {tokens}")

    # Final recommendations
    print_section("RECOMMENDATIONS")

    recommendations = [
        "✓ Use query-based retrieval for dynamic, user-driven tasks",
        "✓ Use category-based retrieval when you have a router/classifier",
        "✓ Limit tools to 10-15 per LLM call for best performance",
        "✓ Combine approaches: route to category, then retrieve top-k within category",
        "✗ Avoid passing all 70 tools to the LLM at once"
    ]

    for rec in recommendations:
        print(f"\n{rec}")

    print_section("SETUP COMPLETE!")

    print("\n✅ Your tool database is ready to use!")
    print("\nNext steps:")
    print("   1. Check out the notebooks for implementation examples")
    print("   2. Run example agents with different tool selection strategies")
    print("   3. Compare performance between naive, category, and retrieval approaches")
    print("\n")


if __name__ == "__main__":
    main()
