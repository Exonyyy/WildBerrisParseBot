import asyncio

from aiogram import Dispatcher, Bot

from settings import BOT_TOKEN
from handlers import router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)


async def main():
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    asyncio.run(main())
