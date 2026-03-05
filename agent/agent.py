# agent/agent.py
import pandas as pd
import os

from compliance.hipaa_ccpa_guard import check_access
from mitigation.response_handler import handle_violation
from policy.policy_engine import check_record_limit


DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "synthetic_patients.csv")
DATA_PATH = os.path.abspath(DATA_PATH)


class MedicalAIAgent:
    def __init__(self, agent_id="MedAgent-01"):
        self.agent_id = agent_id
        self.access_log = []

    def load_data(self):
        return pd.read_csv(DATA_PATH)

    def query_patient(self, patient_id, field):
        df = self.load_data()
        patient = df[df["PatientID"] == patient_id]

        if patient.empty:
            return "Patient not found."

        # Policy-as-Code: session limit
        allowed_limit, reason_limit = check_record_limit(len(self.access_log) + 1)
        if not allowed_limit:
            handle_violation(self.agent_id, field, reason_limit)
            return f"ACCESS DENIED: {reason_limit}"

        # HIPAA / CCPA Compliance
        allowed, reason = check_access(field, patient.iloc[0])
        if not allowed:
            handle_violation(self.agent_id, field, reason)
            return f"ACCESS DENIED: {reason}"

        value = patient.iloc[0][field]
        self.access_log.append({
            "agent_id": self.agent_id,
            "patient_id": patient_id,
            "field": field
        })

        return value


if __name__ == "__main__":
    agent = MedicalAIAgent()
    print("\n--- MedShield AI Agent Demo ---\n")
    print("Allowed access (Diagnosis):", agent.query_patient(1, "Diagnosis"))
    print("Blocked access (SSN):", agent.query_patient(1, "SSN"))
    print("\nTesting session limit enforcement:")
    for i in range(1, 15):
        result = agent.query_patient(i, "Diagnosis")
        print(f"Access {i} → {result}")