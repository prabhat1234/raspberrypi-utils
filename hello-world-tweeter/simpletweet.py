#!/usr/bin/env python
import sys
from twython import Twython
CONSUMER_KEY = 'APevtgZG5AMCTEGGvWKGcB8hB'
CONSUMER_SECRET = 'WrX9Oq8cpzdXLHFiVUaFSbfWJWndcqqpzGZIsBHmGHuv6ou71F'
ACCESS_KEY = '2907832382-ZEEMpXd1iSwsAIV7ovw4FK5Z0IgafsNzUfxdQd2'
ACCESS_SECRET = 'rPaxvTPlNqvqe4arIrXJEcCagTqQoFW6QTyw7JLMlWTyu'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

api.update_status(status=sys.argv[1][:139])
