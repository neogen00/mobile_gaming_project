# import src.db as db
# import models as models

class Earnings():
    __table__ = 'earnings'
    columns = ['id', 'game_id', 'price', 'inapp',
            'revenue', 'downloads']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            if not v:
                v = None
            setattr(self, k, v)