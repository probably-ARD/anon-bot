import os
import asyncio

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError

import settings
from src import db
from src.phrases import BotPhrases, LogPhrases
from custom_logging import getLogger


logger = getLogger('bot')

async def main():
    load_dotenv('.env')

    db.init()

    token = os.getenv('TOKEN')
    bot = Bot(token)
    dp = Dispatcher()
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    try:
        await dp.start_polling(bot)
    
    except TelegramNetworkError:
        logger.warning('ошибка подключения, переподключение')
    
    except Exception as e:
        logger.critical('неизвестная ошибка:', '\n', e, stack_info=True)


if __name__ == '__main__':
    print(BotPhrases.CMD_BOT_START)
    logger.info(BotPhrases.BOT_START)
    
    try:
        asyncio.run(main())
    
    except KeyboardInterrupt:
        logger.info(LogPhrases.InterruptException)
    
    finally:
        db.close()
        logger.info()
