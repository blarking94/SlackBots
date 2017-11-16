from slackclient import SlackClient
import time
import os

# I used the legacy token (must start with xoxp-)
# Find yours here https://api.slack.com/docs/token-types#legacy
token = 'xxxxxx'
#E.g C35DGDFG2
channel_id = "xxxxxx"

sc = SlackClient(token)

latestReply = None

if sc.rtm_connect():
        while True:
                print ('sleeping....')

                messages = sc.api_call(
                	"conversations.history",
                	channel=channel_id,
                	token=token,
                	)

                if latestReply != None and latestReply["ts"] != messages["messages"][0]["ts"]:
                        # Print the latest message then try to run it! (Warning could be anything! Try "shutdown -f" if you're on windows ..)
                	print(messages["messages"][0]["text"])
                	os.system(messages["messages"][0]["text"])

                if latestReply != messages["messages"][0]:
                        latestReply = messages["messages"][0]

                time.sleep(5)
else:
	print ("Connection Failed, invalid token?")