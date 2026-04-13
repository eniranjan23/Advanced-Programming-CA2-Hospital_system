from collections import deque

class HospitalSystem:
    def __init__(self):
        # deque is an efficient data structure for a hospital waiting list (FIFO)
        self.waiting_list = deque() 
        self.patients = {} 

    def register_patient(self, name, age, ailment):
        # Logic to generate a unique ID
        patient_id = f"P{len(self.patients) + 101}"
        record = {"name": name, "age": age, "ailment": ailment}
        self.patients[patient_id] = record
        self.waiting_list.append(patient_id)
        return patient_id, record

    def get_next_patient(self):
        if self.waiting_list:
            return self.waiting_list.popleft() 
        return None