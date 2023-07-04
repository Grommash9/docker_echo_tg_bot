import logging
import aiogram.types
from aiogram import Bot, Dispatcher, executor, types
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

API_TOKEN = os.environ.get('BOT_TOKEN')

if API_TOKEN is not None:
    print("BOT_TOKEN:", API_TOKEN)
else:
    print("BOT_TOKEN not found!")

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(content_types=aiogram.types.ContentType.ANY)
async def echo(message: types.Message):
    await message.copy_to(message.from_user.id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
