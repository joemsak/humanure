#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from twython import Twython
import time

CONSUMER_KEY    = 'iAsmYLEOXvcUKmBdB31UnSf39'
CONSUMER_SECRET = 'x5pgFtC1a7GLXQeGbUn1rVkO4p1XOcRQViY12ii1Ab9u6umlQR'
OAUTH_TOKEN     = '501407305-QW818odRc9DKuUqCqZOAXwKu7p091C3XJlp7la8i'
OAUTH_SECRET    = 'RD4ShNSCCAwsTkqAzaNS17BFCtSPUTxEkaPcRx6Muetq6'

twitter  = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)  
img      = open("album_artwork.jpeg", 'rb')
filepath = 'tmp/replied_status_ids.txt'

while True:
  mention   = twitter.get_mentions_timeline()[0]
  status_id = mention['id']
  statuses  = open(filepath).read() # read the file here
 
  if str(status_id) not in statuses:
    screen_name = '@' + mention['user']['screen_name']
    twitter.update_status_with_media(status = screen_name,
                                     media  = img,
                                     in_reply_to_status_id = status_id)
    with open(filepath, 'a') as database: # open the file a second time for writing
      database.write(str(status_id) + "\n")
  else:
    print 'We replied to this one already!'
    
  time.sleep(60) # 1 minute