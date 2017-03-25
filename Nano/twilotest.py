# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:39:21 2017

@author: fang2
"""

from twilio.rest import TwilioRestClient

account = "AC590107981995c567bbc88d644ac84db5"
token = "c41442ed277c036dc8280fe98a956eee"
client = TwilioRestClient(account, token)


message = client.messages.create(to="+12166660006", from_="+18156714759",
                                 body="Hello there!")
print(message.sid)