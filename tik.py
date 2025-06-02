#SMD: This progam will take in user input  in the format of HH:MM 
#where the digits can represent any valid 12 hr clock time
#for example, 01:59 would be 01:59 would be AM or PM
#after taking in a time, 1 more user input will be a positive interger which ticks the clock foward that many minutes and displays the new
#maybe use modules
#Will be tested from numbers ranging through 0-125
#bonus1): handle seconds also, so instead of taking minutes to tick foward, it will take seconds to tick foward
#bonus 2): handles AM and PM
#Program will politely and clearly ask the user to put in the required information
#time + 1 minute
#convert the hours into minutes

def convert_time_to_minutes(time_string):
    # This function turns 
    # "HH:MM AM/PM" into total minutes. Does a number reset after 12.

    time_string = time_string.strip().upper()  # Clean and uppercase input like '11:30 pm' → '11:30 PM'
    #Using Chatgpt, I have created a variable that not only capitalizes AM and PM but fixes messy input
    # ex: " 9: 15 pm" -> "9:15 PM" 

    if "AM" in time_string:
        period = "AM"
        time_part = time_string.replace("AM", "").strip()
    elif "PM" in time_string:
        period = "PM"
        time_part = time_string.replace("PM", "").strip()
        #PM is a repeat of AM
    else:
        print("Time must include AM or PM.")
        return None
        #Used Chatgpt to learn the return None function

    if ":" not in time_part:
        print("Please use HH:MM format.")
        return None
        #This was created in order to require the user to enter a valid time so a time like 12 45 would not function in the program

    hour_str, minute_str = time_part.split(":")
    #This was created in order to separate the hours and minutes but have them on the same line

    if not (hour_str.isdigit() and minute_str.isdigit()):
        print("Hour and minute must be numbers.")
        return None
    #This is to prevent the user from inputting anything besides numbers

    hour = int(hour_str)
    minute = int(minute_str)

    if hour < 1 or hour > 12:
        #After consulting google, this was the best solution to keep the numbers in a 1-12 range
        print("Hour must be between 1 and 12.")
        return None
    if minute < 0 or minute >= 60:
        #this turns 1 hr into minutes and anything in between
        print("Minutes must be between 0 and 59.")
        return None

    # converts to 24-hour style in minutes (needed chatgbt on this)
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    total_minutes = hour * 60 + minute
    return total_minutes
    #multiply the number hour with 60 (as 60 minutes = 1 hr) and then add left over minutes


def convert_minutes_to_time(total_minutes):
    #this uses the left over minutes and turns it into "HH:MM AM/PM" format 

    total_minutes = total_minutes % 1440 
    #1440 minutes in 24hrs
    #uses modulo because it keeps balanced 12 frame

    hour_24 = total_minutes // 60
    minute = total_minutes % 60

    if hour_24 == 0:
        hour_12 = 12
        period = "AM"
    elif hour_24 < 12:
        hour_12 = hour_24
        period = "AM"
    elif hour_24 == 12:
        hour_12 = 12
        period = "PM"
    else:
        hour_12 = hour_24 - 12
        period = "PM"

    return f"{hour_12:02d}:{minute:02d} {period}"


#main program loop
while True:
    print("\nWelcome to the Simple 12-Hour Clock!")

    #step 1: ask for time
    user_time = input("Enter current time (e.g., 11:30 AM), or Q to quit: ")

    if user_time.strip().lower() == "q":
        print("Goodbye!")
        break

    minutes_now = convert_time_to_minutes(user_time)

    if minutes_now is None:
        continue  # Ask again if input was invalid

    #step 2: ask how many minutes to add
    minutes_to_add_input = input("How many minutes do you want to add? ")

    if not minutes_to_add_input.isdigit():
        print("Please enter a whole number of minutes.")
        continue

    minutes_to_add = int(minutes_to_add_input)

    #step 3: calculate new time
    new_minutes = minutes_now + minutes_to_add
    new_time = convert_minutes_to_time(new_minutes)

    #step 4: show the result
    print(f"\n⏰ New time is: {new_time}")