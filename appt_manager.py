#
# appt_manager - This program tests the majority of the methods in the Appointment class
#
# Author: Nic Draffin, Jihun Gwak, Nara Park
# Version/Date: 2023-12-06
#

# imports
from datetime import datetime
import appointment

# constants
MENS_CUT = 50
LADIES_CUT = 80
MENS_COLOURING = 50
LADIES_COLOURING = 120

# do not create another class
# rather in appt manager like a regular 
# create a list for appointment objects
# dont need to 
# getting rid of class calendar
# call that from your main
# one of the functions, find appointment by time to locate in calendar that particular time slot, if avaliable then gather information, and then call schedule method 
# call the appointment class


def create_weekly_calendar(date, description):
    pass

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

def find_appointment_by_time():
    pass

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
    '''main function'''
    print("Starting the appointment Manager system")
    print("Weekly Calendar Created")
    option_load = input("Would you like to load previously scheduled appointments from a file (Y/N)?: ")
    if option_load == 'Y' or 'y':
        load_scheduled_appointments()
    else:
        create_weekly_calendar()

    menu = print_menu()
    while menu in ['1', '2', '3', '4', '9']:
        menu = print_menu()
        if menu == '1':
            print("** Schedule an appointment **")
            appointment_set = appointment.Appointment()
            appointment_set._day_of_week = input("What day: ")
            appointment_set._start_time_hour = input("Enter start hour (24 hour clock): ")
            appointment_set._client_name = input("Client Name: ")
            appointment_set._client_phone = input("Client Phone: ")
           
        elif menu == '2':
            pass
 
        elif menu == '3':
            pass
 
        elif menu == '4':
            pass
 
        else:
            print('\n**Exit System**')
    else:
        pass

if __name__ == "__main__":
    main()
