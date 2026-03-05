# generate_synthetic_patients.py
"""
Synthetic Medical Data Generator
---------------------------------
Generates synthetic healthcare records for security research.
⚠️ No real patient data is used.
Designed for HIPAA / CCPA compliance simulation.
"""

import pandas as pd
from faker import Faker
import random
import json
from datetime import datetime, timedelta
import os

fake = Faker()
num_patients = 500

diagnoses = ["Hypertension", "Diabetes", "Asthma", "COPD", "Depression",
             "Anxiety", "Arthritis", "Migraine", "Obesity", "Hypothyroidism"]
medications = ["Metformin", "Lisinopril", "Atorvastatin", "Albuterol",
               "Omeprazole", "Levothyroxine", "Gabapentin",
               "Hydrochlorothiazide", "Amlodipine", "Simvastatin"]
allergies = ["Penicillin", "Peanuts", "Shellfish", "Latex", "Pollen", "None"]

data = []

for i in range(num_patients):
    lab_results = {
        "WBC": round(random.uniform(4000, 11000), 1),
        "Hgb": round(random.uniform(12.0, 17.5), 1),
        "Platelets": round(random.uniform(150, 400), 1),
        "Glucose": round(random.uniform(70, 140), 1)
    }

    record = {
        "PatientID": i + 1,
        "Name": fake.name(),
        "SSN": fake.ssn(),
        "PhoneNumber": fake.phone_number(),
        "Email": fake.email(),
        "InsuranceID": fake.bothify(text="???-#######"),
        "Gender": random.choice(["Male", "Female", "Other"]),
        "DateOfBirth": fake.date_of_birth(minimum_age=0, maximum_age=100).strftime("%Y-%m-%d"),
        "Age": random.randint(1, 100),
        "Diagnosis": random.choice(diagnoses),
        "TreatmentPlan": fake.sentence(nb_words=6),
        "Medications": ", ".join(random.sample(medications, k=random.randint(1, 3))),
        "LabResults": json.dumps(lab_results),
        "Allergies": random.choice(allergies),
        "LastVisitDate": (datetime.today() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "DoctorAssigned": fake.name(),
        "Notes": fake.sentence(nb_words=10),
        "DataDeletionRequested": random.choice([True, False])
    }

    data.append(record)

df = pd.DataFrame(data)

# Robust path
project_root = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(project_root, "data")
os.makedirs(data_folder, exist_ok=True)

csv_path = os.path.join(data_folder, "synthetic_patients.csv")
df.to_csv(csv_path, index=False)

print(f"✅ Synthetic patient dataset created at {csv_path} with {num_patients} records!")