from aiogram import Bot,Dispatcher,executor,types
from configuration import TOKEN_BOT

bot = Bot(TOKEN_BOT)
disp = Dispatcher(bot)

command_help = """
/start
/help
/description
/count
"""

description = """My bot is weak
it needs to be upgraded"""

count_call = 0

async def on_startup(_):
    print("Good work!")

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


@disp.message_handler(commands=['start'])
async def start_bot(message:types.Message):
    await message.reply(text="Welcome")
    await message.delete()


@disp.message_handler(commands=['help'])
async def help_bot(message:types.Message):
    await message.reply(text=command_help)
    await message.delete()


@disp.message_handler(commands=['description'])
async def description_bot(message:types.Message):
    await message.reply(text=description)
    await message.delete()


@disp.message_handler(commands=['count'])
async def count_bot(message:types.Message):
    global count_call
    await message.reply(f'count -> {count_call}')
    await message.delete()
    count_call += 1


@disp.message_handler()
async def yes_or_no(message:types.Message):
    if '0' in message.text:
        await message.answer(text='YES')
    else:
        await message.answer(text='NO')


@disp.message_handler(commands=['emodji'])
async def get_emodji(messange:types.Message):
    await bot.send_sticker(messange.from_user.id,sticker="CAACAgIAAxkBAAEJpkBkq8giWz8XLjeyvYN1sgABvoKhrewAAh4VAAKl0-lLUnW8uJFVS0IvBA")


@disp.message_handler()
async def bold_font(message:types.Message):
    await message.answer("<b>Font bold</b>",parse_mode="HTML")


@disp.message_handler()
async def italics_font(message:types.Message):
    await message.answer("<em>Font italics</em>",parse_mode="HTML")

if __name__ == "__main__":
    executor.start_polling(disp)