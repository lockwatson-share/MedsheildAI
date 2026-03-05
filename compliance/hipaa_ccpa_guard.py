# compliance/hipaa_ccpa_guard.py
from policy.policy_engine import is_sensitive_access_allowed

SENSITIVE_FIELDS = ["Name", "SSN", "PhoneNumber", "Email", "InsuranceID"]

def check_access(field, patient_record):
    # HIPAA: check if sensitive access is allowed
    if field in SENSITIVE_FIELDS and not is_sensitive_access_allowed():
        return False, "HIPAA violation: Access to PHI restricted"

    # CCPA: enforce deletion requests
    if patient_record.get("DataDeletionRequested", False):
        return False, "CCPA violation: Data deletion requested"

    return True, "Access granted"