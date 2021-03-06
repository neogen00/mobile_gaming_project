import pytest

import view_functions


games_list = [{"id": 1, "name": "Among Us", "platform": "android", "publisher": "Innersloth LLC", "release_date": "2018-07-25", "genre": "action", "game_engine": "Unity"}, {"id": 2, "name": "Minecraft", "platform": "android", "publisher": "Mojang", "release_date": "2009-05-10", "genre": "arcade", "game_engine": "Bedrock Engine"}, {"id": 3, "name": "Roblox", "platform": "android", "publisher": "Roblox Corporation", "release_date": None, "genre": "adventure", "game_engine": None}]

def test_game_name():
    assert view_functions.game_name(games_list) == ["Among Us", "Minecraft", "Roblox"]