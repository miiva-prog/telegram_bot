from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from random import randint
import configuration

bot = Bot(configuration.TOKEN_BOT)
disp = Dispatcher(bot)

command_help = """
<b>/start</b>
<b>/help</b>
<b>/description</b>
<b>/count</b>
<b>/stiker</b>
<b>/heart</b>
<b>/hedgehog</b>
<b>/map</b>
<b>/social_network</b>
"""

description = """My bot is weak
it needs to be upgraded"""

count_call = 0

keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)# type: ignore
keyboard.add(KeyboardButton('/start'))# type: ignore
keyboard.add(KeyboardButton('/help'))# type: ignore
keyboard.add(KeyboardButton('/description'))# type: ignore
keyboard.add(KeyboardButton('/count'))# type: ignore
keyboard.add(KeyboardButton('/stiker'))# type: ignore
keyboard.add(KeyboardButton('/heart'))# type: ignore
keyboard.add(KeyboardButton('/hedgehog'))# type: ignore
keyboard.add(KeyboardButton("/map"))# type: ignore
keyboard.add(KeyboardButton("/social_network"))#type: ignore

inline = InlineKeyboardMarkup()
inline_button1 = InlineKeyboardButton("VK",configuration.VK)# type: ignore
inline_button2 = InlineKeyboardButton("Instagram",configuration.INSTAGRAM)# type: ignore
inline.add(inline_button1,inline_button2)

async def on_startup(_):
    print("Good work!")

"""
@disp.message_handler()
async def echo(message:types.Message):
    await message.answer(text=message.text)
"""
"""
@disp.message_handler()
async def message_capitalize(message:types.Message):
    await message.answer(text=message.text.capitalize())
"""
"""
@disp.message_handler()
async def message_upper(message:types.Message):
    await message.answer(text=message.text.upper())
"""
"""
@disp.message_handler()
async def answer_two_words(message:types.Message):
    if message.text.count(' ') == 1:
        await message.answer(text=message.text)
"""

@disp.message_handler(commands=['start'])
async def start_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text="Welcome",reply_markup=keyboard)
    await message.delete()


@disp.message_handler(commands=['help'])
async def help_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text=command_help,parse_mode="HTML")
    await message.delete()


@disp.message_handler(commands=['description'])
async def description_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text=description)
    await message.delete()


@disp.message_handler(commands=['count'])
async def count_bot(message:types.Message):
    global count_call
    count_call += 1
    await message.answer(f'count -> {count_call}')
    await message.delete()

"""
@disp.message_handler()
async def yes_or_no(message:types.Message):
    if '0' in message.text:
        await message.answer(text='YES')
    else:
        await message.answer(text='NO')
"""

@disp.message_handler(commands=['stiker'])
async def stiker_bot(messange:types.Message):
    await bot.send_sticker(messange.from_user.id,sticker=configuration.HASBULLA)

"""
@disp.message_handler()
async def bold_font(message:types.Message):
    await message.answer(text="<b>Font bold</b>",parse_mode="HTML")
"""
"""
@disp.message_handler()
async def italics_font(message:types.Message):
    await message.answer(text="<em>Font italics</em>",parse_mode="HTML")
"""

@disp.message_handler(commands=['heart'])
async def heart_bot(message:types.Message):
    await message.reply(text="❤️")
    await message.delete()

"""
@disp.message_handler()
async def replace_heart(message:types.Message):
    if message.text == "❤️":
        await message.answer(text="💔")
"""
"""
@disp.message_handler()
async def message_chat(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,text="Good!") 
"""

@disp.message_handler(commands=['hedgehog'])
async def hedgehog_bot(message:types.Message):
    random_value = randint(1,10)
    if random_value == 1:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG1)
    if random_value == 2:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG2)
    if random_value == 3:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG3)
    if random_value == 4:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG4)
    if random_value == 5:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG5)
    if random_value == 6:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG6)
    if random_value == 7:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG7)
    if random_value == 8:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG8)
    if random_value == 9:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG9)
    if random_value == 10:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.HEDGEHOG10)


@disp.message_handler(commands=['map'])
async def map_bot(messange:types.Message):
    await bot.send_location(chat_id=messange.chat.id,latitude=randint(1,100),longitude=randint(1,100))

@disp.message_handler(commands=['social_network'])
async def social_network_bot(messange:types.Message):
    await bot.send_message(chat_id=messange.chat.id,text="My social network",reply_markup=inline)

if __name__ == "__main__":
    executor.start_polling(disp,skip_updates=True)