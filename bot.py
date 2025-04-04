import asyncio
from aiogram import Bot, Dispatcher

from handlers import router

async def main():
    bot = Bot(token='7279615675:AAGu0cVd-c14y7PpuzbpoCCIT1GrT1CBhH0')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except:
        print('Бот СТОП')
