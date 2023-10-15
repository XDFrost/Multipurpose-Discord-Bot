import peewee                     # Used to work on a database
from database import db

class Account(peewee.Model):             # Inherits from peewee model i.e. account will be represented as a single table
    user_id : str = peewee.CharField(max_length=255)
    guild_id : str = peewee.CharField(max_length=255)
    amount : int = peewee.IntegerField()
    
    
    class Meta:
        database = db
        
    @staticmethod                     # Used to not create a instance of a class since static methods can work on a class without creating its instance
    def fetch(message):
        try:
            account = Account.get(Account.user_id == message.author.id, Account.guild_id == message.guild.id)
        except peewee.DoesNotExist:
            account = Account.create(user_id = message.author.id, guild_id = message.guild.id, amount  = 100)
        return account
    