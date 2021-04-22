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
        self.airlineName = airline
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
        cost = self.distance * 5
        return cost

    def transactionProcess(self):  # Takes in pin/upiid and returns whichever is required
        if self.paymentMethod == "PayTM":
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
        try:  # AIRLINE_NAME + FLIGHT_NUMBER
            x = open(path_to_requiredFrame)
            frame = pd.read_csv(path_to_requiredFrame)
        except IOError:
            frame = pd.DataFrame(None, [n for n in range(1, 24, 1)], ['A', 'B', 'C'])  # If it can't find the csv
            # file it creates an empty database
            frame.to_csv(path_to_requiredFrame, index=False)  # and creates a csv file with the said convention
        requiredFrame = frame.loc[:, "A"]

        if preference.lower() == "window":  # if preference is window then it checks if any of the A
            allTaken = 0  # seats are empty if not returns message that window seats
            for i in range(1, 24):  # are full
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

        if preference.lower() == 'aisle':  # if preference is aisle seat then first the B seats are checked
            BFilled = False  # if they are full, then C seats are checked
            for i in range(0, 24):  # if c seats are full, then flight is completely booked is printed
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
