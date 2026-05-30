import os
import requests

def send_alert(message: str):

    BOT_TOKEN = ("8751910148:AAEVfOuXy4kgaQxnd2G9PHa5UMhDErD8Tz8")
    CHAT_ID = ("7798249693")

    print("BOT:", BOT_TOKEN)
    print("CHAT:", CHAT_ID)

    if not BOT_TOKEN or not CHAT_ID:
        print("Missing BOT_TOKEN or CHAT_ID")
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)

    print("STATUS:", response.status_code)
    print("Telegram response:", response.text)