from models import Applicant, Appointment, Customer
from database import session, init_db

def apply_for_job(session):
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    years_worked = input("How many years have you worked as a hairstylist? ")
    age = input("How old are you? ")

    new_applicant = Applicant(
        first_name=first_name, last_name=last_name, years_worked=years_worked, age=age
    )

    session.add(new_applicant)
    session.commit()
    print("Application submitted successfully!\n(call us at: 0712345678 Welcome)")

def view_appointments(session):
    appointments = session.query(Appointment).all()
    for appointment in appointments:
        print(f"Customer ID: {appointment.customer_id}, Appointment Date: {appointment.appointment_date}, Service: {appointment.service}")

def add_customer(session):
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")

    print("Select haircut type:")
    haircut_choices = {
        "1": "fade $100",
        "2": "tapar $100",
        "3": "afro $100",
        "4": "wave $200",
        "5": "quiff $200",
        "6": "mohawk $200",
        "7": "cornrows $200",
        "8": "braid $200",
        "9": "twist $200",
        "10": "undercut $200",
        "11": "cornrow $200",
        "12": "widfade $200",
        "13": "low fade $200",
        "14": "cop top $200"
    }
    for key, value in haircut_choices.items():
        print(f"{key}. {value}")

    haircut_choice = input("Choose the haircut number you want: ")
    if haircut_choice not in haircut_choices:
        print("Invalid haircut choice.")
        return

    appointment_date = input("Enter Appointment Date (YYYY-MM-DD HH:MM): ")
    payment_method = input("Enter Payment Method: ")

    new_customer = Customer(
        first_name=first_name,
        last_name=last_name,
        haircut_choice=haircut_choices[haircut_choice],
        appointment_date=appointment_date,
        payment_method=payment_method
    )
    session.add(new_customer)
    session.commit()

    new_appointment = Appointment(
        customer_id=new_customer.id,
        appointment_date=appointment_date,
        service=haircut_choices[haircut_choice]
    )
    session.add(new_appointment)
    session.commit()

    print("Customer and appointment added successfully!")

def main():
    # Initialize the database and create tables
    init_db()

    while True:
        print("Please select an option:")
        print("0. Exit the program")
        print("1. Apply for a job")
        print("2. Schedule an appointment")
        print("3. View appointments")
        choice = input("> ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            apply_for_job(session)
        elif choice == "2":
            add_customer(session)
        elif choice == "3":
            view_appointments(session)
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
