from telegram import Update, Message
from telegram.ext import ContextTypes
from Utils.system_info import (
    get_system_info, 
    get_cpu_info, 
    get_gpu_info, 
    get_network_info, 
    get_memory_info, 
    get_disk_info, 
    get_speedtest_info, 
    get_os_info
)

async def system_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        info = get_system_info()
        response = "\n".join([f"{key}: {value}" for key, value in info.items()])
        await message.reply_text(f"System Info:\n{response}")

async def cpu_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        info = get_cpu_info()
        response = "\n".join([f"{key}: {value}" for key, value in info.items()])
        await message.reply_text(f"CPU Info:\n{response}")

async def gpu_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        info = get_gpu_info()
        response = "\n".join([f"GPU {i+1}:\n" + "\n".join([f"{key}: {value}" for key, value in gpu.items()]) for i, gpu in enumerate(info)])
        await message.reply_text(f"GPU Info:\n{response}")

async def network_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        info = get_network_info()
        response = "\n".join([f"{key}: {value}" for key, value in info.items()])
        await message.reply_text(f"Network Info:\n{response}")

async def memory_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        info = get_memory_info()
        response = "\n".join([f"{key}: {value}" for key, value in info.items()])
        await message.reply_text(f"Memory Info:\n{response}")

async def disk_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        info = get_disk_info()
        response = "\n\n".join([f"Disk {i+1}:\n" + "\n".join([f"{key}: {value}" for key, value in disk.items()]) for i, disk in enumerate(info)])
        await message.reply_text(f"Disk Info:\n{response}")

async def speedtest_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        try:
            info = get_speedtest_info()
            response = "\n".join([f"{key}: {value}" for key, value in info.items()])
            await message.reply_text(f"Speedtest Info:\n{response}")
        except Exception as e:
            await message.reply_text(f"Speedtest failed: {e}")

async def os_info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        info = get_os_info()
        response = "\n".join([f"{key}: {value}" for key, value in info.items()])
        await message.reply_text(f"OS Info:\n{response}")
