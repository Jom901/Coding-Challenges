#################################################################################################
#Jonathan Medina Morales																		#
#This program is part of a the challenge programs for CODE2040's applications in  November 2014 #
#This program receives a JSON with a prefix and an array called. The objective of this program  #
#is to return an array with all the strings that don't have the supplied prefix. 				#
#################################################################################################

import requests 							#import requests library for post management
import json 								#import json for json handling


#Define authentication token
payload = { 'token': 'FqpBQgTWQw' }

#send a post to the api with the token and receive a JSON based response
r = requests.post('http://challenge.code2040.org/api/prefix' , data=json.dumps(payload))

#Load the contents of the json into a variable, from here on out treated as a dictionary
k = json.loads(r.text)

#assign contents of the JSON to their own variables
prefix = k['result']['prefix']
prefixcheck = k['result']['array']

#Define the length of the prefix
check = len(prefix)
#Define our array for the answer
reply = []

#For each word in the array
for word in prefixcheck:
	if word[0:check] != prefix: 			#Check to see if the word contains the prefix
		print word 							#if so, print the word and add it to the answers list
		reply.append(word)

#prepare reply dictionary and add token and array fields
replydict = {}
replydict['token'] = 'FqpBQgTWQw'
replydict["array"] = reply

#Send post to the API with the answers and receive a reply
finalverdict = requests.post('http://challenge.code2040.org/api/validateprefix' , data=json.dumps(replydict))


#Print reply
print finalverdict
print finalverdict.text