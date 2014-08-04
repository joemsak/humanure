import sqlalchemy.orm 
sqlalchemy.orm.ScopedSession = sqlalchemy.orm.scoped_session
from elixir import *
import os
 
metadata.bind = os.environ['DATABASE_URL']
metadata.bind.echo = True
 
class Mention(Entity):
  status_id = Field(String)