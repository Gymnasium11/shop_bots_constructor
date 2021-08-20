from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


def run(token):
    bot = Bot(token=token)
    dp = Dispatcher(bot)

    trash = [('Honey',
              'https://medrossii.ru/images/001/%D0%91%D0%B0%D1%88%D0%BA%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BC'
              '%D0%B5%D0%B4.jpg'),
             ('Milk', 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Milk_glass.jpg')]

    @dp.message_handler(commands=['start'])
    async def start(message):
        text = f'{message.from_user.first_name + " " + message.from_user.last_name}, добро' \
               'пожаловать в магазин «Store» bot!\n' \
               'Дата открытия магазина: ХХ.ХХ.ХХ\n' \
               'Количество категорий: X\n' \
               'Количество товаров: X\n' \
               'Здесь Вы найдете и закажите тот' \
               'самый товар, который давно искали!' \
               'Либо Вам понравится другой товар!\n' \
               ':)'

        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        kb.add(types.KeyboardButton('📖Каталог'))
        kb.add(types.KeyboardButton('🛒Корзина'))
        kb.add(types.KeyboardButton('🎪О магазине'))
        kb.add(types.KeyboardButton('📞Связаться с оператором'))
        await message.answer(text, reply_markup=kb)
        print(message)

    @dp.message_handler(lambda message: message.text == '📖Каталог')
    async def catalog(message):
        text = "Каталог\n|\n|\n|\n|\n|"
        await message.answer(text)

    @dp.message_handler(lambda message: message.text == '🛒Корзина')
    async def trash(message):
        text = ' Корзина' \
               '' \
               '\n|\n|\n|\n|\n| **жирный шрифт** *курсив*'

        await message.answer(text, parse_mode='Markdown')

        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(types.InlineKeyboardButton(callback_data='nothing', text='Подробнее про знак', ))
        kb.add(types.InlineKeyboardButton(callback_data='nothing', text='назад'))

        for i in trash:
            await message.answer_photo(i[1], caption=i[0], reply_markup=kb)

    @dp.message_handler(lambda message: message.text == '🎪О магазине')
    async def about_shop(message):
        text = 'Рейтинг: X\n' \
               'Количество заказов: X\n' \
               'Название: XXX\n' \
               'Дата открытия: XX.XX.XX\n' \
               'Количество товаров: X\n' \
               'Категория магазина: XXX\n' \
               'Описание: XXX\n' \
               'Контакты: XXX\n'
        await message.answer(text)

    @dp.message_handler(lambda message: message.text == '📞Связаться с оператором')
    async def contact_with_operator(message):
        text = "По всем вопросам обращайтесь к @Uxuxd"
        await message.answer(text)



    @dp.message_handler()
    async def echo_message(msg: types.Message):
        await bot.send_message(msg.from_user.id, msg.text)

    executor.start_polling(dp)
