import configparser
import json

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

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

print('success!')


