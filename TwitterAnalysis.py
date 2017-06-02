from __future__ import division
import tweepy
import nltk
from sklearn.cluster import KMeans
import numpy as np

consumer_key = "4BC9yJWYekhi5XaqzaCXs1g1y"
consumer_secret = "Z6qTU9J5gHfJ7cn31M17qNMoHFuvd3VAjPuCLCOCRsANKva5Iw"
access_token = "1722517680-cyhUqcDoMzISda38kCj6yhc2WIOCLejmdyRMvvW"
access_token_secret = "EEbUCmilOIoIVkBfU5Tv2I9e6Ke7RM1Ni6FgfiOJPmS3t"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

following = api.friends(screen_name = 'katyperry',count = 50);
mean_var = []
for user in following:
	tweets = api.user_timeline(screen_name = user.screen_name,count=100);
	words = 0 
	tweetlen = len(tweets)
	for tweet in tweets:
		lst = tweet.text.split()
		words = words + len(lst)

	mean_words = words/tweetlen #find mean
	variance=0
	for tweet in tweets:
		lst = tweet.text.split()
		variance = variance + (mean_words-len(lst))**2
	variance = variance/tweetlen #find variance
	mean_var.append([mean_words,variance]);

mean_var = np.array(mean_var)

Clustering = KMeans(n_clusters =4)
Clustering.fit(mean_var)

print Clustering.labels_
print Clustering.cluster_centers_
