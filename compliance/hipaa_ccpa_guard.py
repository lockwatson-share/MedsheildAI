# compliance/hipaa_ccpa_guard.py
from policy.policy_engine import is_sensitive_access_allowed
import os
import pandas as pd

SENSITIVE_FIELDS = ["Name", "SSN", "PhoneNumber", "Email", "InsuranceID"]

# Optional: path to synthetic patient data
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "synthetic_patients.csv")
DATA_PATH = os.path.abspath(DATA_PATH)


def load_patients():
    """Load synthetic patient dataset."""
    return pd.read_csv(DATA_PATH)


def check_access(field, patient_record):
    """
    Check HIPAA and CCPA compliance for a single field access.
    Returns (allowed: bool, reason: str)
    """

    # HIPAA: check if sensitive access is allowed
    if field in SENSITIVE_FIELDS and not is_sensitive_access_allowed():
        return False, "HIPAA violation: Access to PHI restricted"

    # CCPA: enforce Right to Delete
    if patient_record.get("DataDeletionRequested", False):
        return False, "CCPA violation: Data deletion requested"

    return True, "Access granted"


def check_ccpa_right_to_delete(patient_id):
    """
    Standalone CCPA Right-to-Delete check for auditing or batch enforcement.
    Returns (violation: bool, message: str)
    """
    df = load_patients()
    patient = df[df["PatientID"] == patient_id]

    if patient.empty:
        return False, "Patient not found."

    if patient.iloc[0].get("DataDeletionRequested", False):
        return True, f"CCPA violation: Data deletion requested for patient {patient_id}"

    return False, "No deletion requested. Access allowed"


if __name__ == "__main__":
    # Example usage
    df = load_patients()
    print("Testing HIPAA and CCPA compliance checks...\n")

    for i, row in df.iterrows():
        for field in ["Diagnosis", "SSN"]:
            allowed, reason = check_access(field, row)
            print(f"Patient {row['PatientID']}, Field {field}: {reason}")

        violation, msg = check_ccpa_right_to_delete(row['PatientID'])
        print(f"CCPA Right to Delete check for Patient {row['PatientID']}: {msg}\n")