# System Architecture: Multi-Agent Ticket Analyzer

## 🎯 Objective
Analyze incoming support tickets and route them efficiently using AI agents with different perspectives.

---

## 🧠 Agent 1: Sentiment & Urgency Agent

### Input:
- Subject, Message

### Output:
- Sentiment (angry, neutral, polite)
- Urgency (urgent, medium, low)

### Example Prompt:
> "You are a Sentiment & Urgency Analyzer. Given the subject and message, classify tone and urgency."

---

## 🧠 Agent 2: Routing Agent

### Input:
- Customer tier, Sentiment, Urgency, History

### Output:
- Route (e.g., Tech Support, Retention Team, Escalation)

### Example Logic:
```
if enterprise + urgent → Escalation
if free + angry → Retention
if angry or urgent → Tech Support
else → Customer Success
```

---

## 🤝 Agent Communication
1. Sentiment Agent processes ticket first.
2. Routing Agent takes the enriched context to decide route.

---

## 📊 Evaluation
- Metric: How many tickets routed to critical support paths
- Purpose: Assess triage effectiveness and prioritization

---

## 🧪 Prompt Iteration Example
### Version 1:
> “Analyze sentiment.”

### Version 2:
> “Analyze sentiment and urgency of the message: {message}. Output JSON with `sentiment` and `urgency`.”