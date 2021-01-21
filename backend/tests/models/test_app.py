from flask import json
import pytest

from api.src import create_app
from api.src.db import db
import api.src.models as models
from tests.data.builder_data import build_records_test_flask


@pytest.fixture(scope = 'module')
def app():
    flask_app = create_app('mobilegaming_test', testing = True, debug = True)

    with flask_app.app_context():
        conn = db.get_db()
        cursor = conn.cursor()
        db.drop_all_tables(conn, cursor)
        db.reset_all_primarykey(conn, cursor)
        build_records(conn, cursor)

        conn.commit()
        db.close_db()
    yield flask_app

    with flask_app.app_context():
        db.close_db()
        conn = db.get_db()
        cursor = conn.cursor()
        db.drop_all_tables(conn, cursor)
        db.reset_all_primarykey(conn, cursor)
        db.close_db()


def build_records(conn, cursor):
    build_records_test_flask(conn, cursor)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_root_url(app, client):
    response = client.get('/')
    assert b'Welcome to the mobile gaming api' in response.data

def test_games_index(app, client):
    response = client.get('/games')
    json_response = json.loads(response.data)

    assert len(json_response) == 6
    assert json_response[3]['name'] == 'Among Us!'
    assert json_response[5]['name'] == 'Roblox'
    assert list(json_response[0].keys()) == ['id', 'name', 'platform', 'publisher', 'release_date', 'genre', 'game_engine']

def test_games_id(app, client):
    response = client.get('/games')
    json_response = json.loads(response.data)
    last_record_id = json_response[-1]['id']

    response = client.get(f'/games/{last_record_id}')
    json_response = json.loads(response.data)
    assert json_response['name'] == 'Roblox'

def test_games_earnings_search(app, client):
    response = client.get('/games/earnings/search?platform=iOS&rank_type=top%20paid')
    json_response = json.loads(response.data)

    assert json_response[0]['game']['name'] == 'Minecraft'
    assert json_response[0]['game']['platform'] == 'iOS'

def test_games_rating_id(app, client):
    response = client.get('/games/rating/4')
    json_response = json.loads(response.data)

    assert json_response[0]['game'] == {"id": 4, "name": "Among Us!", "platform": "iOS", "publisher": "InnerSloth LLC", "release_date": "2018-07-25", "genre": "action", "game_engine": "Unity"} 
    assert json_response[0]['ranking'] == 1
    assert json_response[0]['rank_type'] == 'top free'

def test_games_all_data(app, client):
    response = client.get('/games/all_data')
    json_response = json.loads(response.data)

    assert len(json_response) == 6
    assert json_response[2]['game']['name'] == "Roblox"
    assert json_response[2]['game']['platform'] == "android"
    assert json_response[1]['game']['name'] == "Minecraft"
    assert json_response[1]['game']['platform'] == "android"