#!/usr/bin/env python
# encoding: utf-8

import tweepy
import json
import time
import csv
import jsonpickle

# Open/Create a file to append data
path = "/home/user/Downloads/twitter_app/twitter_data.json"

def start_mining():

    #Twitter API credentials
    access_token="838889260862287873-u6euWQmmwa5L5iq9SQOIGyS0YEY1234"
    access_token_secret="swSCZ0VQfcUSZWIiF1GhRuTx7qCp0UA4cVNgHDQoW1234"
    consumer_key="cibxA1ldS1l4DezpvBlcF1234"
    consumer_secret="kkMidtUj5Oy7icTMhT5AfRperYfrPsziF2CPNSdjWPCY1F1234"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #Search term
    searchquery="elephant"
    searchquery_long="place:4797714c95971ac1 elephant"
    count = 0
    errorCount=0
    date_sta="2017-03-09"
    date_end="2017-03-10"
 
    api = tweepy.API(auth)

    csvFile = open(path, 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    places = api.geo_search(query="CHINA", granularity="country")
    place_id = places[0].id
    #print("CHINA ID: ", place_id)
    
    method=3

    if(method==1): 	#searching by word
      try:
	for status in tweepy.Cursor(api.search,
                        q=searchquery,
                        since=date_sta,
                        until=date_end).items():
     	    if status._json["place"]==place_id:
		print status
	    else:		
		print status._json["place"]
      except BaseException,e:
        print "Failed on ",str(e)



    if(method==2): 	#searching by place
			#also it's possible use coordinates
			#geocode="41.376809,86.923828,10000km").items():
      try:
	for status in tweepy.Cursor(api.search,
			q="place:%s" % place_id).items():
	    print status

      except BaseException,e:
        print "Failed on ",str(e)



    if(method==3): 	#storing all the tweets
     with open(path, 'w') as f:
      try:
	#for tweet in tweepy.Cursor(api.search,
        #                q=searchquery_long,
        #                since=date_sta,
        #                until=date_end).items():

	for tweet in tweepy.Cursor(api.search,
                        q=searchquery,
                        since=date_sta,
                        until=date_end).items():
	    count +=1
	    print count, "tweets found"		
	    tuit=tweet._json
	    print tuit["created_at"], tuit["place"]
	    f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')

      except BaseException,e:
        print "Failed on ",str(e)

if __name__ == '__main__':
    start_mining()
