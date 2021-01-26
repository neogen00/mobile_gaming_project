import datetime
import psycopg2
import pytest

import api.src.adapters as adapters
import api.src.db.db as db
import api.src.models as models
# from  tests.data.builder_data import (s3d_rating, s3d_earnings, s3d_details, s3d_record_date, s3d_rank_type, s3d_input, s3d_lower, s3d_higher, TS_details, amongus_ios)


@pytest.fixture(scope = 'module')
def test_conn():
    test_conn = psycopg2.connect(dbname = 'mobilegaming_test', 
            user = 'postgres', password = 'postgres')
    cursor = test_conn.cursor()
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)
    yield test_conn
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)


# def build_record(test_conn, cursor):
#     r1 = {"id": 1, "game_id": 1, "metacritic": 84, "TS_rating": 4.43, "rank_type": "top free", "ranking": 1, "date_created": "2021-01-01"}
#     g1 = {"id": 1, "name": "Among Us", "platform": "android", "publisher": "Innersloth LLC", "release_date": "2018-07-25", "genre": "action", "game_engine": "Unity"}
#     e1 = {"id": 1, "game_id": 1, "price": 0.0, "inapp": True, "shows_ads": False, "revenue": 2000000, "downloads": 29000000}
#     game = db.save(models.Game(**g1), test_conn, cursor)
#     rating = db.save(models.Rating(**r1), test_conn, cursor)
#     earnings = db.save(models.Earnings(**e1), test_conn, cursor)
#     return game, rating, earnings

def test_update_column_for_games_table(test_conn):
    test_cursor = test_conn.cursor()
    g1 = {"id": 1, "name": "Among Us", "platform": "android", "publisher": "Innersloth LLC", "release_date": "2018-07-25", "genre": "action", "game_engine": "Unity"}
    game = db.save(models.Game(**g1), test_conn, test_cursor)
    
    game.game_engine = 'something_else'
    db.update_column(game, 'game_engine', test_conn, test_cursor)
    game.genre = 'Space Wars'
    db.update_column(game, 'genre', test_conn, test_cursor)
    
    game_update = db.find(models.Game, game.id, test_cursor)
    assert game_update.game_engine == 'something_else'
    assert game_update.genre == 'Space Wars'


def test_update_column_for_earnings_table(test_conn):
    test_cursor = test_conn.cursor()
    # g1 = {"id": 1, "name": "Among Us", "platform": "android", "publisher": "Innersloth LLC", "release_date": "2018-07-25", "genre": "action", "game_engine": "Unity"}
    e1 = {"id": 1, "game_id": 1, "price": 0.0, "inapp": True, "shows_ads": False, "revenue": 2000000, "downloads": 29000000}
    # game = db.save(models.Game(**g1), test_conn, test_cursor)
    earnings = db.save(models.Earnings(**e1), test_conn, test_cursor)
    
    earnings.downloads = 23000000
    db.update_column(earnings, 'downloads', test_conn, test_cursor)
    earnings.revenue = 1
    db.update_column(earnings, 'revenue', test_conn, test_cursor)
    
    earnings_update = db.find(models.Earnings, earnings.id, test_cursor)
    assert earnings_update.downloads == 23000000
    assert earnings_update.revenue == 1