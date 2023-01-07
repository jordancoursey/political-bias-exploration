def get_tweets(handle, count=200):
    # Authenticate with the Twitter API
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    
    # Get the tweets
    tweets = api.user_timeline(screen_name=handle, count=200)
    
    # Create a list to store the tweets
    tweet_list = []
    for tweet in tweets:
        tweet_list.append(tweet)
        
    # Keep getting tweets until there are no more to get
    while len(tweets) > 0:
    # The max_id param will get the oldest tweets not yet retrieved
    oldest_tweet = tweets[-1].id - 1
    tweets = api.user_timeline(screen_name=handle, count=200, max_id=oldest_tweet)
    for tweet in tweets:
        tweet_list.append(tweet)
        
    
