from math import ceil

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder, InlineKeyboardButton, KeyboardButton

from callbacks import UserPage
from settings import MAX_BUTTON_ROWS


def inline_keyboard(buttons_count: int, columns: int, buttons_text: list, callbacks: list):
    builder = InlineKeyboardBuilder()
    buttons = list()
    for button in range(buttons_count):
        buttons.append(InlineKeyboardButton(text=buttons_text[button], callback_data=callbacks[button]))
    for row in range(0, buttons_count, buttons_count // columns):
        buttons_row = list()
        for position in range(row, row + buttons_count // columns):
            buttons_row.append(buttons[position])
        builder.row(*buttons_row)
    return builder.as_markup()


def column_reply_keyboard(buttons_count: int, buttons_text: list):
    builder = ReplyKeyboardBuilder()
    buttons = list()
    for button in range(buttons_count):
        buttons.append(KeyboardButton(text=buttons_text[button]))
    for row in range(0, buttons_count, ceil(buttons_count / MAX_BUTTON_ROWS)):
        buttons_row = list()
        for position in range(row, row + ceil(buttons_count / MAX_BUTTON_ROWS)):
            if position < buttons_count:
                buttons_row.append(buttons[position])
        builder.row(*buttons_row)
    return builder.as_markup()


def pagination(pages: int, page: int = 1):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="<<", callback_data=UserPage(event="prev", page=page).pack()),
                InlineKeyboardButton(text=f"Страница: {page}/{pages}", callback_data="page"),
                InlineKeyboardButton(text=">>", callback_data=UserPage(event="next", page=page).pack()))
    builder.row(InlineKeyboardButton(text="Сохранить в таблице", callback_data="save_table"))
    builder.row(InlineKeyboardButton(text="Меню", callback_data="menu"))
    return builder.as_markup()


def one_inline_button(text: str, data: str):
    return InlineKeyboardBuilder().add(InlineKeyboardButton(text=text, callback_data=data)).as_markup()
