import pandas as pd

'''these bank.csv and paytm.csv files must be in the same location as specified here
or change the location if they are present somewhere else '''

bankData = pd.read_csv("../resources/bank.csv")
paytmData = pd.read_csv("../resources/paytm.csv")

bankDf = pd.DataFrame(bankData)
paytmDf = pd.DataFrame(paytmData)


# it takes pin, cost, name from the main.py file

def deductBalanceBank(pin, cost, name):
    requiredDf = bankDf.loc[bankDf.Name == name]  # selects the row with user given name
    indexNumber = requiredDf.index.values[0]  # gets the index of the selected row
    password = requiredDf.at[indexNumber, 'PIN']  # gets the pin
    if password == pin:
        balance = requiredDf.at[indexNumber, 'Balance']
        if balance < cost:
            print("Not enough Balance")
        else:
            finalBalance = balance - cost
            file = open("../resources/bank.csv", 'w+')
            file.close()
            bankDf.at[indexNumber, 'Balance'] = finalBalance
            bankDf.to_csv("../resources/bank.csv")


def deductBalancePayTM(UpiID, cost, name):  # same as the above function with some different variables
    requiredDf = paytmDf.loc[paytmDf.Name == name]  # and file format
    indexNumber = requiredDf.index.values[0]
    password = requiredDf.at[indexNumber, 'upiid']
    if password == UpiID:
        balance = requiredDf.at[indexNumber, 'Balance']
        if balance < cost:
            print("Not enough balance")
        else:
            finalBalance = balance - cost
            file = open("../resources/paytm.csv", 'w+')
            file.close()
            paytmDf.at[indexNumber, 'Balance'] = finalBalance
            paytmDf.to_csv("../resources/paytm.csv")
