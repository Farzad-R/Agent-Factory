"""
Test Script - Verify Tool System
Quick tests to ensure everything is working correctly
"""

from tool_manager import ToolManager
from ecommerce_tools import TOOL_REGISTRY, TOOL_CATEGORIES
import json


def test_tool_count():
    """Test: Verify we have exactly 70 tools"""
    print("\n🧪 Test 1: Tool Count")
    total_tools = len(TOOL_REGISTRY)
    print(f"   Expected: 70 tools")
    print(f"   Actual: {total_tools} tools")

    if total_tools == 70:
        print("   ✅ PASSED")
    else:
        print("   ❌ FAILED")

    return total_tools == 70


def test_category_distribution():
    """Test: Verify category distribution"""
    print("\n🧪 Test 2: Category Distribution")
    expected = {
        "inventory_management": 15,
        "customer_operations": 15,
        "order_processing": 15,
        "analytics_reporting": 13,
        "marketing_content": 12
    }

    passed = True
    for category, expected_count in expected.items():
        actual_count = len(TOOL_CATEGORIES[category])
        status = "✅" if actual_count == expected_count else "❌"
        print(f"   {status} {category}: {actual_count}/{expected_count}")

        if actual_count != expected_count:
            passed = False

    if passed:
        print("   ✅ PASSED")
    else:
        print("   ❌ FAILED")

    return passed


def test_schema_conversion():
    """Test: Verify schema conversion works"""
    print("\n🧪 Test 3: Schema Conversion")

    try:
        manager = ToolManager()

        # Test converting a few tools
        test_tools = ["check_stock", "process_refund", "create_order"]

        for tool_name in test_tools:
            schema = manager.convert_to_openai_schema(
                tool_name,
                TOOL_REGISTRY[tool_name][1]
            )

            # Verify schema structure
            assert "type" in schema
            assert "function" in schema
            assert "name" in schema["function"]
            assert "description" in schema["function"]
            assert "parameters" in schema["function"]

            print(f"   ✅ {tool_name}: Schema valid")

        print("   ✅ PASSED")
        return True

    except Exception as e:
        print(f"   ❌ FAILED: {str(e)}")
        return False


def test_chromadb_integration():
    """Test: Verify ChromaDB can store and retrieve tools"""
    print("\n🧪 Test 4: ChromaDB Integration")

    try:
        # Initialize with test collection
        manager = ToolManager(collection_name="test_tools",
                              persist_directory="./test_chroma_db")

        # Reset collection for clean test
        manager.reset_collection()

        # Add tools
        count = manager.add_tools_to_chromadb()
        print(f"   ✅ Added {count} tools to ChromaDB")

        # Verify count
        stored_count = manager.collection.count()
        assert stored_count == 70, f"Expected 70, got {stored_count}"
        print(f"   ✅ Verified {stored_count} tools in database")

        # Test retrieval
        query = "check inventory and reorder products"
        results = manager.retrieve_relevant_tools(query, n_results=5)

        assert len(results) > 0, "No results returned"
        assert len(results) <= 5, "Too many results returned"
        print(f"   ✅ Retrieved {len(results)} relevant tools")

        # Verify result structure
        first_tool = results[0]
        assert "function" in first_tool
        assert "name" in first_tool["function"]
        print(f"   ✅ Result structure valid: {first_tool['function']['name']}")

        print("   ✅ PASSED")
        return True

    except Exception as e:
        print(f"   ❌ FAILED: {str(e)}")
        return False


def test_category_retrieval():
    """Test: Verify category-based retrieval"""
    print("\n🧪 Test 5: Category-Based Retrieval")

    try:
        manager = ToolManager()

        # Test each category
        for category in TOOL_CATEGORIES.keys():
            tools = manager.get_tools_by_category(category)
            expected_count = len(TOOL_CATEGORIES[category])
            actual_count = len(tools)

            assert actual_count == expected_count, \
                f"{category}: Expected {expected_count}, got {actual_count}"

            print(f"   ✅ {category}: {actual_count} tools")

        print("   ✅ PASSED")
        return True

    except Exception as e:
        print(f"   ❌ FAILED: {str(e)}")
        return False


def test_tool_search():
    """Test: Verify tool search by name"""
    print("\n🧪 Test 6: Tool Name Search")

    try:
        manager = ToolManager()

        # Search for specific tools
        searches = [
            ("refund", ["process_refund"]),
            ("order", ["create_order", "cancel_order", "get_order_status"]),
            ("inventory", ["check_stock", "update_inventory"])
        ]

        for search_term, expected_tools in searches:
            results = manager.search_tools_by_name(search_term)
            result_names = [r["function"]["name"] for r in results]

            for expected in expected_tools:
                assert expected in result_names, \
                    f"Expected '{expected}' in search results for '{search_term}'"

            print(f"   ✅ Search '{search_term}': Found {len(results)} tools")

        print("   ✅ PASSED")
        return True

    except Exception as e:
        print(f"   ❌ FAILED: {str(e)}")
        return False


def run_all_tests():
    """Run all tests and report results"""
    print("="*70)
    print("  RUNNING TOOL SYSTEM TESTS")
    print("="*70)

    tests = [
        test_tool_count,
        test_category_distribution,
        test_schema_conversion,
        test_chromadb_integration,
        test_category_retrieval,
        test_tool_search
    ]

    results = []
    for test_func in tests:
        result = test_func()
        results.append(result)

    # Summary
    print("\n" + "="*70)
    print("  TEST SUMMARY")
    print("="*70)

    passed = sum(results)
    total = len(results)

    print(f"\n   Passed: {passed}/{total}")
    print(f"   Failed: {total - passed}/{total}")

    if passed == total:
        print("\n   🎉 ALL TESTS PASSED! System is ready to use.")
    else:
        print("\n   ⚠️  Some tests failed. Please review errors above.")

    print("\n" + "="*70)


if __name__ == "__main__":
    run_all_tests()
