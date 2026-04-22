"""
Telegram AI Bot powered by OpenClaw
Author: Jaswant Singh
"""

import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USER_IDS = list(map(int, os.getenv("ALLOWED_USER_IDS", "").split(",")))


def is_authorized(user_id: int) -> bool:
    """Check if user is in the allowlist."""
    return user_id in ALLOWED_USER_IDS


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command."""
    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await update.message.reply_text("Unauthorized. Access denied.")
        logger.warning(f"Unauthorized access attempt by user {user_id}")
        return
    await update.message.reply_text(
        "Hi! I am your AI assistant.\n"
        "Send me a message and I will respond intelligently.\n"
        "Use /status to check usage."
    )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /status command."""
    if not is_authorized(update.effective_user.id):
        return
    await update.message.reply_text("Bot is active and running.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all incoming user messages."""
    user_id = update.effective_user.id
    if not is_authorized(user_id):
        await update.message.reply_text("Unauthorized.")
        return

    user_message = update.message.text
    logger.info(f"Message from {user_id}: {user_message}")

    # Placeholder: replace with actual OpenClaw / AI API call
    response = f"You said: {user_message!r} (AI response would appear here)"
    await update.message.reply_text(response)


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
