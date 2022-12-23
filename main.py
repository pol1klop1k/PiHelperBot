from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  CallbackQuery
from aiogram.dispatcher.middlewares import BaseMiddleware
import config
import os
from keyboards import *

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

    history = KeyboardButton(
    text='История',
    )

    informatic = KeyboardButton(
    text='Информатика',
    )

    functional = ReplyKeyboardMarkup(
    resize_keyboard=True,
    )

    await message.answer(text='Вот список моих некоторых комманд', reply_markup=functional.row(history, informatic))

#@dp.message_handler(lambda message: message.text in config.objects)
async def answer_or_question(message: types.Message):

    question = InlineKeyboardButton(
    text='Вопросы',
    callback_data=f'Вопросы {message.text}',
    )

    answer = InlineKeyboardButton(
    text='Ответы',
    callback_data=f'Ответы {message.text}',
    )

    aoq = InlineKeyboardMarkup(
    row_width=2
    ).row(question, answer)

    await message.answer(
    text='Вам нужны вопросы или ответы?',
    reply_markup=aoq,
    )

@dp.message_handler(lambda message: message.text in config.objects)
async def choose_answer(message: types.Message):

    obj = message.text
    text = f'Какой вопрос по {config.declination[obj]} интересует?'


    ikb = AnswerKeyboard(57)

    await message.answer(
    text=text,
    reply_markup=ikb.markup,
    )


if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )