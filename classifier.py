import re

def classify(msg: str) -> str:
    """
    Simple rule-based emergency classifier.
    Returns: "EMERGENCY" or "NORMAL"
    """

    if not msg:
        return "NORMAL"

    msg = msg.lower()

    # Strong emergency keywords
    emergency_keywords = [
        "help",
        "emergency",
        "danger",
        "save me",
        "accident",
        "fire",
        "attack",
        "robbery",
        "hurt",
        "bleeding",
        "police",
        "kidnap",
        "sos"
    ]

    # Check keyword match
    for word in emergency_keywords:
        if word in msg:
            return "EMERGENCY"

    # Regex patterns (more realistic detection)
    patterns = [
        r"\bcall\s+(police|ambulance)\b",
        r"\bi\s+am\s+in\s+danger\b",
        r"\bi'?m\s+trapped\b",
        r"\bneed\s+help\b"
    ]

    for pattern in patterns:
        if re.search(pattern, msg):
            return "EMERGENCY"

    return "NORMAL"