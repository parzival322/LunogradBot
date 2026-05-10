from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  
from aiogram.utils.keyboard import ReplyKeyboardBuilder
#from aiogram.filters.callback_data import CallbackData
import asyncio
 

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подать заявку 📄')
        ],
        [
            KeyboardButton(text='Получить форму 👨‍✈️')
        ],
        [
            KeyboardButton(text='Обратиться к Мэру Города 💬')
        ]],
        resize_keyboard=True
)

return_to_menu = KeyboardButton(text='Назад в меню')

