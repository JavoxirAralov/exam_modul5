from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
def minu_button():
    n1 = KeyboardButton(text='Filial📍')
    n2 = KeyboardButton(text='Start✅')
    n3 = KeyboardButton(text='Admin👨🏻‍💻')
    n4 = KeyboardButton(text='News🗞')
    design = [
        [n1, n2],
        [n3,n4]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm

def start_button():
    n1 = KeyboardButton(text='Woman👱‍♀')
    n2 = KeyboardButton(text='Man👨‍🦰')
    n3 = KeyboardButton(text='Back🔙')
    design = [
        [n1, n2],
          [n3]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm



def  woman_botton ():
    n1 = KeyboardButton(text='1- oy ')
    n2 = KeyboardButton(text='2- oy ')
    n3 = KeyboardButton(text='3- oy ')
    n4 = KeyboardButton(text='4- oy ')
    n5 = KeyboardButton(text='Back🔙')
    design = [
        [n1, n2],
        [n3,n4],
          [n5]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def  man_botton ():
    n1 = KeyboardButton(text='1- oy ')
    n2 = KeyboardButton(text='2- oy ')
    n3 = KeyboardButton(text='3- oy ')
    n4 = KeyboardButton(text='4- oy ')
    n5 = KeyboardButton(text='Back🔙')
    design = [
        [n1, n2],
        [n3,n4],
          [n5]
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm


def admin_botton():

    n1 = KeyboardButton(text='Send a message @javoxir_aralov')
    n2 = KeyboardButton(text='Back🔙')
    design = [
        [n1],
        [n2],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm

def news_botton():
    n2 = KeyboardButton(text='Back🔙')
    design = [
        [n2],
    ]
    rkm = ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)
    return rkm


