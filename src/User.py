import main
import pandas as pd
import random

class AvailableFlights:

    def __init__(self, first, last, email, starting, destination, payment):
        self.firstName = first
        self.lastName = last
        self.email = email
        self.startingPoint = starting
        self.destination = destination
        self.paymentMethod = payment

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

class User(Payment):
    def __init__(self, first, last, email, starting, destination, payment):
        super().__init__(first, last, email, starting, destination, payment)
        self.seatBooked = None

    def statusCheck(self):
        if self.transactionStatus:
            self.seatBooked = True
        else:
            self.seatBooked = False

    def setSeatNumber(self, flightClass, preference):
        frame = pd.DataFrame(None, [n for n in range(1, 24, 1)], ['A', 'B', 'C'])
        requiredFrame = frame.loc[[n for n in range(1, 24)], 'A']
        if preference.lower() == "window":
            allTaken = 0
            for i in range(1, 24):
                if pd.isnull(requiredFrame[i])
                    requiredFrame[i] = "Taken"
                    break
                else:
                    allTaken += 1
            if allTaken == 23:
                print("Sorry but all the window seats are taken")
            else:
                print("All done")

















