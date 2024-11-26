from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
import configuration

bot = Bot(configuration.TOKEN_BOT)
disp = Dispatcher(bot)

async def on_startup(_):
    print("Let's go")

disp.message_handler(commands=['start'])
async def start_bot(message:types.Message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("Hi 🤚",callback_data="hello")#type: ignore
    button2 = InlineKeyboardButton("World 🌍",callback_data="world")#type: ignore
    keyboard.add(button1,button2)
    
    await bot.send_message(chat_id=message.chat.id,text="Welcome to my BOT",reply_markup=keyboard)
    await message.delete()


disp.callback_query_handler()
async def callback_start(callback:types.CallbackQuery):
    if callback.data == "hello":
        await callback.answer(text="Hello")
    
    if callback.data == "world":
        await callback.answer(text="World")


if __name__ == "__main__":
    executor.start_polling(disp,skip_updates=True,on_startup=on_startup)