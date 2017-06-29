import logging, socket
import requests

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

localpi = 'mpi.local'
"""
Change this to the DNS name of ortalctl on your Pi
"""

try:
    rpi = socket.gethostbyname(localpi)
    
except Exception:
    print('Unable to find ortalctl ' + localpi)
    exit(1)

app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_session():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)
    
@ask.intent('OnIntent')
def on_intent():
    response = requests.get('http://' + localpi + ':8000/on')
    if response.status_code != 200:
        text = render_template('on_error')
    else:
        text = render_template('on')
    return statement(text).simple_card('On', text)

@ask.intent('OffIntent')
def off_intent():
    response = requests.get('http://' + localpi + ':8000/off')
    if response.status_code != 200:
        text = render_template('off_error')
    else:
        text = render_template('off')
    return statement(text).simple_card('Off', text)

if __name__ == '__main__':

    app.run(debug=True)
