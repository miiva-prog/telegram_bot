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
    keyboard.add(KeyboardButton("/question"))#type: ignore

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
    inline2_button3 = InlineKeyboardButton("random",callback_data="rand")#type: ignore
    inline2_button4 = InlineKeyboardButton("clear",callback_data="0")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_one_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("И.А.Гончаров",callback_data="Гончаров")#type: ignore
    inline2_button2 = InlineKeyboardButton("Л.Н.Толстой",callback_data="Толстой")#type: ignore
    inline2_button3 = InlineKeyboardButton("И.С.Тургенев",callback_data="Тургенев")#type: ignore
    inline2_button4 = InlineKeyboardButton("М.Ю.Лермонтов",callback_data="Лермонтов")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_two_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Тула",callback_data="тула!")#type: ignore
    inline2_button2 = InlineKeyboardButton("Иваново",callback_data="иваново!")#type: ignore
    inline2_button3 = InlineKeyboardButton("Казань",callback_data="казань!")#type: ignore
    inline2_button4 = InlineKeyboardButton("Москва",callback_data="москва!")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_three_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Мадагаскар",callback_data="мадагаскар!")#type: ignore
    inline2_button2 = InlineKeyboardButton("Шри-Ланка",callback_data="шри-ланка!")#type: ignore
    inline2_button3 = InlineKeyboardButton("Сахалин",callback_data="сахалин!")#type: ignore
    inline2_button4 = InlineKeyboardButton("Исландия",callback_data="исландия!")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_four_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("1758",callback_data="(1758)")#type: ignore
    inline2_button2 = InlineKeyboardButton("1819",callback_data="(1819)")#type: ignore
    inline2_button3 = InlineKeyboardButton("1799",callback_data="(1799)")#type: ignore
    inline2_button4 = InlineKeyboardButton("1827",callback_data="(1827)")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_five_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Левый желудочек",callback_data="левыйжелудочек")#type: ignore
    inline2_button2 = InlineKeyboardButton("Правый желудочек",callback_data="правыйжелудочек")#type: ignore
    inline2_button3 = InlineKeyboardButton("Левое предсердие",callback_data="левоепредсердие")#type: ignore
    inline2_button4 = InlineKeyboardButton("Правое предсердие",callback_data="правоепредсердие")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_six_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Магний",callback_data="магний!")#type: ignore
    inline2_button2 = InlineKeyboardButton("Алюминий",callback_data="алюминий!")#type: ignore
    inline2_button3 = InlineKeyboardButton("Цинк",callback_data="цинк!")#type: ignore
    inline2_button4 = InlineKeyboardButton("Железо",callback_data="железо!")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_seven_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("М.Ю.Лермонтов",callback_data="Лермонтов")#type: ignore
    inline2_button2 = InlineKeyboardButton("Д.И.Менделеев",callback_data="Менделеев")#type: ignore
    inline2_button3 = InlineKeyboardButton("А.С.Попов",callback_data="Попов")#type: ignore
    inline2_button4 = InlineKeyboardButton("М.С.Горбачев",callback_data="Горбачев")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_eight_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Метафора",callback_data="метафора!")#type: ignore
    inline2_button2 = InlineKeyboardButton("Гипероним",callback_data="гипероним!")#type: ignore
    inline2_button3 = InlineKeyboardButton("Фразиолагизм",callback_data="фразиолагизм!")#type: ignore
    inline2_button4 = InlineKeyboardButton("Эпитет",callback_data="эпитет!")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_nine_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("1754",callback_data="(1754)")#type: ignore
    inline2_button2 = InlineKeyboardButton("1861",callback_data="(1861)")#type: ignore
    inline2_button3 = InlineKeyboardButton("2020",callback_data="(2020)")#type: ignore
    inline2_button4 = InlineKeyboardButton("1798",callback_data="(1798)")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_ten_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("116",callback_data="(116)")#type: ignore
    inline2_button2 = InlineKeyboardButton("100",callback_data="(100)")#type: ignore
    inline2_button3 = InlineKeyboardButton("104",callback_data="(104)")#type: ignore
    inline2_button4 = InlineKeyboardButton("97",callback_data="(97)")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_eleven_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("А.П.Чехов",callback_data="чехов")#type: ignore
    inline2_button2 = InlineKeyboardButton("А.Т.Твардовский",callback_data="твардовский")#type: ignore
    inline2_button3 = InlineKeyboardButton("Б.Л.Пастернак",callback_data="пастернак")#type: ignore
    inline2_button4 = InlineKeyboardButton("Н.А.Некрасов",callback_data="некрасов")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_twelve_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Растительная клетка",callback_data="растительнаяклетка")#type: ignore
    inline2_button2 = InlineKeyboardButton("Животная клетка",callback_data="животнаяклетка")#type: ignore
    inline2.add(inline2_button1,inline2_button2)

    return inline2

def create_inline_thirteen_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Сев Америка",callback_data="севамерика")#type: ignore
    inline2_button2 = InlineKeyboardButton("Юж Америка",callback_data="южамерика")#type: ignore
    inline2_button3 = InlineKeyboardButton("Евразия",callback_data="евразия")#type: ignore
    inline2_button4 = InlineKeyboardButton("Азия",callback_data="азия")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_fourteen_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Пизанская башня",callback_data="пизанскаябашня")#type: ignore
    inline2_button2 = InlineKeyboardButton("Эльфивая башня",callback_data="эльфиваябашня")#type: ignore
    inline2_button3 = InlineKeyboardButton("Башня Кристофера",callback_data="башнякристофера")#type: ignore
    inline2_button4 = InlineKeyboardButton("Замок Люксембурга",callback_data="замоклюксембурга")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_fiveteen_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("368",callback_data="(368)")#type: ignore
    inline2_button2 = InlineKeyboardButton("370",callback_data="(370)")#type: ignore
    inline2_button3 = InlineKeyboardButton("379",callback_data="(379)")#type: ignore
    inline2_button4 = InlineKeyboardButton("371",callback_data="(371)")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_sixteen_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("x1 = 2 x2 = -1",callback_data="(x1=2x2=-1)")#type: ignore
    inline2_button2 = InlineKeyboardButton("x1 = 2/3 x2 = -3",callback_data="(x1=2/3x2=-3)")#type: ignore
    inline2_button3 = InlineKeyboardButton("x1 = -1/2 x2 = 3",callback_data="(x1=-1/2x2=3)")#type: ignore
    inline2_button4 = InlineKeyboardButton("x = 0",callback_data="(x=0)")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2

def create_inline_seventeen_question() -> InlineKeyboardMarkup:#type: ignore
    inline2 = InlineKeyboardMarkup()
    inline2_button1 = InlineKeyboardButton("Крем для рук",callback_data="кремддярук")#type: ignore
    inline2_button2 = InlineKeyboardButton("Головной убор",callback_data="головнойубор")#type: ignore
    inline2_button3 = InlineKeyboardButton("Вид блюда",callback_data="видблюда")#type: ignore
    inline2_button4 = InlineKeyboardButton("Светильник",callback_data="светильник")#type: ignore
    inline2.add(inline2_button1,inline2_button2,inline2_button3)
    inline2.add(inline2_button4)

    return inline2