import api.src.db as db
import api.src.models as models

class Earnings():
    __table__ = 'earnings'
    columns = ['id', 'game_id', 'price', 'inapp', 'shows_ads',
            'revenue', 'downloads']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            if v is '':     #   TS_Client uses '' when false, fix 
                v = False
            if k == 'shows_ads':
                if v == None: v = False
            setattr(self, k, v)

    def game(self, cursor):
        game_query = "SELECT * FROM games WHERE id = %s;"
        cursor.execute(game_query, (self.game_id,))
        record = cursor.fetchone()
        return db.build_from_record(models.Game, record)

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

    def to_json(self, cursor):
        earnings_json = self.__dict__
        game = self.game(cursor)
        if game:
            earnings_json['game'] = game.__dict__
        return earnings_json

    @classmethod
    def search_clause(self, params):
        search_tuple = (params['platform'], params['rank_type'])
        query_str = f"""SELECT e.* FROM earnings AS e JOIN games AS g
                        ON g.id = e.game_id JOIN ratings AS r ON r.game_id = g.id 
                        WHERE g.platform = %s AND r.rank_type = %s"""
        return query_str, search_tuple

    @classmethod
    def search(self, params, cursor):
        if not params: return db.find_all(Earnings, cursor)
        query, search_tuple = self.search_clause(params)
        cursor.execute(query, search_tuple)
        records = cursor.fetchall()
        return db.build_from_records(Earnings, records)