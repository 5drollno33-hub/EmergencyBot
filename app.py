from flask import Flask, request
from classifier import classify
from telegram_alert import send_alert

app = Flask(__name__)

@app.route("/")
def home():
    return "Emergency Bot Running"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():

    msg = request.form.get("Body", "")
    sender = request.form.get("From", "")

    result = classify(msg)

    if result == "EMERGENCY":
        send_alert(
            f"🚨 EMERGENCY DETECTED 🚨\n\nFrom: {sender}\nMessage: {msg}"
        )

    return "OK", 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)