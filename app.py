import asyncio
import logging
import config
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.TOKEN)
dp = Dispatcher()

async def main():
    from handlers import dp
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
