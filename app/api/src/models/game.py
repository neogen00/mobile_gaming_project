# import src.db as db
# import src.models as models

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