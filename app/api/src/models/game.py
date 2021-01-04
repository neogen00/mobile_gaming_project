import api.src.db as db
import api.src.models as models

class Game():
    __table__ = 'games'
    columns = ['id', 'name', 'platform', 'publisher',
            'release_date', 'genre', 'game_engine']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_game_name_platform(self, name, platform, cursor):
        game_query = "SELECT * FROM games WHERE name = %s AND platform = %s;"
        cursor.execute(game_query, (name, platform))
        record = cursor.fetchone()
        return db.build_from_record(models.Game, record)

    def ratings(self, cursor):
        ratings_query = "SELECT * FROM ratings WHERE ratings.game_id = %s;"
        cursor.execute(ratings_query, (self.id,))
        record = cursor.fetchone()
        return db.build_from_record(models.Rating, record)

    def earnings(self, cursor):
        earnings_query = "SELECT * FROM earnings WHERE earnings.game_id = %s"
        cursor.execute(earnings_query, (self.id,))
        record = cursor.fetchone()
        return db.build_from_record(models.Earnings, record)