from pydantic import BaseModel

class RoutingInput(BaseModel):
    customer_tier: str
    sentiment: str
    urgency: str
    previous_tickets: int
    monthly_revenue: int
    account_age_days: int

class RoutingOutput(BaseModel):
    route: str

def route_ticket(data: RoutingInput) -> RoutingOutput:
    if data.customer_tier == "enterprise" and data.urgency == "urgent":
        return RoutingOutput(route="Escalation")
    elif data.customer_tier == "free" and data.sentiment == "angry":
        return RoutingOutput(route="Retention Team")
    elif data.sentiment == "angry" or data.urgency == "urgent":
        return RoutingOutput(route="Tech Support")
    elif data.customer_tier in ["premium", "enterprise"]:
        return RoutingOutput(route="Customer Success")
    else:
        return RoutingOutput(route="Tech Support")