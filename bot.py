import os
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# Load secrets
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Set OpenAI key
openai.api_key = OPENAI_API_KEY

async def chat_with_trollo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are TROLLO, a funny, sarcastic, and clever meme lord. Reply short, bold, playful, and meme-style. Never sound like a boring bot."},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response['choices'][0]['message']['content']
    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_with_trollo))
    app.run_polling()

if __name__ == '__main__':
    main()
