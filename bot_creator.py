from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import states
import keyboards
from config import TOKEN
from messages import MESSAGES
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest

# Создание экземпляров классов Bot и Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def username2id(username):
    async with TelegramClient('hhsked', 7891326, "b626fc3516cdef753a9d27dcf096fd25") as client:
        user = await client(GetFullUserRequest(username))
    return user.user.id


async def is_bot(username):
    async with TelegramClient('hhsked', 7891326, "b626fc3516cdef753a9d27dcf096fd25") as client:
        user = await client(GetFullUserRequest(username))
    return user.user.bot


@dp.message_handler(commands=['start'])
async def process_start_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['start'], reply_markup=keyboards.bot_creator_keyboard, )


@dp.message_handler(commands=['help'])
async def process_start_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['help'], reply_markup=keyboards.bot_creator_keyboard)


@dp.message_handler(commands=['set_admin'])
async def process_set_admin_command(message):
    args = [arg.strip('@ ') for arg in message.text.split()[1:]]
    if await is_bot(args[0]) and not await is_bot(args[1]):
        print("ТУТ ЗАПРОС В БД")
    else:
        await bot.send_message(message.from_user.id, 'Invalid Syntax', reply_markup=keyboards.bot_creator_keyboard)


@dp.message_handler(lambda message: [message.text] in keyboards.bot_creator_keyboard['keyboard'])
async def process_three_base_commands(message):
    await bot.send_message(message.from_user.id, MESSAGES[message.text])
    if message.text == 'Добавить магазин':
        await states.TwoStates.ADD_SHOP.set()


@dp.message_handler(state=states.TwoStates.ADD_SHOP)
async def process_add_shop_command(message):
    token = message.text
    await bot.send_message(message.from_user.id, MESSAGES['done'])
    await states.TwoStates.next()


if __name__ == '__main__':
    executor.start_polling(dp)
