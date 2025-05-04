import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing. Add it to your environment variables.")

trollo_quotes = [
    "You again? Still poor?",
    "Buy the dip, they said. Now cry in the meme pit.",
    "HODL? More like HOPES and DREAMS.",
    "One does not simply sell TROLLO.",
    "Welcome to the meme-verse, rookie.",
]

def start(update: Update, context: CallbackContext):
    update.message.reply_text("TROLLO is alive... and watching.")

def ask_trollo(update: Update, context: CallbackContext):
    from random import choice
    update.message.reply_text(choice(trollo_quotes))

def reply_to_mentions(update: Update, context: CallbackContext):
    if context.bot.username.lower() in update.message.text.lower():
        from random import choice
        update.message.reply_text(f"TROLLO says: {choice(trollo_quotes)}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("trollo", ask_trollo))
    dp.add_handler(MessageHandler(Filters.text & Filters.group, reply_to_mentions))

    updater.bot.delete_webhook(drop_pending_updates=True)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
