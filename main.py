import os
import time
import telebot
from dotenv import load_dotenv
from commands import register_commands

# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = telebot.TeleBot(TOKEN)
register_commands(bot)

def send_alert(chat_id, message):
    try:
        bot.send_message(chat_id, message)
    except Exception as e:
        print(f"Error sending alert: {e}")
    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        """
        Handle '/start' and '/hello' commands.

        Args:
            message (telebot.types.Message): The message object.
        """
        bot.reply_to(message, "Hello! I'm a simple Telegram bot.")

    @bot.message_handler(func=lambda msg: True)
    def echo_all(message):
        """
        Echo all incoming text messages back to the user.

        Args:
            message (telebot.types.Message): The message object.
        """
        bot.reply_to(message, message.text)

    # Remove webhook to avoid conflicts with polling
    bot.delete_webhook(drop_pending_updates=True)
print("Bot is running...")

bot.infinity_polling()
