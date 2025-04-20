import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import Dispatcher
from aiogram import F
from aiogram.utils.token import Token
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.client.bot import DefaultBotProperties
from dotenv import load_dotenv
import asyncio

load_dotenv()
API_TOKEN = os.getenv("TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create bot and dispatcher
bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

# Register handlers
@dp.message(Command(commands=["start", "help"]))
async def command_start_handler(message: Message):
    await message.answer("Hi\nI am Luci Bot!\nPowered by DeepSeek.")

@dp.message(F.text)
async def echo_handler(message: Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
