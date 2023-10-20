import peewee

db = peewee.SqliteDatabase('economy.db')
item_db = peewee.SqliteDatabase('items.db')
stats_db = peewee.SqliteDatabase('Player_stats.db')
