# mitigation/response_handler.py
import os
import datetime

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "logs", "security_events.log")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def handle_violation(agent_id, field, reason):
    timestamp = datetime.datetime.now()
    log_entry = f"{timestamp} | Agent: {agent_id} | Field: {field} | Reason: {reason}\n"

    print("🚨 SECURITY ALERT:", reason)

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)