from aiogram import Bot, Router
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import Command, CommandObject

from src.handlers.filters import ChatTypeFilter
from src.plogger import get_pretty_logger


user_router = Router()

# start for any user
@user_router.message(
    Command(commands=['start']),
    ChatTypeFilter('private')
)
async def cmd_start(msg: Message, cmd: CommandObject):
    'start handler'
    # TODO дописать, бд тоже

