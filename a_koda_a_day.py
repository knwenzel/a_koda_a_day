from twilio.rest import Client
import json
import random

with open("config.json","r") as f: 
    config = json.load(f)

with open("img_list","r") as f:
    img_list = f.readlines()
    img_index = random.randint(0,len(img_list)-1)
    img_url = img_list[img_index]

# Your Account Sid and Auth Token from twilio.com/console
account_sid = config["twilio_sid"]
auth_token = config["twilio_auth_token"]
client = Client(account_sid, auth_token)

number_list = config["number_list"]
for number in number_list:
    message = client.messages \
        .create(
            body ='Heres the pooper',
            from_= config["twilio_from_phone"],
            media_url = img_url,
            to = number
        )

    print(message.sid)