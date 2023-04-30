import configparser
import json

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)

config_path = r'/Users/dp_user/Documents/универ/диплом/config_tele.ini'

# Reading Configs
config = configparser.ConfigParser()
config.read(config_path)

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = str(config['Telegram']['api_hash'])
phone = config['Telegram']['phone']
username = config['Telegram']['username']

#print(api_id, api_hash, phone, username)

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)
client.start()
print("Client Created")
# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        client.sign_in(password=input('Password: '))

print('success1!')


# part with channel

user_input_channel = 'https://t.me/markettwits'

if user_input_channel.isdigit():
    entity = PeerChannel(int(user_input_channel))
else:
    entity = user_input_channel

my_channel = client.get_entity(entity)

print('success2!')

# get channel messages

history = client(GetHistoryRequest(
    peer=my_channel,
    offset_id=0,
    offset_date=None,
    add_offset=0,
    limit=10,
    max_id=0,
    min_id=0,
    hash=0
))

#TODO надо с этим разобраться, почему нет messages

if not history.messages:
        print("There's no messages")
        raise FileNotFoundError

all_messages = []
messages = history.messages
for message in messages:
    all_messages.append(message.to_dict())

print(f'Len of messages: {len(all_messages)}')
print(f'Messages: \n {all_messages}')

print('Success!3')

