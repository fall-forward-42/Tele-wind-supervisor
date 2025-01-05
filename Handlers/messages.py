from telegram import Chat, Message, Update, MessageEntity, InputFile, Bot
from telegram.ext import ContextTypes
from Utils.responses import handle_response  
import asyncio
from Utils.screenshot import take_screenshot
from typing import Final

TOKEN: Final = '8072336146:AAFawucr2XRfd33ihjArIJUCZ9ZPPIfu--Q'
BOT_USERNAME = '@Lihihihibot'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message: Message | None = update.message

    if not message:
        return  # Thoát nếu không có message

    text: str | None = message.text
    if not text:
        return  # Thoát nếu không có nội dung tin nhắn
    
    chat: Chat = message.chat
    print(f'User ({chat.id}) in {chat.type}: "{text}"')

    # Xử lý tin nhắn trong nhóm
    if chat.type == 'group':
        entities = message.entities or []
        if any(entity.type == MessageEntity.MENTION and BOT_USERNAME in text for entity in entities):
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
            await message.reply_text(response)
    else:
        # Xử lý tin nhắn cá nhân
        response = handle_response(text)
        await message.reply_text(response)

