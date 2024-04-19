from aiogram.fsm.state import StatesGroup, State


class ParseProduct(StatesGroup):
    category = State()
    product = State()
    sort = State()
    count = State()