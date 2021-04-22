import main

'''Takes in firstName lastName email starting airport and destination airport as parameters which are given in 
main.py file'''


def userInput(first, last, email, starting, destination):
    valid = True
    while True:
        if len(first) < 2:  # The firstName should be at least 2 characters long
            valid = False
            print("Enter valid first name")
            return valid

        if len(last) < 2:  # The lastName should also be at least 2 characters long
            valid = False
            print("Enter valid last name")
            return valid
        emailCount = 0
        for i in email:  # For email '@' must be present.   may add more checks later
            if i == '@':
                valid = True
                return valid
            else:
                emailCount += 1
                valid = False
        if valid == False:
            print("Enter valid email ID")
            return valid
        startingFlights = main.requiredDf["ORIGIN_AIRPORT"].str.contains(starting)
        for i in startingFlights:  # Checks if the origin airport exists in the database
            if i == True:
                valid = True
                return valid
            else:
                valid = False
        if valid == False:
            print("Enter valid origin airport")
            return valid
        endingFlights = main.requiredDf["DESTINATION_AIRPORT"].str.contains(destination)
        for i in endingFlights:  # Checks if the destination airport exists in the database
            if i == True:
                valid = True
                return valid
            else:
                valid = False
        if valid == False:
            print("Enter valid destination airport")
            return valid
