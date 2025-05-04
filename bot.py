import os
import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in environment variables.")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# TROLLO phrases
trollo_lines = [
    "Who summoned the meme lord?",
    "Another day, another poor trader.",
    "Don't trust green candles... or clowns.",
    "Keep calm and TROLLO on.",
    "When in doubt, zoom out.",
]

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("TROLLO has entered the chat. Say something...")

# /trollo command
async def trollo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(trollo_lines))

# respond to any group message mentioning bot
async def reply_in_group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.bot.username.lower() in update.message.text.lower():
        await update.message.reply_text(random.choice(trollo_lines))

# MAIN
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trollo", trollo))
    app.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, reply_in_group))

    await app.run_polling()

# run
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
