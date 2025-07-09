from telegram.ext import Updater, CommandHandler

# Actual bot token provided by the user
TOKEN = "8017612261:AAEC3xixxLi1Vhz28qq2oowRRmgiS1o5sS8"

def start(update, context):
    update.message.reply_text("سلام! ربات امنیتی شما فعال است.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
