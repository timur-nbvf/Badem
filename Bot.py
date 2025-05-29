from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from fastapi import FastAPI, Request
import uvicorn
import os
import threading
import threading
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, executor
from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from fastapi import FastAPI, Request
import uvicorn

API_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = int(os.environ.get("CHAT_ID"))

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send-order")
async def send_order(request: Request):
    data = await request.json()
    order_list = "\n".join(data.get("order", []))
    text = f"Новый заказ:\n\n{order_list}"
    await bot.send_message(chat_id=CHAT_ID, text=text)
    return {"status": "ok"}

# Команда старт
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("Открыть меню", web_app=WebAppInfo(url="https://timur-nbvf.github.io/Badem-menu/NewIndex.html"))
    )
    await message.answer("Нажми на кнопочку ниже, чтобы заказать еду 🍽", reply_markup=keyboard)

def start_fastapi():
    uvicorn.run("bot:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    threading.Thread(target=start_fastapi).start()
    executor.start_polling(dp, skip_updates=True)