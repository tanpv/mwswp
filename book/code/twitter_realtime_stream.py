import tweepy
from  tweepy import  StreamListener
from  tweepy import  Stream

consumer_key = 'your consumer_key'
consumer_secret = 'your consumer_secret'
access_key = 'your access_key'
access_secret = 'your access_secret'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['money'])
