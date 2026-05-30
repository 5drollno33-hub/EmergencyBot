def classify(msg):
    msg = msg.lower()

    if "help" in msg or "emergency" in msg or "danger" in msg:
        return "EMERGENCY"

    return "NORMAL"