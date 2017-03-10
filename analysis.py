### to read a file that contains tweets in json format.

#!/usr/bin/env python
# encoding: utf-8

import json
import pandas as pd
import matplotlib.pyplot as plt
import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

def main():

	searchquery="elephant"
	#Reading Tweets
	print 'Reading Tweets\n'
	tweets_data_path = "/home/user/Downloads/twitter_app/twitter_data7.json"

	tweets_data = []
	tweets_file = open(tweets_data_path, "r")

	for line in tweets_file:
	    try:
	        tweet = json.loads(line)
	        tweets_data.append(tweet)
	    except:
	        continue

	#Structuring Tweets
	try:
    	    print 'Structuring Tweets\n'
	    tweets = pd.DataFrame()
	    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
	    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
	    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
	except BaseException,e:
            print 'Failed on structuring tweets', str(e)


	#Analyzing Tweets by Language
	try:
    	    print 'Analyzing tweets by language:'
	    tweets_by_lang = tweets['lang'].value_counts()
	    if (len(tweets_by_lang)>0):
	       print tweets_by_lang 
	    else:
	       print "Empty data \n"
	except BaseException,e:
            print 'Failed on Data',str(e)


	#Analyzing Tweets by Country
	try:
	    print '\nAnalyzing tweets by country'
	    tweets_by_country = tweets['country'].value_counts()
  
	    if (len(tweets_by_country)>0):
               print tweets_by_country
	    else:
	       print "Empty data \n"
	except BaseException,e:
            print 'Failed on Data',str(e)


	#Adding columns that contain the word 
	try:
	    print 'Adding tags in the data'
	    tweets[searchquery] = tweets['text'].apply(lambda tweet: word_in_text(searchquery, tweet))
	    #print tweets[searchquery]
     
	except BaseException,e:
            print 'Failed on Data',str(e)


	#Analyzing Tweets by programming language
	try:
	    print '\nAnalyzing tweets by searching word'
	    tweets_by_sch_word = [tweets[searchquery].value_counts()[True]] 

	    if (len(tweets_by_sch_word)>0):
               print tweets_by_sch_word
	    else:
	       print "Empty data \n"

	except BaseException,e:
            print 'Failed on Data',str(e)


if __name__=='__main__':
	main()
