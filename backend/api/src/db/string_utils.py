import datetime
import string
import unidecode


def isUnicode(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def encode_utf8(str_raw):
    temp_s = unidecode.unidecode(str_raw)
    return temp_s.split('[')[0]

def filter_name(name):
    return ''.join(filter(lambda x: x in string.printable, name))

def strip_last_specialchar(s):
    if not s[-1].isalpha():
        return s[:-1]
    else:
        return s

def date_adding_formatter(date_str='2021-1-1', days=3):
    date_temp = datetime.datetime.strptime(date_str, '%Y-%m-%d') + datetime.timedelta(days)
    date_new = date_temp.strftime('%F').replace('-0','-')
    return date_new
