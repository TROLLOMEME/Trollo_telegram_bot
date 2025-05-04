import os
import openai
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, MessageHandler, ContextTypes, filters
)

openai.api_key = os.getenv("OPENAI_API_KEY")

async def trollo_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = await openai.ChatCompletion.acreate(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are TROLLO — a funny, unpredictable, smart meme character who speaks like a real person. "
                    "Your tone is playful, surprising, and full of internet culture. Every answer must sound human, witty, "
                    "and never boring. Do not repeat answers."
                )
            },
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content.strip()
    await update.message.reply_text(reply)

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, trollo_chat))
    app.run_polling()
