# good tutorial
# https://www.pythoncentral.io/introduction-to-tweepy-twitter-for-python/

import tweepy
from  tweepy import  StreamListener
from  tweepy import  Stream

# for tw
consumer_key = 'ehkQnDRIQsKf9y8hzGqIZVkQt'
consumer_secret = 'xnUbEqzv9yC10l6py5DESC7MCOeuWfQhIRbobdxqF4jiBoHllV'
access_key = '312132184-ogXwvGCrHh73By67WeE95Vf6lPN7boFqoLeGhBnX'
access_secret = 'vV0wx1epPBPqh7he0M85yq2Awrt2Qm47s7NeBo7oINxnO'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
# api.update_status('Hello Python Central!')

user = api.me()
 
print('Name: ' + user.name)
print('Location: ' + user.location)
print('Friends: ' + str(user.friends_count))

counter_limit = 10
counter = 0
class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['money'])








