import datetime
import psycopg2
import pytest

import src.adapters as adapters
import src.db as db
import src.models as models
from settings import (DBTEST_USER, DBTEST_NAME, DBTEST_PASSWORD)
from  tests.data.builder_data import (s3d_rating, s3d_earnings, s3d_details, s3d_record_date, 
    s3d_rank_type, s3d_input, s3d_lower, s3d_higher, TS_details, amongus_ios, build_records_testing_models)


@pytest.fixture()
def test_conn():
    test_conn = psycopg2.connect(dbname = DBTEST_NAME, 
            user = DBTEST_USER, password = DBTEST_PASSWORD)
    cursor = test_conn.cursor()
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)
    yield test_conn
    db.drop_all_tables(test_conn, cursor)
    db.reset_all_primarykey(test_conn, cursor)


def test_Game_object_attributes():
    s3d_game = models.Game(**s3d_input)

    assert s3d_game.name == 'Sushi Roll 3D'
    assert s3d_game.genre == 'simulation' 

def test_Rating_object_attributes():
    s3d_r = models.Rating(**s3d_rating)

    assert s3d_r.ranking == 1
    assert s3d_r.date_created == datetime.date(2021, 1, 6)

def test_Earnings_object_attributes():
    s3d_e = models.Earnings(**s3d_earnings)

    assert s3d_e.inapp == False
    assert s3d_e.shows_ads == True 
    assert s3d_e.revenue == 1000 
    assert s3d_e.downloads == 21000000 

def test_Game_find_by_game_name_platform(test_conn):
    test_cursor = test_conn.cursor()
    build_records_testing_models(test_conn, test_cursor)
    amongus_i = models.Game.find_by_game_name_platform('Among Us!', 'iOS', test_cursor)

    assert amongus_i.name == 'Among Us!' 
    assert amongus_i.platform == 'iOS' 
    assert amongus_i.genre == '[6014,7001,7015]'
    assert amongus_i.release_date == None
    assert amongus_i.game_engine == None

def test_Game_get_sibling(test_conn):
    test_cursor = test_conn.cursor()
    build_records_testing_models(test_conn, test_cursor)
    amongus_i = models.Game.find_by_game_name_platform('Among Us!', 'iOS', test_cursor)
    amongus_a = amongus_i.get_sibling(amongus_i.name, amongus_i.platform, test_cursor)

    assert amongus_i.platform == 'iOS'
    assert amongus_a.platform == 'android'
    assert amongus_a.genre == 'action'
    assert amongus_a.release_date == datetime.date(2018, 7, 25)    

def test_Game_try_sibling_params_if_None(test_conn):
    test_cursor = test_conn.cursor()
    build_records_testing_models(test_conn, test_cursor)
    amongus_i = models.Game.find_by_game_name_platform('Among Us!', 'iOS', test_cursor)

    assert amongus_i.release_date == None
    assert amongus_i.game_engine == None

    amongus_i.try_sibling_params_if_None(test_conn, test_cursor)
    amongus_i_new = models.Game.find_by_game_name_platform('Among Us!', 'iOS', test_cursor)
    assert amongus_i_new.release_date == datetime.date(2018, 7, 25)
    assert amongus_i_new.game_engine == 'Unity' 

def test_update_revenue_downloads_equal_lower_value_no_update(test_conn):
    test_cursor = test_conn.cursor()
    builder = adapters.Builder()
    game_objs = builder.run(s3d_details, s3d_record_date, s3d_rank_type, test_conn, test_cursor)
    game = game_objs['game']
    same_earnings = game.earnings(s3d_lower, test_conn, test_cursor)

    assert same_earnings.revenue == 1000
    assert same_earnings.downloads == 21000000

def test_update_revenue_downloads_bigger_value_update(test_conn):
    test_cursor = test_conn.cursor()
    builder = adapters.Builder()
    game_objs = builder.run(s3d_details, s3d_record_date, s3d_rank_type, test_conn, test_cursor)
    game = game_objs['game']
    same_earnings = game.earnings(s3d_higher, test_conn, test_cursor)

    assert same_earnings.revenue == 2000
    assert same_earnings.downloads == 22000000

def test_integrated_try_sibling_params_if_None_update(test_conn):
    test_cursor = test_conn.cursor()
    builder = adapters.Builder()
    amongus_ios_objs_1st = builder.run(amongus_ios, '2020-12-20', 'top free', test_conn, test_cursor)

    assert amongus_ios_objs_1st['game'].genre == '[6014, 7001, 7015]'
    assert amongus_ios_objs_1st['game'].game_engine == None
    assert amongus_ios_objs_1st['game'].release_date == None   

    amongus_android_objs = builder.run(TS_details, '2020-12-28', 'top free', test_conn, test_cursor)
    amongus_ios_objs_2nd = builder.run(amongus_ios, '2020-12-20', 'top free', test_conn, test_cursor)

    assert amongus_ios_objs_2nd['game'].genre == 'action'
    assert amongus_ios_objs_2nd['game'].game_engine == 'Unity'
    assert amongus_ios_objs_2nd['game'].release_date == datetime.date(2018, 7, 25)





