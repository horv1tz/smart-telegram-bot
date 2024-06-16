from app import dp
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from gtts import gTTS
from utils import handle_data
import os
import re

@dp.message()
async def start(message: Message, state: FSMContext):
    # Отправляем сообщение и сохраняем его идентификатор
    waiting_message = await message.answer("Пожалуйста подождите...")

    # Проверка наличия ключевых слов для фото запроса
    photo_prompt = ['фото', 'нарисуй']
    if any(word in message.text.lower().split() for word in photo_prompt):
        await message.answer('Я пока что так не умею')
    else:
        # Обработка запроса с помощью GigaChat
        response_ai = handle_data(query=message.text)

        # Создание аудиофайла с озвучкой ответа
        tts = gTTS(re.sub(r'[=#\|\-*`]+', '', response_ai), lang='ru')
        audio_file_path = f'response_{message.message_id}.mp3'
        tts.save(audio_file_path)

        # Отправка ответа с поддержкой Markdown
        await message.answer(response_ai, parse_mode=ParseMode.MARKDOWN)

        # Отправка аудиофайла
        audio = FSInputFile(audio_file_path)
        await message.answer_voice(audio)

        # Удаление временного аудиофайла
        os.remove(audio_file_path)

    # Удаление сообщения "Пожалуйста подождите..."
    await waiting_message.delete()
