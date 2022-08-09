from multiprocessing import Value
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
from datetime import datetime
from user import User

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(msg: types.Message):
    User(msg.from_user)
    
@dp.message_handler(commands=['setdata'])
async def set_data(msg: types.Message):
    args = msg.get_args().split()
    User(msg.from_user).SetColumn(str(args[0]), args[1])
    await msg.reply(f"Изменено {args[0]} = {args[1]}")

@dp.message_handler(commands=['getdata'])
async def get_data(msg: types.Message):
    column = msg.get_args().split()
    await msg.reply(f"Информация {column[0]} = {str(User(msg.from_user).GetColumn(str(column[0])))}" )

if __name__ == '__main__':
    print(f"Bot started at {datetime.now}")
    executor.start_polling(dp)