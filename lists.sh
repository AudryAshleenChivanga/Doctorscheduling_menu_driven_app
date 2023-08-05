 appointment_details = schedule_appointment()

    print("\nThank you for scheduling your appointment!" + " " + "Your Appointment Has Been Booked :)")
    print("\n ")
    print("Appointment Summary:")
    print("*************************||***********************||************************||")
    print(f"Hospital: {selected_hospital}")
    print("*************************||***********************||************************||")
    print(f"Department: {selected_department}")
    if "Specialist" in appointment_details:
        print(appointment_details)
