# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
import pprint

env_var = os.environ

# Print the list of user's
# environment variables
# print("User's Environment variable:")
# pprint.pprint(dict(env_var), width=1)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


def sendMessage(msg, to):
    message = client.messages.create(
        body=msg,
        from_='whatsapp:+14155238886',
        to=to
    )
    print(message.sid)
