from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="UtvwIiZk2CP23yNRnaccyikwq"
consumer_secret="zUO0QlVcHTbtVnOsqhmZQK7x6AMRybqfI2jeO9CxEcgLvjaYAg"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1896691364-tZ7M0eBKe3Y014DjjM9vjpaM1LoEMHfNAdjUMTn"
access_token_secret="NDUsQ8Qg1oCoSK4jGwgdTf5DwN5lxS3LaZedqgHynINVW"

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['fast furious','fast n furious','fast and furious','FF8','fast & furious','fast furious 8','fast n furious 8','fast and furious 8','fast & furious 8','guardians of the galaxy','gotg','guardians of the galaxy vol. 2','gotg vol. 2','gotg 2','guardians of the galaxy 2'])
