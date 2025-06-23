# Draconic AI Engineer Case Study – Customer Support Ticket Analyzer

## 🔍 Project Overview
A multi-agent system that analyzes customer support tickets and determines the best routing strategy using specialized agents.

## 🧠 Agents

- **Sentiment & Urgency Agent**: Classifies ticket tone (angry/neutral/polite) and urgency (urgent/medium/low).
- **Routing Agent**: Uses sentiment, urgency, and customer info to assign routes like Tech Support, Escalation, etc.

## 🧪 Evaluation
Run:
```
python evaluation/evaluate.py
```

Outputs:
- Route decisions for each ticket
- % routed to Escalation/Tech Support

## ▶️ Run Main Flow
```
python main.py
```

## 🗂️ File Structure
```
├── main.py
├── agents/
│   ├── sentiment_agent.py
│   └── router_agent.py
├── test_cases.py
├── evaluation/
│   └── evaluate.py
├── docs/
│   └── architecture.md
├── README.md
```

## ✅ Dependencies
- Python 3.8+
- `pydantic`

Install using:
```
pip install pydantic
```