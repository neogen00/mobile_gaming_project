import datetime
import pdb
import src.adapters as adapters
import src.db as db


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

def test_RAWG_game_request():
    # check if RAWG can search for a specific game title
    rawg = adapters.RAWG_Client()
    game = rawg.request_games(query_params = {'search' : 'Roblox'})
    assert game['name'] == 'ROBLOX'

def test_find_release_date():
    # check if game release date is in RAWG API
    rawg = adapters.RAWG_Client()
    game = rawg.request_games(query_params = {'search' : 'Roblox'})
    assert game['released'] == '2006-08-27'

def test_find_metacritic_score():
    # check if game metacritic is in RAWG API
    rawg = adapters.RAWG_Client()
    game = rawg.request_games(query_params = {'search' : 'Among Us'})
    assert game['metacritic'] == 82

def test_Tower_Sensor_get_rankings():
    # check to see if lists come out from Tower Sensor API
    date_now = datetime.datetime.now().date()
    record_date = date_now.strftime('%F').replace('-0','-')
    ts1 = adapters.TowerSensor_Client()
    ts_try1 = ts1.get_rankings(platform='iOS', date=record_date, limit=1)

    assert len(ts_try1[0]) == 3
    assert isinstance(ts_try1[0][0]['name'], str) == True
    assert len(ts_try1[0][0].keys()) == 50