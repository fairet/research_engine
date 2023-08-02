from aiogram import Bot, Dispatcher, executor, types
from config import *
from main import *

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def on_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, text="Для доступа подайте завяку внизу.")

@dp.message_handler(content_types=['text'])
async def on_text_message(message: types.Message):
    await bot.send_message(message.from_user.id, text=search(message.text))


def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()