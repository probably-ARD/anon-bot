import os
import asyncio

import colorama
from colorama import Fore, Back

from dotenv import load_dotenv

from aiogram.types import Message
from aiogram import Bot, Dispatcher, Router

from src import db
from src.logger import get_logger
from src.phrases import BotPhrases


colorama.init(autoreset=True)

logger = get_logger('bot')


async def main():
    load_dotenv('.env')
    db.init()
    
    token = os.getenv("TOKEN")
    bot = Bot(token)
    dp = Dispatcher()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print(Fore.RED + BotPhrases.CMD_BOT_START.value)
    print(Back.GREEN + BotPhrases.BOT_START.value)
    logger.info(BotPhrases.BOT_START.value)
    
    try:
        asyncio.run(main())
    
    except KeyboardInterrupt:
        logger.info('Bot stopped by keyboard')
    
    finally:
        logger.info(BotPhrases.BOT_STOP.value)
        print(Back.RED + BotPhrases.BOT_STOP.value)
