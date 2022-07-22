from flask import Flask, request, Response
import requests
# from bot import sendMessage
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

def citacao():
  r = requests.get('https://api.quotable.io/random')
  if r.status_code == 200:
    data = r.json()
    quote = f'{data["content"]} ({data["author"]})'
    return quote
  else:
    quote = 'I could not retrieve a quote at this time, sorry.'
    return quote

@app.route('/bot', methods=['POST'])
def bot():
  incoming_msg = request.values.get('Body', '').lower()
  resp = MessagingResponse()
  msg = resp.message()
  responded = False
  if "quote" in incoming_msg:
    quote=citacao()
    msg.body(quote)
    responded = True
  if 'cat' in incoming_msg:
    # return a cat pic
    msg.media('https://cataas.com/cat')
    responded = True
  if not responded:
    msg.body('I only know about famous quotes and cats, sorry!')
  return Response(str(resp), mimetype="application/xml"), 200

if __name__ == '__main__':
    app.run()
