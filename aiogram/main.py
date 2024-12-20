from aiogram import Bot,Dispatcher,executor,types
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton,InputFile
import random
import configuration
import key_board

bot = Bot(configuration.TOKEN_BOT)
disp = Dispatcher(bot)

count_call = 0
change_number = 0
random_value = 0

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
    await bot.send_message(chat_id=message.chat.id,text="Welcome",reply_markup=key_board.create_keybord())
    await message.delete()


@disp.message_handler(commands=['help'])
async def help_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text=configuration.COMMAND_HELP,parse_mode="HTML")
    await message.delete()


@disp.message_handler(commands=['description'])
async def description_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text=configuration.DESCRIPTION)
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
    await bot.send_message(chat_id=message.chat.id,text="My social network",reply_markup=key_board.create_inline())
    await message.delete()


@disp.message_handler(commands=['mood'])
async def mood_bot(message:types.Message):
    inline_2 = InlineKeyboardMarkup()
    inline_2_button1 = InlineKeyboardButton(text="Good",callback_data="good")# type: ignore
    inline_2_button2 = InlineKeyboardButton(text="Bad",callback_data="bad")# type: ignore
    inline_2.add(inline_2_button1,inline_2_button2)

    await bot.send_message(chat_id=message.chat.id,text="how is your mood?",reply_markup=inline_2)
    await message.delete()


@disp.callback_query_handler()
async def callback_mood(callback:types.CallbackQuery):
    if callback.data == "good":
        await callback.answer(text="Nice!")
    if callback.data == "bad":
        await callback.answer(text="Everything will be alright!")


@disp.message_handler(commands=['dogs'])
async def dogs_bot(message:types.Message):
    await bot.send_message(chat_id=message.chat.id,text="choose a breed",reply_markup=key_board.create_keyboard_2())
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
    inline3_button1 = InlineKeyboardButton("👍",callback_data="like")#type: ignore
    inline3_button2 = InlineKeyboardButton("👎",callback_data="dislike")#type: ignore
    inline3_button3 = InlineKeyboardButton("Close",callback_data="close")#type: ignore
    inline3.add(inline3_button1,inline3_button2,inline3_button3)

    await bot.send_photo(chat_id=message.chat.id,photo=random.choice(configuration.ARR_ARTIST),caption="Do you like?",reply_markup=inline3)


@disp.callback_query_handler()
async def callback_voting(callback:types.CallbackQuery):
    if callback.data == "close":    
        await callback.message.delete()

    if callback.data == "like" or callback.data == "dislike": 
        await callback.answer(show_alert=True,text=callback.data)


@disp.message_handler(commands=['change_number'])
async def change_number_bot(message:types.Message):
    global change_number
    await bot.send_message(chat_id=message.chat.id,text=f"You can change it's -> {change_number}",reply_markup=key_board.create_inline_change_bot())
    await message.delete()


@disp.callback_query_handler()
async def callback_change_number(callback:types.CallbackQuery):
    global change_number
    if callback.data == '+':
        change_number += 1
        await callback.message.edit_text(text=f"You can change it's -> {change_number}",reply_markup=key_board.create_inline_change_bot())

    if callback.data == '-':
        change_number -= 1
        await callback.message.edit_text(text=f"You can change it's -> {change_number}",reply_markup=key_board.create_inline_change_bot())

    if callback.data == "rand":
        change_number = random.randint(1,1000)
        await callback.message.edit_text(text=f"You can change it's -> {change_number}",reply_markup=key_board.create_inline_change_bot())

    if callback.data == '0':
        change_number = 0
        await callback.message.edit_text(text=f"You can change it's -> {change_number}",reply_markup=key_board.create_inline_change_bot())


@disp.message_handler(commands=['question'])
async def test_bot(message:types.Message):
    global random_value

    random_value = random.randint(1,17)

    if random_value == 1:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION1,reply_markup=key_board.create_inline_one_question())

    if random_value == 2:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION2,reply_markup=key_board.create_inline_two_question())  

    if random_value == 3:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION3,reply_markup=key_board.create_inline_three_question()) 

    if random_value == 4:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION4,reply_markup=key_board.create_inline_four_question())

    if random_value == 5:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION5,reply_markup=key_board.create_inline_five_question())
    
    if random_value == 6:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION6,reply_markup=key_board.create_inline_six_question())
    
    if random_value == 7:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.MENDELEEV,caption=configuration.QUESTION7,reply_markup=key_board.create_inline_seven_question())

    if random_value == 8:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION8,reply_markup=key_board.create_inline_eight_question())

    if random_value == 9:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION9,reply_markup=key_board.create_inline_nine_question())

    if random_value == 10:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION10,reply_markup=key_board.create_inline_ten_question())

    if random_value == 11:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.PASTERNAK,caption=configuration.QUESTION7,reply_markup=key_board.create_inline_eleven_question())

    if random_value == 12:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION11,reply_markup=key_board.create_inline_twelve_question())

    if random_value == 13:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION12,reply_markup=key_board.create_inline_thirteen_question())

    if random_value == 14:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.PIZANSKAIA,caption=configuration.QUESTION7,reply_markup=key_board.create_inline_fourteen_question())

    if random_value == 15:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION13,reply_markup=key_board.create_inline_fiveteen_question())

    if random_value == 16:
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.EQUATION,caption=configuration.QUESTION14,reply_markup=key_board.create_inline_sixteen_question())

    if random_value == 17:
        await bot.send_message(chat_id=message.chat.id,text=configuration.QUESTION15,reply_markup=key_board.create_inline_seventeen_question())

    await message.delete()


@disp.callback_query_handler()
async def callback_test(callback:types.CallbackQuery):
    global random_value

    if random_value == 1:
        if callback.data == "Тургенев":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 2:
        if callback.data == "иваново!":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 3:
        if callback.data == "исландия!":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 4:
        if callback.data == "(1799)":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 5:
        if callback.data == "правыйжелудочек":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 6:
        if callback.data == "алюминий!":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 7:
        if callback.data == "Менделеев":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 8:
        if callback.data == "эпитет!":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 9:
        if callback.data == "(1861)":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 10:
        if callback.data == "(116)":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 11:
        if callback.data == "пастернак":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 12:
        if callback.data == "растительнаяклетка":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 13:
        if callback.data == "южамерика":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 14:
        if callback.data == "пизанскаябашня":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 15:
        if callback.data == "(371)":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 16:
        if callback.data == "(x1=2/3x2=-3)":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")

    if random_value == 17:
        if callback.data == "светильник":
            await callback.answer(text="Prioperly")
        else:
            await callback.answer(text="Wrong")


@disp.message_handler()
async def love(message:types.Message):
    if message.text == '🥰':
        await bot.send_photo(chat_id=message.chat.id,photo=configuration.VIKA)

        
if __name__ == "__main__":
    executor.start_polling(disp,skip_updates=True,on_startup=on_startup)