
import random
import telebot
from dotenv import load_dotenv
import os
load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

filenames = [
    "todolist.txt",
]

def send_message(question):
    bot = telebot.TeleBot(TELEGRAM_TOKEN)
    bot.send_message(CHAT_ID, question)
# ""
if __name__ == '__main__':
    question = "Hey Gautam, here is your tasks for today. What is the status of them ? \n"
    cnt = 1
    for filename in filenames:
        with open(filename, 'r',encoding="utf-8") as file:
            lines = file.readlines()
        file.close()
    for line in lines:
        question += line
    send_message(question)
    print(question)
    
    
