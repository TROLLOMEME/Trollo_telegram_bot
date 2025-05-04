from random import choice

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
        def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = generate_trollo_reply(user_message)
    update.message.reply_text(response)
