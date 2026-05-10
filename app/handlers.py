from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter
from aiogram.types import Message, CallbackQuery, ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import os
from dotenv import load_dotenv

load_dotenv()

router = Router()

import app.keyboards as kb


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Привет! Слава Лунограду!! Выбери, что тебе надо путник: ', reply_markup=kb.main_menu)


@router.message(F.text == 'Назад в меню')
async def cmd_mainmenu(message: Message):
    await message.answer('Главное меню:', 
                         reply_markup=kb.main_menu)


#================ПУНКТЫ ГЛАВНОГО МЕНЮ================
@router.message(F.text == 'Подать заявку 📄')
async def cmd_applyToCity(message: Message):
    await message.answer(text='Попасть в город Коля Жепа 1', 
                         reply_markup=kb.return_to_menu)
    
@router.message(F.text == 'Получить форму 👨‍✈️')
async def cmd_getSuit(message: Message):
    await message.answer(text='Форма Коля Жепа 2', 
                         reply_markup=kb.return_to_menu)
    
@router.message(F.text == 'Обратиться к Мэру Города 💬')
async def cmd_appealtoMayor(message: Message):
    await message.answer(text='Мил Государь теперь Коля Жепа 3', 
                         reply_markup=kb.return_to_menu)