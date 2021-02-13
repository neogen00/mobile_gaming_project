import datetime
import psycopg2
import pytest

import src.adapters as adapters
import src.db.db as db
import src.models as models
from settings import (DBTEST_USER, DBTEST_NAME, DBTEST_PASSWORD)


@pytest.fixture(scope = 'module')
def test_conn():
    test_conn = psycopg2.connect(dbname = DBTEST_NAME, 
            user = DBTEST_USER, password = DBTEST_PASSWORD)
    cursor = test_conn.cursor()
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)
    yield test_conn
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)


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
    e1 = {"id": 1, "game_id": 1, "price": 0.0, "inapp": True, "shows_ads": False, "revenue": 2000000, "downloads": 29000000}
    earnings = db.save(models.Earnings(**e1), test_conn, test_cursor)
    
    earnings.downloads = 23000000
    db.update_column(earnings, 'downloads', test_conn, test_cursor)
    earnings.revenue = 1
    db.update_column(earnings, 'revenue', test_conn, test_cursor)
    
    earnings_update = db.find(models.Earnings, earnings.id, test_cursor)
    assert earnings_update.downloads == 23000000
    assert earnings_update.revenue == 1