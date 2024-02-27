import os
import asyncio

import colorama
from colorama import Fore, Back

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError

from src import db
from src.logger import get_logger
from src.phrases import BotPhrases


colorama.init(autoreset=True)

logger = get_logger('bot')


@logger.catch()
async def main():
    load_dotenv('.env')
    
    db.init()
    
    token = os.getenv("TOKEN")
    bot = Bot(token)
    dp = Dispatcher()
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    try:
        await dp.start_polling(bot)
    
    except TelegramNetworkError:
        logger.info('Connection reset by peer, retry after 1 sec')
    
    except Exception:
        logger.critical()


if __name__ == '__main__':
    print(Fore.RED + BotPhrases.CMD_BOT_START)
    print(Back.GREEN + BotPhrases.BOT_START)
    logger.info(BotPhrases.BOT_START)
    
    try:
        asyncio.run(main())
    
    except KeyboardInterrupt:
        logger.info('Bot stopped by keyboard')
    
    finally:
        logger.info(BotPhrases.BOT_STOP)
        print(Back.RED + BotPhrases.BOT_STOP)
