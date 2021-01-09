import pdb

# from api.src.adapters.client_debug import RAWG_Client
# from api.src.adapters.client_debug import IGDB_Client
# from api.src.adapters.client_debug import TowerSensor_Client

import api.src.db as db
import api.src.adapters as adapters


# @pytest.fixture()
# def test_conn():
#     test_conn = psycopg2.connect(dbname = 'mobilegaming_test', 
#             user = 'postgres', password = 'postgres')
#     cursor = test_conn.cursor()
#     db.drop_all_tables(test_conn, cursor)
#     db.reset_all_primarykey(test_conn, cursor)
#     yield test_conn
#     db.drop_all_tables(test_conn, cursor)
#     db.reset_all_primarykey(test_conn, cursor)








def test_find_game_engine_hit():
    # check Among Us game with search
    ig = adapters.IGDB_Client()
    engine = ig.find_game_engine('Among Us')
    assert engine == 'Unity'

def test_find_game_engine_no_game():
    # check Roblox game with search and gets [] and returns unknown
    ig = adapters.IGDB_Client()
    engine = ig.find_game_engine('Roblox')
    assert engine == None

def test_find_game_engine_hit_no_engine():
    # check Candy Crush Saga game with search and finds game with no game engine info and returns unknown
    ig = adapters.IGDB_Client()
    engine = ig.find_game_engine('Candy Crush Saga')
    assert engine == None