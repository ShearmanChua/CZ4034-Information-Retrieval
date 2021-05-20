import twint
from randomDate import random_dates

start = "2013-01-01 00:00:00"
end = "2019-01-01 00:00:00"
dates = random_dates("2008-01-01 00:00:00","2021-01-01 00:00:00", numOfDates=4)
dates.append(end)
for date in dates:
    c = twint.Config()
    # search random tweets with alphabet letters
    c.Lang = "en"
    c.Search = "e OR a OR r"
    c.Store_csv = True
    c.Limit = 1000
    c.Output = "random_tweets.csv"
    c.Until = date
    twint.run.Search(c)
