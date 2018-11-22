from twilio.rest import Client
import json


with open("config.json","r") as f: 
    config = json.load(f)
print (config)

# Your Account Sid and Auth Token from twilio.com/console
account_sid = config["twilio_sid"]
auth_token = config["twilio_auth_token"]
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body ='Heres the pooper',
         from_= config["twilio_from_phone"],
         to = config["twilio_to_phone"]
     )

print(message.sid)