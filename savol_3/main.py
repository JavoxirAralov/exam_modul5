import asyncio
import logging
import sys
from aiogram.filters.command import CommandStart
import psycopg2
from aiogram import Bot, Dispatcher, types

from sqlalchemy import create_engine, BIGINT, CheckConstraint, TIMESTAMP, ForeignKey, VARCHAR, text
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy.sql.functions import current_timestamp

engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/modul_5lesson_6")

Base = declarative_base()

BOT_TOKEN = "6984228503:AAEFL2SlEG6GVSVOJ8DkxpZIVRJMccKX_z4"
dp = Dispatcher()


con = psycopg2.connect(
    dbname="postgres",
    user='postgres',
    password='1',
    host="localhost",
    port=5432
)

cur = con.cursor()
con.commit()
class bot_info(Base):
    __tablename__ = 'bot_info'
    id: Mapped[int] = mapped_column(__type_pos=BIGINT, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column()
    user_name: Mapped[str] = mapped_column()
    first_name : Mapped[str] = mapped_column()
    last_name : Mapped[str] = mapped_column()


Base.metadata.create_all(engine)



def save_to_database(user_id, user_name, first_name, last_name):
    select_query = "SELECT * FROM bot_info WHERE user_id = %s"
    cur.execute(select_query, (user_id,))
    existing_user = cur.fetchone()

    if existing_user:
        print("User already exists in the database.")
    else:
        insert_query = """
            INSERT INTO user_info (user_id, user_name, first_name, last_name)
            VALUES (%s, %s, %s, %s)
        """
        params = (user_id, user_name, first_name, last_name)

        cur.execute(insert_query, params)
        con.commit()
        print("User information saved to the database.")




@dp.message(CommandStart())
async def start_handler(msg: types.Message):
    user_id = msg.from_user.id
    user_name = msg.from_user.username
    first_name = msg.from_user.first_name
    last_name = msg.from_user.last_name

    await msg.answer(f"{user_name }   Your info was saved in database ",
                     reply_markup=save_to_database(user_id, user_name, first_name, last_name))


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())




