from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bot_creator_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
bot_creator_keyboard.add('Мои магазины')
bot_creator_keyboard.add('Добавить магазин')
bot_creator_keyboard.add('Связаться с оператором')