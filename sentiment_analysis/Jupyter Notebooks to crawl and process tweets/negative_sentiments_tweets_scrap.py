import twint

config = twint.Config()
# config.Username = "YahooFinance"
config.Lang = "en"
config.Limit = 1000
config.Search = "fuck you OR fuck off OR screw you OR dumbass OR fucking bitch OR asshole"
config.Since = "2001-01-01 00:00:00"
config.Until = "2022-01-01 00:00:00"
config.Store_csv = True
config.Output = "tweets/toxic_tweets_1.csv"
config.Hide_output = True
#running search
twint.run.Search(config)

config = twint.Config()
# config.Username = "YahooFinance"
config.Lang = "en"
config.Limit = 1000
config.Search = "go to hell OR go and die OR hope you die"
config.Since = "2001-01-01 00:00:00"
config.Until = "2022-01-01 00:00:00"
config.Store_csv = True
config.Output = "tweets/toxic_tweets_2.csv"
config.Hide_output = True
#running search
twint.run.Search(config)

config = twint.Config()
# config.Username = "YahooFinance"
config.Lang = "en"
config.Limit = 1000
config.Search = "whore OR slut"
config.Since = "2001-01-01 00:00:00"
config.Until = "2022-01-01 00:00:00"
config.Store_csv = True
config.Output = "tweets/toxic_tweets_3.csv"
config.Hide_output = True
#running search
twint.run.Search(config)

config = twint.Config()
# config.Username = "YahooFinance"
config.Lang = "en"
config.Limit = 1000
config.Search = "you loser OR you are a loser OR what a loser"
config.Since = "2001-01-01 00:00:00"
config.Until = "2022-01-01 00:00:00"
config.Store_csv = True
config.Output = "tweets/toxic_tweets_4.csv"
config.Hide_output = True
#running search
twint.run.Search(config)

config = twint.Config()
# config.Username = "YahooFinance"
config.Lang = "en"
config.Limit = 1000
config.Search = "retard OR stupid OR dumb"
config.Since = "2001-01-01 00:00:00"
config.Until = "2022-01-01 00:00:00"
config.Store_csv = True
config.Output = "tweets/toxic_tweets_5.csv"
config.Hide_output = True
#running search
twint.run.Search(config)