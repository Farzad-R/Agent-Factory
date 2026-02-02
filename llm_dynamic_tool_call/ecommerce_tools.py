"""
E-commerce Platform Management Tools
70 tools across 5 categories for LLM agent demonstration
"""

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum


# ============================================================================
# CATEGORY 1: INVENTORY MANAGEMENT (15 tools)
# ============================================================================

class StockLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

def check_stock(product_id: str) -> Dict[str, Any]:
    """Check current stock level for a product"""
    return {"status": "success", "product_id": product_id, "stock": 150}

def update_inventory(product_id: str, quantity: int, operation: str = "add") -> Dict[str, Any]:
    """Update inventory quantity for a product (add or subtract)"""
    return {"status": "success", "product_id": product_id, "new_quantity": quantity}

def reorder_product(product_id: str, quantity: int, supplier_id: str) -> Dict[str, Any]:
    """Create a reorder request for a product from supplier"""
    return {"status": "success", "order_id": "PO-12345", "quantity": quantity}

def track_shipment(shipment_id: str) -> Dict[str, Any]:
    """Track the status and location of a shipment"""
    return {"status": "in_transit", "location": "Distribution Center", "eta": "2 days"}

def set_low_stock_alert(product_id: str, threshold: int) -> Dict[str, Any]:
    """Set automatic alert when product stock falls below threshold"""
    return {"status": "success", "alert_set": True, "threshold": threshold}

def get_inventory_report(category: Optional[str] = None, format: str = "json") -> Dict[str, Any]:
    """Generate inventory report for all products or specific category"""
    return {"status": "success", "total_items": 450, "report_format": format}

def transfer_stock(product_id: str, from_warehouse: str, to_warehouse: str, quantity: int) -> Dict[str, Any]:
    """Transfer stock between warehouses"""
    return {"status": "success", "transfer_id": "TR-98765"}

def audit_inventory(warehouse_id: str) -> Dict[str, Any]:
    """Perform inventory audit for a warehouse"""
    return {"status": "completed", "discrepancies": 3, "warehouse": warehouse_id}

def reserve_inventory(product_id: str, quantity: int, order_id: str) -> Dict[str, Any]:
    """Reserve inventory for a pending order"""
    return {"status": "reserved", "reservation_id": "RES-44556"}

def get_product_location(product_id: str) -> Dict[str, Any]:
    """Get warehouse location and bin number for a product"""
    return {"warehouse": "WH-01", "aisle": "A", "bin": "15", "shelf": "3"}

def batch_update_inventory(updates: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Update inventory for multiple products in one batch"""
    return {"status": "success", "updated_count": len(updates)}

def predict_stockout(product_id: str, days: int = 30) -> Dict[str, Any]:
    """Predict if product will stock out in given days based on sales velocity"""
    return {"will_stockout": True, "estimated_days": 12, "recommendation": "reorder"}

def get_supplier_inventory(supplier_id: str) -> Dict[str, Any]:
    """Check available inventory from a supplier"""
    return {"supplier": supplier_id, "available_products": 245, "lead_time_days": 7}

def set_reorder_point(product_id: str, reorder_quantity: int, reorder_level: int) -> Dict[str, Any]:
    """Set automatic reorder point for a product"""
    return {"status": "success", "reorder_level": reorder_level}

def get_dead_stock_report(days_threshold: int = 90) -> Dict[str, Any]:
    """Get report of products with no sales in specified days"""
    return {"status": "success", "dead_stock_items": 23, "total_value": 15000}


# ============================================================================
# CATEGORY 2: CUSTOMER OPERATIONS (15 tools)
# ============================================================================

def create_customer(name: str, email: str, phone: Optional[str] = None) -> Dict[str, Any]:
    """Create a new customer account"""
    return {"status": "success", "customer_id": "CUST-78901", "email": email}

def update_customer_profile(customer_id: str, field: str, value: str) -> Dict[str, Any]:
    """Update specific field in customer profile"""
    return {"status": "success", "customer_id": customer_id, "updated_field": field}

def get_customer_details(customer_id: str) -> Dict[str, Any]:
    """Retrieve complete customer profile and history"""
    return {"customer_id": customer_id, "name": "John Doe", "total_orders": 15, "lifetime_value": 2500}

def send_customer_notification(customer_id: str, message: str, channel: str = "email") -> Dict[str, Any]:
    """Send notification to customer via email, SMS, or push"""
    return {"status": "sent", "channel": channel, "message_id": "MSG-55443"}

def process_refund(order_id: str, amount: float, reason: str) -> Dict[str, Any]:
    """Process refund for an order"""
    return {"status": "processed", "refund_id": "REF-99887", "amount": amount}

def add_customer_note(customer_id: str, note: str, category: str = "general") -> Dict[str, Any]:
    """Add internal note to customer profile"""
    return {"status": "success", "note_id": "NOTE-33221"}

def get_customer_order_history(customer_id: str, limit: int = 10) -> Dict[str, Any]:
    """Retrieve customer's order history"""
    return {"customer_id": customer_id, "orders": [], "total_orders": 15}

def apply_customer_discount(customer_id: str, discount_code: str) -> Dict[str, Any]:
    """Apply discount code to customer account"""
    return {"status": "applied", "discount_percentage": 10, "valid_until": "2024-12-31"}

def update_customer_tier(customer_id: str, new_tier: str) -> Dict[str, Any]:
    """Update customer loyalty tier (bronze, silver, gold, platinum)"""
    return {"status": "success", "new_tier": new_tier, "benefits_unlocked": 5}

def merge_customer_accounts(primary_id: str, secondary_id: str) -> Dict[str, Any]:
    """Merge duplicate customer accounts"""
    return {"status": "merged", "primary_id": primary_id, "orders_transferred": 8}

def get_customer_lifetime_value(customer_id: str) -> Dict[str, Any]:
    """Calculate customer lifetime value and metrics"""
    return {"ltv": 2500, "avg_order_value": 166, "frequency": 15}

def block_customer(customer_id: str, reason: str) -> Dict[str, Any]:
    """Block customer account for fraud or policy violation"""
    return {"status": "blocked", "reason": reason, "can_appeal": True}

def create_customer_support_ticket(customer_id: str, issue: str, priority: str = "medium") -> Dict[str, Any]:
    """Create support ticket for customer issue"""
    return {"status": "created", "ticket_id": "TICK-66554", "priority": priority}

def get_customer_preferences(customer_id: str) -> Dict[str, Any]:
    """Get customer communication and product preferences"""
    return {"email_subscribed": True, "sms_subscribed": False, "favorite_categories": ["electronics"]}

def award_loyalty_points(customer_id: str, points: int, reason: str) -> Dict[str, Any]:
    """Award loyalty points to customer"""
    return {"status": "success", "total_points": 1500, "points_added": points}


# ============================================================================
# CATEGORY 3: ORDER PROCESSING (15 tools)
# ============================================================================

def create_order(customer_id: str, items: List[Dict[str, Any]], shipping_address: str) -> Dict[str, Any]:
    """Create a new order for a customer"""
    return {"status": "success", "order_id": "ORD-11223", "total": 299.99}

def cancel_order(order_id: str, reason: str) -> Dict[str, Any]:
    """Cancel an existing order"""
    return {"status": "cancelled", "order_id": order_id, "refund_initiated": True}

def get_order_status(order_id: str) -> Dict[str, Any]:
    """Get current status of an order"""
    return {"order_id": order_id, "status": "shipped", "tracking_number": "TRK-998877"}

def update_order_status(order_id: str, new_status: str) -> Dict[str, Any]:
    """Update order status (pending, processing, shipped, delivered)"""
    return {"status": "success", "order_id": order_id, "new_status": new_status}

def calculate_shipping_cost(order_id: str, shipping_method: str, destination: str) -> Dict[str, Any]:
    """Calculate shipping cost for an order"""
    return {"shipping_cost": 15.99, "method": shipping_method, "estimated_days": 3}

def apply_discount_code(order_id: str, discount_code: str) -> Dict[str, Any]:
    """Apply discount code to an order"""
    return {"status": "applied", "discount_amount": 25.00, "new_total": 274.99}

def split_order(order_id: str, item_groups: List[List[str]]) -> Dict[str, Any]:
    """Split order into multiple shipments"""
    return {"status": "split", "new_order_ids": ["ORD-11223-A", "ORD-11223-B"]}

def process_payment(order_id: str, payment_method: str, amount: float) -> Dict[str, Any]:
    """Process payment for an order"""
    return {"status": "success", "transaction_id": "TXN-77665", "amount": amount}

def validate_order(order_id: str) -> Dict[str, Any]:
    """Validate order details (inventory, address, payment)"""
    return {"valid": True, "issues": [], "ready_to_ship": True}

def get_order_invoice(order_id: str, format: str = "pdf") -> Dict[str, Any]:
    """Generate and retrieve order invoice"""
    return {"status": "success", "invoice_url": "https://invoices.example.com/inv-123", "format": format}

def add_items_to_order(order_id: str, items: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Add additional items to existing order"""
    return {"status": "success", "items_added": len(items), "new_total": 349.99}

def remove_items_from_order(order_id: str, item_ids: List[str]) -> Dict[str, Any]:
    """Remove items from existing order"""
    return {"status": "success", "items_removed": len(item_ids), "new_total": 249.99}

def update_shipping_address(order_id: str, new_address: str) -> Dict[str, Any]:
    """Update shipping address for an order"""
    return {"status": "success", "order_id": order_id, "address_updated": True}

def reschedule_delivery(order_id: str, new_date: str) -> Dict[str, Any]:
    """Reschedule delivery date for an order"""
    return {"status": "rescheduled", "new_delivery_date": new_date}

def mark_order_as_gift(order_id: str, gift_message: Optional[str] = None) -> Dict[str, Any]:
    """Mark order as gift with optional message"""
    return {"status": "success", "gift_wrap_added": True, "gift_message": gift_message}


# ============================================================================
# CATEGORY 4: ANALYTICS & REPORTING (13 tools)
# ============================================================================

def generate_sales_report(start_date: str, end_date: str, granularity: str = "daily") -> Dict[str, Any]:
    """Generate sales report for date range"""
    return {"status": "success", "total_sales": 125000, "orders": 450, "avg_order_value": 278}

def get_customer_analytics(metric: str, time_period: str = "30d") -> Dict[str, Any]:
    """Get customer analytics (acquisition, retention, churn)"""
    return {"metric": metric, "value": 245, "change_percentage": 12.5}

def forecast_inventory_demand(product_id: str, days: int = 30) -> Dict[str, Any]:
    """Forecast product demand for future period"""
    return {"product_id": product_id, "predicted_demand": 450, "confidence": 0.85}

def generate_revenue_dashboard(date: str) -> Dict[str, Any]:
    """Generate comprehensive revenue dashboard"""
    return {"total_revenue": 15000, "orders": 75, "avg_cart_value": 200, "top_products": []}

def get_product_performance(product_id: str, days: int = 30) -> Dict[str, Any]:
    """Get product performance metrics"""
    return {"units_sold": 120, "revenue": 5400, "return_rate": 2.5, "avg_rating": 4.5}

def analyze_cart_abandonment(time_period: str = "7d") -> Dict[str, Any]:
    """Analyze cart abandonment rate and reasons"""
    return {"abandonment_rate": 68.5, "total_carts": 230, "completed": 72}

def get_top_selling_products(category: Optional[str] = None, limit: int = 10) -> Dict[str, Any]:
    """Get top selling products overall or by category"""
    return {"status": "success", "products": [], "time_period": "30d"}

def calculate_profit_margin(product_id: Optional[str] = None, category: Optional[str] = None) -> Dict[str, Any]:
    """Calculate profit margin for product or category"""
    return {"margin_percentage": 35.5, "gross_profit": 15000, "revenue": 42000}

def get_customer_segmentation_report() -> Dict[str, Any]:
    """Get customer segmentation analysis (RFM, behavioral)"""
    return {"segments": {"high_value": 120, "at_risk": 45, "new": 200}}

def analyze_return_rate(time_period: str = "30d", category: Optional[str] = None) -> Dict[str, Any]:
    """Analyze product return rate and reasons"""
    return {"return_rate": 3.2, "total_returns": 24, "top_reasons": ["size", "defect"]}

def get_conversion_funnel(start_date: str, end_date: str) -> Dict[str, Any]:
    """Get conversion funnel analytics"""
    return {"visits": 10000, "carts": 2000, "checkouts": 800, "purchases": 600}

def compare_period_performance(period1: str, period2: str, metric: str) -> Dict[str, Any]:
    """Compare performance metrics between two time periods"""
    return {"period1_value": 15000, "period2_value": 18000, "change_percentage": 20}

def get_channel_attribution_report(order_id: Optional[str] = None) -> Dict[str, Any]:
    """Get marketing channel attribution for sales"""
    return {"channels": {"organic": 40, "paid": 35, "email": 15, "social": 10}}


# ============================================================================
# CATEGORY 5: MARKETING & CONTENT (12 tools)
# ============================================================================

def create_marketing_campaign(name: str, channel: str, budget: float, duration_days: int) -> Dict[str, Any]:
    """Create new marketing campaign"""
    return {"status": "created", "campaign_id": "CAMP-55443", "budget": budget}

def send_email_blast(segment: str, subject: str, template_id: str) -> Dict[str, Any]:
    """Send bulk email to customer segment"""
    return {"status": "scheduled", "recipients": 1500, "send_time": "2024-01-30 10:00"}

def update_product_description(product_id: str, description: str) -> Dict[str, Any]:
    """Update product description and details"""
    return {"status": "success", "product_id": product_id, "updated": True}

def schedule_social_post(platform: str, content: str, scheduled_time: str) -> Dict[str, Any]:
    """Schedule social media post"""
    return {"status": "scheduled", "platform": platform, "post_id": "POST-88776"}

def create_discount_campaign(code: str, percentage: float, valid_until: str, conditions: Dict[str, Any]) -> Dict[str, Any]:
    """Create discount code campaign"""
    return {"status": "created", "code": code, "discount": percentage}

def analyze_campaign_performance(campaign_id: str) -> Dict[str, Any]:
    """Get campaign performance metrics"""
    return {"clicks": 2500, "conversions": 125, "roi": 3.5, "cost_per_acquisition": 25}

def create_product_bundle(name: str, product_ids: List[str], discount: float) -> Dict[str, Any]:
    """Create product bundle with discount"""
    return {"status": "created", "bundle_id": "BNDL-33221", "products": len(product_ids)}

def update_pricing(product_id: str, new_price: float, sale_price: Optional[float] = None) -> Dict[str, Any]:
    """Update product pricing"""
    return {"status": "success", "product_id": product_id, "new_price": new_price}

def create_abandoned_cart_campaign(hours_threshold: int = 24) -> Dict[str, Any]:
    """Create automated abandoned cart recovery campaign"""
    return {"status": "active", "target_carts": 150, "estimated_recovery": "15%"}

def generate_product_recommendations(customer_id: str, limit: int = 5) -> Dict[str, Any]:
    """Generate personalized product recommendations"""
    return {"customer_id": customer_id, "recommendations": [], "algorithm": "collaborative_filtering"}

def update_seo_metadata(product_id: str, title: str, keywords: List[str], description: str) -> Dict[str, Any]:
    """Update product SEO metadata"""
    return {"status": "success", "product_id": product_id, "indexed": True}

def create_loyalty_program_tier(tier_name: str, min_spend: float, benefits: List[str]) -> Dict[str, Any]:
    """Create or update loyalty program tier"""
    return {"status": "created", "tier": tier_name, "min_spend": min_spend}


# ============================================================================
# PYDANTIC SCHEMAS FOR TOOL CONVERSION
# ============================================================================

# We'll create Pydantic models for each tool's parameters
# This allows automatic conversion to JSON schema for LLM function calling

class CheckStockInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")

class UpdateInventoryInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")
    quantity: int = Field(description="Quantity to add or subtract")
    operation: str = Field(default="add", description="Operation type: 'add' or 'subtract'")

class ReorderProductInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")
    quantity: int = Field(description="Quantity to reorder")
    supplier_id: str = Field(description="Supplier identifier")

class TrackShipmentInput(BaseModel):
    shipment_id: str = Field(description="Shipment tracking identifier")

class SetLowStockAlertInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")
    threshold: int = Field(description="Minimum quantity threshold for alert")

class GetInventoryReportInput(BaseModel):
    category: Optional[str] = Field(default=None, description="Product category to filter by")
    format: str = Field(default="json", description="Report format: json, csv, or pdf")

class TransferStockInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")
    from_warehouse: str = Field(description="Source warehouse ID")
    to_warehouse: str = Field(description="Destination warehouse ID")
    quantity: int = Field(description="Quantity to transfer")

class AuditInventoryInput(BaseModel):
    warehouse_id: str = Field(description="Warehouse identifier to audit")

class ReserveInventoryInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")
    quantity: int = Field(description="Quantity to reserve")
    order_id: str = Field(description="Order ID for reservation")

class GetProductLocationInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")

class BatchUpdateInventoryInput(BaseModel):
    updates: List[Dict[str, Any]] = Field(description="List of inventory updates")

class PredictStockoutInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")
    days: int = Field(default=30, description="Number of days to predict")

class GetSupplierInventoryInput(BaseModel):
    supplier_id: str = Field(description="Supplier identifier")

class SetReorderPointInput(BaseModel):
    product_id: str = Field(description="Unique identifier for the product")
    reorder_quantity: int = Field(description="Quantity to order when reorder point is reached")
    reorder_level: int = Field(description="Stock level that triggers reorder")

class GetDeadStockReportInput(BaseModel):
    days_threshold: int = Field(default=90, description="Days without sales to consider dead stock")

# Customer Operations Schemas
class CreateCustomerInput(BaseModel):
    name: str = Field(description="Customer full name")
    email: str = Field(description="Customer email address")
    phone: Optional[str] = Field(default=None, description="Customer phone number")

class UpdateCustomerProfileInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    field: str = Field(description="Field name to update")
    value: str = Field(description="New value for the field")

class GetCustomerDetailsInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")

class SendCustomerNotificationInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    message: str = Field(description="Notification message")
    channel: str = Field(default="email", description="Communication channel: email, sms, or push")

class ProcessRefundInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    amount: float = Field(description="Refund amount")
    reason: str = Field(description="Reason for refund")

class AddCustomerNoteInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    note: str = Field(description="Note content")
    category: str = Field(default="general", description="Note category")

class GetCustomerOrderHistoryInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    limit: int = Field(default=10, description="Maximum number of orders to return")

class ApplyCustomerDiscountInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    discount_code: str = Field(description="Discount code to apply")

class UpdateCustomerTierInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    new_tier: str = Field(description="New loyalty tier: bronze, silver, gold, or platinum")

class MergeCustomerAccountsInput(BaseModel):
    primary_id: str = Field(description="Primary customer account ID to keep")
    secondary_id: str = Field(description="Secondary customer account ID to merge")

class GetCustomerLifetimeValueInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")

class BlockCustomerInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    reason: str = Field(description="Reason for blocking")

class CreateCustomerSupportTicketInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    issue: str = Field(description="Issue description")
    priority: str = Field(default="medium", description="Ticket priority: low, medium, or high")

class GetCustomerPreferencesInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")

class AwardLoyaltyPointsInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    points: int = Field(description="Points to award")
    reason: str = Field(description="Reason for awarding points")

# Order Processing Schemas
class CreateOrderInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    items: List[Dict[str, Any]] = Field(description="List of items in order")
    shipping_address: str = Field(description="Shipping address")

class CancelOrderInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    reason: str = Field(description="Cancellation reason")

class GetOrderStatusInput(BaseModel):
    order_id: str = Field(description="Order identifier")

class UpdateOrderStatusInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    new_status: str = Field(description="New order status")

class CalculateShippingCostInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    shipping_method: str = Field(description="Shipping method: standard, express, or overnight")
    destination: str = Field(description="Destination address or zip code")

class ApplyDiscountCodeInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    discount_code: str = Field(description="Discount code to apply")

class SplitOrderInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    item_groups: List[List[str]] = Field(description="Groups of items for separate shipments")

class ProcessPaymentInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    payment_method: str = Field(description="Payment method: card, paypal, etc.")
    amount: float = Field(description="Payment amount")

class ValidateOrderInput(BaseModel):
    order_id: str = Field(description="Order identifier")

class GetOrderInvoiceInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    format: str = Field(default="pdf", description="Invoice format: pdf or html")

class AddItemsToOrderInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    items: List[Dict[str, Any]] = Field(description="Items to add")

class RemoveItemsFromOrderInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    item_ids: List[str] = Field(description="Item IDs to remove")

class UpdateShippingAddressInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    new_address: str = Field(description="New shipping address")

class RescheduleDeliveryInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    new_date: str = Field(description="New delivery date (YYYY-MM-DD)")

class MarkOrderAsGiftInput(BaseModel):
    order_id: str = Field(description="Order identifier")
    gift_message: Optional[str] = Field(default=None, description="Optional gift message")

# Analytics & Reporting Schemas
class GenerateSalesReportInput(BaseModel):
    start_date: str = Field(description="Report start date (YYYY-MM-DD)")
    end_date: str = Field(description="Report end date (YYYY-MM-DD)")
    granularity: str = Field(default="daily", description="Data granularity: hourly, daily, weekly, or monthly")

class GetCustomerAnalyticsInput(BaseModel):
    metric: str = Field(description="Metric to analyze: acquisition, retention, or churn")
    time_period: str = Field(default="30d", description="Time period: 7d, 30d, 90d, etc.")

class ForecastInventoryDemandInput(BaseModel):
    product_id: str = Field(description="Product identifier")
    days: int = Field(default=30, description="Days to forecast")

class GenerateRevenueDashboardInput(BaseModel):
    date: str = Field(description="Dashboard date (YYYY-MM-DD)")

class GetProductPerformanceInput(BaseModel):
    product_id: str = Field(description="Product identifier")
    days: int = Field(default=30, description="Number of days to analyze")

class AnalyzeCartAbandonmentInput(BaseModel):
    time_period: str = Field(default="7d", description="Time period to analyze")

class GetTopSellingProductsInput(BaseModel):
    category: Optional[str] = Field(default=None, description="Product category filter")
    limit: int = Field(default=10, description="Number of products to return")

class CalculateProfitMarginInput(BaseModel):
    product_id: Optional[str] = Field(default=None, description="Specific product ID")
    category: Optional[str] = Field(default=None, description="Product category")

class GetCustomerSegmentationReportInput(BaseModel):
    pass  # No parameters needed

class AnalyzeReturnRateInput(BaseModel):
    time_period: str = Field(default="30d", description="Time period to analyze")
    category: Optional[str] = Field(default=None, description="Product category filter")

class GetConversionFunnelInput(BaseModel):
    start_date: str = Field(description="Start date (YYYY-MM-DD)")
    end_date: str = Field(description="End date (YYYY-MM-DD)")

class ComparePeriodPerformanceInput(BaseModel):
    period1: str = Field(description="First period (e.g., '2024-01' or '2024-01-01:2024-01-31')")
    period2: str = Field(description="Second period to compare")
    metric: str = Field(description="Metric to compare: sales, orders, revenue, etc.")

class GetChannelAttributionReportInput(BaseModel):
    order_id: Optional[str] = Field(default=None, description="Specific order ID to analyze")

# Marketing & Content Schemas
class CreateMarketingCampaignInput(BaseModel):
    name: str = Field(description="Campaign name")
    channel: str = Field(description="Marketing channel: email, social, paid_search, etc.")
    budget: float = Field(description="Campaign budget")
    duration_days: int = Field(description="Campaign duration in days")

class SendEmailBlastInput(BaseModel):
    segment: str = Field(description="Customer segment to target")
    subject: str = Field(description="Email subject line")
    template_id: str = Field(description="Email template identifier")

class UpdateProductDescriptionInput(BaseModel):
    product_id: str = Field(description="Product identifier")
    description: str = Field(description="New product description")

class ScheduleSocialPostInput(BaseModel):
    platform: str = Field(description="Social platform: facebook, twitter, instagram, etc.")
    content: str = Field(description="Post content")
    scheduled_time: str = Field(description="Scheduled post time (ISO format)")

class CreateDiscountCampaignInput(BaseModel):
    code: str = Field(description="Discount code")
    percentage: float = Field(description="Discount percentage")
    valid_until: str = Field(description="Expiration date (YYYY-MM-DD)")
    conditions: Dict[str, Any] = Field(description="Discount conditions and rules")

class AnalyzeCampaignPerformanceInput(BaseModel):
    campaign_id: str = Field(description="Campaign identifier")

class CreateProductBundleInput(BaseModel):
    name: str = Field(description="Bundle name")
    product_ids: List[str] = Field(description="List of product IDs in bundle")
    discount: float = Field(description="Bundle discount percentage")

class UpdatePricingInput(BaseModel):
    product_id: str = Field(description="Product identifier")
    new_price: float = Field(description="New regular price")
    sale_price: Optional[float] = Field(default=None, description="Optional sale price")

class CreateAbandonedCartCampaignInput(BaseModel):
    hours_threshold: int = Field(default=24, description="Hours after abandonment to trigger")

class GenerateProductRecommendationsInput(BaseModel):
    customer_id: str = Field(description="Customer identifier")
    limit: int = Field(default=5, description="Number of recommendations")

class UpdateSEOMetadataInput(BaseModel):
    product_id: str = Field(description="Product identifier")
    title: str = Field(description="SEO title")
    keywords: List[str] = Field(description="SEO keywords")
    description: str = Field(description="SEO meta description")

class CreateLoyaltyProgramTierInput(BaseModel):
    tier_name: str = Field(description="Tier name")
    min_spend: float = Field(description="Minimum spend to qualify")
    benefits: List[str] = Field(description="List of tier benefits")


# ============================================================================
# TOOL REGISTRY - Maps function names to their schemas and functions
# ============================================================================

TOOL_REGISTRY = {
    # Inventory Management
    "check_stock": (check_stock, CheckStockInput),
    "update_inventory": (update_inventory, UpdateInventoryInput),
    "reorder_product": (reorder_product, ReorderProductInput),
    "track_shipment": (track_shipment, TrackShipmentInput),
    "set_low_stock_alert": (set_low_stock_alert, SetLowStockAlertInput),
    "get_inventory_report": (get_inventory_report, GetInventoryReportInput),
    "transfer_stock": (transfer_stock, TransferStockInput),
    "audit_inventory": (audit_inventory, AuditInventoryInput),
    "reserve_inventory": (reserve_inventory, ReserveInventoryInput),
    "get_product_location": (get_product_location, GetProductLocationInput),
    "batch_update_inventory": (batch_update_inventory, BatchUpdateInventoryInput),
    "predict_stockout": (predict_stockout, PredictStockoutInput),
    "get_supplier_inventory": (get_supplier_inventory, GetSupplierInventoryInput),
    "set_reorder_point": (set_reorder_point, SetReorderPointInput),
    "get_dead_stock_report": (get_dead_stock_report, GetDeadStockReportInput),
    
    # Customer Operations
    "create_customer": (create_customer, CreateCustomerInput),
    "update_customer_profile": (update_customer_profile, UpdateCustomerProfileInput),
    "get_customer_details": (get_customer_details, GetCustomerDetailsInput),
    "send_customer_notification": (send_customer_notification, SendCustomerNotificationInput),
    "process_refund": (process_refund, ProcessRefundInput),
    "add_customer_note": (add_customer_note, AddCustomerNoteInput),
    "get_customer_order_history": (get_customer_order_history, GetCustomerOrderHistoryInput),
    "apply_customer_discount": (apply_customer_discount, ApplyCustomerDiscountInput),
    "update_customer_tier": (update_customer_tier, UpdateCustomerTierInput),
    "merge_customer_accounts": (merge_customer_accounts, MergeCustomerAccountsInput),
    "get_customer_lifetime_value": (get_customer_lifetime_value, GetCustomerLifetimeValueInput),
    "block_customer": (block_customer, BlockCustomerInput),
    "create_customer_support_ticket": (create_customer_support_ticket, CreateCustomerSupportTicketInput),
    "get_customer_preferences": (get_customer_preferences, GetCustomerPreferencesInput),
    "award_loyalty_points": (award_loyalty_points, AwardLoyaltyPointsInput),
    
    # Order Processing
    "create_order": (create_order, CreateOrderInput),
    "cancel_order": (cancel_order, CancelOrderInput),
    "get_order_status": (get_order_status, GetOrderStatusInput),
    "update_order_status": (update_order_status, UpdateOrderStatusInput),
    "calculate_shipping_cost": (calculate_shipping_cost, CalculateShippingCostInput),
    "apply_discount_code": (apply_discount_code, ApplyDiscountCodeInput),
    "split_order": (split_order, SplitOrderInput),
    "process_payment": (process_payment, ProcessPaymentInput),
    "validate_order": (validate_order, ValidateOrderInput),
    "get_order_invoice": (get_order_invoice, GetOrderInvoiceInput),
    "add_items_to_order": (add_items_to_order, AddItemsToOrderInput),
    "remove_items_from_order": (remove_items_from_order, RemoveItemsFromOrderInput),
    "update_shipping_address": (update_shipping_address, UpdateShippingAddressInput),
    "reschedule_delivery": (reschedule_delivery, RescheduleDeliveryInput),
    "mark_order_as_gift": (mark_order_as_gift, MarkOrderAsGiftInput),
    
    # Analytics & Reporting
    "generate_sales_report": (generate_sales_report, GenerateSalesReportInput),
    "get_customer_analytics": (get_customer_analytics, GetCustomerAnalyticsInput),
    "forecast_inventory_demand": (forecast_inventory_demand, ForecastInventoryDemandInput),
    "generate_revenue_dashboard": (generate_revenue_dashboard, GenerateRevenueDashboardInput),
    "get_product_performance": (get_product_performance, GetProductPerformanceInput),
    "analyze_cart_abandonment": (analyze_cart_abandonment, AnalyzeCartAbandonmentInput),
    "get_top_selling_products": (get_top_selling_products, GetTopSellingProductsInput),
    "calculate_profit_margin": (calculate_profit_margin, CalculateProfitMarginInput),
    "get_customer_segmentation_report": (get_customer_segmentation_report, GetCustomerSegmentationReportInput),
    "analyze_return_rate": (analyze_return_rate, AnalyzeReturnRateInput),
    "get_conversion_funnel": (get_conversion_funnel, GetConversionFunnelInput),
    "compare_period_performance": (compare_period_performance, ComparePeriodPerformanceInput),
    "get_channel_attribution_report": (get_channel_attribution_report, GetChannelAttributionReportInput),
    
    # Marketing & Content
    "create_marketing_campaign": (create_marketing_campaign, CreateMarketingCampaignInput),
    "send_email_blast": (send_email_blast, SendEmailBlastInput),
    "update_product_description": (update_product_description, UpdateProductDescriptionInput),
    "schedule_social_post": (schedule_social_post, ScheduleSocialPostInput),
    "create_discount_campaign": (create_discount_campaign, CreateDiscountCampaignInput),
    "analyze_campaign_performance": (analyze_campaign_performance, AnalyzeCampaignPerformanceInput),
    "create_product_bundle": (create_product_bundle, CreateProductBundleInput),
    "update_pricing": (update_pricing, UpdatePricingInput),
    "create_abandoned_cart_campaign": (create_abandoned_cart_campaign, CreateAbandonedCartCampaignInput),
    "generate_product_recommendations": (generate_product_recommendations, GenerateProductRecommendationsInput),
    "update_seo_metadata": (update_seo_metadata, UpdateSEOMetadataInput),
    "create_loyalty_program_tier": (create_loyalty_program_tier, CreateLoyaltyProgramTierInput),
}

# Category mapping for tools
TOOL_CATEGORIES = {
    "inventory_management": [
        "check_stock", "update_inventory", "reorder_product", "track_shipment",
        "set_low_stock_alert", "get_inventory_report", "transfer_stock", "audit_inventory",
        "reserve_inventory", "get_product_location", "batch_update_inventory",
        "predict_stockout", "get_supplier_inventory", "set_reorder_point", "get_dead_stock_report"
    ],
    "customer_operations": [
        "create_customer", "update_customer_profile", "get_customer_details",
        "send_customer_notification", "process_refund", "add_customer_note",
        "get_customer_order_history", "apply_customer_discount", "update_customer_tier",
        "merge_customer_accounts", "get_customer_lifetime_value", "block_customer",
        "create_customer_support_ticket", "get_customer_preferences", "award_loyalty_points"
    ],
    "order_processing": [
        "create_order", "cancel_order", "get_order_status", "update_order_status",
        "calculate_shipping_cost", "apply_discount_code", "split_order", "process_payment",
        "validate_order", "get_order_invoice", "add_items_to_order", "remove_items_from_order",
        "update_shipping_address", "reschedule_delivery", "mark_order_as_gift"
    ],
    "analytics_reporting": [
        "generate_sales_report", "get_customer_analytics", "forecast_inventory_demand",
        "generate_revenue_dashboard", "get_product_performance", "analyze_cart_abandonment",
        "get_top_selling_products", "calculate_profit_margin", "get_customer_segmentation_report",
        "analyze_return_rate", "get_conversion_funnel", "compare_period_performance",
        "get_channel_attribution_report"
    ],
    "marketing_content": [
        "create_marketing_campaign", "send_email_blast", "update_product_description",
        "schedule_social_post", "create_discount_campaign", "analyze_campaign_performance",
        "create_product_bundle", "update_pricing", "create_abandoned_cart_campaign",
        "generate_product_recommendations", "update_seo_metadata", "create_loyalty_program_tier"
    ]
}