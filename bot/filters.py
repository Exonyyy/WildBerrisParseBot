from aiogram.filters import BaseFilter
from aiogram import types


class IsExist(BaseFilter):
    def __init__(self, data_list: list):
        self._list = data_list

    async def __call__(self, message: types.Message):
        msg = message.text
        return msg in self._list


class IsProduct(BaseFilter):
    def __init__(self, data_dict: dict):
        self._data_dict = data_dict

    async def __call__(self, message: types.Message):
        msg = message.text
        for category in self._data_dict.keys():
            if msg in self._data_dict[category]:
                return True
        else:
            return False


class ValidValue(BaseFilter):

    async def __call__(self, message: types.Message):
        if message.text.isnumeric():
            msg = int(message.text)
            return all((msg >= 100, msg%100 == 0, msg <= 10000))
        else:
            return False
