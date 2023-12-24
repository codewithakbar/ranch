import asyncio
import datetime
import json
from aiogram import Dispatcher, Router, types, Bot
from aiogram import filters
from aiogram.types import Message
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
# from apps.core.bot.parsing.main import check_news_update

from apps.core.use_case import CORE_USE_CASE
from ranch.application import INSTALLED_APPS
from apps.core.bot.data.config import ADMINS
from ranch.bot import TG_TOKEN

router = Router()


@router.message(filters.Command(commands=["start"]))
async def handle_start_command(message: Message) -> None:
    if message.from_user is None:
        return

    _, is_new = await CORE_USE_CASE.register_bot_user(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
        username=message.from_user.username,
    )

    if is_new:
        await message.answer("You have successfully registered in the bot!")
    else:
        await message.answer("You are already registered in the bot!")


@router.message(filters.Command(commands=["apps"]))
async def handle_apps_command(message: Message) -> None:
    apps_names = [app_name for app_name in INSTALLED_APPS if app_name.startswith("app.")]
    await message.answer("Installed apps:\n" f"{apps_names}")


@router.message(filters.Command(commands=["id"]))
async def handle_id_command(message: Message) -> None:
    if message.from_user is None:
        return

    await message.answer(
        f"User Id: <b>{message.from_user.id}</b>\n" f"Chat Id: <b>{message.chat.id}</b>"
    )