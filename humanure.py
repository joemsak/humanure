#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython
from mention import *
import time, os

setup_all()
create_all()

CONSUMER_KEY    = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
OAUTH_TOKEN     = os.environ['OAUTH_TOKEN']
OAUTH_SECRET    = os.environ['OAUTH_SECRET']

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)
img = open("album_artwork.jpeg", 'rb')

while True:
  for mention in twitter.get_mentions_timeline():
    status_id = str(mention['id'])
    if not Mention.query.filter_by(status_id=status_id).all():
      screen_name = '@' + mention['user']['screen_name']
      try:
        twitter.update_status_with_media(status = screen_name,
                                         media  = img,
                                         in_reply_to_status_id = status_id)
      except:
        continue
      finally:
        Mention(status_id=status_id) # builds new mention
        session.commit() # saves Mention
    else:
      print 'We replied to this one already!'

  time.sleep(60) # 1 minute
