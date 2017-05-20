import pandas as pd
import json
import numpy as np
keyword_ff = ['fast furious','fast n furious','fast and furious','ff8','fast & furious','fast furious 8','fast n furious 8','fast and furious 8','fast & furious 8']
keyword_gotg = ['guardians of the galaxy','gotg','guardians of the galaxy vol. 2','gotg vol. 2','gotg 2','guardians of the galaxy 2']

with open('../hasilstreaming.json')as f:

    tweets_data = []
    for line in f:
        try:
            tweet = json.loads(line)
            if any(ext.lower() in line for ext in keyword_gotg):
            # if any(ext.lower() in line for ext in keyword_ff):
             tweets_data.append(tweet)
        except ValueError as e:
            # print(e)
            pass
print "Lokasi kota yang men-tweet terkait Guardian of the Galaxy 2:"

for ind, d in enumerate(tweets_data):
    for k, v in d.items():
        if isinstance(v, dict) and "time_zone" in v:
            print v["time_zone"]

for ind, d in enumerate(tweets_data):
    if "time_zone" not in d:
        print("No time_zone {}".format(ind))
    elif "place" not in d:
        print("No place {}".format(ind))

tweets = pd.DataFrame()

tweets['Location'] = [tweet['place']['country']if "place" in tweet and tweet['place'] else np.nan for tweet in tweets_data ]
tweets['time_zone'] = [tweet['time_zone'] if 'time_zone' in tweet else np.nan for tweet in tweets_data]
