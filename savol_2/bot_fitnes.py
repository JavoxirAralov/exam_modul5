import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from   replay import  *




TOKEN = "6984228503:AAEFL2SlEG6GVSVOJ8DkxpZIVRJMccKX_z4"
dp = Dispatcher()



@dp.message(CommandStart() )
async def start_handler(message: Message) -> None:
    await message.answer(f"Asalomu alekum bu botimiz sizga kunlik qilinadigan 🏋️ mashiqlarni korsatib beradi ", reply_markup= minu_button())


@dp.message(lambda msg: msg.text == 'Start✅')
async def campaign_button(msg: Message):
    await msg.answer(f"Quydagilardan birontasini tanlang 👇🏿",reply_markup=start_button())


@dp.message(lambda msg: msg.text == 'Filial📍')
async def campaign_button(msg: Message):
    await msg.answer(f"Yaqin ordada filial yoq sport bilan shugulanma uka ")



@dp.message(lambda msg: msg.text == "Woman👱‍♀")
async def campaign_button(msg: Message):
    await msg.answer(f"Quydagilardan birontasini tanlang 👇🏿",reply_markup =woman_botton())


@dp.message(lambda msg: msg.text == "Man👨‍🦰")
async def campaign_button(msg: Message):
    await msg.answer(f"Quydagilardan birontasini tanlang 👇🏿",reply_markup =man_botton())


@dp.message(lambda msg: msg.text == "Admin👨🏻‍💻")
async def campaign_button(msg: Message):
    await msg.answer(f"Admin  @javoxir_aralov ",reply_markup = admin_botton())

async def main() -> None:
    bot = Bot(TOKEN ,parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())