import os
import openai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, MessageHandler, ContextTypes, filters
)

openai.api_key = os.getenv("OPENAI_API_KEY")

async def trollo_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are TROLLO. A funny, unpredictable and smart character who responds like a real human with meme energy."},
            {"role": "user", "content": user_text}
        ]
    )

    reply = response.choices[0].message.content.strip()
    await update.message.reply_text(reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, trollo_reply))
    app.run_polling()
