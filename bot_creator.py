from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor
from aiogram.dispatcher.filters import BoundFilter
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import states
import keyboards
from config import TOKEN
from messages import MESSAGES

# Создание экземпляров классов Bot и Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def process_start_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['start'], reply_markup=keyboards.bot_creator_keyboard)

@dp.message_handler(commands=['help'])
async def process_start_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['help'], reply_markup=keyboards.bot_creator_keyboard)

@dp.message_handler(lambda message: [message.text] in keyboards.bot_creator_keyboard['keyboard'])
async def process_three_base_commands(message):
    await bot.send_message(message.from_user.id, MESSAGES[message.text])
    if message.text == 'Добавить магазин':
        await states.TwoStates.ADD_SHOP.set()
    elif message.text == 'Мои магазины':
        await states.TwoStates.ADD_SHOP.set()

@dp.message_handler(state=states.ThreeStates.ADD_SHOP)
async def process_add_shop_command(message):
    token = message.text
    await bot.send_message(message.from_user.id, MESSAGES['done'])
    await states.TwoStates.next()


@dp.message_handler(state=states.TwoStates.MY_SHOPS)
async def process_my_shops_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['done'])
    await states.TwoStates.next()


if __name__ == '__main__':
    executor.start_polling(dp)
