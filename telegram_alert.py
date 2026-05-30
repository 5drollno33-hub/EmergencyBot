import requests

BOT_TOKEN = "8751910148:AAEVfOuXy4kgaQxnd2G9PHa5UMhDErD8Tz8"
CHAT_ID = "7798249693"

def send_alert(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )