import main
import pandas as pd

'''Available Flights is the parent class'''


class AvailableFlights:

    def __init__(self, first, last, email, starting, destination, payment):
        self.firstName = first
        self.lastName = last
        self.email = email
        self.startingPoint = starting
        self.destination = destination
        self.paymentMethod = payment
        self.choosenFlight = None

    def getAllFlights(self):  # Gets all the flights which operate between the user defined airports
        self.allFlights = main.requiredDf.loc[(main.requiredDf.ORIGIN_AIRPORT == self.startingPoint) &
                                              (main.requiredDf.DESTINATION_AIRPORT == self.destination)]
        return self.allFlights

    def chooseFlight(self, airline, number):  # selects the flight which the user wants and returns it
        self.airlineName = airline          # if it doesn't find any flights returns a blank list
        self.airlineNumber = number
        self.choosenFlight = self.allFlights.loc[(self.allFlights.AIRLINE == self.airlineName) &
                                                 (self.allFlights.FLIGHT_NUMBER == self.airlineNumber)].reset_index()
        return self.choosenFlight


class Distance(AvailableFlights):

    def __init__(self, first, last, email, starting, destination, payment):
        super().__init__(first, last, email, starting, destination, payment)
        self.distance = None

    def getDistance(self):  # simply gets the distance column for the chosen flight
        y = self.choosenFlight
        self.distance = y.at[0, 'DISTANCE']
        return self.distance


class Payment(Distance):

    def __init__(self, first, last, email, starting, destination, payment):
        super().__init__(first, last, email, starting, destination, payment)
        self.transactionStatus = None

    def calculateCost(self):  # calculates the cost of the ticket based on the cost per km
        costPerKM = 5         # taken as 5
        cost = self.distance * costPerKM
        return cost

    def transactionProcess(self):  # Takes in pin/upiid and returns whichever is required
        if self.paymentMethod == "PayTM": # this is required for the functions in AccountChecker.py
            number = int(input("Enter your UPI ID"))
            self.transactionStatus = True
            return number
        elif self.paymentMethod == "Bank":
            account = int(input("Enter your pin"))
            self.transactionStatus = True
            return account
        else:
            self.transactionStatus = False


class User(Payment):
    def __init__(self, first, last, email, starting, destination, payment):
        super().__init__(first, last, email, starting, destination, payment)
        self.seatBooked = None

    def statusCheck(self):
        if self.transactionStatus:
            self.seatBooked = True
        else:
            self.seatBooked = False

    def setSeatNumber(self, preference):
        flightName = self.choosenFlight.at[0, 'AIRLINE']
        flightNumber = self.choosenFlight.at[0, 'FLIGHT_NUMBER']

        path_to_requiredFrame = '{}{}.csv'.format(flightName,
                                                  flightNumber)  # naming convention for the csv file for each file is

        '''This try and except block looks for a file with the naming convention written above.
        If it isn't able to find the file then it creates an empty database with 3 columns with 23 rows each.
        23 rows is taken as the number of seats in a single column.'''

        try:
            x = open(path_to_requiredFrame)
            frame = pd.read_csv(path_to_requiredFrame)
        except IOError:
            frame = pd.DataFrame(None, [n for n in range(1, 24, 1)], ['A', 'B', 'C'])  # If it can't find the csv
            frame.to_csv(path_to_requiredFrame, index=False)  # file it creates an empty database
        requiredFrame = frame.loc[:, "A"]  # and creates a csv file with the said convention

        '''If preference is window then it checks if any of the A seats are empty if not returns message
        saying that window seats are full.'''

        if preference.lower() == "window":
            allTaken = 0
            for i in range(1, 24):
                if pd.isnull(requiredFrame[i]):
                    requiredFrame[i] = self.firstName
                    frame.to_csv(path_to_requiredFrame, index=False)
                    break
                else:
                    allTaken += 1
            if allTaken == 23:
                print("Sorry but all the window seats are taken")
            else:
                print("All done")
        try:
            requiredFrame = open(path_to_requiredFrame)
            frame = pd.read_csv(path_to_requiredFrame)
        except IOError:
            frame = pd.DataFrame(None, [n for n in range(1, 24, 1)], ['A', 'B', 'C'])
            frame.to_csv(path_to_requiredFrame, index=False)
        requiredFrame1 = frame.loc[:, "B"]
        requiredFrame2 = frame.loc[:, "C"]

        '''If preference is aisle seat then first the B seats are checked if they are full, then C seats
        are checked and if they are also full then flight is completely booked is printed'''

        if preference.lower() == 'aisle':
            BFilled = False
            for i in range(0, 24):
                if pd.isnull(requiredFrame1[i]):
                    requiredFrame1.iloc[i] = self.firstName
                    frame.to_csv(path_to_requiredFrame, index=False)
                    break
                else:
                    BFilled = True
            counter = 0
            if BFilled == True:
                for i in range(0, 24):
                    if pd.isnull(requiredFrame2[i]):
                        requiredFrame2.iloc[i] = self.firstName
                        frame.to_csv(path_to_requiredFrame, index=False)
                        break
                    else:
                        counter += 1
                if counter == 23:
                    print("The flight is completely booked")
