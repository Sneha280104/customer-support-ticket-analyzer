from pydantic import BaseModel

class TicketInput(BaseModel):
    subject: str
    message: str

class SentimentOutput(BaseModel):
    sentiment: str  # angry / neutral / polite
    urgency: str    # urgent / medium / low

def analyze_sentiment(ticket: TicketInput) -> SentimentOutput:
    msg = ticket.message.lower()

    if "worst" in msg or "broken" in msg or "urgent" in msg or "security" in msg:
        return SentimentOutput(sentiment="angry", urgency="urgent")
    elif "feature request" in ticket.subject.lower():
        return SentimentOutput(sentiment="polite", urgency="low")
    elif "minor" in msg or "just noticed" in msg:
        return SentimentOutput(sentiment="neutral", urgency="low")
    else:
        return SentimentOutput(sentiment="neutral", urgency="medium")