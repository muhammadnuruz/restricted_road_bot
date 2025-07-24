from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor
import aiohttp

API_TOKEN = '7664298861:AAHIhU5eevYPiac0WJW3eB9nyFWYPvcGElk'
ROADS_API_URL = "http://127.0.0.1:8001/api/roads/"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def handle_message(message: Message):
    if message.chat.type not in ("supergroup", "group"):
        return

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(ROADS_API_URL) as response:
                if response.status == 200:
                    data = await response.json()
                    roads = data.get("results", [])

                    for road in roads:
                        search_name = road.get("search_name")
                        if search_name and search_name.lower() in message.text.lower():
                            name = road.get("name", "Noma'lum")
                            image_url = road.get("image")[26:]
                            with open("restricted_road_bot/" + image_url, "rb") as photo_file:
                                await message.reply_photo(
                                    photo=photo_file,
                                    caption=name)
                                await message.answer(text="""
🚨 Restricted Route Alert 🚨

Dear Driver,

Check the attached image for restricted routes.

❌ Avoid all restricted areas marked in red.

✅ Follow only approved highways or marked routes.

Driving through restricted areas may lead to 2-week Amazon suspension.

Please confirm after reviewing.

Stay compliant and safe!""")
        except Exception as e:
            await message.reply(f"Xatolik yuz berdi: {e}")
            await bot.send_message(chat_id=1974800905, text=e)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
