from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


from common.database import add_user, get_user_by_id


start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать!!!')


@start_router.message(Command('register'))
async def register(message: Message):
    telegram_id = message.from_user.id
    user_data = await get_user_by_id(telegram_id)

    if user_data is None:
        # Если пользователь не найден, добавляем его в базу данных
        await add_user(
            telegram_id=telegram_id,
            username=message.from_user.username,
            first_name=message.from_user.first_name
        )
        await message.answer('Успешно')        
    else:
        await message.answer('Пользователь уже зарегистрирован')        
    