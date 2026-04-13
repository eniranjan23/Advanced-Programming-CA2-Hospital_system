import json
import os

class DataManager:
    def __init__(self, filename='data/patients.json'):
        self.filename = filename
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({}, f)

    def save_patient(self, patient_id, data):
        with open(self.filename, 'r+') as f:
            patients = json.load(f)
            patients[patient_id] = data
            f.seek(0)
            json.dump(patients, f, indent=4)