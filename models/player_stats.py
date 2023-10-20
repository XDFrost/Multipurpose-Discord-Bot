import peewee
from database import stats_db


class Stats(peewee.Model):
    hp : int = peewee.IntegerField()
    defense_points : int = peewee.IntegerField()
       
       
    class Meta:
        database = stats_db
        
    @staticmethod                     # Used to not create a instance of a class since static methods can work on a class without creating its instance
    def fetch(member):
        try:
            stats = Stats.get(Stats.user_id == member.id, Stats.guild_id == member.guild.id)
        except peewee.DoesNotExist:
            stats = Stats.create(user_id=member.id, guild_id=member.guild.id, hp=100, defense_points=100)
        return stats

    