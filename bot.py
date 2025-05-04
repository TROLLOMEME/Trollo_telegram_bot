import os
import logging
from telegram.ext import Updater, MessageHandler, Filters
from openai import OpenAI, OpenAIError

# Env vars
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

print("=== DEBUG | BOT_TOKEN:", BOT_TOKEN)
print("=== DEBUG | OPENAI_API_KEY:", OPENAI_API_KEY)

if not BOT_TOKEN or not OPENAI_API_KEY:
    print("BOT_TOKEN or OPENAI_API_KEY is missing!")
    exit()

# Set up OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# TROLLO personality prompt
trollo_system_prompt = "You are TROLLO, a playful, cheeky, funny and slightly sarcastic meme crypto troll. You never give financial advice. Respond in short, witty style."

# Handler
def trollo_reply(update, context):
    chat_type = update.message.chat.type
    message = update.message.text
    chat_id = update.message.chat_id

    if chat_type not in ["private", "group", "supergroup"]:
        return  # Ignore other types

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": trollo_system_prompt},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message.content.strip()
    except OpenAIError:
        reply = "Oops, my brain just went mining... try again later."

    context.bot.send_message(chat_id=chat_id, text=reply)

# Set up Telegram bot
updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, trollo_reply))

updater.start_polling()
updater.idle()
