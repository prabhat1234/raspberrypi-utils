#!/usr/bin/env python
import sys
from datetime import datetime
from twython import Twython
CONSUMER_KEY = 'APevtgZG5AMCTEGGvWKGcB8hB'
CONSUMER_SECRET = 'WrX9Oq8cpzdXLHFiVUaFSbfWJWndcqqpzGZIsBHmGHuv6ou71F'
ACCESS_KEY = '2907832382-ZEEMpXd1iSwsAIV7ovw4FK5Z0IgafsNzUfxdQd2'
ACCESS_SECRET = 'rPaxvTPlNqvqe4arIrXJEcCagTqQoFW6QTyw7JLMlWTyu'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 
current_time=datetime.now().strftime('%c')
last_count=int(open('/home/pi/hello-world/tweet_count','r').read())
api.update_status(status="Waking up for %dth time at %s"%(last_count+1,current_time))
open('/home/pi/hello-world/tweet_count','w').write(str(last_count+1))

