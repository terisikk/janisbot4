from telethon.sessions import StringSession
from telethon.sync import TelegramClient

# Run this file once to create a new session, if needed. This needs manual input from the user:
# phone number and verification code.
# This prints a session string that can be used in automated tests.

# Get these from https://my.telegram.org/apps
api_id = 12345678
api_hash = "1234567890abcd"
dc_number = 2
dc_ip = "1.2.3.4"

session = StringSession()
session.set_dc(2, api_id, 443)

with TelegramClient(StringSession(), api_id, api_hash) as client:
    client.session.set_dc(dc_number, dc_ip, 443)
    print("Your session string is:", client.session.save())
