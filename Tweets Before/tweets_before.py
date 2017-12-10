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
from pygame import mixer


#creates & returns the OAuthHandler object that is used to connect to twitter.
#return type: OAuthHandler
def createAuthHandler():
	#consumer_key & consumer_secret are used inorder for tweepy to work.
	consumer_key = "INSERT CONSUMER_KEY"
	consumer_secret = "INSERT CONSUMER SECRET"
	
	#created so that you can access twitter data.
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	#used to access your twitter account.
	access_token = "INSERT ACCESS TOKEN"
	access_token_secret = "INSERT ACCESS TOKEN SECRET"
	
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
	
	print "\nThe following tweets were by " + username + " and made before " + str(year) + ":\n"
	
	#print out all tweets by the username given before the year given 
	for tweet in tweets:
		if date_before > tweet.created_at:
			print tweet.text
			print str(tweet.created_at) + "\n"
			count_of_tweets += 1
	
	print str(count_of_tweets) + " were made before " + str(year)


#Play an mp3 file in the background of the program.
#return type: void
def playMusic(path_to_sound_file):
	#play a dumbass song
	mixer.init()
	mixer.music.load(path_to_sound_file)
	mixer.music.play()


#see if the user would like to reloop the program for different tweets.
#return type: boolean
def runAgain():
	run_again = raw_input("Would you like to play to check another user's tweets(Y/N)? ")
	#check to see if user input is valid.
	if run_again.lower() != "y" and run_again.lower() != "n":
		#print "That is not a valid answer."
		runAgain()
	#return the user's yes or no responce
	else:
		#print run_again
		return run_again.lower() == "y"


#-------------------------------------------------------------------------
def main():
	#object used for connecting to twitter.
	auth = createAuthHandler()

	#attempt to connect to twitter.
	requestToken(auth)

	#Consturt the API instance.
	api = tweepy.API(auth)

	#play song file in the background.
	playMusic('songs/Alan Walker - The Spectre.mp3')

	#get tweets from a user before a certain year.
	print "\nThis program gets all the tweets of any given user before a specified year."
	
	#This variable will be used to check and see if the user would like to run the program again.
	run_again = True

	#this loop will continue to run until the user no longer wants to look at tweets.
	#inside of this while loop is where all of the real programming work takes place.
	while run_again:
		print "\n"

		#used as the username for which twitter account to grab tweets from.
		username = raw_input("Enter a valid twitter username: ")
		
		#used as the year that tweets will be grabbed before.
		before_year = raw_input("Before what year would you like to get these tweets?(Enter a year): ")
		
		#print out all of the tweets by a user before a certain year.
		getTweetsBeforeYear(api, username, before_year)

		#ask user if they want to run the program again (check more tweets).
		run_again = runAgain()

	#nice little exit note.
	print "Have a good day."

	#stop the song when the program ends.
	mixer.music.stop()

main()
