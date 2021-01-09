from flask import Flask
import simplejson as json
from flask import request

import api.src.models as models
import api.src.db as db

def create_app(database='mobilegaming_development', testing = False, debug = True):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=database,
        DEBUG = debug,
        TESTING = testing
    )

    @app.route('/')
    def root_url():
        return 'Welcome to the mobile gaming api'

    @app.route('/games')
    def games():
        conn = db.get_db()
        cursor = conn.cursor()

        games = db.find_all(models.Game, cursor)
        game_dicts = [game.__dict__ for game in games]
        return json.dumps(game_dicts, default = str)
    
    @app.route('/games/earnings')
    def search_games_add_earnings():
        conn = db.get_db()
        cursor = conn.cursor()

        games = models.Game.search(cursor)
        game_dicts = [game.to_json(cursor) for game in games]
        return json.dumps(game_dicts, default = str)

    @app.route('/earnings')
    def earnings():
        conn = db.get_db()
        cursor = conn.cursor()

        earnings = db.find_all(models.Earnings, cursor)
        earning_dicts = [earning.__dict__ for earning in earnings]
        return json.dumps(earning_dicts, default = str)

    @app.route('/ratings')
    def ratings():
        conn = db.get_db()
        cursor = conn.cursor()

        ratings = db.find_all(models.Rating, cursor)
        rating_dicts = [rating.__dict__ for rating in ratings]
        return json.dumps(rating_dicts, default = str)

    return app