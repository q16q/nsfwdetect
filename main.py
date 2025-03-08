from nsfw_detector import predict
from dotenv import load_dotenv

load_dotenv()


MODEL_PATH = "./mobilenet_v2_140_224/saved_model.h5"

print('using', MODEL_PATH)
model = predict.load_model(MODEL_PATH)

import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import os

TOKEN = getenv("TOKEN")

dp = Dispatcher()

@dp.message()
async def handle_message(message: Message):
    if message.photo:
        file = await message.bot.get_file(message.photo[-1].file_id)
        file_path = file.file_path
        save_fp = 'p%s.png' % file.file_id
        await message.bot.download_file(file_path, destination = save_fp)
        
        # analyzing
        result = predict.classify(model, save_fp)[save_fp]

        print(result)

        CRITERIA = 0.34
        if result['hentai'] >= CRITERIA or result['porn'] >= CRITERIA or result['sexy'] >= CRITERIA:
            flagged = max(result, key = result.get)

            await message.answer_photo(file.file_id, caption = 'content type: %s\nfrom %s\n%s' % (flagged, message.from_user.username or message.from_user.full_name, message.caption or '(no caption)'), has_spoiler = True)
            await message.delete()
        
        os.remove(save_fp)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    print('running bot')
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())