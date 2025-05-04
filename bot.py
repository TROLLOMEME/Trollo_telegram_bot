import os
from telegram.ext import Updater, MessageHandler, Filters

# Debug BOT_TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")
print("=== DEBUG | BOT_TOKEN:", BOT_TOKEN)

if not BOT_TOKEN or BOT_TOKEN.strip() == "":
    print("=== ERROR | BOT_TOKEN is missing or empty!")
    exit()

# If token exists, continue
def handle_message(update, context):
    update.message.reply_text("TROLLO is alive!")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()
