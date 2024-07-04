import os
import sqlite3

from datetime import datetime

from custom_logging import getLogger
from settings import DB_PATH


logger = getLogger('db')

class Status():
    


def init() -> None:
    '''
    database initialization
    '''
    # init db, cur
    global db, cur
    db = sqlite3.connect(DB_PATH)
    cur = db.cursor()
    
    # creating tables
    _create_tables()

    logger.info('Инициализация базы данных')

    # making dir for photos
    try:
        os.mkdir(r'photos')
    except FileExistsError:
        pass


def close() -> None:
    global db
    db.close()
    logger.info('база данных закрыта')


def _create_tables() -> None:
    '''
    Creating db tables if they not exists
    '''
    global cur, db
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS users(
            user_tg_id INTEGER,
            date STRING,
            fullname STRING,
            username STRING,
            status STRING,
            old_info STRING
        )'''
    )
    db.commit()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS moderators(
            moder_tg_id INTEGER,
            moderating_msgs_msg_id INTEGER
        )'''
    )
    db.commit()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS messages(
        msg_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_tg_id INTEGER
        date STRING,
        text STRING,
        has_photo BOOLEAN,
        status STRING,
        reason_if_refused STRING
        )'''
    )


# TODO написать функцию обновления данных юзера при написании им сообщения
# TODO добавить в логи присоединения и удаления пользователей с канала
# TODO добавить сохранение комментов (опционально)

def add_user(
    user_tg_id: int,
    fullname: str,
    username: str
    ):
    cur.execute(
        'INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)',
        (int(user_tg_id), datetime.today, fullname, username, '')
    )

def _check_user_id_in_db(user_tg_id: int) -> bool:
    global cur
    id = cur.execute('SELECT user_tg_id FROM users WHERE user_tg_id = ?', user_tg_id)
    if len(id) == 1:
        return True
    return False
