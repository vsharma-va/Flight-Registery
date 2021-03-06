import main


def userInput(first, last, email, starting, destination):
    valid = True
    notDone = True
    while True:
        if len(first) < 2:
            valid = False
            print("Enter valid first name")
            return valid

        if len(last) < 2:
            valid = False
            print("Enter valid last name")
            return valid
        emailCount = 0
        for i in email:
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
        for i in startingFlights:
            if i == True:
                valid = True
                return valid
            else:
                valid = False
        if valid == False:
            print("Enter valid origin airport")
            return valid
        endingFlights = main.requiredDf["DESTINATION_AIRPORT"].str.contains(destination)
        for i in endingFlights:
            if i == True:
                valid = True
                return valid
            else:
                valid = False
        if valid == False:
            print("Enter valid destination airport")
            return valid

