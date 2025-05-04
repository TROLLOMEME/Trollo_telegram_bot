import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import openai

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TROLLO_SYSTEM_PROMPT = (
    "You are TROLLO, a mysterious, funny and cheeky crypto troll. "
    "You talk in meme-style sarcasm, give short smart replies and never give financial advice."
)

def ask_trollo(update: Update, context: CallbackContext):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text("Say something, human...")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": TROLLO_SYSTEM_PROMPT},
                {"role": "user", "content": query}
            ]
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = "TROLLO glitched. Try again later."

    update.message.reply_text(reply, reply_to_message_id=update.message.message_id)

def reply_to_mentions(update: Update, context: CallbackContext):
    if update.message.text and ('@' in update.message.text or update.message.reply_to_message):
        ask_trollo(update, context)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("trollo", ask_trollo))
    dp.add_handler(MessageHandler(Filters.text & Filters.group, reply_to_mentions))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler()

    # Clear any existing webhook
    updater.bot.delete_webhook(drop_pending_updates=True)

    updater.start_polling()
    updater.idle()
