# E-Commerce Tools Overview

## What These Tools Represent

These are 70 realistic e-commerce platform management tools organized into 5 functional categories. They represent the kind of tool ecosystem you'd find in a real production system - think Shopify, Amazon Seller Central, or any modern e-commerce platform where you need to manage inventory, handle customer requests, process orders, analyze data, and run marketing campaigns.

## The 5 Categories

**1. Inventory Management (15 tools)**
- Stock checking, reordering, warehouse transfers
- Low stock alerts, supplier management
- Inventory forecasting and auditing

**2. Customer Operations (15 tools)**
- Customer account management, profile updates
- Refund processing, support tickets
- Loyalty programs, notifications

**3. Order Processing (15 tools)**
- Order creation, cancellation, status updates
- Shipping calculations, payment processing
- Invoice generation, delivery scheduling

**4. Analytics & Reporting (13 tools)**
- Sales reports, revenue dashboards
- Customer analytics, cart abandonment analysis
- Performance metrics, profit margins

**5. Marketing & Content (12 tools)**
- Campaign creation, email blasts
- Social media scheduling, discount codes
- Product descriptions, pricing updates

## Important Details

### They're Mock Functions
The tools don't actually connect to real systems - they return dummy responses like `{"status": "success", "order_id": "ORD-123"}`. This is intentional. We're testing **tool selection**, not tool execution. The LLM just needs to pick the right tools, not actually process orders.

### Pydantic Schemas Included
Every tool has a proper Pydantic schema that defines its parameters, types, and descriptions. These schemas are automatically converted to OpenAI function calling format, making them ready to use with GPT-4, GPT-4o-mini, or any LLM that supports function calling.

### Category Overlap is Intentional
Some queries naturally need tools from multiple categories (like "analyze cart abandonment and create recovery campaign" needs both analytics and marketing). This cross-category requirement is a real-world challenge that exposes weaknesses in category-based routing.

### Naming Conventions
Tool names are clear and descriptive:
- Action verbs: `create_`, `update_`, `get_`, `process_`
- Domain context: `customer_`, `order_`, `inventory_`
- No ambiguity: `update_pricing` vs `update_product_description`