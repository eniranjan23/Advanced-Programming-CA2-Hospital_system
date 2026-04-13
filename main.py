import getpass
from hospital_logic import HospitalSystem
from database import DataManager

def login():
    print("--- Hospital Staff Login ---")
    username = input("Username: ")
    
    password = getpass.getpass("Password: ")
    
    if username == "admin" and password == "password":
        print("Access Granted.\n")
        return True
    else:
        print("Access Denied.")
        return False

def main():
    system = HospitalSystem()
    db = DataManager()
    
    print("--- Dublin Hospital Management System ---")
    name = input("Enter Patient Name: ")
    
    
    while True:
        age = input("Enter Age: ")
        if age.isdigit():
            break
        print("Invalid input. Please enter a numerical value for age.")
        
    issue = input("Enter Ailment: ")
    
    
    p_id, p_data = system.register_patient(name, age, issue)
    
    
    db.save_patient(p_id, p_data)
    
    print(f"\nSuccess! Patient Registered with ID: {p_id}")
    print(f"Current Waiting List: {list(system.waiting_list)}")


if __name__ == "__main__":
    if login():
        main()