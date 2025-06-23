from agents.sentiment_agent import analyze_sentiment, TicketInput
from agents.router_agent import route_ticket, RoutingInput
from test_cases import TEST_TICKETS

def process_ticket(ticket: dict):
    sentiment_data = analyze_sentiment(TicketInput(subject=ticket["subject"], message=ticket["message"]))

    routing_data = RoutingInput(
        customer_tier=ticket["customer_tier"],
        sentiment=sentiment_data.sentiment,
        urgency=sentiment_data.urgency,
        previous_tickets=ticket["previous_tickets"],
        monthly_revenue=ticket["monthly_revenue"],
        account_age_days=ticket["account_age_days"]
    )

    route = route_ticket(routing_data)

    print(f"\nTicket ID: {ticket['ticket_id']}")
    print(f"Subject: {ticket['subject']}")
    print(f"Sentiment: {sentiment_data.sentiment}, Urgency: {sentiment_data.urgency}")
    print(f"Suggested Route: {route.route}")
    print("—" * 40)

if __name__ == "__main__":
    for ticket in TEST_TICKETS:
        process_ticket(ticket)