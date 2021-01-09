import pytest
import string
import unidecode

from api.src.db.string_utils import (isUnicode, encode_utf8, filter_name, strip_last_specialchar)


BingoBlitz_name_error = 'Bingo Blitz️'
pokemongo = 'Pokémon GO'
amongus_ios = 'Among Us!'

def test_BingoBlitz_game_title_filter_non_unicode():
    name_filtered = filter_name(encode_utf8(BingoBlitz_name_error))
    assert name_filtered == 'Bingo Blitz'

def test_pokemon_go_name_filter_accent_mark():
    name_filtered = filter_name(encode_utf8(pokemongo))
    assert name_filtered == 'Pokemon GO'

def test_filter_chinese_character():
    name_filtered = filter_name(encode_utf8('通'))
    assert name_filtered == 'Tong '

def test_isUnicode_true():
    assert isUnicode(amongus_ios) == True

def test_isUnicode_false():
    assert isUnicode(BingoBlitz_name_error) == False

def test_strip_last_specialchar_exclamation():
    assert strip_last_specialchar(amongus_ios) == 'Among Us'

def test_strip_last_specialchar_does_not_strip_alphanum():
    assert strip_last_specialchar(pokemongo) == 'Pokémon GO'
    
