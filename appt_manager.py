#
# appt_manager - This program tests the majority of the methods in the Appointment class
#
# Author: Nic Draffin, Jihun Gwak, Nara Park
# Version/Date: 2023-12-06
#

# imports
from datetime import datetime
from appointment import Appointment

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
            appointment_list.append(Appointment(day, hour))
    return appointment_list


def load_scheduled_appointments(appointment_list):
        file_name = input("Enter appointment filename: ")
        while file_name != file:
            if file_name == file:
                file = open(file_name, 'r')
                lines = file.readlines()
                for line in lines:
                    client_name, client_phone, appt_type, day_of_week, start_time_hour = line.strip().split(',')
                    appointment = find_appointment_by_time(day_of_week, int(start_time_hour), appointment_list)
                if appointment:
                    Appointment.schedule(client_name, client_phone, int(appt_type))
            else:
                filename = input("File not found. Re-enter appointment filename: ")
        
     
        return len(lines)

                
def find_appointment_by_time(day, start_time_hour, appointment_list):
    appointment_time = Appointment()
    for appointment in appointment_list:
        if appointment_time.get_day_of_week() == day and appointment_time.get_start_time_hour() == start_time_hour:
            return appointment
    return None
    


def show_appointment_by_name(appointment_list):
    print("** Find appointment by name **")
    client_name = input("Enter Client Name: ")
    print(f"Appointments for {client_name}")
    matching_appointments = [appointment for appointment in appointment_list if client_name.lower() in Appointment.get_client_name().lower()]
    if matching_appointments:
        for appointment in matching_appointments:
            print(Appointment.__str__(appointment))
    else:
        print("No appointments found.")

def show_appointments_by_day(appointment_list):
    print("** Print calendar for a specific day **")
    day_of_week = input("Enter day of week: ")
    print(f"Appointment for {day_of_week}")
    matching_appointments = [appointment for appointment in appointment_list if Appointment.get_day_of_week().lower() == day_of_week.lower()]
  
    for appointment in matching_appointments:
        print(Appointment.__str__(appointment))

def save_scheduled_appointments(appointment_list):
    option_save = input("Would nyou like to save all scheduled appointments to a file (Y/N)?")
    if option_save == 'Y' or 'y':
        file_name = input("Enter appointment filename: ")
        if file_name == file:


    if not filename(""):
        filename += ""
    try:
        with open(filename, 'w') as file:
            for appointment in appointment_list:
                if appointment.get_appt_type() != 0:
                    file.write(appointment.format_record() + "\n")
        print(f"{len(appointment_list)} appointments saved to {filename}.")
    except Exception as e:
        print(f"Error saving appointments: {e}")
        ####




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
def main(appointment_list):
    '''main function'''
    print("Starting the appointment Manager system")
    create_weekly_calendar()
    print("Weekly Calendar Created")
    option_load = input("Would you like to load previously scheduled appointments from a file (Y/N)?: ")
    if option_load == 'Y' or 'y':
        load_scheduled_appointments()
    else:
        pass
        

    menu = print_menu()
    while menu in ['1', '2', '3', '4', '9']:
        menu = print_menu()
        if menu == '1':
            print("** Schedule an appointment **")
            day = input("What day: ")
            start_time_hour = int(input("Enter start hour(24 hour clock): "))
            client_name = input("Client name: ")
            client_phone = input("Client phone: ")
            print("Appointment types")
            print(Appointment.get_appt_type_desc)
            appt_type = int(input("Type of Appointment: "))
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
            start_hour = input("Enter start hour (24 hour clock): ")
            current_appt = appointment_list[start_hour - 1]
            current_appt.remove()
            start_hour_end = start_hour + 1
            print(f"Appointment: {enter_day} for {start_hour}-{start_hour_end} has been cancelled!")
        else:
            print('\n**Exit System**')
            save_scheduled_appointments(appointment_list)
    

if __name__ == "__main__":
    main()
