import logging import os from telegram import Update from telegram.ext import ( ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters )

Logging 

logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO ) logger = logging.getLogger(name)

Main reply function 

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE): message = update.message.text.lower() user = update.message.from_user.first_name

if 'hello' in message: reply = f"Yo {user}, what's up? You just got TROLLO'd!" elif 'trollo' in message: reply = "The legend never dies. I'm watching you... with my Bitcoin shades." else: reply = f"Hmm... I felt that, {user}. But you better be talking memes or crypto!" await update.message.reply_text(reply) Start command 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text("TROLLO is here. Type something... if you dare.")

Run the bot 

async def main(): token = os.environ.get("BOT_TOKEN") if not token: logger.error("BOT_TOKEN is missing in environment variables.") return

app = ApplicationBuilder().token(token).build() app.add_handler(CommandHandler("start", start)) app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)) logger.info("TROLLO bot is up and running...") await app.run_polling() 

if name == 'main': import asyncio asyncio.run(main())

