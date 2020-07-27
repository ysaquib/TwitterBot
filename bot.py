import time
import random
import tweepy

# Access Keys redacted for privacy and security
auth = tweepy.OAuthHandler("[REDACTED]", "[REDACTED]")
auth.set_access_token("[REDACTED]", "[REDACTED]")
api = tweepy.API(auth)

def tweet(tweeted):
	allTweets = open("tweets.txt") 		# Open txt file containing all tweets
	twt = random.randint(0, 182)
	while (twt in tweeted):
		twt = random.randint(0, 182) 	# Select random line
	for i, line in enumerate(allTweets):
		if (i == twt): 			# Find line and tweet it
			print (line)
			api.update_status(status=(line))
			tweeted.append(i)	# Append line number to a list

def main(lo, hi):
	tweeted = []
	while (True):
		if (len(tweeted) > 60):			# Reset List
			tweeted = []
		
		tweet(tweeted)

		time.sleep(random.randint(3600*lo,3600*hi))
	return None


main(2,6)					# Give range. Tweets range from every 2 to 5 hours

