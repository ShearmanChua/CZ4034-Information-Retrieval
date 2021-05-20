import twint

c = twint.Config()
c.Search = "fuck OR shit OR dick OR asshole OR bitch"
c.Lang = "en"
c.Store_csv = True
c.Output = "HateToxicTweets.csv"
c.Limit = 10000
c.Hide_output = True
twint.run.Search(c)
