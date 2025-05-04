import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from random import choice

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def generate_trollo_reply(message: str) -> str:
    replies = {
        "funny": [
            "Haha. That's funny, but not TROLLO funny.",
            "Nice try, rookie. TROLLO's on another level.",
            "That joke needs a meme makeover!",
            "TROLLO laughs... slightly.",
            "Almost made me giggle. Almost."
        ],
        "mystery": [
            "The shadows are watching...",
            "Every word you send feeds the ritual.",
            "You’ve triggered the TROLLO protocol.",
            "One more message and it begins.",
            "Your meme energy is... incomplete."
        ],
        "friendly": [
            "Hey buddy! Ready to pump the meme?",
            "What's up legend?",
            "Always here for you, soldier!",
            "TROLLO never sleeps.",
            "Did someone summon a green friend?"
        ],
        "default": [
            "TROLLO is listening.",
            "Type louder, I can't hear your vibes.",
            "Silence is golden, but memes are better.",
            "TROLLO has entered the chat.",
            "I see you... and your weak meme."
        ]
    }

    message = message.lower()
    if "lol" in message or "haha" in message:
        return choice(replies["funny"])
    elif "?" in message or "ritual" in message:
        return choice(replies["mystery"])
    elif "hi" in message or "hello" in message or "hey" in message:
        return choice(replies["friendly"])
    else:
        return choice(replies["default"])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    reply = generate_trollo_reply(user_message)
    await update.message.reply_text(reply)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("TROLLO bot is alive.")
    app.run_polling()
