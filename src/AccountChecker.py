import pandas as pd

bankData = pd.read_csv("../resources/bank.csv")
paytmData = pd.read_csv("../resources/paytm.csv")

bankDf = pd.DataFrame(bankData)
paytmDf = pd.DataFrame(paytmData)


def deductBalanceBank(pin, cost, name):
    requiredDf = bankDf.loc[bankDf.Name == name]
    indexNumber = requiredDf.index.values[0]
    password = requiredDf.at[indexNumber, 'PIN']
    if password == pin:
        balance = requiredDf.at[indexNumber, 'Balance']
        if balance < cost:
            print("Not enought Balance")
        else:
            finalBalance = balance - cost
            file = open("../resources/bank.csv", 'w+')
            file.close()
            bankDf.at[indexNumber, 'Balance'] = finalBalance
            bankDf.to_csv("../resources/bank.csv")


def deductBalancePayTM(UpiID, cost, name):
    requiredDf = paytmDf.loc[paytmDf.Name == name]
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
    