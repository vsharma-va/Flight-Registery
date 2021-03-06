import pandas as pd
import User

data = pd.read_csv('../resources/flights.csv', nrows = 1000)
df = pd.DataFrame(data)
requiredDf = df.loc[:, ['YEAR', "DAY_OF_WEEK", "AIRLINE", "FLIGHT_NUMBER", "TAIL_NUMBER",
            "ORIGIN_AIRPORT", "DESTINATION_AIRPORT", "SCHEDULED_DEPARTURE",
            "AIR_TIME", "DISTANCE", "SCHEDULED_ARRIVAL"]]

def main():


