Define agent roles:
* Classifier Agent,
→ Input: ticket_id, title, description
→ Output: category, urgency, confidence

* Planner Agent,
→ Input: ticket_id, category, urgency, confidence
→ Output: action

* Resolution Agent,
→ Input: ticket_id, action
→ Output: solution

* Verification Agent,
→ Input: ticket_id, solution
→ Output: verified

* Escalation Agent,
→ Input: ticket_id, verified
→ Output: escalated