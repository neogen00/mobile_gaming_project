import requests

import api.src.db as db
from settings import (RAWG_API_KEY, IGDB_CLIENT_ID, IGDB_CLIENT_SECRET, TS_TOKEN)

class RAWG_Client:
    api_key = RAWG_API_KEY
    ROOT_URL = 'https://api.rawg.io/api'

    def auth_params(self):
        return {'key': self.api_key}
   
    def full_params(self, query_params = {"dates": "2019-09-01,2019-09-30", "platforms" : 18}):
        params = self.auth_params().copy()
        params.update(query_params)
        return params

    def request_games(self, query_params = {'search' : 'Among Us'}):
        response = requests.get(f"{self.ROOT_URL}/games?", self.full_params(query_params))
        return response.json()['results'][0]

    def find_release_date(self, name = 'Among Us'):
        game = self.request_games(query_params = {'search': name})
        if not game:
            return None
        elif not game['name'] == name:
            return None
        release_date = game.get('released',[])
        if not release_date:
            return None
        return release_date

    def find_metacritic(self, name = 'Among Us'):
        game = self.request_games(query_params = {'search': name})
        if not game:
            return None
        elif not game['name'] == name:
            return None
        metacritic = game.get('metacritic',[])
        if not metacritic:
            return None
        return metacritic

class IGDB_Client:
    def __init__(self, client_id = IGDB_CLIENT_ID, client_secret = IGDB_CLIENT_SECRET):

        self.client_id = client_id
        self.client_secret = client_secret

    ROOT_URL = 'https://api.igdb.com/v4/'

    def get_access_token(self):
        grant_type = 'client_credentials'
        params = {'client_id' : self.client_id, 'client_secret' : self.client_secret, 'grant_type' : grant_type}
        url = 'https://id.twitch.tv/oauth2/token'

        response=requests.post(url, data=params)
        return response.json()['access_token']

    def auth_params(self):
        token = self.get_access_token()
        return { 'headers' : {'Client-ID': self.client_id, 'Authorization': f'Bearer {token}'}}
   
    def full_params(self, query_params = {'data': 'fields name; limit 10;'}):
        params = self.auth_params().copy()
        params.update(query_params)
        return params

    def search_games(self, query_params = {'data': 'fields name; limit 10;'}):
        response = requests.post(f"{self.ROOT_URL}games", **self.full_params(query_params))
        response.raise_for_status()
        return response.json()


    def find_game_engine(self, name = 'Among Us'):
        game = self.search_games(query_params = {'data': f'f game_engines; w name = "{name}"; limit 1;'})
        if not game:
            return None
        engine_id = game[0].get('game_engines',[])
        if not engine_id:
            return None
        engine = self.game_engines(query_params = {'data': f'f name; w id = {engine_id[0]};'})
        return engine[0]['name']

    def game_engines(self, query_params = {'data': 'fields name; limit 500;'}):
        response = requests.post(f"{self.ROOT_URL}game_engines", **self.full_params(query_params))
        response.raise_for_status()
        return response.json()


class TowerSensor_Client:
    def __init__(self, user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36' , x_csrf_token = TS_TOKEN):

        self.user_agent = user_agent 
        self.x_csrf_token = x_csrf_token

    ROOT_URL_iOS = 'https://sensortower.com/api/ios/rankings/get_category_rankings'
    ROOT_URL_android = 'https://sensortower.com/api/android/rankings/get_category_rankings'

    iOS_query_params = {'category' : 6014, 'country': 'US', 'date': '2020-12-28T00:00:00.000Z', 'device': 'IPHONE', 'limit': 100, 'offset' : 0}
    android_query_params = {'category' : 'game', 'country': 'US', 'date': '2020-12-28T00:00:00.000Z', 'device': 'MOBILE', 'limit': 100, 'offset' : 0}

    def auth_params(self):
        return { 'headers' : {'user-agent': self.user_agent, 'x-csrf-token': self.x_csrf_token }}

    def full_params(self, query_params = {'data': 'fields name; limit 10;'}):
        params = self.auth_params().copy()
        params.update(query_params)
        return params

    def get_rankings(self, platform='iOS', date='2020-12-28', limit=100):
        if platform == 'iOS':
            query = self.iOS_query_params
            root = self.ROOT_URL_iOS
        elif platform == 'android':
            query = self.android_query_params
            root = self.ROOT_URL_android
        date_str = date + 'T00%3A00%3A00.000Z'
        query.update({'date' : date_str , 'limit' : limit})
        response = requests.get(root, self.full_params(query))
        response.raise_for_status()
        return response.json()