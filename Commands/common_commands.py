from telegram import Message, Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        await message.reply_text("Xin chào! Tôi có thể giúp gì cho bạn?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message
    if message:
        await message.reply_text("Giúp đở, vui lòng hỏi tôi về những gì bạn cần!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message: Message | None = update.message

    if message:
        await message.reply_text("Cấu hình đã được kích hoạt!")


# Task commands
# async def add_task_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(update.message.text)
#     try:
#         user_id: int = update.message.chat.id
#         description: str = " ".join(context.args[:-2]) # bỏ qua các đối số cuối
#         remind_date: str = context.args[-2]  # Ngày nhắc nhở (YYYY-MM-DD)
#         remind_time: str = context.args[-1]  # Định dạng HH:MM

#         remind_date_time: datetime = datetime.strptime(f"{remind_date} {remind_time}", "%Y-%m-%d %H:%M")

#         print(user_id,description,remind_date_time)

#         add_task(user_id, description, remind_date_time.isoformat())
#         await update.message.reply_text(f"Đã thêm công việc: {description} vào lúc {remind_time}")
#     except ValueError as ve:
#         print(f"ValueError: {ve}")
#         await update.message.reply_text("Định dạng không hợp lệ. Hãy sử dụng: /task <công việc> <YYYY-MM-DD> <HH:MM>")
#     except Exception as e:
#         print(f"Error: {e}")
#         await update.message.reply_text("Có lỗi xảy ra. Vui lòng thử lại.")

# async def list_task_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_id: int = update.message.chat.id
#     tasks: list = get_tasks(user_id)

#     if tasks:
#         message: str = "Danh sách công việc:\n"
#         for task in tasks:
#             remind_time = datetime.fromisoformat(task[2])#  ISO 8601 into datetime
#             remind_time = remind_time.strftime('%Y-%m-%d %H:%M')
#             message += f"ID: {task[0]}, Mô tả: {task[1]}, Nhắc lúc: {remind_time}, Trạng thái: {task[3]}\n"
#     else:
#         message = "Bạn chưa có công việc nào trong danh sách."
#     await update.message.reply_text(message)
