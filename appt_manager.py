# appt_manager - This program tests the majority of the methods in the Appointment class
#
# Author: Nic Draffin, Jihun Gwak, Nara Park
# Version/Date: 2023-12-06
#
 
# imports
from datetime import datetime
from appointment import Appointment
import os

# constants
MENS_CUT = 50
LADIES_CUT = 80
MENS_COLOURING = 50
LADIES_COLOURING = 120

# create weekly calendar function
# creates a lsit and a for loop to create the specific appointments for those days
# returns the list 
def create_weekly_calendar():
    '''Create Weekly Calendar Function'''
    appointment_list = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days:
        for hour in range(9, 17):
            appointment = Appointment(day, hour)
            appointment_list.append(appointment)
    return appointment_list

# loads in existing CSV files into the appointment list, and returns the amount of appointments loaded in 
def load_scheduled_appointments(appointment_list):
    '''Load Scheduled Appointments'''
    file_path = input("Enter appointment filename: ")
    while not os.path.exists(file_path): # while loop checker to ensure a correct file is inputted
        file_path = input("File not found. Re-enter appointment filename: ")

    if os.path.exists(file_path): # if statement to confirm it exists
        file = open(file_path, 'r')
        lines = file.readlines()
        for line in lines: # for loop to read lines and calls get_appt_type to see what lines have not been read
            client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
            appointment = find_appointment_by_time(appointment_list, day_of_week, int(start_time_hour))
            if appointment and appointment.get_appt_type() == 0:
                appointment.schedule(client_name, client_phone, int(appt_type))
        lines_num = len(lines)
        file.close()
        print(f"{lines_num} previously scheduled appointments have been loaded") # print number of appointments
        return lines_num

# find appointment by time, return the matching appointments 
def find_appointment_by_time(appointment_list, day, start_time_hour):
    '''Find appointment by time Function'''
    for appointment in appointment_list:
        if appointment.get_day_of_week().lower() == day.lower() and appointment.get_start_time_hour() == start_time_hour:
            return appointment
    return None

# shows the appointments by name or parial name, returns the matching appointment
def show_appointment_by_name(appointment_list):
    '''Show appointment by Name Function'''
    print("\n** Find appointment by name **")
    client_name = input("Enter Client Name: ").lower()
    matching_appointments = [appointment for appointment in appointment_list if client_name in appointment.get_client_name().lower()]
    
    if matching_appointments:
        print(f"Appointments for {client_name}:")
        print_appointment_table(matching_appointments)
    else:
        print("{:<19} {:<16} {:<15} {:<11} {:<9} {:<15}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
        print("-" * 95)
        print("No appointments found.")

# show the appointment by the day, returns the entire days schedule
def show_appointments_by_day(appointment_list):
    print("\n** Print calendar for a specific day **")
    day_of_week = input("Enter day of week: ").lower()
    day_appointments = [appointment for appointment in appointment_list if day_of_week in appointment.get_day_of_week().lower()]
   
    if day_appointments:
        print(f"Appointments for {day_of_week}:")
        print_appointment_table(day_appointments)
    else:
        print("{:<19} {:<16} {:<15} {:<11} {:<9} {:<15}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
        print("-" * 95)
 

def print_appointment_table(appointments):
    print("{:<19} {:<16} {:<15} {:<11} {:<9} {:<15}".format("Client Name", "Phone", "Day", "Start", "End", "Type"))
    print("-" * 95)
    for appointment in appointments: # for loop to print all the corresponding heading and uses the getters from the appointment class
        print("{:<20s}{:<17s}{:<16s}{:02d}:00   -   {:02d}:00     {:<20s}".format(
            appointment.get_client_name(),
            appointment.get_client_phone(),
            appointment.get_day_of_week(),
            appointment.get_start_time_hour(),
            appointment.get_end_time_hour(),
            appointment.get_appt_type_desc()
        ))

# saves the scheduled appointments to a csv file, uses the write function
def save_scheduled_appointments(appointment_list):
    '''Save Scheduled Appointment Function'''
    option_save = input("Would you like to save all scheduled appointments to a file (Y/N)? ").lower()
    if option_save in ['y', 'Y']:
        file_name = "N"
        while file_name != " ": # while loop to ensure the an existing file is chosen
            file_name = input("Enter appointment filename: ")
            if os.path.exists(file_name):
                option_ow = input("File already exists. Do you want to overwrite it (Y/N)? ").lower()
                if option_ow in ['y']:
                    file = open(file_name, 'w')
                    for appointment in appointment_list:
                        if appointment.get_client_name():
                            file.write(f"{appointment.format_record()}\n") # writes a file using the format_record function from the appointment class
                    file.close()
                    file = open(file_name, 'r')
                    lines = file.readlines()
                    for line in lines: # for loop to count how many appointments are being saved
                        client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
                        appointment = find_appointment_by_time(appointment_list, day_of_week, int(start_time_hour))
                    lines_num = len(lines)
                    print(f"{lines_num} scheduled appointments have been successfully saved") # print how many files are being saved
                    file.close()
                    print("Good Bye!")
                    break     
            else:
                file = open(file_name, 'x') # same as the other option just opens a new document and writes on that instead of existing one
                for appointment in appointment_list:
                    if appointment.get_client_name():
                        file.write(f"{appointment.format_record()}\n")
                file = open(file_name, 'r')
                lines = file.readlines()
                for line in lines:
                    client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
                    appointment = find_appointment_by_time(appointment_list, day_of_week, int(start_time_hour))
                lines_num = len(lines)
                print(f"{lines_num} scheduled appointments have been successfully saved") 
                file.close()
                print("Good Bye!")
                break
    else:
        print("Good Bye!")

# prints the menu and while loop to ensure correct choice is given
def print_menu():
    '''Print Menu Function'''
    print("\nJojo's Hair Salon Appointment Manager")
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
    print("Starting the Appointment Manager system")
    appointment_list = create_weekly_calendar()
    print("Weekly Calendar Created")
    option_load = input("Would you like to load previously scheduled appointments from a file (Y/N)?: ").lower() # if statement to direct if they want to load a previous file
    if option_load in ['y', 'Y']:
        load_scheduled_appointments(appointment_list)

    while True:
        menu = print_menu()

        if menu == '1':
            '''Option 1'''
            print("\n** Schedule an appointment **")
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            day = input("What day: ")
            start_time_hour = int(input("Enter start hour (24-hour clock): "))
            appointment = find_appointment_by_time(appointment_list, day, start_time_hour)
 
 
            if appointment and appointment.get_appt_type() == 0:
                client_name = input("Client Name: ")
                client_phone = input("Client Phone: ")
                print("Appointment types")
                print("1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")
                appt_type = int(input("Type of Appointment: "))
                appointment.schedule(client_name, client_phone, appt_type)
                print(f"OK, {client_name}'s appointment is scheduled!")
            
            elif day not in days:
                print("Sorry that time slot is not in the weekly calendar!")
            
            
            else:
                print("Sorry, that time slot is booked already!")

        elif menu == '2':
            '''option 2'''
            show_appointment_by_name(appointment_list)

        elif menu == '3':
            '''Option 3'''
            show_appointments_by_day(appointment_list)

        elif menu == '4':
            '''Option 4'''
            print("\n** Cancel an appointment **") 
            day_to_cancel = input("Enter day: ")
            start_hour_to_cancel = int(input("Enter start hour (24-hour clock): "))
            appointment_to_cancel = find_appointment_by_time(appointment_list, day_to_cancel, start_hour_to_cancel)
            if appointment_to_cancel:
                appointment_to_cancel.cancel() # cancels the appointment
                print(f"Appointment: {day_to_cancel} {start_hour_to_cancel:02}:00 - {appointment_to_cancel.get_end_time_hour():02}:00 for {appointment_to_cancel.get_client_name()} has been cancelled!")
            else:
                print("Sorry that time slot is not in the weekly calendar!")

        elif menu == '9':
            '''Option 9'''
            print("\n** Exit the system **")
            save_scheduled_appointments(appointment_list) # saves all the appointments given in a file or creates a new one
            break


if __name__ == "__main__":
    main()
