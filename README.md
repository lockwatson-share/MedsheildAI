MedShield AI

Secure, agentic AI-inspired framework for healthcare data

MedShield AI is an open-source framework designed to demonstrate HIPAA and CCPA-compliant agentic AI workflows. It enforces policy-as-code, monitors anomalies, and logs all activity using synthetic patient data to simulate real-world healthcare scenarios safely.

Features

HIPAA and CCPA Compliance:
- Blocks access to sensitive PHI fields (Name, SSN, Email, Insurance ID)
- Respects CCPA Right-to-Delete flags

Policy-as-Code:
- Configurable session limits
- Toggle for allowing sensitive access
- Logging enforcement

Session Limits:
- Tracks queries per session
- Prevents exceeding maximum allowed requests

Sensitive Data Enforcement:
- Access to PHI is denied automatically according to policy rules

Anomaly Detection:
- Isolation Forest detects unusual query patterns or spikes
- Triggers alerts on anomalies

Audit Logging:
- Logs all queries, blocked access attempts, and anomalies for compliance purposes

Agentic AI-Inspired:
- Semi-autonomous agent that enforces policies and compliance rules without exposing real patient data

What It Currently Does

- Fully functional policy enforcement and compliance guard for synthetic medical datasets
- Tracks sessions, sensitive access, and audit logs
- Detects unusual usage patterns using ML-based anomaly detection
- Uses synthetic patient data only; no real PHI is involved

Notes and Limitations

- The agentic AI is semi-agentic: it can make decisions about allowing or blocking queries, but it does not yet plan multi-step tasks or dynamically adapt policies
- Anomaly detection is prototype-level; production use requires tuning, retraining, and alert integration
- Designed as a proof-of-concept and educational tool for safe AI governance in healthcare

Quick Start

1) Clone the repository
git clone https://github.com/lockwatson-share/MedsheildAI.git
cd MedsheildAI

2) Create virtual environment and activate
python -m venv .venv
source .venv/bin/activate  # Linux or macOS
.venv\Scripts\activate     # Windows

3) Install dependencies
pip install -r requirements.txt

4) Generate synthetic patients
python generate_synthetic_patients.py

5) Run the agent
python agent/agent.py

6) Or open the Jupyter notebook for interactive demos
jupyter notebook notebooks/demo.ipynb

Contributing

MedShield AI is open-source and free to use or develop further. Contributions are welcome for:
- Adding new compliance rules or policies
- Improving anomaly detection algorithms
- Integrating with cloud infrastructure or IaC security
- Enhancing semi-agentic decision-making toward full agentic AI

License

MedShield AI is released under the MIT License. See LICENSE file.