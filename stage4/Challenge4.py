#################################################################################################
#Jonathan Medina Morales																		#
#This program is part of a the challenge programs for CODE2040's applications in  November 2014 #
#This program receives a JSON with a date and a time interval.The objective of this program is  #
#to add the interval, which is in seconds, to the ISO 8601 formatted date. 						#
#################################################################################################

import requests												#import requests library for post responses
import json 												#import JSON library for API response handling
import dateutil.parser 										#import dateutil's parser to convert ISO 8601 into python's datetime format
from datetime import datetime, timedelta					#import datetime and timedelta for addition
import isodate 												#import isodate to revert the date into an ISO 8601 date


#designate api token JSON
payload = { 'token': 'FqpBQgTWQw' }

#send a post to the api with the token and receive a JSON based response
r = requests.post('http://challenge.code2040.org/api/time' , data=json.dumps(payload))
#display the contents of the JSON
print r.text

#Load the contents of the json into a variable, from here on out treated as a dictionary
k = json.loads(r.text)
#dump the datestamp and interval values into their own variables for ease of use.
handler = k['result']
date = handler['datestamp']
interval = handler['interval']
#Parse the datestamp into a datetime value
date = dateutil.parser.parse(date)

#Define the reply as the as the sum between the date and the interval, based on seconds
reply = date + timedelta(seconds=interval)

print reply

#convert the date back into iso8601 format
reply = isodate.datetime_isoformat(reply)
#Define the reply dictionary
replydict = {}
#Add the datestamp and token fields
replydict['token'] = 'FqpBQgTWQw'
replydict['datestamp'] = reply
print reply

#Send a post with the reply dictionary and receive a response
finalverdict = requests.post('http://challenge.code2040.org/api/validatetime' , data=json.dumps(replydict))

#print success or failure message
print finalverdict
print finalverdict.text