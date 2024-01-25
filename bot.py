import asyncio

import colorama
from colorama import Fore, Back

from src import db
from src.logger import get_logger
from src.phrases import Bot


colorama.init(autoreset=True)

logger = get_logger('bot')


@logger.catch
async def main():
    'Bot starting'
    db.init()


if __name__ == '__main__':
    print(Fore.RED + Bot.CMD_BOT_START.value)
    print(Back.GREEN + Bot.BOT_START.value)
    logger.info(Bot.BOT_START.value)
    try:
        asyncio.run(main())
    
    except KeyboardInterrupt:
        logger.info('Bot stopped by keyboard')
    
    except Exception as e:
        logger.exception(f'Bot dropped with exception:\n{e}')
    
    finally:
        logger.info(Bot.BOT_STOP.value)
        print(Back.RED + Bot.BOT_STOP.value)
