"""
seed.py file used to seed data into psql tables. 
fixed drop_all_tables() -> drop_records() using TRUNCATE to delete table with foreign key
added reset_all_primarykey to change primary keys back to 1 every time seed.py is run
"""

import psycopg2

import src.db as db
from src.models.game import Game
from src.models.rating import Rating
from src.models.earnings import Earnings

# delete/truncate all tables and reset primary keys
db.drop_all_tables(db.conn, db.cursor)
db.reset_all_primarykey(db.conn, db.cursor)


# seeding games
amongus = db.save(Game(name = 'Among Us', platform = 'Android', publisher = 'Innersloth LLC', 
    release_date = '2018-11-2', genre = 'Action', game_engine = 'Unity'), db.conn, db.cursor)

roblox = db.save(Game(name = 'Roblox', platform = 'Android', publisher = 'Roblox Corporation', 
    release_date = '2019-12-31', genre = 'Building', game_engine = 'Something Else'), db.conn, db.cursor)

candy = db.save(Game(name = 'Candy Crush Saga', platform = 'Android', publisher = 'King', 
    release_date = '2015-1-1', genre = 'Casual', game_engine = 'Candy Factory'), db.conn, db.cursor)

amongus_ios = db.save(Game(name = 'Among Us', platform = 'iOS', publisher = 'Innersloth LLC', 
    release_date = '2018-11-2', genre = 'Action', game_engine = 'Unity'), db.conn, db.cursor)
# breakpoint()
# seeding ratings
no1 = db.save(Rating(game_id = amongus.id, metacritic = 84, TS_rating = 4.465, 
    rank_type = 'free', ranking = 1, date_created = '2020-12-01'), db.conn, db.cursor)

no2 = db.save(Rating(game_id = roblox.id, metacritic = 90, TS_rating = 4.48, 
    rank_type = 'free', ranking = 2, date_created = '2020-12-02'), db.conn, db.cursor)

no3 = db.save(Rating(game_id = candy.id, metacritic = 75, TS_rating = 4.1, 
    rank_type = 'free', ranking = 3, date_created = '2020-12-03'), db.conn, db.cursor)

no1_ios = db.save(Rating(game_id = amongus_ios.id, metacritic = 84, TS_rating = 4.465, 
    rank_type = 'free', ranking = 1, date_created = '2020-12-01'), db.conn, db.cursor)

# seeding earnings
amongus_e = db.save(Earnings(game_id = amongus.id, price = 0.00, inapp = True, 
    revenue = 35000000, downloads = 100000), db.conn, db.cursor)

roblox_e = db.save(Earnings(game_id = roblox.id, price = 0.01, inapp = False, 
    revenue = 50000000, downloads = 200000), db.conn, db.cursor)

candy_e = db.save(Earnings(game_id = candy.id, price = 0.50, inapp = True, 
    revenue = 100000000, downloads = 300000), db.conn, db.cursor)

amongus_ios_e = db.save(Earnings(game_id = amongus_ios.id, price = 1.00, inapp = False, 
    revenue = 2000000, downloads = 75000), db.conn, db.cursor)
