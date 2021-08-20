from aiogram.dispatcher.filters.state import StatesGroup, State


class TwoStates(StatesGroup):
    MY_SHOPS = State()
    ADD_SHOP = State()