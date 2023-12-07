#
# appt_manager - This program tests the majority of the methods in the Appointment class
#
# Author: Nic Draffin, Jihun Gwak, Nara Park
# Version/Date: 2023-12-06
#

# imports
from datetime import datetime
import appointment as ap

# constants
MENS_CUT = 50
LADIES_CUT = 80
MENS_COLOURING = 50
LADIES_COLOURING = 120
file = "appointments1.csv"
appointments = []
        

def create_weekly_calendar(date, description):
    if date not in appointments:
        appointments[date] = []
        appointments[date].append(description)
        print(f"Appointment added on {date}: {description}")

def load_scheduled_appointments():
        filename = input("Enter appointment filename: ")
        while filename != file:

            if filename == file:
                file = open("/Users/jihungwak/Downloads/appointments1.csv", 'r')
                lines = file.readlines()
                number_appointment = len(lines)
                print(f"{number_appointment} previously scheduled appointments have been loaded")
                file.close
            else:
                filename = input("File not found. Re-enter appointment filename: ")
             
def find_appointment_by_time(date):
        if date in appointments:
            print(f"Appointments on {date}:")
            for appointment in appointments[date]:
                print(f"- {appointment}")
        else:
            print(f"No appointments on {date}")

def show_appointment_by_name():
        pass

def show_appointments_by_day():
        pass

def save_scheduled_appointments():
        pass

def print_menu():
    '''Print Menu Function'''
    print("Jojo's Hair Salon Appointment Manager")
    print("=" * 37)
    print(" 1) Schedule an appointment")
    print(" 2) Find Appointment by name")
    print(" 3) Print calendar for a specific day")
    print(" 4) Cancel an appointment")
    print(" 9) Exit the system")

    menu = input("Enter your selection: ")
    while menu not in ['1', '2', '3', '4', '9']:
        menu = input("Enter your selection: ")
    return menu
def main():
    # Here are the types of appointments:
    # 0 - Available, 1 = Mens cut $50, 2= Ladies cut $80, 3= Mens Colouring $50, 4= Ladies Colouring $120
    # create a list of 7 appointments for Saturday (between 9:00 and 15:00 start time)

    appt_list = []
    day = "Saturday"
    for time in range(9, 16):
        appt_list.append(ap.Appointment(day, time))

    # Book the first appointment slot (9 AM) for Harvey Wallbanger for a Men's Cut (appt_type = 1)
    current_appt = appt_list[0]
    current_appt.schedule("Harvey", "403-233-3944", 1)

    # Book the second appointment slot (10 AM) for Sara for a Ladies Colouring
    current_appt = appt_list[1]
    current_appt.schedule("Sara", "403-233-3945", 4)

    # Go through all the appointments and find the noon hour slot and book Jenny for a cut
    found = False
    index = 0
    while index < len(appt_list) and not found:
        current_appt = appt_list[index]
        # is this appointment the noon hour appointment for Saturday available?
        if current_appt.get_day_of_week() == "Saturday" and \
           current_appt.get_start_time_hour() == 12 and \
           current_appt.get_appt_type() == 0:
            found = True
        index += 1
    if found:
        # book it!
        current_appt.set_client_name("Jenny")
        current_appt.set_client_phone("403-867-5309")
        current_appt.set_appt_type(2)  # 2 - Ladies Cut
    else:
        print("Appointment entry not found")

    # Print only scheduled appointments using format_record()
    print("Scheduled appointment records:")
    for appt in appt_list:
        if appt.get_appt_type() != 0:
            print(appt.format_record())

    # Cancel Sara's appointment
    current_appt = appt_list[1]
    current_appt.cancel()

    # Print report of all appointment times using string method
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
    for appt in appt_list:
        print(appt)

if __name__ == "__main__":
    main()

