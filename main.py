from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import  CallbackQuery
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

    ikb = AnswerInlineKeyboard(5, 57, subj)
    ikb.make_buttons()

    await message.answer(
    text=text,
    reply_markup=ikb,
    )

    paragraphs = [f'{id}. {text}' for id, text in questions]

    for paragraph in paragraphs:
        await bot.send_message(chat_id=message.from_user.id, text=paragraph)

@dp.callback_query_handler(answer_data.filter())
async def answer(callback: CallbackQuery, callback_data: dict):
    await callback.answer(text=callback_data['subject'])

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )