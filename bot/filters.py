from aiogram.filters import BaseFilter
from aiogram import types


class IsExist(BaseFilter):
    def __init__(self, data_list: list):
        self._list = data_list

    async def __call__(self, message: types.Message):
        msg = message.text.lower()
        return msg in self._list

