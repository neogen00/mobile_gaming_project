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
        query = "SELECT * FROM %s WHERE platform = '%s' AND name LIKE '%s%%';" % (self.__table__,os_bar[os],new_name)
        cursor.execute(query)
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
        return
        
    def check_update_game_engine_reldate(self, sib, conn, cursor):
        if not self.game_engine: 
            if sib.game_engine:
                self.game_engine = sib.game_engine
                db.update_column(self, 'game_engine', conn, cursor)
        if not self.release_date: 
            if sib.release_date: 
                self.release_date = sib.release_date
                db.update_column(self, 'release_date', conn, cursor)
        return