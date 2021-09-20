import os

import telebot
import dotenv
import requests

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

url_ = f"http://{os.getenv('IP')}:{os.getenv('PORT')}"

http_post_id = url_ + "/api/insert-sub"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_join(message):
    response = requests.request(method="POST", url=http_post_id, json={"id": message.chat.id})
    if response.status_code == 200:
        message_ = "Welcome to the club, body!"
    else:
        message_ = f"Something was wrong | {response.status_code}"
    bot.send_message(message.chat.id, message_)


bot.polling(none_stop=True)
