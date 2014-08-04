import sqlalchemy.orm 
sqlalchemy.orm.ScopedSession = sqlalchemy.orm.scoped_session
from elixir import *
 
metadata.bind = "postgres://humanure@localhost/humanure_dev"
metadata.bind.echo = True
 
class Mention(Entity):
  status_id = Field(String)