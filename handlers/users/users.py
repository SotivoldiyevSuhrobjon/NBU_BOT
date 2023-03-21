from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import *

from keyboards.inline.users_btn import currency_btn, back_btn
from loader import dp
from database.connections import add_user
from utils.misc.nbu_parser import get_currency

async def bot_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    username = message.from_user.username
    await add_user(user_id, username)
    data = await get_currency()
    await state.update_data(currency=data)
    btn = await currency_btn(data)
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=btn)



async def show_currency_info_callback(call: CallbackQuery, state: FSMContext):
    await call.answer()
    data = await state.get_data()
    code = call.data.split(":")[-1]

    btn = await back_btn()
    context = ""
    for item in data['currency']:
        if item['code'] == code:
            context += f"Nomi: {item['title']}\n" \
                       f"Kurs: {item['cb_price']} so`m\n" \
                       f"Sana: {item['date']}"
    await call.message.edit_text(context, reply_markup=btn)




async def back_btn_callback(call: CallbackQuery, state:FSMContext):
    await call.answer()
    data = await get_currency()
    await state.update_data(currency=data)
    btn = await currency_btn(data)
    await call.message.edit_text(f"Salom, {call.message.from_user.full_name}!", reply_markup=btn)





def register_users_py(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])

    dp.register_callback_query_handler(show_currency_info_callback, text_contains="currency:")
    dp.register_callback_query_handler(back_btn_callback, text_contains="ortga")

