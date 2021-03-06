import pandas as pd
import User
import inputValidationFunctions

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 13)

data = pd.read_csv('../resources/flights.csv', nrows = 1000)
df = pd.DataFrame(data)
requiredDf = df.loc[:, ['YEAR', "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER", "TAIL_NUMBER",
            "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "SCHEDULED_DEPARTURE",
            "AIR_TIME", "DISTANCE", "SCHEDULED_ARRIVAL"]]

def main():
    correct = False
    while not correct:
        first = input("Enter your first name")
        last = input("Enter your last name")
        email = input("Enter your email ID")
        destination = input("Enter your destination")
        starting = input("Enter the starting airport")
        correct = inputValidationFunctions.userInput(first, last, email, destination, starting)
    paymentMethod = input("Enter the payment method:"
                          "PayTM or Bank")
    firstUser = User.User(first, last, email, starting, destination, paymentMethod)
    print(firstUser.getAllFlights())
    airline = input("Select the name of the airline: ")
    airlineNumber = int(input("Select the flight Number: "))
    print()
    print(firstUser.chooseFlight(airline, airlineNumber))
    firstUser.getDistance()
    print(firstUser.calculateCost())
    print()
    print(firstUser.transactionProcess())
    print()
    firstUser.statusCheck()
    print()
    preference = input("Enter your preference window or aisle: ")
    firstUser.setSeatNumber(preference)

main()
