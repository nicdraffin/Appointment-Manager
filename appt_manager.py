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
 
# do not create another class
# rather in appt manager like a regular
# create a list for appointment objects
# dont need to
# getting rid of class calendar
# call that from your main
# one of the functions, find appointment by time to locate in calendar that particular time slot, if avaliable then gather information, and then call schedule method
# call the appointment class
 
 
def create_weekly_calendar():
    appointment_list = []
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for day in days:
        for hour in range(9, 17):
            appointment = Appointment(day, hour)
            appointment_list.append(Appointment(appointment))
    return appointment_list
 
 
def load_scheduled_appointments(appointment_list):
    file_path = input("Enter appointment filename: ")
    while not os.path.exists(file_path):
        file_path = input("File not found. Re-enter appointment filename: ")
    if os.path.exists(file_path):
        file = open(file_path, 'r')
        lines = file.readlines()
        for line in lines:
            client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
            appointment = find_appointment_by_time(appointment_list, day_of_week, int(start_time_hour))
        if appointment:
            Appointment.schedule(client_name, client_phone, int(appt_type))
    lines_num = len(lines)
    print(f"{lines_num} previously scheduled appointments have been loaded")
    return len(lines)
 
               
def find_appointment_by_time(appointment_list, day, start_time_hour):
    for appointment in appointment_list:
        if Appointment.get_day_of_week() == day and Appointment.get_start_time_hour() == start_time_hour:
            return appointment
    return None
 
def show_appointment_by_name(appointment_list):
    # found = False
    # index = 0
    print("** Find appointment by name **")
    client_name = input("Enter Client Name: ").lower() #change this into able to search for partial client name in get client name and have boolean
    print(f"Appointments for {client_name}")
    for appointment in appointment_list:
        if client_name.lower() in Appointment.get_client_name.lower():
            print(Appointment.__str__(appointment))
    else:
        print("No appointments found.")
 
 
def show_appointments_by_day(appointment_list):
    print("** Print calendar for a specific day **")
    day_of_week = input("Enter day of week: ")
    print(f"Appointment for {day_of_week}")
    for appointment in appointment_list:
        if day_of_week.lower() in Appointment.get_day_of_week.lower():
            print(Appointment.__str__(appointment))
    else:
        print("No appointments found.")
    # iterate through appointment and then with if statement
    #for appointment in matching_appointments:
        # print(Appointment.__str__(appointment))
 
def save_scheduled_appointments(file_name, appointment_list):
    option_save = input("Would you like to save all scheduled appointments to a file (Y/N)?")
    if option_save == 'Y' or 'y': # somewhat similiar from load , check exists is the same. IF the file does exist then prompt , then theres a loop to have them re enter file name
        file_name = input("Enter appointment filename: ")
        while os.path.exists(file_name):
            option_ow = input("File already exists. Do you want to overwrite it (Y/N)? ")
            while option_ow == 'Y' or 'y':
                file = open(file_name, 'w')
                while appt_type != 0:
                    client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
                    appointment = find_appointment_by_time(appointment_list, day_of_week, int(start_time_hour))
                    print(f"{len(appointment_list)} appointments saved to {file_name}.")
                file.close()
                file_name = input("Enter appointment filename: ")
        else:
            file = open(file_name, 'x')
    else:
        print("Good Bye!")
            
    option_save = input("Would you like to save all scheduled appointments to a file (Y/N)?")
    if option_save == 'Y' or 'y': # somewhat similiar from load , check exists is the same. IF the file does exist then prompt , then theres a loop to have them re enter file name
        file_name = input("Enter appointment filename: ")
        while os.path.exists(file_name):
            option_ow = input("File already exists. Do you want to overwrite it (Y/N)? ")
            while option_ow == 'Y' or 'y':
                file = open(file_name, 'w')
                while appt_type != 0:
                    client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
                    appointment = find_appointment_by_time(appointment_list, day_of_week, int(start_time_hour))
                    print(f"{len(appointment_list)} appointments saved to {file_name}.")
                file.close()
                file_name = input("Enter appointment filename: ")
        else:
            file = open(file_name, 'x')   
            
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
    create_weekly_calendar()
    print("Weekly Calendar Created")
    option_load = input("Would you like to load previously scheduled appointments from a file (Y/N)?: ")
    if option_load == 'Y' or 'y':
        load_scheduled_appointments()
   
    menu = print_menu()
    while menu in ['1', '2', '3', '4', '9']:
        menu = print_menu()
        if menu == '1':
            appointment_list = create_weekly_calendar()
            print("** Schedule an appointment **")
            day = input("What day: ")
            start_time_hour = int(input("Enter start hour(24 hour clock): "))
            client_name = input("Client name: ")
            client_phone = input("Client phone: ")
            print("Appointment types")
            print(Appointment.get_appt_type_desc)
            appt_type = int(input("Type of Appointment: ")) # 3 wat branch here for all three posssibilitys
            appointment = find_appointment_by_time(day, start_time_hour, appointment_list)
            if appointment and Appointment.get_appt_type() == 0:
                Appointment.schedule(client_name, client_phone, appt_type)
                print(f"Ok, {client_name}'s appointment is scheduled!")
            else:
                print("Sorry that time slot is not in the weekly calendar!")
 
 
        elif menu == '2':
            show_appointment_by_name(appointment_list)
 
        elif menu == '3':
            show_appointments_by_day(appointment_list)
           
        elif menu == '4':
            print("** Cancel an appointment **")
            enter_day = input("What day: ")
            start_hour = input("Enter start hour (24 hour clock): ") # call find by time to find index, and thenv have the three possibilitys again and then have the appointments is booked and go ahead and cancel
            # find from the method
            current_appt = appointment_list[start_hour]
            current_appt.cancel()
            start_hour_end = start_hour + 1
            print(f"Appointment: {enter_day} for {start_hour}-{start_hour_end} has been cancelled!")
        else:
            print('\n**Exit System**')
            save_scheduled_appointments(appointment_list)
   
 
if __name__ == "__main__":
    main()
