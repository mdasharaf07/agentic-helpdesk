### Main entities:
 
* User

* Ticket
- id
- title
- description
- category
- priority
- status
- created_by
- assigned_agent
- created_at
- updated_at

* TicketMessage (optional but recommended)

* AgentDecision
- id
- ticket_id
- agent_name
- decision_type
- decision_output
- confidence_score
- created_at

* AgentLog
- id
- ticket_id
- agent_name
- log_level
- message
- created_at

* One User → Many Tickets
* One Ticket → Many AgentDecisions
* One Ticket → Many AgentLogs