import User
import pandas as pd

def openBankCSV():
    file = pd.read_csv('../resources/bank.csv')
    df = pd.DataFrame(file)
    return df

def openPayCSV():
    file = pd.read_csv('../resources/paytm.csv')
    df = pd.DataFrame(file)
    return df

def deductBalanceBank(pin, cost):
    df = openBankCSV()
    requiredColumn = df.loc[df.PIN == pin]
    balance = requiredColumn.at[0, 'Balance']
    finalAmount = balance - cost
    requiredColumn.at[0, 'Balance'] = finalAmount
    requiredColumn.to_csv('../resources/bank.csv')
    return finalAmount

def deductBalancePayTM(UpiID, cost):
    df = openPayCSV()
    requiredColumn = df.loc[df.UPI_ID == UpiID]
    balance = requiredColumn.at[0, 'Balance']
    finalAmount = balance - cost
    requiredColumn.at[0, 'Balance'] = finalAmount
    requiredColumn.to_csv('../resources/paytm.csv')
    return finalAmount
