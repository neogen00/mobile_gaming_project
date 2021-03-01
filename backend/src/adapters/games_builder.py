import src.models as models
import src.db as db
import src.adapters as adapters

class Builder:
    def run(self, TS_details, search_date, rank_type, conn, cursor):
        game = GameBuilder().run(TS_details, conn, cursor)
        print(game.__dict__)
        rating = RatingBuilder().run(TS_details, game, search_date, rank_type, conn, cursor)
        if game.exists:
            return {'game': game, 'rating': rating, 'earnings': game.earnings(TS_details, conn, cursor)} 
        else:
            earnings = EarningsBuilder().run(TS_details, game, conn, cursor)
            return {'game': game, 'rating': rating, 'earnings': earnings}

class GameBuilder:
    def __init__(self):
        self.IGDB_Client = adapters.IGDB_Client()
        self.RAWG_Client = adapters.RAWG_Client()
 
    attributes = ['name', 'platform', 'publisher', 'release_date', 'genre', 'game_engine']

    def select_attributes(self, TS_details):
        name_filtered = db.filter_name(db.encode_utf8(TS_details.get('humanized_name','')))
        release_date = self.RAWG_Client.find_release_date(name_filtered)
        if TS_details['os'] == 'ios':
            return dict(zip(self.attributes, [name_filtered, 'iOS', TS_details['publisher_name'], release_date, str(TS_details['categories']), None]))
        
        return dict(zip(self.attributes, [name_filtered, 'android', TS_details['publisher_name'], release_date, TS_details['categories'][0].split('_')[1], None]))

    def run(self, TS_details, conn, cursor):
        selected = self.select_attributes(TS_details)
        game_name, game_platform = selected['name'], selected['platform']
        game = models.Game.find_by_game_name_platform(game_name, game_platform, cursor)
        if game:
            game.exists = True            
        else:
            selected['game_engine'] = self.IGDB_Client.find_game_engine(game_name)  # limited query allowance, tap when DNE          
            game = db.save(models.Game(**selected), conn, cursor)
            game.exists = False
        game.try_sibling_params_if_None(conn, cursor)        
        return game

class EarningsBuilder:
    attributes = ['price', 'inapp', 'shows_ads', 'revenue', 'downloads']

    def select_attributes(self, TS_details):
        price, inapp, shows_ads, revenue, downloads = TS_details['price'], TS_details['in_app_purchases'], TS_details['shows_ads'], TS_details['humanized_worldwide_last_month_revenue']['revenue'], TS_details['humanized_worldwide_last_month_downloads']['downloads']
        
        return dict(zip(self.attributes, [price, inapp, shows_ads, revenue, downloads]))

    def run(self, TS_details, game, conn, cursor):
        earnings_attributes = self.select_attributes(TS_details)
        earnings = models.Earnings(**earnings_attributes)
        earnings.game_id = game.id 
        earnings = db.save(earnings, conn, cursor)        
        return earnings

class RatingBuilder:
    def __init__(self):
        self.RAWG_Client = adapters.RAWG_Client()

    attributes = ['metacritic', 'TS_rating', 'rank_type', 'ranking', 'date_created']

    def select_attributes(self, TS_details, search_date, rank_type):
        TS_rating, ranking_type, ranking, date_created = TS_details['rating'], rank_type, TS_details['rank'], search_date
        metacritic = self.RAWG_Client.find_metacritic(TS_details['name'])       
        return dict(zip(self.attributes, [metacritic, TS_rating, ranking_type, ranking, date_created]))

    def run(self, TS_details, game, search_date, rank_type, conn, cursor):
        selected = self.select_attributes(TS_details, search_date, rank_type)
        selected['game_id'] = game.id
        rating = models.Rating.find_by(selected['game_id'], selected['rank_type'], selected['ranking'], selected['date_created'], cursor)
        if not rating:
            rating = db.save(models.Rating(**selected), conn, cursor)        
        return rating