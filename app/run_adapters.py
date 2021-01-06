import api.src.models as models
import api.src.db as db
import api.src.adapters as adapters
import psycopg2

class RequestAndBuild:
    def __init__(self):
        self.TowerSensor_Client = adapters.TowerSensor_Client()
        self.builder = adapters.Builder()
        self.conn = psycopg2.connect(database = 'mobilegaming_development', 
                user = 'postgres', 
                password = 'postgres')
        self.cursor = self.conn.cursor()

    def run(self, platform='iOS', record_date='2020-12-28', limit=100):
        # platform='android', date='2020-12-28', limit=100
        TS_rankings = self.TowerSensor_Client.get_rankings(platform=platform, date=record_date, limit=limit)
        game_objs = []
        map_type = {0:'top free', 1:'top paid', 2:'top grossing'}
        for rank in TS_rankings:
        # for rank in range(72,len(TS_rankings)):
            for rank_code in range(len(rank)):
            # for rank_code in range(2,3):
                game_obj = self.builder.run(rank[rank_code], record_date, map_type[rank_code], self.conn, self.cursor)
                # game_obj = self.builder.run(TS_rankings[rank][rank_code], record_date, ranking_type, self.conn, self.cursor)
                game_objs.append(game_obj)
        return game_objs


