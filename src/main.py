import pandas as pd
import User
import inputValidationFunctions
import AccountChecker

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 13)

data = pd.read_csv('../resources/flights.csv', nrows = 5000)
df = pd.DataFrame(data)
requiredDf = df.loc[:, ['YEAR', "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER", "TAIL_NUMBER",
            "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "SCHEDULED_DEPARTURE",
            "AIR_TIME", "DISTANCE", "SCHEDULED_ARRIVAL"]]

def main():
    correct = False

    '''Takes user input and then calls the input validation function. The input validation function simply returns true if everything is valid
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

    '''If all the inputs are valid then the value is sent to the user class in the User file where all of the dataframe operations and seat 
    assigning is done'''

    firstUser = User.User(first, last, email, starting, destination, paymentMethod)
    print(firstUser.getAllFlights())
    airline = input("Select the name of the airline: ")
    airlineNumber = int(input("Select the flight Number: "))
    print()
    print(firstUser.chooseFlight(airline, airlineNumber))
    firstUser.getDistance()
    print(firstUser.calculateCost())
    if paymentMethod == 'Bank':
        AccountChecker.deductBalanceBank(User.Payment.transactionProcess(firstUser), User.Payment.calculateCost(firstUser))
    elif paymentMethod == 'PayTM':
        AccountChecker.deductBalancePayTM(User.Payment.transactionProcess(firstUser), User.Payment.calculateCost(firstUser))
    print()
    firstUser.statusCheck()
    print()
    preference = input("Enter your preference window or aisle: ")
    firstUser.setSeatNumber(preference)

main()
