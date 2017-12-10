'''
Author:	Eric Zair
File:	tweets_before.py
Description:	This program grabs the tweets of any given user
				before a certain year.
'''


import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
import datetime


#creates & returns the OAuthHandler object that is used to connect to twitter.
#return type: OAuthHandler
def createAuthHandler():
	#consumer_key & consumer_secret are used inorder for tweepy to work.
	consumer_key = "INSERT YOUR CONSUMER KEY"
	consumer_secret = "INSERT YOUR CONSUMER SECRET"
	
	#created so that you can access twitter data.
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	#used to access your twitter account.
	access_token = "INSERT YOUR ACCESS TOKEN"
	access_token_secret = "INSERT YOU ACESS TOKEN SECRET"
	
	#set the access token to the auth object.
	auth.set_access_token(access_token, access_token_secret)

	return auth


#fetch request token for twitter.
#return type: void
def requestToken(auth_handler):
	try:
		redirect_url = auth_handler.get_authorization_url()
	except:
		print "Error! Failed to get request token."
		exit()


#print out tweets that of the username given before the year given.
#return type: void
def getTweetsBeforeYear(api, username, year):
	user = api.get_user(username)
	date_before = datetime.datetime.strptime('01Dec' + str(year), '%d%b%Y')	
	tweets = api.user_timeline(screen_name = username, count = user.statuses_count, include_rts = True)
	count_of_tweets = 0
	print "The following tweets were by " + username + " and made before " + str(year) + ":\n"
	
	#print out all tweets by the username given before the year given 
	for tweet in tweets:
		if date_before > tweet.created_at:
			print tweet.text
			print str(tweet.created_at) + "\n"
			count_of_tweets += 1
	
	print str(count_of_tweets) + " were made before " + str(year)

#-------------------------------------------------------------------------
def main():
	auth = createAuthHandler()

	#attempt to connect to twitter
	requestToken(auth)

	#Consturt the API instance
	api = tweepy.API(auth)

	#get tweets from a user before a certain year.
	print "This program gets all the tweets of any given user before a specified year.\n"
	#used as the username for which twitter account to grab tweets from.
	username = raw_input("Enter a valid twitter username: ")
	
	#used as the year that tweets will be grabbed before.
	before_year = raw_input("Before what year would you like to get these tweets?(Enter a year): ")
	
	#print out all of the tweets by a user before a certain year.
	getTweetsBeforeYear(api, username, before_year)

main()
