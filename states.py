from aiogram.dispatcher.filters.state import StatesGroup, State


class ThreeStates(StatesGroup):
    MY_SHOPES = State()
    ADD_SHOP = State()