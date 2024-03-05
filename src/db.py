import os
import sqlite3
import datetime
from dotenv import load_dotenv

from aiogram.types import Message

from settings import Settings


def init() -> None:
    '''
    database initialization
    '''
    # init db, cur
    global db, cur
    db = sqlite3.connect(r'anon_bot.db')
    cur = db.cursor()

    # creating tables
    _create_tables()

    # making dir for photos
    try:
        os.mkdir(r'photos')
    except FileExistsError:
        pass


def close() -> None:
    global db
    db.close()


def _create_tables() -> None:
    '''
    Creating db tables if they not exists
    '''
    global cur, db
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS users(
            user_tg_id INTEGER,
            date STRING
        )'''
    )
    db.commit()
    
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
            has_photo BOOLEAN
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
            msg_id INTEGER,
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
            msg_id INTEGER,
            text STRING,
            has_photo BOOLEAN,
            reason STRING
        )'''
    )
    db.commit()

def _get_id_to_new_msg() -> int:
    '''
    returns msg_id to new message
    '''
    global cur
    id = len([id[0] for id in cur.execute("""SELECT msg_id FROM messages""")])
    return id


def add_new_msg(msg: Message) -> int:
    '''
    Adding message to msgs_queue table
    Return msg_id: int
    '''
    global db, cur
    if msg.photo:
        has_photo = True
        text = msg.caption
    else:
        has_photo = False
        text = msg.text

    msg_id = _get_id_to_new_msg()
    date = str(datetime.date.today())
    
    # msgs_queue structure
    # user_tg_id INTEGER,
    # user_chat_id INTEGER,
    # user_msg_id INTEGER,
    # msg_id INTEGER,
    # fullname STRING,
    # username STRING,
    # date STRING,
    # text STRING,
    # has_photo BOOLEAN
    
    cur.execute(
        '''INSERT INTO msgs_queue VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (
            msg.from_user.id, msg.chat.id, msg.message_id, 
            msg_id, msg.from_user.full_name, msg.from_user.username, 
            date, text, has_photo
        )
    )
    db.commit()

    return msg_id
