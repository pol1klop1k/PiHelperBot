from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  CallbackQuery
from aiogram.dispatcher.middlewares import BaseMiddleware
import config
import os
from keyboards import *
import info

#env vars
TOKEN = os.getenv('TEST_BOT_TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    pass

async def on_shutdown(dp):
    pass


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply(text=config.COMMANDS)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.delete()
    await message.answer(text="Привет! Я бот помощник по учебному процессу")

    functional = SubjectsReplyKeyboard(config.subjects, resize_keyboard=True,one_time_keyboard=False)
    functional.make_buttons()

    await message.answer(text='Вот список моих некоторых комманд', reply_markup=functional)


@dp.message_handler(lambda message: message.text in config.subjects)
async def choose_answer(message: types.Message):

    subj = message.text
    questions = info.get_questions(subj)

    text = f'Какой вопрос по {config.declination[subj]} интересует?\n'

    await message.answer(text = text)

    ikb = AnswerInlineKeyboard(5, 57, subj)
    ikb.make_buttons()

    #paragraphs = [f'{id}. {text}' for id, text in questions]

    for paragraph in questions:
        question_id, question_text = paragraph
        button = InlineKeyboardButton(text="Получить ответ", callback_data=str(question_id))
        ikb = InlineKeyboardMarkup(row_width=1).add(button)
        await bot.send_message(
            chat_id=message.from_user.id, 
            text=f'{question_id}. {question_text}',
            reply_markup=ikb)

@dp.callback_query_handler()
async def answer(callback: CallbackQuery):
    await callback.answer(text=callback.data)

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )