import requests

def send_alert(message: str):
    BOT_TOKEN = "YOUR_NEW_BOT_TOKEN"
    CHAT_ID = "YOUR_CHAT_ID"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        print("Telegram status:", response.status_code)
    except Exception as e:
        print("Telegram error:", e)