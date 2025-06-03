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

#had chat_gpt also rename my variables as my program kept crashing from similar names

def hours_to_minutes(hours):
    minutes = hours * 60
    return minutes
#this is to turn hours into minutes (had to consult google)

def convert_time_to_minutes(time_string):
    #Using Chatgpt I learned what a function is and how to implement it in code. Def defines the string stated above
    #this current function turns "HH:MM AM/PM" into total minutes as stated in the while loop below
    time_string = time_string.strip().upper()
    #chatgpt explains that
    #strip -> removes excess spaces in front or behind user input
    #upper -> capitalizes AM PM
    if "AM" in time_string:
        time_of_day = "AM"
        #Chatgpt has taught I can use the variable inside of the defined word (time_string insode of covert_minutes_to_time).
    elif "PM" in time_string:
        time_of_day = "PM"
        #PM is a repeat of AM
    else:
        print("Time must include AM or PM.")
        return None
        #Used Chatgpt to learn the return None function
    
    # Remove AM/PM to split time
    time_part = time_string.replace("AM", "").replace("PM", "").strip()


    if ":" not in time_part:
        print("Please use HH:MM format.")
        return None
        #This was created in order to require the user to enter a valid time so a time like 12 45 would not function in the program.
        #I have also learned "in" and "not in" from Chatgpt

    hour_str = time_part.split(":")
    minute_str = time_part.split(":")
    #These were created in order to separate the hours and minutes but have them on the same line
    #Learned .split ability from Chatgpt

    #original code that did not work:
    # if not (hour_str.isdigit() and minute_str.isdigit()):
    #     print("Hour and minute must be numbers.")
    #     return None
    #This is to prevent the user from inputting anything besides numbers

    parts = time_part.split(":")
    #chatgpt explaisn that part splits a string into a list. Ex: 2:45 ["2", "45"]
    if len(parts) != 2:
        #!= means not equal to
        #2 is because there will be two items in the list
        print("Time must be in HH:MM format.")
        return None

    hour_str, minute_str = parts

    if not (hour_str.isdigit() and minute_str.isdigit()):
        print("Hour and minute must be numbers.")
        return None


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

    if time_of_day == "AM":
        if hour == 12:
            hour = 0
    #chatgpt taught:
    elif time_of_day == "PM":
        if hour != 12:
            #!= is a fancy sign for not equal to
            hour += 12
            #+= adds numbers (in this case 12) to original variable
    #all of the above converts 24 hrs into a 12hr formula

    total_minutes = hour * 60 + minute
    return total_minutes
    #multiply the number hour with 60 (as 60 minutes = 1 hr) and then add left over minutes

def convert_minutes_to_time(total_minutes):
    #this uses the left over minutes and turns it into "HH:MM AM/PM" format 

    total_minutes = total_minutes % 1440 
    #1440 minutes in 24hrs
    #uses modulo because it keeps balanced 12 frame
    #needed chatgpt for this because I've never used modulo before and generally don't now when to apply it to code 
    #(so the same goes for minute = total_minutes % 60)

    hour_24 = total_minutes // 60
    #learned when to use // (as it is to remove decimals)
    minute = total_minutes % 60

    if hour_24 == 0:
        hour_12 = 12
        time_of_day = "AM"
    elif hour_24 < 12:
        hour_12 = hour_24
        time_of_day = "AM"
    elif hour_24 == 12:
        hour_12 = 12
        time_of_day = "PM"
    else:
        hour_12 = hour_24 - 12
        time_of_day = "PM"

    return f"{hour_12:02d}:{minute:02d} {time_of_day}"
    #there is the variable and then :02d. 
    #:02d means : -> start of format
    #0 -> filler
    #2 -> two characters
    #d -> decimals



# while True:
#     #step one: ask user for time in a format (print or input, mainly input tho)
#     current_time = input("Please enter the current time or enter 'q' to quit: ")
#     if current_time == "q":
#         break
#     #chatgpt fixed my coding errors...I still don't exactly know what I did wrong
#     minutes = convert_time_to_minutes(current_time)
#     if minutes is None:
#         print("Cannot compute. Try again.")
#         continue

#     print(f"Current time in minutes: {minutes}")

#     #What I originally had
#     # if current_time > 12 or current_time < 1:
#     #     print("Cannot compute")
#     #     running = False
#     # else:
#     #     print(f"Current time is: {current_time}")
#     #     running = True
    
#     #step two: once gathered time from user, ask the user to input how many more minutes ahead of time they desire (ex, 11:59pm, user ticks 1 minute ahead, new time is 12:00 AM)
#     desired_speed = input("Please enter how many minutes you wish to speed ahead to: ")
#     desired_speed = input()
#     if desired_speed is None:
#         continue
#         #Using Chatgpt, I have discovered a way to get the user to re-enter their desired speed if they don't user numbers. I have learned you can simply write out
#         #is None and python will understand it.

#     if not desired_speed.isdigit():
#         print("Please enter a whole number of minutes.")
#         continue
#         #this has a similar feature to the one above (also created from Chatgpt).
    
#     desired_speed = convert_minutes_to_time(current_time)
    
#     minutes_to_add = int(desired_speed)

#     new_minutes = current_time + minutes_to_add
#     new_time = convert_minutes_to_time(new_minutes)



while True:
    current_time = input("Please enter the current time or enter 'q' to quit: ")
    if current_time.lower() == "q":
        break
 #chatgpt fixed my coding errors...I still don't exactly know what I did wrong

    # Convert clock input to minutes
    minutes = convert_time_to_minutes(current_time)

    if minutes is None:
        print("Cannot compute. Try again.")
        continue

    # Ask how many minutes to fast forward
    desired_speed = input("How many minutes to add?: ")

    if not desired_speed.isdigit():
        print("Please enter a whole number.")
        continue

    minutes_to_add = int(desired_speed)

    # Add and convert back to time format
    new_minutes = minutes + minutes_to_add
    new_time = convert_minutes_to_time(new_minutes)

    print(f"New time: {new_time}")