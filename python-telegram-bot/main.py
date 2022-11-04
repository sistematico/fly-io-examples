#!/usr/bin/env python

import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from macunaima.decorators import rate_limited

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.environ.get('TOKEN')

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Olá!')

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))

    # Polling
    # updater.start_polling()
    # Webhook
    updater.start_webhook(listen="0.0.0.0", port=8080, url_path=TOKEN, webhook_url="https://macunaima.fly.dev/" + TOKEN)
    updater.idle()

if __name__ == '__main__':
    main()
