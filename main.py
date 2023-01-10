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

    functional = SubjectsReplyKeyboard(config.subjects, resize_keyboard=True,one_time_keyboard=False)
    functional.make_buttons()

    await message.answer(text='Привет, выбирай предмет!', reply_markup=functional)


@dp.message_handler(lambda message: message.text in config.subjects)
async def choose_answer(message: types.Message):

    subj = message.text
    questions = info.get_questions(subj)

    text = f'Какой вопрос по {config.declination[subj]} интересует?\n'

    await message.answer(text = text)
    
    #paragraphs = [f'{id}. {text}' for id, text in questions]

    for paragraph in questions:
        question_id, question_text = paragraph
        button = InlineKeyboardButton(text="Получить ответ", callback_data=answer_data.new(
            subject=subj,
            id=question_id,
            chat_id=message.from_user.id
        ))
        ikb = InlineKeyboardMarkup(row_width=1).add(button)
        await bot.send_message(
            chat_id=message.from_user.id, 
            text=f'{question_id}. {question_text}',
            reply_markup=ikb)

@dp.callback_query_handler(answer_data.filter())
async def answer(callback: CallbackQuery, callback_data: dict):
    answer = info.get_answer(subject=callback_data['subject'], id=callback_data['id'])[0]
    await bot.send_message(chat_id=callback_data['chat_id'],text=f'Вопрос №{callback_data["id"]}.\n{answer}')

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )