import main
import pandas as pd
import os.path


class AvailableFlights:

    def __init__(self, first, last, email, starting, destination, payment):
        self.firstName = first
        self.lastName = last
        self.email = email
        self.startingPoint = starting
        self.destination = destination
        self.paymentMethod = payment
        self.choosenFlight = None

    def getAllFlights(self):
        self.allFlights = main.requiredDf.loc[(main.requiredDf.ORIGIN_AIRPORT == self.startingPoint) &
                                         (main.requiredDf.DESTINATION_AIRPORT == self.destination)]
        return self.allFlights

    def chooseFlight(self, airline, number):
        self.airlineName = airline
        self.airlineNumber = number
        self.choosenFlight = self.allFlights.loc[(self.allFlights.AIRLINE == self.airlineName) &
                                            (self.allFlights.FLIGHT_NUMBER == self.airlineNumber)]
        return self.choosenFlight


class Distance(AvailableFlights):

    def __init__(self, first, last, email, starting, destination, payment):
        super().__init__(first, last, email, starting, destination, payment)
        self.distance = None

    def getDistance(self):
        y = self.choosenFlight
        self.distance = y.loc[:,"DISTANCE"]
        return self.distance

class Payment(Distance):

    def __init__(self, first, last, email, starting, destination, payment):
        super().__init__(first,  last, email, starting, destination, payment)
        self.transactionStatus = None

    def calculateCost(self):
        cost = self.distance * 5
        return cost

    def transactionProcess(self):
        if self.paymentMethod == "PayTM":
            number = int(input("Enter your UPI ID"))
            self.complete = True
        elif self.paymentMethod == "Bank":
            account = int(input("Enter your pin"))
            self.transactionStatus = True
        else:
            self.transactionStatus = False
        return "Complete"


class User(Payment):
    def __init__(self, first, last, email, starting, destination, payment):
        super().__init__(first, last, email, starting, destination, payment)
        self.seatBooked = None

    def statusCheck(self):
        if self.transactionStatus:
            self.seatBooked = True
        else:
            self.seatBooked = False
        return 'Seat Booked'

    def setSeatNumber(self, flightClass, preference):

        path_to_requiredFrame = '{}{}.csv'.format(self.choosenFlight.at[0, 'AIRLINE'], self.choosenFlight.at[0, 'FLIGHT_NUMBER'])
        try:
            x = open(path_to_requiredFrame)
            frame = pd.read_csv(path_to_requiredFrame)
        except IOError:
            frame = pd.DataFrame(None, [n for n in range(1, 24, 1)], ['A', 'B', 'C'])
            frame.to_csv(path_to_requiredFrame, index = False)
        requiredFrame = frame.loc[:, "A"]

        if preference.lower() == "window":
            allTaken = 0
            for i in range(1, 24):
                if pd.isnull(requiredFrame[i]):
                    requiredFrame[i] = self.firstName
                    frame.to_csv(path_to_requiredFrame, index = False)
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
            frame.to_csv(path_to_requiredFrame, index = False)
        requiredFrame1 = frame.loc[:, "B"]
        requiredFrame2 = frame.loc[:, "C"]

        if preference.lower() == 'aisle':
            BFilled = False
            for i in range(0, 24):
                if pd.isnull(requiredFrame1[i]):
                    requiredFrame1.iloc[i] = self.firstName
                    frame.to_csv(path_to_requiredFrame, index = False)
                    break
                else:
                    BFilled = True
            if BFilled == True:
                for i in range(0, 24):
                    if pd.isnull(requiredFrame2[i]):
                        requiredFrame2.iloc[i] = self.firstName
                        requiredFrame2.to_csv(path_to_requiredFrame)
                        break




















