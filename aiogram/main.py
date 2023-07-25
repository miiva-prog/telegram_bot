from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,InputFile
import random
import configuration

bot = Bot(configuration.TOKEN_BOT)
disp = Dispatcher(bot)

command_help = """
<b>/start</b>
<b>/help</b>
<b>/description</b>
<b>/count</b>
<b>/sticker</b>
<b>/heart</b>
<b>/hedgehog</b>
<b>/map</b>
<b>/social_network</b>
<b>/mood</b>
<b>/dogs</b>
<b>/voting</b>
"""

description = """My bot is weak
it needs to be upgraded"""

count_call = 0

keyboard = ReplyKeyboardMarkup(one_time_keyboard=True)# type: ignore
keyboard.add(KeyboardButton('/start'))# type: ignore
keyboard.add(KeyboardButton('/help'))# type: ignore
keyboard.add(KeyboardButton('/description'))# type: ignore
keyboard.add(KeyboardButton('/count'))# type: ignore
keyboard.add(KeyboardButton('/sticker'))# type: ignore
keyboard.add(KeyboardButton('/heart'))# type: ignore
keyboard.add(KeyboardButton('/hedgehog'))# type: ignore
keyboard.add(KeyboardButton("/map"))# type: ignore
keyboard.add(KeyboardButton("/social_network"))#type: ignore
keyboard.add(KeyboardButton("/mood"))#type: ignore
keyboard.add(KeyboardButton("/dogs"))#type: ignore
keyboard.add(KeyboardButton("🥰"))#type: ignore
keyboard.add(KeyboardButton("/voting"))#type: ignore

keyboard_2 = ReplyKeyboardMarkup(one_time_keyboard=True)#type: ignore
keyboard_2.add(KeyboardButton("/spitz"))#type: ignore
keyboard_2.add(KeyboardButton("/pug"))#type: ignore
keyboard_2.add(KeyboardButton("/french_bulldog"))#type: ignore
keyboard_2.add(KeyboardButton("/chihuahua"))#type: ignore
keyboard_2.add(KeyboardButton("/corgi"))#type: ignore
keyboard_2.add(KeyboardButton("/labrador"))#type: ignore

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


@disp.message_handler()
async def message_capitalize(message:types.Message):
    await message.answer(text=message.text.capitalize())


@disp.message_handler()
async def message_upper(message:types.Message):
    await message.answer(text=message.text.upper())


@disp.message_handler()
async def answer_two_words(message:types.Message):
    if message.text.count(' ') == 1:
        await message.answer(text=message.text)


@disp.message_handler()
async def replace_heart(message:types.Message):
    if message.text == "❤️":
        await message.answer(text="💔")


@disp.message_handler()
async def message_chat(message:types.Message):
    await bot.send_message(chat_id=message.from_user.id,text="Good!") 


@disp.message_handler()
async def bold_font(message:types.Message):
    await message.answer(text="<b>Font bold</b>",parse_mode="HTML")


@disp.message_handler()
async def yes_or_no(message:types.Message):
    if '0' in message.text:
        await bot.send_message(chat_id=message.chat.id,text='YES')
    else:
        await bot.send_message(chat_id=message.chat.id,text='NO')

     
@disp.message_handler()
async def italics_font(message:types.Message):
    await message.answer(text="<em>Font italics</em>",parse_mode="HTML")
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


@disp.message_handler(commands=['sticker'])
async def sticker_bot(messange:types.Message):
    await bot.send_sticker(messange.from_user.id,sticker=configuration.HASBULLA)
    await messange.delete()


@disp.message_handler(commands=['heart'])
async def heart_bot(message:types.Message):
    await message.reply(text="❤️")
    await message.delete()


@disp.message_handler(commands=['hedgehog'])
async def hedgehog_bot(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_HEDGEHOG))
    await message.delete()


@disp.message_handler(commands=['map'])
async def map_bot(message:types.Message):
    await bot.send_location(chat_id=message.chat.id,latitude=random.randint(1,100),longitude=random.randint(1,100))
    await message.delete()


@disp.message_handler(commands=['social_network'])
async def social_network_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text="My social network",reply_markup=inline)
    await message.delete()


@disp.message_handler(commands=['mood'])
async def mood_bot(message:types.Message):
    inline_2 = InlineKeyboardMarkup()
    inline_2_button1 = InlineKeyboardButton(text="Good",callback_data="like")# type: ignore
    inline_2_button2 = InlineKeyboardButton(text="Bad",callback_data="dislike")# type: ignore
    inline_2.add(inline_2_button1,inline_2_button2)

    await bot.send_message(chat_id=message.chat.id,text="how is your mood?",reply_markup=inline_2)
    await message.delete()


@disp.callback_query_handler()
async def callback_mood(callback:types.CallbackQuery):
    if callback.data == "like":
        await callback.answer(text="Nice!")
    else:
        await callback.answer(text="Everything will be alright!")


@disp.message_handler(commands=['dogs'])
async def dogs_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text="choose a breed",reply_markup=keyboard_2)
    await message.delete()


@disp.message_handler(commands=['spitz'])
async def spitz_bot(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_SPITZ))
    await message.delete() 


@disp.message_handler(commands=['pug'])
async def pug_bot(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_PUG))
    await message.delete() 


@disp.message_handler(commands=['french_bulldog'])
async def french_bulldog_bot(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_FRENCH_BULLDOG))
    await message.delete()


@disp.message_handler(commands=['chihuahua'])
async def chihuahua_bot(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_CHIHUAHUA))
    await message.delete()


@disp.message_handler(commands=['corgi'])
async def corgi_bot(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_CORGI))
    await message.delete()


@disp.message_handler(commands=['labrador'])
async def labrador_bot(message:types.Message):
    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_LABRADOR))
    await message.delete()


@disp.message_handler(commands=['voting'])
async def voting_bot(message:types.Message):
    inline3 = InlineKeyboardMarkup()
    inline3_button1 = InlineKeyboardButton("👍",callback_data="Like")#type: ignore
    inline3_button2 = InlineKeyboardButton("👎",callback_data="Dislike")#type: ignore
    inline3_button3 = InlineKeyboardButton("Close",callback_data="close")#type: ignore
    inline3.add(inline3_button1,inline3_button2,inline3_button3)

    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_ARTIST),caption="say your voice",reply_markup=inline3)


@disp.callback_query_handler()
async def callback_voting(callback:types.CallbackQuery):
    if callback.data == "close":    
        await callback.message.delete()

    if callback.data == "Like" or callback.data == "Dislike": 
        await callback.answer(text=callback.data,show_alert=True)

 
@disp.message_handler()
async def love(message:types.Message):
    if message.text == '🥰':
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.VIKA)


if __name__ == "__main__":
    executor.start_polling(disp,skip_updates=True,on_startup=on_startup)