from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




async def currency_btn(data: list):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{item['title']}", callback_data=f"currency:{item['code']}") for item in data]
    )
    return btn