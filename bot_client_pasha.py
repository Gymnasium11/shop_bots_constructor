from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from database import read
import telebot


def run(token):
    bot = Bot(token=token)
    dp = Dispatcher(bot)

    @dp.message_handler(content_types=['document'])
    def catalog(message):
        print(message)
        raw = message.document.file_id
        path = raw + ".xls"
        file_info = bot.get_file(raw)
        downloaded_file = bot.download_file(file_info.file_id)
        # print(l)
        with open(path, 'wb') as new_file:
            new_file.write(downloaded_file)
        message.answer('nonnnnononon')

    @dp.message_handler(commands=['start'])
    async def start(message):
        l = [message.from_user.first_name, message.from_user.first_name]
        l_n = [i for i in l if i]
        text = f'{" ".join(l_n)}, Добро ' \
               'пожаловать в магазин «Store» bot!\n' \
               'Дата открытия магазина: ХХ.ХХ.ХХ\n' \
               'Количество категорий: X\n' \
               'Количество товаров: X\n' \
               'Здесь Вы найдете и закажите тот' \
               'самый товар, который давно искали!' \
               'Либо Вам понравится другой товар!\n' \
               ':)'
        a = await bot.get_me()
        print(a)
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        kb.add(types.KeyboardButton('📖Каталог'))
        kb.add(types.KeyboardButton('🛒Корзина'))
        kb.add(types.KeyboardButton('🎪О магазине'))
        kb.add(types.KeyboardButton('📞Связаться с оператором'))

        admins = read(f"SELECT DISTINCT admins FROM shops WHERE name='{a.username}';")
        if admins and message.from_user.id and str(message.from_user.id) in admins[0][0].split(' '):
            kb.add(types.KeyboardButton('🛠Загрузить таблицу товаров'))
        await message.answer(text, reply_markup=kb)

    @dp.message_handler(lambda message: message.text == "🛠Загрузить таблицу товаров")
    async def catalog(message):
        text = "Оправьте мне таблицу товаров в формате xls/xlsx"

        await message.answer(text)

    @dp.message_handler(lambda message: message.text == '📖Каталог')
    async def catalog(message):
        text = "Каталог"
        a = await bot.get_me()
        rez = read(f"SELECT * FROM product WHERE id_shop='{a.username}'")
        print(rez)
        for i in rez:
            product_id = i[0]

            article = i[2]
            title = i[3]
            price = i[4]
            cat = i[5]
            short_desc = i[6]
            desc = i[7]
            pict_url = i[8]
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(callback_data=f'further_{product_id}', text='Подробнее'))
            kb.add(types.InlineKeyboardButton(callback_data=f'totrash_{product_id}', text='В корзину'))
            text = f'**{title}**\n' + short_desc
            await message.answer_photo(pict_url, caption=text, reply_markup=kb, parse_mode='markdown')

    @dp.message_handler(lambda message: message.text == '🛒Корзина')
    async def trash(message):
        trash = [('Honey',
                  'https://medrossii.ru/images/001/%D0%91%D0%B0%D1%88%D0%BA%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BC'
                  '%D0%B5%D0%B4.jpg'),
                 ('Milk', 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Milk_glass.jpg')]
        text = 'Корзина' \
               '**жирный шрифт** *курсив*'

        await message.answer(text, parse_mode='Markdown')

        for i in trash:
            kb = types.InlineKeyboardMarkup()
            kb.add(types.InlineKeyboardButton(callback_data=f'further_{id}', text='Подробнее'))
            kb.add(types.InlineKeyboardButton(callback_data='nothing', text='назад'))
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
        print(message)
        text = "По всем вопросам обращайтесь к @uxuxd"
        a = await message.answer(text)
        admins = read(f"SELECT * FROM shops WHERE nick_name='{a['from']['username']}';")
        print(admins)

    @dp.callback_query_handler(lambda call: call.data.startswith('further'))
    async def update_further(call):
        d = call.data
        id = int(d.split('_')[1])
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(callback_data=f'fromfurther_{id}', text='Назад'))
        kb.add(types.InlineKeyboardButton(callback_data=f'totrash_{id}', text='В корзину'))
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=kb
        )

    @dp.callback_query_handler(lambda call: call.data.startswith('fromfurther'))
    async def update_from_futher(call):
        d = call.data
        id = int(d.split('_')[1])
        kb = types.InlineKeyboardMarkup()
        kb.add(types.InlineKeyboardButton(callback_data=f'further_{id}', text='Подробнее'))
        kb.add(types.InlineKeyboardButton(callback_data=f'totrash_{id}', text='В корзину'))
        await bot.edit_message_caption(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            reply_markup=kb
        )

    @dp.message_handler()
    async def echo_message(msg: types.Message):
        print('fisc')
        await bot.send_message(msg.from_user.id, msg.text)

    executor.start_polling(dp)
