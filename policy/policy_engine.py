# policy/policy_engine.py
import os
import json

POLICY_FILE = os.path.join(os.path.dirname(__file__), "policies.json")

def load_policies():
    with open(POLICY_FILE, "r") as f:
        return json.load(f)

def check_record_limit(current_access_count):
    policies = load_policies()
    max_allowed = policies.get("max_records_per_session", 10)

    if current_access_count > max_allowed:
        return False, "Policy violation: Record access limit exceeded"

    return True, "Within record access limits"

def is_sensitive_access_allowed():
    policies = load_policies()
    return policies.get("allow_sensitive_access", False)

def is_logging_required():
    policies = load_policies()
    return policies.get("require_logging", True)

def is_anomaly_detection_enabled():
    policies = load_policies()
    return policies.get("anomaly_detection_enabled", True)