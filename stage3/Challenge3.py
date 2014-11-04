import requests
import json

payload = { 'token': 'FqpBQgTWQw' }

r = requests.post('http://challenge.code2040.org/api/prefix' , data=json.dumps(payload))


k = json.loads(r.text)

prefix = k['result']['prefix']
prefixcheck = k['result']['array']


check = len(prefix)
reply = []
for word in prefixcheck:
	if word[0:check] != prefix:
		print word
		reply.append(word)

replydict = {}
replydict['token'] = 'FqpBQgTWQw'
replydict["array"] = reply

finalverdict = requests.post('http://challenge.code2040.org/api/validateprefix' , data=json.dumps(replydict))



print finalverdict
print finalverdict.text