__author__ = 'fairet'

from aiogram import Bot, Dispatcher, executor, types
from json import load
from main import *

def parse(one, two):
    with open ('config', 'r') as read:
        parsed = load(read)

    return parsed[one][two]

bot = Bot(parse('config', 'API_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def on_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text=f"(Автор: {__author__}\nДля доступа подайте заявку внизу.")

@dp.message_handler(content_types=['text'])
async def on_text_message(message: types.Message):
    await bot.send_message(message.from_user.id, text=search(message.text))

async def main():
    executor.start_polling(dp)