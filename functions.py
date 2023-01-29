import tweepy

class PoliticalSentiment:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
    def get_tweets(self, handle, count=200):
        # Authenticate with the Twitter API
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)

        # Get the tweets
        tweets = api.user_timeline(screen_name=handle, count=count)

        return tweets

