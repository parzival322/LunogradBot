import asyncio
import logging

from aiogram import Bot, Dispatcher

import os
from dotenv import load_dotenv

from app.handlers import router
#from app.database.models import async_main

load_dotenv()

dp = Dispatcher()


async def main():
    #await async_main()
    bot = Bot(token=os.environ.get('TOKEN'))
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__=='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except Exception as e:
        print(e)
        print('Бот был приостановлен вручную')