import asyncio
import os
from datetime import datetime
from re import X
import pyautogui
import telegram 
import keyboard

# Thư mục lưu trữ ảnh chụp màn hình
SAVE_DIR = "screenshots"
os.makedirs(SAVE_DIR, exist_ok=True)  # Tạo thư mục nếu chưa tồn tại

def take_screenshot():
    """Chụp màn hình và lưu vào thư mục."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Định dạng thời gian
    file_path = os.path.join(SAVE_DIR, f"photo_{timestamp}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)
    print(f"Đã lưu ảnh chụp màn hình: {file_path}")
    return file_path

def listen_for_enter():
    """Lắng nghe phím Enter và chụp ảnh màn hình."""
    print("Nhấn Enter để chụp ảnh màn hình")
    try:
        while True:
            keyboard.wait("enter")  #
            take_screenshot()
    except KeyboardInterrupt:
        print("\nĐã thoát chương trình.")

def get_all_screenshots():
    """Gửi tất cả ảnh chụp màn hình trong thư mục lên Telegram."""
    if not os.path.exists(SAVE_DIR):
        return []

    files = [f for f in os.listdir(SAVE_DIR) if f.endswith(('.png', '.jpg', '.jpeg'))]

    if not files:
        return []
    
    return files
