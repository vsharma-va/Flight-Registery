import pandas as pd
import User
import inputValidationFunctions
import AccountChecker

# Run The user.py file only

# Pandas options to display more columns and rows
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# The data contains more than 20000 rows
# therefore i have limited it to 7000 rows
# if you want more rows you can change the nrows to a bigger number
data = pd.read_csv('../resources/flights.csv', nrows=7000)
df = pd.DataFrame(data)
requiredDf = df.loc[:, ['YEAR', "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER", "TAIL_NUMBER",
                        "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "SCHEDULED_DEPARTURE",
                        "AIR_TIME", "DISTANCE", "SCHEDULED_ARRIVAL"]]


'''correct variable is used in the while loop to check whether to ask the user for their details again or
not. Correct variables bool value comes from inputValidationFunctions.py

displayMoreFlights is a sentinel variable. It is used in the while loop to stop displaying more rows
from the database. As the database is fairly large the rows are displayed in chunks of 100

maxRowsToDisplay is used to control the maximum amount of rows displayed at once
displayRowsFrom is used as a start point. The rows are displayed from displayRowsFrom to maxRowsToDisplay'''

def main():
    correct = False
    displayMoreFlights = 1
    maxRowsToDisplay = 100
    displayRowsFrom = 0
    rowsToDisplayAtOnce = 100

    while displayMoreFlights != 0:
        print(requiredDf.iloc[displayRowsFrom:maxRowsToDisplay, :])
        maxRowsToDisplay += rowsToDisplayAtOnce
        displayRowsFrom += rowsToDisplayAtOnce
        displayMoreFlights = int(input('Press any number to display more rows or press 0 to stop: '))

    '''Takes user input and then calls the input validation function. The input validation function simply returns 
    true if everything is valid
    else it returns false and user has to enter the details again till he/she gets it right'''

    while not correct:
        first = input("Enter your first name")
        last = input("Enter your last name")
        email = input("Enter your email ID")
        destination = input("Enter your destination")
        starting = input("Enter the starting airport")
        correct = inputValidationFunctions.userInput(first, last, email, destination, starting)
    paymentMethod = input("Enter the payment method:\n"
                          "PayTM or Bank")

    '''If all the inputs are valid then the value is sent to the user class in the User file where all of the 
    dataframe operations and seat 
    assigning is done'''

    firstUser = User.User(first, last, email, starting, destination, paymentMethod)
    print(firstUser.getAllFlights())
    airline = input("Select the name of the airline: ")
    airlineNumber = int(input("Select the flight Number: "))
    print()
    print(firstUser.chooseFlight(airline, airlineNumber))
    firstUser.getDistance()
    print('\n', 'Cost: ', firstUser.calculateCost())
    if paymentMethod == 'Bank':
        AccountChecker.deductBalanceBank(User.Payment.transactionProcess(firstUser),
                                         User.Payment.calculateCost(firstUser), first)
    elif paymentMethod == 'PayTM':
        AccountChecker.deductBalancePayTM(User.Payment.transactionProcess(firstUser),
                                          User.Payment.calculateCost(firstUser), first)
    print()
    firstUser.statusCheck()
    print()
    preference = input("Enter your preference window or aisle: ")
    firstUser.setSeatNumber(preference)


main()
