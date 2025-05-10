import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import filters as Filters  # Правильный импорт Filters из filters модуля (добавили 'filters' к модулю)

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен бота
TOKEN = 'YOUR_BOT_TOKEN'


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш помощник в этом чате. Как я могу вам помочь?')


def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    if user_message == '/start':  # Проверка на команду /start для ответа при первом обращении пользователя
        start(update, context)
    else:
        update.message.reply_text(f'Привет {update.message.from_user.first_name}! Вы сказали: {user_message}')


def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    # Применение фильтров к MessageHandler для фильтрации сообщений перед обработкой в handle_message функции
    dispatcher.add_handler(MessageHandler(Filters & ~Filters.command & ~Filters.retweet & ~Filters.edited & ~Filters.bot & ~Filters.regex(".*@.*") & ~Filters.reply & ~Filters.command & ~Filters.private & ~Filters.chat("@your_channel") & ~Filters.chat("@your_other_channel") & ~Filters.chat("@your_third_channel") & ~Filters
