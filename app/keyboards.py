from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  
from aiogram.utils.keyboard import ReplyKeyboardBuilder
#from aiogram.filters.callback_data import CallbackData
import asyncio
 

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Подать заявку 📄', callback_data="applyToCity")
        ],
        [
            KeyboardButton(text='Получить форму 👨‍✈️', callback_data="getSuit")
        ],
        [
            KeyboardButton(text='Обратиться к Мэру Города 💬', callback_data="appealtoMayor")
        ]],
        resize_keyboard=True
)

return_to_menu = KeyboardButton(text='Назад в меню', callback_data="main_menu")

