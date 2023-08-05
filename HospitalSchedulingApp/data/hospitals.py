#!/usr/bin/env python3

#This is the whole first group code for the Schedulling App.
hospitals_data = {
    "hospitals": [
        {
            "name": "Kibagabaga Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "University Teaching Hospital of Kigali",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "Kacyiyu Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "Muhima Health Center",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "La Croix du Sud Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "Proposed General Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "Nyarugenge District Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "Ubuzima Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "Omega Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
        {
            "name": "Mbc Hospital",
            "departments": ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]
        },
    ]
}

def display_hospitals():
    print("\033[1;34mWelcome to Kigali Hospitals! Your health, Our priority!\033[0m")
    print("Select a hospital:")
    for i, hospital in enumerate(hospitals_data["hospitals"], 1):
        print(f"{i}. {hospital['name']}")

def display_departments(hospital_index):
    hospital = hospitals_data["hospitals"][hospital_index]
    print(f"Select a department for {hospital['name']}:")
    for i, department in enumerate(hospital["departments"], 1):
        print(f"{i}. {department}")

def get_selected_hospital():
    try:
        selected_option = int(input("Enter the number corresponding to the hospital: "))
        if 1 <= selected_option <= len(hospitals_data["hospitals"]):
            return selected_option - 1
        else:
            print("Invalid option. Please select a valid number.")
            return get_selected_hospital()
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_selected_hospital()

def get_selected_department(hospital_index):
    try:
        hospital = hospitals_data["hospitals"][hospital_index]
        display_departments(hospital_index)
        selected_option = int(input("Enter the number corresponding to the department: "))
        if 1 <= selected_option <= len(hospital["departments"]):
            return selected_option - 1
        else:
            print("Invalid option. Please select a valid number.")
            return get_selected_department(hospital_index)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return get_selected_department(hospital_index)

def schedule_appointment():
    specialist_choice = input("Do you want to see a specialist? (yes/no): ").lower()
    if specialist_choice == "yes":
        specialist_name = input("Enter the name of the specialist: ")
        appointment_time = input("Enter the time for the appointment: ")
        return f"Specialist: {specialist_name}, Appointment Time: {appointment_time}"
    else:
        appointment_time = input("Enter the time for the appointment: ")
        return f"Appointment Time: {appointment_time}"

if __name__ == "__main__":
    display_hospitals()
    selected_hospital_index = get_selected_hospital()
    selected_hospital = hospitals_data["hospitals"][selected_hospital_index]["name"]
    selected_department_index = get_selected_department(selected_hospital_index)
    selected_department = hospitals_data["hospitals"][selected_hospital_index]["departments"][selected_department_index]

    print(f"\nYou selected: Hospital: {selected_hospital}, Department: {selected_department}")
    appointment_details = schedule_appointment()

    print("\nThank you for scheduling your appointment!")
    print("Appointment Summary:")
    print(f"Hospital: {selected_hospital}")
    print(f"Department: {selected_department}")
    if "Specialist" in appointment_details:
        print(appointment_details)
    else:
        print(f"Appointment Time: {appointment_details}")
        print("Your Appointment Has Been Booked :)")
