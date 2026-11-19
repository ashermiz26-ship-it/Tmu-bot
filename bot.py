import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
MY_LINK = os.environ.get("MY_LINK")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "היי! שלח לי קישור של טימו")

@bot.message_handler(func=lambda m: True)
def handle(message):
    text = message.text or ""
    if "temu" in text.lower():
        bot.reply_to(message, f"הנה הדיל שלך:\n{MY_LINK}")
    else:
        bot.reply_to(message, "שלח לי קישור של טימו")

print("הבוט דולק...")
bot.infinity_polling()
