import pandas as pd
import pysolr
import os

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# Read the toxic tweet data from csv file
directory = find("sample_data.csv", ".")
tweets = pd.read_csv(directory, dtype={'id': str})

# Re-structure raw data for indexing
data = [{"id": index, "tweet": row["text"], "user_location": row["user_location"], "link": row["url"],  \
    "user_geo": list(map(float, row["user_geo"].strip("()").split(","))), \
    "toxicity": row["toxicity"], "subjectivity": row["subjectivity"]} \
    for index, row in tweets.iterrows()]

# Index and add data to Solr with core 'toxictweets'
solr = pysolr.Solr("http://localhost:8983/solr/toxictweets", always_commit=True)
print("Add data to Solr:")
print(solr.add(data))

# Test indexed data
query = "shit"
query_search = "tweet: %s" % (query)
fl_search = "id,tweet"

search_results = solr.search(query_search, **{
    'fl': fl_search
}, rows=15)

for result in search_results:
    print(result["id"], result["tweet"])
