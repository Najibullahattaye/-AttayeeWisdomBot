import os
from telegram import Bot, Update
from telegram.ext import CommandHandler, Updater

def start(update, context):
    update.message.reply_text("سلام، ربات مخفی شما فعال شد.")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()