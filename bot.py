import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
    MenuButtonWebApp,
    BotCommand
)

# ✅ O'z bot tokeningizni kiriting
BOT_TOKEN = "8667119084:AAEmMJUYIrx7e-Vbm5FC_X5kvIIBMxgovuo"

# ✅ Web App URL — GitHub Pages yoki hosting linkingiz
WEBAPP_URL = "https://yourusername.github.io/jadidlar/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📚 Jadidlarni tanlash",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]
    ])
    await message.answer(
        "🌟 Assalomu alaykum!\n\n"
        "Bu bot orqali O'rta Osiyo jadidlari haqida ma'lumot olishingiz mumkin.\n\n"
        "👇 Quyidagi tugmani bosing:",
        reply_markup=keyboard
    )


async def set_menu_button():
    """Botning asosiy menu tugmasini o'rnatish"""
    await bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(
            text="📚 Jadidlarni tanlash",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )


async def set_commands():
    await bot.set_my_commands([
        BotCommand(command="start", description="Botni boshlash"),
    ])


async def main():
    await set_commands()
    await set_menu_button()
    print("✅ Bot ishga tushdi!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
