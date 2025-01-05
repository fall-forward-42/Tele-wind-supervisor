from datetime import datetime
from typing import Final
from telegram import Update, MessageEntity
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from Commands.screenshot_commands import get_photos_command, start_screenshot_command
from Database.database import add_task, get_tasks, init_db
from Commands.common_commands import custom_command, help_command, start_command
from Handlers.errors import error
from Handlers.messages import handle_message
from Commands.system_commands import (
    system_info_command, 
    cpu_info_command, 
    gpu_info_command, 
    network_info_command, 
    memory_info_command, 
    disk_info_command, 
    speedtest_command, 
    os_info_command
)
import keyboard

from Utils.screenshot import get_all_screenshots

#from Functions.reminder import schedule_reminders
# Token and bot username

TOKEN: Final = '8072336146:AAFawucr2XRfd33ihjArIJUCZ9ZPPIfu--Q'




# Main function
if __name__ == '__main__':

    if not TOKEN:
        print("Error: Missing TOKEN. Please provide a valid Telegram bot token.")
        exit(1)
    print('Bot is starting...')
    app = Application.builder().token(TOKEN).build()
    init_db()

    

    # Register command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #System info cmds
    app.add_handler(CommandHandler('system', system_info_command))
    app.add_handler(CommandHandler('cpu', cpu_info_command))
    app.add_handler(CommandHandler('gpu', gpu_info_command))
    app.add_handler(CommandHandler('network', network_info_command))
    app.add_handler(CommandHandler('memory', memory_info_command))
    app.add_handler(CommandHandler('disk', disk_info_command))
    app.add_handler(CommandHandler('speedtest', speedtest_command))
    app.add_handler(CommandHandler('os', os_info_command))


    #Task commands
    # app.add_handler(CommandHandler('task', add_task_command))
    # app.add_handler(CommandHandler('tasks', list_task_command))


    # Register message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    #Screenshot commands
    app.add_handler(CommandHandler('screenshot', start_screenshot_command))
    app.add_handler(CommandHandler('photos', get_photos_command)) 

    # schedule_reminders(app)


    # Register error handler
    app.add_error_handler(error) # type: ignore



    # Start polling
    print('Bot is polling...')
    app.run_polling(poll_interval=3)
