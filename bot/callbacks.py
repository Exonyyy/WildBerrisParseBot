from aiogram.filters.callback_data import CallbackData


class UserPage(CallbackData, prefix='pages'):
    event: str
    page: int
