# import src.db as db
# import src.models as models

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