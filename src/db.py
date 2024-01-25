import os
import sqlite3
import datetime
from dotenv import load_dotenv

from settings import Settings


def init() -> None:
    '''
    database initialization
    '''
    # init db, cur
    global db, cur
    db = sqlite3.connect(Settings.DB_PATH.value)
    cur = db.cursor()

    # creating tables
    _create_tables()

    # making dir to photos
    try:
        os.mkdir(r'photos')
    except FileExistsError:
        pass


def _create_tables() -> None:
    '''
    Creating db tables if they not exists
    '''
    global cur, db
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS msgs_queue(
            user_tg_id INTEGER,
            user_chat_id INTEGER,
            user_msg_id INTEGER,
            msg_id INTEGER,
            fullname STRING,
            username STRING,
            date STRING,
            text STRING,
            has_photo BOOLEAN,
            moder_tg_id INTEGER
        )'''
    )
    db.commit()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS moders(
            moder_tg_id INTEGER,
            moderating_msg_id INTEGER,
            count_msgs_tg_id INTEGER,
            not_msgs_tg_id INTEGER
        )'''
    )
    db.commit()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS approved_msgs(
            user_tg_id INTEGER,
            fullname STRING,
            username STRING,
            date STRING,
            text STRING,
            has_photo BOOLEAN
        )'''
    )
    db.commit()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS refused_msgs(
            user_tg_id INTEGER,
            fullname STRING,
            username STRING,
            date STRING,
            text STRING,
            has_photo BOOLEAN,
            reason STRING
        )'''
    )
    db.commit()
