import pdb
from api.src.adapters.client_debug import RAWG_Clent
from api.src.adapters.client_debug import IGDB_Clent
from api.src.adapters.client_debug import TowerSensor_Clent



def test_find_game_engine_hit():
    # check Among Us game with search
    ig = IGDB_Clent()
    engine = ig.find_game_engine('Among Us')
    assert engine == 'Unity'

def test_find_game_engine_no_game():
    # check Roblox game with search and gets [] and returns unknown
    ig = IGDB_Clent()
    engine = ig.find_game_engine('Roblox')
    assert engine == 'unknown'

def test_find_game_engine_hit_no_engine():
    # check Candy Crush Saga game with search and finds game with no game engine info and returns unknown
    ig = IGDB_Clent()
    engine = ig.find_game_engine('Candy Crush Saga')
    assert engine == 'unknown'