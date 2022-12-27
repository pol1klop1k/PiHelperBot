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

    functional = SubjectsReplyKeyboard(config.subjects, resize_keyboard=True,one_time_keyboard=False)
    functional.make_buttons()

    await message.answer(text='Вот список моих некоторых комманд', reply_markup=functional)


@dp.message_handler(lambda message: message.text in config.subjects)
async def choose_answer(message: types.Message):

    obj = message.text
    text = f'Какой вопрос по {config.declination[obj]} интересует?'


    ikb = AnswerInlineKeyboard(5, 57)
    ikb.make_buttons()

    await message.answer(
    text=text,
    reply_markup=ikb,
    )

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