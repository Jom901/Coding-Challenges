import requests
import json

payload = { 'token': 'FqpBQgTWQw' }

r = requests.post('http://challenge.code2040.org/api/getstring' , data=json.dumps(payload))
print r.text
k = json.loads(r.text)
handler = k['result']

print handler

reply = handler[::-1]

replydict = {}
replydict['token'] = 'FqpBQgTWQw'
replydict['string'] = reply

finalverdict = requests.post('http://challenge.code2040.org/api/validatestring' , data=json.dumps(replydict))

print finalverdict
print finalverdict.text
