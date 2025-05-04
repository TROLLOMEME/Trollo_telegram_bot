import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Set your token here from environment variable
TOKEN = os.getenv("BOT_TOKEN")

# List of TROLLO-style fun replies
TROLLO_REPLIES = [
    "Haha. That’s funny, but not TROLLO funny.",
    "You just summoned the Meme Lord.",
    "That joke made my Bitcoin glasses fog up.",
    "Boom. Roasted. TROLLO style.",
    "Say less, HODL more.",
    "Try harder. TROLLO is watching.",
    "Insert legendary response here.",
    "Not bad, human. Not bad at all."
]

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = random.choice(TROLLO_REPLIES)
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == '__main__':
    main()
