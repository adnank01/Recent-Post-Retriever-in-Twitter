import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '2'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    list=json.loads(data)
    print(data[:250])
    print("Most recent post: ",list[0]['text']) #specifically for the first text of the most recent post
    headers = dict(connection.getheaders())
    print (headers)
    print('Remaining', headers['x-rate-limit-remaining'])
#