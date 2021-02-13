import psycopg2

import src.db as db
import src.adapters as adapters
from settings import (DB_USER, DB_NAME, DB_PASSWORD)


class RequestAndBuild:
    def __init__(self):
        self.TowerSensor_Client = adapters.TowerSensor_Client()
        self.builder = adapters.Builder()
        self.conn = psycopg2.connect(database = DB_NAME, 
                user = DB_USER, 
                password = DB_PASSWORD)
        self.cursor = self.conn.cursor()

    def run(self, record_start='2020-12-28', days=1, limit=100):
        game_objs = []
        for day in range(days):
            record_date = db.date_adding_formatter(record_start,day)
            for os in range(2):
                map_os = {0:'android', 1:'iOS'}
                TS_rankings = self.TowerSensor_Client.get_rankings(platform=map_os[os], date=record_date, limit=limit) 
                map_type = {0:'top free', 1:'top paid', 2:'top grossing'}
                for rank in TS_rankings:
                    for rank_code in range(len(rank)):
                        game_obj = self.builder.run(rank[rank_code], record_date, map_type[rank_code], self.conn, self.cursor)
                        game_objs.append(game_obj)
        return game_objs


