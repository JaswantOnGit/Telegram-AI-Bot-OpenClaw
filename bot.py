"""
Telegram AI Bot powered by OpenClaw
Author: Jaswant Singh

A Telegram chatbot that uses the OpenAI API (via OpenClaw) for intelligent,
context-aware responses. Supports allowlist-based access control and
automated cron-style proactive messaging.
"""

import os
import logging
import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USER_IDS = list(map(int, os.getenv("ALLOWED_USER_IDS", "").split(",")))

openai.api_key = os.getenv("OPENCLAW_API_KEY")


def is_authorized(user_id: int) -> bool:
        """Check if user is in the allowlist."""
        return user_id in ALLOWED_USER_IDS


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /start command."""
        user_id = update.effective_user.id
        if not is_authorized(user_id):
                    await update.message.reply_text("Unauthorized. Access denied.")
                    logger.warning(f"Unauthorized access attempt by user {user_id}")
                    return
                await update.message.reply_text(
                            "Hi! I am your AI assistant powered by OpenClaw.\n"
                            "Send me a message and I will respond intelligently.\n"
                            "Use /status to check bot status."
                )


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle /status command."""
    if not is_authorized(update.effective_user.id):
                await update.message.reply_text("Unauthorized. Access denied.")
                return
            await update.message.reply_text("Bot is active and running.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handle all incoming user messages and return an AI-generated response."""
    user_id = update.effective_user.id
    if not is_authorized(user_id):
                await update.message.reply_text("Unauthorized.")
                return

    user_message = update.message.text
    logger.info(f"Message from {user_id}: {user_message}")

    try:
                response = openai.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[
                                                    {
                                                                            "role": "system",
                                                                            "content": (
                                                                                                        "You are a helpful AI assistant running inside a Telegram bot. "
                                                                                                        "Keep your answers concise and friendly."
                                                                                ),
                                                    },
                                                    {"role": "user", "content": user_message},
                                ],
                                max_tokens=500,
                )
                ai_reply = response.choices[0].message.content.strip()
except openai.OpenAIError as e:
        logger.error(f"OpenAI API error: {e}")
        ai_reply = "Sorry, I encountered an error while processing your request. Please try again."

    await update.message.reply_text(ai_reply)


def main() -> None:
        """Start the bot."""
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    logger.info("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
        main()
