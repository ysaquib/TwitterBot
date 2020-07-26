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
	start = time.gmtime().tm_hour		# Start time on first execution
	tweeted = []
	diff = 0				# This is to tweet upon execution
	while (True):
		current = time.gmtime().tm_hour # Update current time in hours

		if (len(tweeted) > 60):		# Reset List
			tweeted = []

		if (current == start + diff):	# Check if its been diff hrs from start
			tweet(tweeted)
			start = current		# Change start to the current time
		
		diff = random.randint(lo, hi)	# Get new diff based on random int
		time.sleep(random.randint(30,1500))
	return None


main(2,5)					# Give range. Tweets range from every 2 to 5 hours

