from app import dp
from aiogram import types
from aiogram.filters.command import Command

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот который поможет ответить на твои вопросы")
