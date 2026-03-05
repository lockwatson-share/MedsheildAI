MedShield AI

Secure Agentic AI Framework for Synthetic Medical Data
HIPAA and CCPA Compliant AI Security, Policy-as-Code, and Anomaly Detection

Overview

MedShield AI is a research-grade framework for experimenting with agentic AI accessing medical data while enforcing:

- HIPAA compliant PHI protection
- CCPA Right to Delete simulation
- Policy-as-Code governance (session limits, sensitive access toggles)
- ML based anomaly detection for abnormal access patterns
- Logging and auditing of all security events

Important: No real patient data is used. All data is synthetic.

Features

- Synthetic Medical Data Generator (generate_synthetic_patients.py)
    Generates 500 patient records including demographics, diagnosis, medications, lab results, and PHI
- MedShield AI Agent (agent/agent.py)
    Queries patient data safely
    Enforces session-based policy limits
    Checks HIPAA / CCPA compliance before allowing access
    Logs violations to logs/security_events.log
- Policy-as-Code Engine (policy/policy_engine.py)
    Governs runtime agent behavior
    Enforces record limits, sensitive access, logging, and anomaly detection toggles
- Anomaly Detection (detection/anomaly_detector.py)
    Detects abnormal access spikes using Isolation Forest
- Compliance Guard (compliance/hipaa_ccpa_guard.py)
    Enforces HIPAA PHI restrictions and CCPA deletion requests
- Mitigation / Logging (mitigation/response_handler.py)
    Prints security alerts and writes detailed logs

Project Structure

MedShieldAI/
    agent/                  # Agent code for querying patient data
    compliance/             # HIPAA and CCPA enforcement
    detection/              # Anomaly detection models
    mitigation/             # Logging and violation handling
    policy/                 # Policy-as-Code engine
        policies.json       # Configurable policy rules
    data/                   # Synthetic patient CSV dataset
    logs/                   # Security events logs
    notebooks/              # Demo Jupyter notebooks
    generate_synthetic_patients.py
    README.md
    requirements.txt

Quick Start (Run Locally)

1. Clone the repository

git clone https://github.com/<your-username>/MedShieldAI.git
cd MedShieldAI

2. Create a virtual environment (recommended)

python -m venv .venv
source .venv/bin/activate  # macOS / Linux
.venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

4. Generate the synthetic dataset

python generate_synthetic_patients.py

5. Run the agent demo

python agent/agent.py

6. Run the Jupyter demo notebook

jupyter notebook

- Open notebooks/demo.ipynb
- Run all cells to see:
    Allowed vs blocked access
    Session limit enforcement
    ML anomaly detection with plots

Policies (Policy-as-Code)

Located at policy/policies.json:

{
  "max_records_per_session": 10,
  "allow_sensitive_access": false,
  "require_logging": true,
  "enforce_ccpa_deletion": true,
  "anomaly_detection_enabled": true
}

Modify these values to simulate different compliance scenarios. The agent enforces these at runtime.

Usage Examples

from agent.agent import MedicalAIAgent

agent = MedicalAIAgent()

# Allowed access
agent.query_patient(1, "Diagnosis")

# Blocked access (HIPAA PHI)
agent.query_patient(1, "SSN")

Security and Compliance

HIPAA: Sensitive fields (Name, SSN, Email, InsuranceID) are blocked by default
CCPA: If DataDeletionRequested is True, access is denied
Policy-as-Code: Limits number of records per session, controls sensitive access, requires logging
Anomaly Detection: Flags abnormal spikes in access counts

Demo Notebook

Located at notebooks/demo.ipynb
Shows visualizations of access behavior and anomaly detection
Ideal for interviews or showcasing agentic AI governance

Contribution

This project is open source

Fork the repo
Submit PRs for:
    New compliance policies
    Improved anomaly detection
    Infrastructure-as-Code integrations
    Agent role-based access

License

MIT License - free to use, modify, and distribute

Notes

All data is synthetic
Ideal for research, portfolio, or interview demonstrations
Does not use real patient information