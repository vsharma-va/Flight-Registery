import pandas as pd

'''Imports the bank.csv file and returns it as a dataframe.'''


def openBankCSV():
    file = pd.read_csv('../resources/bank.csv')
    df = pd.DataFrame(file)
    return df


'''Imports the paytm.csv file and returns it as a dataframe'''


def openPayCSV():
    file = pd.read_csv('../resources/paytm.csv')
    df = pd.DataFrame(file)
    return df


'''It takes pin and cost as parameters which are given in the main.py file 
In main.py the user enters the pin and the cost is taken from the Payment class in User.py'''


def deductBalanceBank(pin, cost, name):
    df = openBankCSV()
    requiredColumn = df.loc[df.PIN == pin]
    balance = requiredColumn.at[0, 'Balance']
    finalAmount = balance - cost
    requiredColumn.at[0, 'Balance'] = finalAmount
    df.to_csv('../resources/bank.csv')
    return finalAmount


'''If the user enters payment method as paytm then the user will have to enter the upiid instead of pin number
The upiid of every person is in the paytm.csv file'''


def deductBalancePayTM(UpiID, cost, name):
    df = openPayCSV()
    requiredColumn = df.loc[df.UPI_ID == UpiID]
    balance = requiredColumn.at[0, 'Balance']
    finalAmount = balance - cost
    requiredColumn.at[0, 'Balance'] = finalAmount
    df.to_csv('../resources/paytm.csv')
    return finalAmount
