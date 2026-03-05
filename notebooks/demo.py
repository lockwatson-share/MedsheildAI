import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.agent import MedicalAIAgent
from detection.anomaly_detector import AgentAnomalyDetector
import matplotlib.pyplot as plt
import random

print("\n--- MedShield AI Demo ---\n")

agent = MedicalAIAgent()

# Simulate normal activity
normal_access_counts = [5, 6, 7, 5, 6, 8, 7]

# Simulate abnormal spike
anomalous_access = 25

# Train anomaly detector
detector = AgentAnomalyDetector()
detector.train(normal_access_counts)

print("Normal behavior test:", detector.detect(6))
print("Anomalous behavior test:", detector.detect(anomalous_access))

# Visualize behavior
data_points = normal_access_counts + [anomalous_access]

plt.figure()
plt.plot(data_points)
plt.title("Agent Access Behavior Over Time")
plt.xlabel("Time")
plt.ylabel("Number of Patient Records Accessed")
plt.show()

# Compliance test
print("\nCompliance Tests:")
print("Allowed access:", agent.query_patient(1, "Diagnosis"))
print("Blocked access:", agent.query_patient(1, "SSN"))