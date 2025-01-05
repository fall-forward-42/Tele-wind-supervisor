from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import sqlite3

# async def send_reminder(context: ContextTypes.DEFAULT_TYPE):
#     job = context.job
#     await context.bot.send_message(chat_id=job.chat_id, text=f"Nhắc nhở: {job.data}")

# async def send_early_reminder(context: ContextTypes.DEFAULT_TYPE, description: str, time_type: str):
#     job = context.job
#     await context.bot.send_message(chat_id=job.chat_id, text=f"Nhắc nhở sớm ({time_type}): {description}")


# def add_early_reminder(scheduler, remind_datetime, early_time, description, time_type, application, user_id):
#     if early_time > datetime.now():
#         scheduler.add_job(
#             send_early_reminder, 'date', run_date=early_time,
#             args=[application.bot, description, time_type]
#         )


# def schedule_reminders(application):
#     conn: sqlite3.Connection = sqlite3.connect('tasks.db')
#     c: sqlite3.Cursor = conn.cursor()
#     c.execute("SELECT id, user_id, description, remind_time FROM tasks WHERE status = 'pending'")
#     tasks = c.fetchall()
#     conn.close()

#     scheduler = BackgroundScheduler()

#     for task in tasks:
#         task_id, user_id, description, remind_time = task
#         remind_datetime = datetime.fromisoformat(remind_time)  # Chuyển từ chuỗi ISO 8601 sang datetime

#         # Lập nhắc chính
#         if remind_datetime > datetime.now():
#             scheduler.add_job(
#                 send_reminder, 'date', run_date=remind_datetime,
#                 args=[application.bot, user_id, f"Nhắc nhở: {description}"]
#             )

#             # Nhắc trước 5 phút nếu trong ngày
#             if remind_datetime.date() == datetime.now().date():
#                 early_reminder_time = remind_datetime - timedelta(minutes=5)
#                 add_early_reminder(scheduler, remind_datetime, early_reminder_time, description, "5 phút", application, user_id)

#             # Nhắc trước 1 ngày nếu trong tuần
#             elif (remind_datetime - datetime.now()).days < 7:
#                 early_reminder_time = remind_datetime - timedelta(days=1)
#                 add_early_reminder(scheduler, remind_datetime, early_reminder_time, description, "1 ngày", application, user_id)

#     scheduler.start()

