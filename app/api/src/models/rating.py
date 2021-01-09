import api.src.db as db
import api.src.models as models

class Rating():
    __table__ = 'ratings'
    columns = ['id', 'game_id', 'metacritic', 'TS_rating',
            'rank_type', 'ranking', 'date_created']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by(self, game_id, rank_type, ranking, date_created, cursor):
        rating_query = "SELECT * FROM ratings WHERE game_id = %s AND rank_type = %s AND ranking = %s AND date_created = %s;"
        cursor.execute(rating_query, (game_id, rank_type, ranking, date_created))
        record = cursor.fetchone()
        return db.build_from_record(models.Rating, record)
