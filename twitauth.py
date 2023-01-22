import tweepy
import keys


auth = tweepy.OAuth2BearerHandler(keys.bearer_token)
api = tweepy.API(auth)

