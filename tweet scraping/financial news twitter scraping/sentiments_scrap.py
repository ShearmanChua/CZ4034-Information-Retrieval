import twint

config = twint.Config()
config.Username = "YahooFinance"
config.Lang = "en"
config.Limit = 1000
config.Since = "2021-01-01 00:00:00"
config.Until = "2022-01-01 00:00:00"
config.Store_csv = True
config.Output = "tweets/bloomberg_financial_news_sentiments_test.csv"
#running search
twint.run.Search(config)

config = twint.Config()
config.Username = "business"
config.Lang = "en"
config.Limit = 1000
config.Since = "2021-01-01 00:00:00"
config.Until = "2022-01-01 00:00:00"
config.Store_csv = True
config.Output = "tweets/bloomberg_financial_news_sentiments.csv"
#running search
twint.run.Search(config)

