import os
import twitter
import requests
import json

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY") or ""
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET") or ""
TWITTER_ACCESS_TOKEN_KEY = os.environ.get("TWITTER_ACCESS_TOKEN_KEY") or ""
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET") or ""

api = twitter.Api(
	consumer_key=TWITTER_CONSUMER_KEY,
	consumer_secret=TWITTER_CONSUMER_SECRET,
	access_token_key=TWITTER_ACCESS_TOKEN_KEY,
	access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
)

url = 'http://hangang.dkserver.wo.tc/'
result = requests.get(url).text
data = json.loads(result)

str = f"현재 온도는 {data['temp']}도 입니다."
api.PostUpdate(status=str)
