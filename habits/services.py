import requests

from config.settings import TG_BOT_TOKEN, TELEGRAM_URL


def send_telegram_message(tg_chat_id, message):
    """Отправляет сообщение в Телеграм через бота"""
    params = {"chat_id": tg_chat_id, "text": message}
    requests.get(f"{TELEGRAM_URL}{TG_BOT_TOKEN}/sendMessage", params=params)
