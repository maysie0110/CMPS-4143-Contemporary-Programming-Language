# May Trinh
# CMPS 4143: Contemporary Programming Language
# 09/09/19
# Program 1
# The program will ask the users to enter a month, day, and 2-digit year in numeric format
# Determine if the date is a magic date by compare the product of month and day with year
# Limit users input for month, day, and year

import datetime 

print(""" May Trinh
 CMPS 4143: Contemporary Programming Language
 09/09/19
 Program 1 - The program will ask the users to enter a month, day, and 2-digit year in numeric format
 Determine if the date is a magic date by compare the product of month and day with year
 Limit users input for month, day, and year """)

while True: 
    try:
        # ask the user to enter date in a specific format
        inputDate = input("Enter the date in format mm/dd/yy:")

        # convert the input date into 3 numbers for month, day, and year
        month, day, year = map(int,inputDate.split("/"))
        # month, day, year = (int(x) for x in inputDate.split("/"))

        #limit year to 2 digit number
        if year > 99:
            raise Exception("Invalid year. Only 2-digit number year. Try Again!")
        
        # check for validation of input date
        datetime.datetime(year,month,day)
        break
    except ValueError as error:
        print("Oops. Invalid date. {0}. Try Again!". format(error))

    except Exception as err:
        print(err)

# Product of month and day
result = month * day 

#Compare with year
if result == year:
    # display message
    print("The date {0} is Magic" .format(inputDate))
else:
    print("The date {0} is not magic" .format(inputDate)) 
