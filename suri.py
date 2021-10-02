import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "/opt/suricata/token.key"

async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )

async def suri_handler(event: types.Message):
    await event.answer(
        f"Hello, my fellow {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )

async def main():
    with open(TOKEN, 'r') as file:
        BOT_TOKEN = file.read().replace('\n', '')
    bot = Bot(token=BOT_TOKEN)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        disp.register_message_handler(suri_handler, commands={"suri"})
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())
