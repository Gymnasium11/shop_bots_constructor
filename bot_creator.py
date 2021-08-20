from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram import executor

import keyboards
from config import TOKEN
from messages import MESSAGES

# Создание экземпляров классов Bot и Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['start'])

@dp.message_handler(commands=['help'])
async def process_start_command(message):
    await bot.send_message(message.from_user.id, MESSAGES['help'])

@dp.message_handler(lambda message: message in keyboards.bot_creator_keyboard['keyboard'])
async def process_three_base_commands(message):
    await message.reply(MESSAGES[message])


if __name__ == '__main__':
    executor.start_polling(dp)
