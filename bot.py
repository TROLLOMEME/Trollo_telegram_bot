import os
import random
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Read token from environment variable
TOKEN = os.getenv("BOT_TOKEN")

# Funny and varied TROLLO replies
TROLLO_REPLIES = [
    "Haha. That’s funny, but not TROLLO funny.",
    "You just summoned the Meme Lord.",
    "I see you trying to be funny... Respect.",
    "That’s cute. But have you heard of TROLLO?",
    "Boom. Roasted. TROLLO style.",
    "You speak. I troll.",
    "Try harder. TROLLO is watching.",
    "That joke made my Bitcoin glasses fog up.",
    "TROLLO approves... kinda.",
    "Say less, HODL more.",
    "Insert legendary response here.",
    "You’re in the presence of greatness. Behave.",
    "Not bad, human. Not bad at all."
]

def trollo_reply(update: Update, context: CallbackContext):
    user_message = update.message.text
    reply = random.choice(TROLLO_REPLIES)
    update.message.reply_text(reply)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Handle all text messages
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), trollo_reply))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
