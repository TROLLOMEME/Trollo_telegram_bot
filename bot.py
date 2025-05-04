import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from openai import OpenAI

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def trollo_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": (
                "You are TROLLO — a funny, sharp-witted meme character who talks like a cool internet friend. "
                "You love memes, chaos, crypto jokes, and never give boring replies. Be playful, unpredictable, and entertaining.")},
            {"role": "user", "content": user_message}
        ]
    )

    bot_reply = response.choices[0].message.content.strip()
    await update.message.reply_text(bot_reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, trollo_chat))
    app.run_polling()
