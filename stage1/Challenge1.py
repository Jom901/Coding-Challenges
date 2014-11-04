#################################################################################################
#Jonathan Medina Morales																		#
#This program is part of a the challenge programs for CODE2040's applications in  November 2014 #
#It receives a string from the CODE2040 coding challenge API and then reverses the string.      #
#																								#
#################################################################################################
import requests 							#import requests library to handle post messages
import json 								#Import json library for json handling

#Define token JSON
payload = { 'token': 'FqpBQgTWQw' }

#Send token to api to authenticate and receive problem data
r = requests.post('http://challenge.code2040.org/api/getstring' , data=json.dumps(payload))
print r.text

#Receive load json received from post into a dictionary
k = json.loads(r.text)
#Hand off the problem string into a handler variable
handler = k['result']

print handler

#Use python's slicing functionality to invert the string
reply = handler[::-1]
print reply

#prepare reply dictionary and set token and string fields
replydict = {}
replydict['token'] = 'FqpBQgTWQw'
replydict['string'] = reply

#Send post message with answers to api and receive response
finalverdict = requests.post('http://challenge.code2040.org/api/validatestring' , data=json.dumps(replydict))


#Print response
print finalverdict
print finalverdict.text
