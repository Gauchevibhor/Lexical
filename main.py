import json
import tweepy



keys = json.load(open('twitterKeys.json', 'r'))
consumer_key = keys['apiKey']
consumer_secret = keys['apiSecretKey']
access_key = keys['accessToken']
access_secret = keys['accessTokenSecret']

def get_tweets(username):
		# csvFile = open('result.csv', 'a')

        # #Use csv writer
        # csvWriter = csv.writer(csvFile)
		# Authorization to consumer key and consumer secret
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		# Access to user's access key and access secret
		auth.set_access_token(access_key, access_secret)

		# Calling api
		api = tweepy.API(auth)

		# 200 tweets to be extracted
		number_of_tweets=200
		tweets = api.user_timeline(screen_name=username)

		# Empty Array
		tmp=[]

		# create array of tweet information: username,
		# tweet id, date/time, text
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
		for j in tweets_for_csv:

			# Appending tweets to the empty array tmp
			tmp.append(j)

		# Printing the tweets
		print(tmp)


# Driver code
if __name__ == '__main__':

	# Here goes the twitter handle for the user
	# whose tweets are to be extracted.
	get_tweets("jungeKatz")
