from flask import Flask, request
from classifier import classify
from telegram_alert import send_alert

app = Flask(__name__)

@app.route("/")
def home():
    return "Emergency Bot Running"

@app.route("/message", methods=["POST"])
def message():

    data = request.json

    msg = data["message"]

    result = classify(msg)

    if "EMERGENCY" in result:
        send_alert(
            f"🚨 EMERGENCY DETECTED\n\nMessage:\n{msg}"
        )

    return result

if __name__ == "__main__":
    app.run(debug=True)