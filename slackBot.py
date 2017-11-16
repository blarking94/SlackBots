from slackclient import SlackClient
import time
import os

token = 'xoxp-4694707283-120003528163-272697352275-cf4a5c328a401faf92589fc4d5b3a602'

sc = SlackClient(token)

print (sc.api_call("api.test"))

latestReply = None

if sc.rtm_connect():
        while True:
                print ('sleeping')
                responseList = sc.rtm_read()

                if len(responseList) > 0:
                	print (responseList[0])

                messages = sc.api_call(
                	"conversations.history",
                	channel="C757PADHN",
                	token=token,
                	)

                if latestReply != None and latestReply["ts"] != messages["messages"][0]["ts"]:
                	print(messages["messages"][0]["text"])
                	os.system(messages["messages"][0]["text"])

                latestReply = messages["messages"][0]

                time.sleep(5)
else:
	print ("Connection Failed, invalid token?")