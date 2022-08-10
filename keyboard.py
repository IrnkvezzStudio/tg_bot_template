from ctypes import resize
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
    
def GenerateTestKeyboard():
    ret = ReplyKeyboardMarkup(resize_keyboard=True)
    ret.add(KeyboardButton(text="Тестовая кнопка"))
    ret.row(
        KeyboardButton(text="Кнопка 1"),
        KeyboardButton(text="Кнопка 2")
    )
    ret.insert(
        KeyboardButton(text="Отправить контакт", request_contact=True)
        
    ).insert(
        KeyboardButton(text="Отправить локацию", request_location=True)
    )
    return ret

def GenerateTextInlineKeyboard():
    ret = InlineKeyboardMarkup(resize_keyboard=True)
    ret.add(InlineKeyboardButton(text="Тестовая кнопка", callback_data='testbtn'))
    ret.row(
        InlineKeyboardButton(text="Кнопка 1",callback_data='testbtn'),
        InlineKeyboardButton(text="Кнопка 2",callback_data='testbtn')
    )
    ret.insert(
        KeyboardButton(text="Отправить контакт", request_contact=True,callback_data='testbtn')
        
    ).insert(
        KeyboardButton(text="Отправить локацию", request_location=True,callback_data='testbtn')
    )
    return ret

#add u keyboards here