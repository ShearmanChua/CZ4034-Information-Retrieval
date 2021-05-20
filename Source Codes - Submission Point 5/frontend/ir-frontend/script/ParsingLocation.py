import requests
import json


class ParsingLocation:
    def __init__(self):
        r = requests.get(
            'http://localhost:8983/solr/toxictweets/select?q=*:*&rows=100000')
        self.tweets = r.json()['response']['docs']

        self.country_count = {}
        self.geo_locations = []

    def parseLocation(self):
        for tweet in self.tweets:
            country = tweet['user_location'][0].split(",")[-1].strip()
            if country not in self.country_count:
                self.country_count[country] = 0
            self.country_count[country] += 1
            user_geo = tweet['user_geo'][0][1:-1].split(",")
            longi, lati = float(user_geo[0]), float(user_geo[1])
            geo_location = {}
            geo_location['CountryName'] = country
            geo_location['Longitudinal'] = longi
            geo_location['Latitudinal'] = lati
            self.geo_locations.append(geo_location)

        return self.country_count, self.geo_locations
        # return json.dumps(self.country_count), json.dumps(self.geo_locations)


p = ParsingLocation()
res = p.parseLocation()
loc = res[0]
print(loc)
print(json.dumps(loc))
# print(res[0])
# print(res[1][0])
