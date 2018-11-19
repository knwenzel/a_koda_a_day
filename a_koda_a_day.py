from fbchat import Client
from fbchat.models import *
from configparser import SafeConfigParser
#Parse config file
parser = SafeConfigParser()

#Change with your own directory
parser.read('./config.ini')
#Get fb_cred
email = parser.get('fb_cred', 'EMAIL')
password = parser.get('fb_cred', 'PASSWORD')

def send_message(message):
    client = Client(email, password)
    client.send(Message(text=message), thread_id=client.uid, thread_type=ThreadType.USER)
    client.logout()

def send_image(message, image_path):
    client = Client(email, password)
    client.sendLocalImage(image_path, message=Message(text=message), thread_id=thread_id, thread_type=thread_type)
    client.logout()

#send_image("GOOD MORNING!", 'path/to/image')
send_message("GOOD MORNING!")

