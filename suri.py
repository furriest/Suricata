import asyncio
import os
from aiogram import Bot, Dispatcher, types

TOKEN = os.path.join(os.path.dirname(__file__), 'token.key')

async def start_handler(event: types.Message):
    await event.answer(
        f"Привет, {event.from_user.get_mention(as_html=True)} 👋! Прочитай мой /help",
        parse_mode=types.ParseMode.HTML,
    )

async def help_handler(event: types.Message):
    await event.answer(
        f"Ты можешь подписаться на любой поиск на сайте moscow.qtickets.events. Есть три команды - /subscribe Запрос, /list, /unsubscribe Запрос. Например, /subscribe Гринько",
        parse_mode=types.ParseMode.HTML,
    )

async def subscribe_handler(event: types.Message):
    await event.answer(
        f"Chat ID is {event.chat.id}, Message is {event.text}",
        parse_mode=types.ParseMode.HTML,
    )

async def unsubscribe_handler(event: types.Message):
    await event.answer(
        f"Chat ID is {event.chat.id}, Message is {event.text}",
        parse_mode=types.ParseMode.HTML,
    )

async def list_handler(event: types.Message):
    await event.answer(
        f"Chat ID is {event.chat.id}, Message is {event.text}",
        parse_mode=types.ParseMode.HTML,
    )

async def id_handler(event: types.Message):
    await event.answer(
        f"Chat ID is {event.chat.id}",
        parse_mode=types.ParseMode.HTML,
    )

async def main():
    with open(TOKEN, 'r') as file:
        BOT_TOKEN = file.read().replace('\n', '')
    bot = Bot(token=BOT_TOKEN)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        disp.register_message_handler(help_handler, commands={"help"})
        disp.register_message_handler(id_handler, commands={"id"})
        disp.register_message_handler(subscribe_handler, commands={"subscribe"})
        disp.register_message_handler(unsubscribe_handler, commands={"unsubscribe"})
        disp.register_message_handler(list_handler, commands={"list"})
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())
