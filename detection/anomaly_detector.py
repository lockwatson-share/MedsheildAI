# detection/anomaly_detector.py
from sklearn.ensemble import IsolationForest
import numpy as np

class AgentAnomalyDetector:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def train(self, access_counts):
        reshaped = np.array(access_counts).reshape(-1, 1)
        self.model.fit(reshaped)

    def detect(self, new_value):
        prediction = self.model.predict([[new_value]])
        return "Anomaly Detected" if prediction[0] == -1 else "Normal Behavior"


if __name__ == "__main__":
    detector = AgentAnomalyDetector()
    detector.train([5, 6, 7, 5, 6, 8, 7])
    print(detector.detect(20))