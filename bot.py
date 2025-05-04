import os
import logging
from telegram.ext import Updater, MessageHandler, Filters
from openai import OpenAI, OpenAIError

# Load env variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("=== DEBUG | BOT_TOKEN:", BOT_TOKEN)
print("=== DEBUG | OPENAI_API_KEY:", OPENAI_API_KEY)

if not BOT_TOKEN or BOT_TOKEN.strip() == "":
    print("=== ERROR | BOT_TOKEN is missing!")
    exit()

if not OPENAI_API_KEY or OPENAI_API_KEY.strip() == "":
    print("=== ERROR | OPENAI_API_KEY is missing!")
    exit()

# Set up OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Message handler
def trollo_reply(update, context):
    if update.message.chat.type != "private":
        return
    
    user_input = update.message.text
    chat_id = update.message.chat_id

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are TROLLO, a playful, cheeky and smart crypto meme bot."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content.strip()
    except OpenAIError as e:
        reply = "Oops... TROLLO's brain just glitched. Try again later!"

    context.bot.send_message(chat_id=chat_id, text=reply)

# Start bot
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, trollo_reply))

updater.start_polling()
updater.idle()
