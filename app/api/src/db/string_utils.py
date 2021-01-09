import unidecode
import string
import re

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

def strip_str_special(s):
    res = re.findall(r"[\w']+", s)
    new_name = " ".join(res)

def strip_last_specialchar(s):
    if not s[-1].isalpha():
        return s[:-1]
    else:
        return s