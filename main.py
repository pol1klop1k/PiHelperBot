from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import config
import os

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

    #functional = ReplyKeyboardMarkup(
    #resize_keyboard=True,
    #)

    functional = ReplyKeyboardMarkup(
    resize_keyboard=True,
    )

    await message.answer(text='Вот список моих некоторых комманд', reply_markup=functional.row(history, informatic))


@dp.message_handler(lambda message: message.text=='История')
async def history(message: types.Message):

    ikb = InlineKeyboardMarkup(row_width=5)
    count = 57
    a = iter(range(1,count+1))
    for i in range(count//5+1):
        butts = []
        for k in a:
            current = str(k)
            butts.append(InlineKeyboardButton(text=current, callback_data=current))
            if k % 5 == 0:
                break
        ikb.row(*butts)


    await message.answer(
    text='Какой вопрос по истории интересует?',
    reply_markup=ikb,
    )


@dp.message_handler(lambda message: message.text=='Информатика')
async def informatic(message: types.Message):

    ikb = InlineKeyboardMarkup(row_width=5)
    count = 77
    a = iter(range(1,count+1))
    for i in range(count//5+1):
        butts = []
        for k in a:
            current = str(k)
            butts.append(InlineKeyboardButton(text=current, callback_data=current))
            if k % 5 == 0:
                break
        ikb.row(*butts)

    await message.answer(
    text='Какой вопрос по информатике интересует?',
    reply_markup=ikb,
    )



if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
