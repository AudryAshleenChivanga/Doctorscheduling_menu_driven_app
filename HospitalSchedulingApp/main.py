#!/usr/bin/env python3

class Hospital:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

class SchedulingApp:
    def __init__(self):
        self.hospitals = [
            Hospital(" Kacyiru Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital(" Kibagabaga Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital(" King Faisal Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital(" La Croix du Sud Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital(" Masaka Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital(" Mbc Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital(" Muhima Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital("Nyarugenge Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
            Hospital("Ndera Hospital", ["Outpatient", "General", "Opthalmology", "Physiotherapy", "Emergency"]),
        ]

    def display_hospitals(self):
        print("\033[1;34m        Welcome to Kigali Hospitals!\033[0m")
        print("\033[1;34m*********Your health, Our priority!*********\033[0m")
        print("Select a hospital:")
        for i, hospital in enumerate(self.hospitals, 1):
            print(f"{i}. {hospital.name}")
        print("0. Exit")

    def display_departments(self, hospital_index):
        hospital = self.hospitals[hospital_index]
        print(f"Select a department for {hospital.name}:")
        for i, department in enumerate(hospital.departments, 1):
            print(f"{i}. {department}")
        print("0. Back")

    def get_selected_hospital(self):
        try:
            selected_option = int(input("Enter the number corresponding to the hospital: "))
            if 0 <= selected_option <= len(self.hospitals):
                return selected_option - 1
            else:
                print("Invalid option. Please select a valid number.")
                return self.get_selected_hospital()
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_selected_hospital()

    def get_selected_department(self, hospital_index):
        try:
            hospital = self.hospitals[hospital_index]
            self.display_departments(hospital_index)
            selected_option = int(input("Enter the number corresponding to the department: "))
            if 0 <= selected_option <= len(hospital.departments):
                return selected_option - 1
            else:
                print("Invalid option. Please select a valid number.")
                return self.get_selected_department(hospital_index)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.get_selected_department(hospital_index)

    def schedule_appointment(self):
        specialist_choice = input("Do you want to see a specialist? (yes/no): ").lower()
        if specialist_choice == "yes":
            specialist_name = input("Enter the name of the specialist: ")
            appointment_time = input("Enter the time for the appointment: ")
            return f"Specialist: {specialist_name}, Appointment Time: {appointment_time}"
        else:
            appointment_time = input("Enter the time for the appointment: ")
            return f"Appointment Time: {appointment_time}"

    def run(self):
        while True:
            self.display_hospitals()
            selected_option = self.get_selected_hospital()

            if selected_option == -1:
                print("Exiting the app. Thank you!")
                break

            if selected_option >= 0 and selected_option < len(self.hospitals):
                selected_hospital = self.hospitals[selected_option].name
                selected_department_index = self.get_selected_department(selected_option)
                selected_department = self.hospitals[selected_option].departments[selected_department_index]

                print(f"\nYou selected: Hospital: {selected_hospital}, Department: {selected_department}")
                appointment_details = self.schedule_appointment()

                print("\nThank you for scheduling your appointment! Your Appointment Has Been Booked :)")
                print("\n ")
                print("||***************************||")
                print("Appointment Summary:")
                print("||***************************||")
                print(f"Hospital: {selected_hospital}")
                print("||***************************||")
                print(f"Department: {selected_department}")
                print("Your Appointment ID is :34267")
                if "Specialist" in appointment_details:
                    print(appointment_details)
                else:
                    print(f"Appointment Time: {appointment_details}")
                print("\n ")

if __name__ == "__main__":
    app = SchedulingApp()
    app.run()
