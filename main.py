from aiogram import Bot, Dispatcher, executor, types
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
    await message.answer(text="Привет! Я бот помощник по учебному процессу.")
    await message.answer(text='Чтобы увидеть список моих комманд пиши "/help"')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(text=message.text)

if __name__ == '__main__':
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
