import src.db as db
import src.models as models

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

    def earnings(self, TS_details, conn, cursor):
        earnings_query = "SELECT * FROM earnings WHERE earnings.game_id = %s"
        cursor.execute(earnings_query, (self.id,))
        record = cursor.fetchone()
        earnings = db.build_from_record(models.Earnings, record)
        earnings.check_update_revenue_downloads(TS_details, conn, cursor)        
        return earnings
    
    def get_sibling(self, name, os, cursor):
        new_name = db.strip_last_specialchar(name)
        os_bar = {'android':'iOS', 'iOS':'android'}
        query = "SELECT * FROM games WHERE platform = %s AND name LIKE %s"
        cursor.execute(query, (os_bar[os],f"{new_name}%%"))
        record = cursor.fetchone()       
        return db.build_from_record(models.Game, record)

    def try_sibling_params_if_None(self, conn, cursor):
        try: sib = self.get_sibling(self.name, self.platform, cursor)
        except: cursor.execute('rollback;')
        if not sib: return
        if self.platform == 'iOS':
            self.genre = sib.genre
            db.update_column(self, 'genre', conn, cursor)
        self.check_update_game_engine_reldate(sib, conn, cursor)
        
    def check_update_game_engine_reldate(self, sib, conn, cursor):
        if not self.game_engine: 
            if sib.game_engine:
                self.game_engine = sib.game_engine
                db.update_column(self, 'game_engine', conn, cursor)
        if not self.release_date: 
            if sib.release_date: 
                self.release_date = sib.release_date
                db.update_column(self, 'release_date', conn, cursor)
    
    def revenue_per_downloads(self, cursor):
        rpd_columns = ['revenue', 'downloads', 'RPD', 'inapp', 'shows_ads']
        query_str =  """SELECT e.revenue, e.downloads, 
                        ROUND(e.revenue::NUMERIC/e.downloads, 2) AS RPD,
                        e.inapp, e.shows_ads FROM earnings AS e 
                        WHERE e.game_id = %s"""
        cursor.execute(query_str, (self.id,))
        record = cursor.fetchone()
        record_dict = dict(zip(rpd_columns, record))        
        return record_dict
    
    def to_json(self, cursor):
        game_json = self.__dict__
        game_json['RPD'] = self.revenue_per_downloads(cursor)        
        return game_json
