from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import configuration

def create_keybord() -> ReplyKeyboardMarkup:# type: ignore
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
    keyboard.add(KeyboardButton("/change_number"))#type: ignore

    return keyboard

def create_keyboard_2() -> ReplyKeyboardMarkup:#type: ignore
    keyboard_2 = ReplyKeyboardMarkup(one_time_keyboard=True)#type: ignore
    keyboard_2.add(KeyboardButton("/spitz"))#type: ignore
    keyboard_2.add(KeyboardButton("/pug"))#type: ignore
    keyboard_2.add(KeyboardButton("/french_bulldog"))#type: ignore
    keyboard_2.add(KeyboardButton("/chihuahua"))#type: ignore
    keyboard_2.add(KeyboardButton("/corgi"))#type: ignore
    keyboard_2.add(KeyboardButton("/labrador"))#type: ignore

    return keyboard_2

def create_inline() -> InlineKeyboardMarkup:# type: ignore
    inline = InlineKeyboardMarkup()
    inline_button1 = InlineKeyboardButton("VK",configuration.VK)# type: ignore
    inline_button2 = InlineKeyboardButton("Instagram",configuration.INSTAGRAM)# type: ignore
    inline.add(inline_button1,inline_button2)

    return inline

def create_inline_change_bot() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("boost",callback_data="+")#type: ignore
    inline2_button2 = InlineKeyboardButton("lessen",callback_data="-")#type: ignore
    inline2.add(inline2_button1,inline2_button2)

    return inline2