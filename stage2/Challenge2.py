import requests
import json

payload = { 'token': 'FqpBQgTWQw' }

r = requests.post('http://challenge.code2040.org/api/haystack' , data=json.dumps(payload))


k = json.loads(r.text)

needle = k['result']['needle']
hay  = k['result']['haystack']


for x in range(0, len(hay)-1):
	if needle == hay[x]:
		reply = x
		print "Hey, I found it"
		print reply


replydict = {}
replydict['token'] = 'FqpBQgTWQw'
replydict['needle'] = reply

finalverdict = requests.post('http://challenge.code2040.org/api/validateneedle' , data=json.dumps(replydict))

print finalverdict
print finalverdict.text
