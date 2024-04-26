import snscrape.modules.twitter as sntwitter
from datetime import date, timedelta
import pandas as pd
import itertools
data=pd.read_csv('/Users/zhukang/position.csv')
#df_city = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    #'burger near:"New Lynn" within:10km').get_items(), 50))
df_list = []
for position in data.Position:
    tweet_iterator = itertools.islice(sntwitter.TwitterSearchScraper(' geocode:"{}"'.format(position)).get_items(), 500)
    df = pd.DataFrame(tweet_iterator)
    df = df.assign(Location= position)
    df_list.append(df)
merged_df = pd.concat(df_list, axis=0)
merged_df.to_csv('solution.csv')