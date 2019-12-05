
import sys
import slack
import os

client = slack.WebClient(token=os.environ["SLACK_API_TOKEN"])

response = client.chat_postMessage(
    channel='#test',
    text=sys.argv[1])
# assert response["ok"]
# assert response["message"]["text"] == "Hello world!"

