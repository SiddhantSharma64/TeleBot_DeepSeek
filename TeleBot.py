import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from dotenv import load_dotenv
from openai import OpenAI

# Store previous conversation
class Reference:
    def __init__(self):
        self.response = ""

reference = Reference()

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")
API_KEY = os.getenv("DeepSeek_API_KEY")

client = OpenAI(
    api_key=os.getenv("DeepSeek_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Model name
MODEL_NAME = "deepseek/deepseek-chat-v3-0324:free"  

# Init bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("Hi\nI am Luci Bot! Created by Siddhant. How can I assist you?")


@dp.message(Command("clear"))
async def clear_handler(message: Message):
    reference.response = ""
    await message.answer("I've cleared the past conversation and context.")


@dp.message(Command("help"))
async def help_handler(message: Message):
    help_text = """
Hi There, I'm Luci Bot created by Siddhant! Please follow these commands:
    
/start - Start the conversation  
/clear - Clear previous conversation and context  
/help - Show this help menu  

I hope this helps. 🙂
"""
    await message.answer(help_text)


@dp.message()
async def chatgpt_handler(message: Message):
    print(f">>> USER: {message.text}")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "assistant", "content": reference.response},
            {"role": "user", "content": message.text}
        ]
    )
    reply = response.choices[0].message.content
    reference.response = reply
    print(f">>> Luci Bot: {reply}")
    await message.answer(reply)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
