from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


#automated "hello" to start the bot
TOKEN = "your token here"
BOT_USERNAME = "@SomeUsernameBot"

reminder_bot = Bot(TOKEN)
dp = Dispatcher(reminder_bot)

button1 = InlineKeyboardButton(text="complete", callback_data="data")
button2 = InlineKeyboardButton(text="incomplete", callback_data="data")
keyboard_inline = InlineKeyboardMarkup().add(button1, button2)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hello, my name is SomeUsernameBot, I send reminders to employees about their tasks!")

executor.start_polling(dp)