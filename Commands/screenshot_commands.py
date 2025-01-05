import asyncio
import os
from typing import Final
from telegram import Bot, Message, Update
from telegram.ext import ContextTypes

from Utils.screenshot import SAVE_DIR, get_all_screenshots, listen_for_enter


async def start_screenshot_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        await message.reply_text(f"Bắt đầu chụp ảnh !")
        listen_for_enter()

async def get_photos_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    
    if message:
        await message.reply_text(f"Đang tìm kiếm ảnh...")

        photos = get_all_screenshots()
        if not photos:
            await message.reply_text("Không có ảnh nào!")

        
        for file_name in photos:
            file_path  = os.path.join(SAVE_DIR, file_name)
            try:
                with open(file_path, 'rb') as photo:
                    await context.bot.send_photo(chat_id=message.chat.id, photo=photo)
                print(f"Đã gửi ảnh: {file_path}")
            except Exception as e:
                print(f"Lỗi khi gửi ảnh {file_name}: {e}")
                await message.reply_text(f"Lỗi khi gửi ảnh: {file_name}")

        await message.reply_text("Đã gửi xong tất cả ảnh.")