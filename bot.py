import os
from telegram.ext import Updater, MessageHandler, Filters
import openai

BOT_TOKEN = os.getenv(BOT_TOKEN)
OPENAI_API_KEY = os.getenv(OPENAI_API_KEY)
openai.api_key = OPENAI_API_KEY

def handle_message(update, context):
    user_input = update.message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're TROLLO, a funny and clever crypto meme bot. Keep replies short, sharp, and funny."},
            {"role": "user", "content": user_input}
        ]
    )
    answer = response["choices"][0]["message"]["content"]
    update.message.reply_text(answer)

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()
