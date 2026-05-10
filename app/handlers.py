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


@router.message(F.data == 'main_menu')
async def cmd_mainmenu(message: Message):
    await message.answer('Главное меню:', 
                         reply_markup=kb.main_menu)


#================ПУНКТЫ ГЛАВНОГО МЕНЮ================
@router.message(F.data=='applyToCity')
async def cmd_applyToCity(message: Message):
    await message.answer(text='Коля Жепа 1', 
                         reply_markup=kb.return_to_menu)
    
@router.message(F.data=='getSuit')
async def cmd_applyToCity(message: Message):
    await message.answer(text='Коля Жепа 2', 
                         reply_markup=kb.return_to_menu)

@router.message(F.data=='appealtoMayor')
async def cmd_applyToCity(message: Message):
    await message.answer(text='Коля Жепа 3', 
                         reply_markup=kb.return_to_menu)