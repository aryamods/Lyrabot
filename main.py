import os
import signal
import sys
import time
from colorama import Fore, Style, init
from chat_management import ChatManager
from user_management import UserManager

def signal_handler(sig, frame):
    print(Fore.RED + "\n⚠️  Anda telah menekan CTRL + C. Keluar dari Chat...")
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    init(autoreset=True)
    user_manager = UserManager()
    chat_manager = ChatManager(user_manager)
    chat_manager.start_chat()