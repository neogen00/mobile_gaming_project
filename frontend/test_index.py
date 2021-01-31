import pytest


games_list = [{"id": 1, "name": "Among Us", "platform": "android", "publisher": "Innersloth LLC", "release_date": "2018-07-25", "genre": "action", "game_engine": "Unity"}, {"id": 2, "name": "Minecraft", "platform": "android", "publisher": "Mojang", "release_date": "2009-05-10", "genre": "arcade", "game_engine": "Bedrock Engine"}, {"id": 3, "name": "Roblox", "platform": "android", "publisher": "Roblox Corporation", "release_date": None, "genre": "adventure", "game_engine": None}]

def game_name(games_list):
    return [game['name'] for game in games_list]

def test_game_name():
    assert game_name(games_list) == ["Among Us", "Minecraft", "Roblox"]