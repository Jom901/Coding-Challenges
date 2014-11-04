#################################################################################################
#Jonathan Medina Morales																		#
#This program is part of a the challenge programs for CODE2040's applications in  November 2014 #
#This program receives a JSON with a string called a 'needle' and an array called a 'haystack'. #
#The objective of this program is to find the needle in the haystack							#
#################################################################################################

import requests 						#import requests library for post management
import json 							#import json for json management

#Define token JSON
payload = { 'token': 'FqpBQgTWQw' }

#send post to the api with the token and receive the data for the problem
r = requests.post('http://challenge.code2040.org/api/haystack' , data=json.dumps(payload))

#Assign the the JSON data to a dictionary
k = json.loads(r.text)

#Assign dictionary contents to holder variables
needle = k['result']['needle']
hay  = k['result']['haystack']

#For every item in the array
for x in range(0, len(hay)-1): 	#If you've found the needle
	if needle == hay[x]:		#the position at which it was found will be the reply
		reply = x
		print "Hey, I found it"
		print reply

#Prepare reply dictionary and assign its fields
replydict = {}
replydict['token'] = 'FqpBQgTWQw'
replydict['needle'] = reply

#Send post message with the answers and receive response
finalverdict = requests.post('http://challenge.code2040.org/api/validateneedle' , data=json.dumps(replydict))

#Print Response
print finalverdict
print finalverdict.text
