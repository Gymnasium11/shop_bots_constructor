from aiogram import types
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

bot_creator_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
bot_creator_keyboard.add('Мои магазины')
bot_creator_keyboard.add('Добавить магазин')
bot_creator_keyboard.add('Связаться с оператором')