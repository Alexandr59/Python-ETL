import pandas as pd

flightsDataFrame = pd.read_csv('../data/flights.csv')
flightsDataFrame = flightsDataFrame.loc['2020-04-01':]

usersDataFrame = pd.read_csv('../data/users.csv')
usersDataFrame = usersDataFrame[(usersDataFrame['gender'] == 'female') & (usersDataFrame['age'] > 35)]

hotelsDataFrame = pd.read_csv('../data/hotels.csv')

result = pd.DataFrame(flightsDataFrame.join(usersDataFrame.set_index('code'), on='userCode')
                      .join(hotelsDataFrame.set_index('travelCode'), on='travelCode', lsuffix='_left', rsuffix='_right')
                      )

result.to_parquet('../result/result.parquet')
