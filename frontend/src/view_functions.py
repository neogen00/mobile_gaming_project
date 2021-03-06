import requests

API_URL_games = "http://127.0.0.1:5000/games"
API_URL_earnings_search = "http://127.0.0.1:5000/games/earnings/search"
API_URL_RPD = "http://127.0.0.1:5000/games/earnings/RPD"
API_URL_ratings_all = "http://127.0.0.1:5000/games/all_data"


def get_games():
    response = requests.get(API_URL_games)
    return response.json()

def get_earnings_games():
    response = requests.get(API_URL_earnings_search)
    return response.json()

def get_RPD():
    response = requests.get(API_URL_RPD)
    return response.json()

def get_ratings_all():
    response = requests.get(API_URL_ratings_all)
    return response.json()

def game_name(games_list):
    return [game['name'] for game in games_list]
  