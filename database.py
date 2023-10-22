import peewee

economy_account_db = peewee.SqliteDatabase('economy.db')
stats_db = peewee.SqliteDatabase('Player_stats.db')
server_rank_db = peewee.SqliteDatabase('Server_rank.db')
