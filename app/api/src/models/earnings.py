import api.src.db as db
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
            if v is '':     #   TS_Client uses '' when false, fix 
                v = False
            setattr(self, k, v)


    def check_update_revenue_downloads(self, TS_details, conn, cursor):
        if self.revenue < TS_details['humanized_worldwide_last_month_revenue']['revenue']: 
            self.revenue = TS_details['humanized_worldwide_last_month_revenue']['revenue']
            db.update_revenue(self, conn, cursor)
            self.update_rev = True
        if self.downloads < TS_details['humanized_worldwide_last_month_downloads']['downloads']: 
            self.downloads = TS_details['humanized_worldwide_last_month_downloads']['downloads']
            db.update_downloads(self, conn, cursor)
            self.update_update_dl = True
        return

