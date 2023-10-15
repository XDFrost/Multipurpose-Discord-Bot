import peewee                     # Used to work on a database
from database import db

class Account(peewee.Model):             # Inherits from peewee model i.e. account will be represented as a single table
    user_id : str = peewee.CharField(max_length=255)
    guild_id : str = peewee.CharField(max_length=255)
    amount : int = peewee.IntegerField()
    
    
    class Meta:
        database = db