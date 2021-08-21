from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from database import read
from asyncio import sleep

import states
import pandas
import keyboards
from config import TOKEN
from messages import MESSAGES
from telethon import TelegramClient
from telethon.tl.functions.users import GetFullUserRequest
import telebot
import database


def get_info(token):
    try:
        a = telebot.TeleBot(token).get_me()
    except:
        return False
    return a.first_name, a.username


# Создание экземпляров классов Bot и Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.callback_query_handler(lambda call: call.data.startswith('getInfo_'))
async def da(call):
    admin = call['from']['id']
    shop = call.data[8:]
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(callback_data=f'myShops_{admin}', text='Назад'))
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        text=f"Магазин {shop}",
        message_id=call.message.message_id,
        reply_markup=kb
    )


@dp.callback_query_handler(lambda call: call.data.startswith('myShops_'))
async def da(call):
    admin = call.data[8:]
    rez = read("SELECT * FROM shops;")
    rez = [i[1] for i in rez if str(admin) in i[3].split()]
    kb = types.InlineKeyboardMarkup()
    for i in rez:
        kb.add(types.InlineKeyboardButton(text=i, callback_data="getInfo_" + i))
    await bot.edit_message_text(
        chat_id=call.message.chat.id,
        text=f"Мои магазины:",
        message_id=call.message.message_id,
        reply_markup=kb
    )


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
    await bot.send_message(message.from_user.id, MESSAGES['start'], reply_markup=keyboards.bot_creator_keyboard)


@dp.message_handler(commands=['help'])
async def process_start_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['help'], reply_markup=keyboards.bot_creator_keyboard)


@dp.message_handler(
    lambda message: [message.text] in keyboards.bot_creator_keyboard['keyboard'] and message.text == 'Мои магазины')
async def process_three_base_commands(message):
    admin = message.from_user.id
    rez = read("SELECT * FROM shops;")
    rez = [i[1] for i in rez if str(admin) in i[3].split()]
    kb = types.InlineKeyboardMarkup()
    for i in rez:
        kb.add(types.InlineKeyboardButton(text=i, callback_data="getInfo_" + i))
    await message.answer("Мои магазины:", reply_markup=kb)


@dp.message_handler(lambda message: [message.text] in keyboards.bot_creator_keyboard['keyboard'])
async def process_three_base_commands(message):
    if message.text == 'Добавить магазин':
        await message.answer(MESSAGES['Добавить магазин'])
        await states.TwoStates.ADD_SHOP.set()
    else:
        await message.answer(MESSAGES[message.text])


@dp.message_handler(state=states.TwoStates.ADD_SHOP)
async def process_add_shop_command(message):
    token = message.text
    if get_info(token):
        first_name, username = get_info(token)
        database.insert(
            f"INSERT INTO shops (name, nick_name, token, admins, rating, count_solled) VALUES ('{first_name}', '{username}' ,'{token}', '{message.from_user.id}', '{0}', '{0}')")
        await bot.send_message(message.from_user.id, "Бот успешно создан. Enjoy it!")
        await states.TwoStates.next()
    else:
        await bot.send_message(message.from_user.id, "Токен невалиден")
        await states.TwoStates.next()
        await sleep(0.7)
        await bot.send_message(message.from_user.id, "Вы в меню")


if __name__ == '__main__':
    executor.start_polling(dp)
