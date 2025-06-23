from agents.sentiment_agent import analyze_sentiment, TicketInput
from agents.router_agent import route_ticket, RoutingInput
from test_cases import TEST_TICKETS

def evaluate_system():
    results = []
    for ticket in TEST_TICKETS:
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

        results.append({
            "ticket_id": ticket["ticket_id"],
            "sentiment": sentiment_data.sentiment,
            "urgency": sentiment_data.urgency,
            "route": route.route
        })

    # Sample metric: count how many were routed to escalation or tech support
    escalation_or_tech = sum(1 for r in results if r["route"] in ["Escalation", "Tech Support"])
    total = len(results)
    print(f"Escalation/Tech Support Rate: {escalation_or_tech}/{total} ({(escalation_or_tech/total)*100:.2f}%)")

    for r in results:
        print(r)

if __name__ == "__main__":
    evaluate_system()