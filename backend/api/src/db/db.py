from flask import current_app
from flask import g
import psycopg2

conn = psycopg2.connect(database = 'mobilegaming_development', user = 'postgres', password = 'postgres')
cursor = conn.cursor()

def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(user = 'postgres', password = 'postgres',
            dbname = current_app.config['DATABASE'])
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def build_from_record(Class, record):
    if not record: return None
    attr = dict(zip(Class.columns, record))
    obj = Class()
    obj.__dict__ = attr
    return obj

def build_from_records(Class, records):
   return [build_from_record(Class, record) for record in records]

def find_all(Class, cursor):
    sql_str = f"SELECT * FROM {Class.__table__} ORDER BY id"
    cursor.execute(sql_str)
    records = cursor.fetchall()
    return [build_from_record(Class, record) for record in records]

def find_all_games_withattr(Class, attribute, cursor):
    sql_str = f"SELECT {attribute} FROM {Class.__table__}"
    cursor.execute(sql_str)
    record = cursor.fetchone()
    return build_from_record(Class, record)

def find(Class, id, cursor):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE id = %s"
    cursor.execute(sql_str, (id,))
    record = cursor.fetchone()
    return build_from_record(Class, record)

def find_by_game_id(Class, id, cursor):
    sql_str = f"SELECT * FROM {Class.__table__} WHERE game_id = %s"
    cursor.execute(sql_str, (id,))
    records = cursor.fetchall()
    return build_from_records(Class, records)

def save(obj, conn, cursor):
    s_str = ', '.join(len(values(obj)) * ['%s'])
    game_str = f"""INSERT INTO {obj.__table__} ({keys(obj)}) VALUES ({s_str});"""
    cursor.execute(game_str, list(values(obj)))
    conn.commit()
    cursor.execute(f'SELECT * FROM {obj.__table__} ORDER BY id DESC LIMIT 1')
    record = cursor.fetchone()
    return build_from_record(type(obj), record)

def values(obj):
    game_attrs = obj.__dict__
    return [game_attrs[attr] for attr in obj.columns if attr in game_attrs.keys()]

def keys(obj):
    game_attrs = obj.__dict__
    selected = [attr for attr in obj.columns if attr in game_attrs.keys()]
    return ', '.join(selected)

def reset_all_primarykey(conn, cursor):
    table_names = ['games', 'earnings', 'ratings']
    for table in table_names:
        cursor.execute(f'ALTER SEQUENCE {table}_id_seq RESTART;')
        conn.commit()

def drop_records(cursor, conn, table_name):
    # cursor.execute(f"DELETE FROM {table_name};")
    cursor.execute(f"TRUNCATE {table_name} CASCADE;")  # allows to delete table with foreign key
    conn.commit()

def drop_tables(table_names, cursor, conn):
    for table_name in table_names:
        drop_records(cursor, conn, table_name)

def drop_all_tables(conn, cursor):
    table_names = ['games', 'earnings', 'ratings']
    drop_tables(table_names, cursor, conn)

def find_by_name(Class, name, cursor):
    query = f"""SELECT * FROM {Class.__table__} WHERE name = %s """
    cursor.execute(query, (name,))
    record =  cursor.fetchone()
    obj = build_from_record(Class, record)
    return obj

def find_or_create_by_name(Class, name, conn, cursor):
    obj = find_by_name(Class, name, cursor)
    if not obj:
        new_obj = Class()
        new_obj.name = name
        obj = save(new_obj, conn, cursor)
    return obj

def find_or_build_by_name(Class, name, cursor):
    obj = Class.find_by_name(name, cursor)
    if not obj:
        obj = Class()
        obj.name = name
    return obj

def update_column(obj, column, conn, cursor):
    obj_dict = obj.__dict__
    update_str = f"""UPDATE {obj.__table__} SET {column} = '{obj_dict.get(column,[])}'
                    WHERE id = {obj.id};"""
    cursor.execute(update_str)
    conn.commit()
    return