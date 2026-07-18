import re

# -----------------------------
# Keyword Lists
# -----------------------------

SUSPICIOUS_TLDS = [
    ".xyz",
    ".top",
    ".click",
    ".zip",
    ".country",
    ".ru"
]

FAKE_BRANDS = [
    "amaz0n",
    "paypa1",
    "micr0soft",
    "faceb00k",
    "g00gle"
]

URGENT_WORDS = [
    "urgent",
    "immediately",
    "verify",
    "suspend",
    "password",
    "login",
    "expired",
    "limited",
    "confirm"
]

DANGEROUS_EXTENSIONS = [
    ".exe",
    ".bat",
    ".scr",
    ".cmd",
    ".js"
]


# -----------------------------
# Main Risk Calculator
# -----------------------------

def calculate_risk(email):

    score = 0
    findings = []

    body = email["body"].lower()
    sender = email["sender"].lower()

    # Sender checks
    for brand in FAKE_BRANDS:
        if brand in sender:
            findings.append(f"Fake brand detected: {brand}")
            score += 30

    for tld in SUSPICIOUS_TLDS:
        if sender.endswith(tld):
            findings.append(f"Suspicious sender domain: {tld}")
            score += 20

    # URL checks
    for url in email["urls"]:

        if url.startswith("http://"):
            findings.append("Uses HTTP instead of HTTPS")
            score += 15

        for tld in SUSPICIOUS_TLDS:
            if tld in url:
                findings.append(f"Suspicious URL domain: {tld}")
                score += 20

    # Attachment checks
    for attachment in email["attachments"]:

        lower = attachment.lower()

        for ext in DANGEROUS_EXTENSIONS:

            if lower.endswith(ext):
                findings.append(f"Dangerous attachment: {attachment}")
                score += 30

        if ".pdf.exe" in lower:
            findings.append("Double extension attachment detected")
            score += 25

    # Urgent language
    for word in URGENT_WORDS:

        if re.search(rf"\b{word}\b", body):
            findings.append(f"Urgent keyword detected: {word}")
            score += 5

    # Risk level
    if score >= 70:
        risk = "HIGH"

    elif score >= 40:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "score": score,
        "risk": risk,
        "findings": findings
    }


# -----------------------------
# Sender Analysis
# -----------------------------

def analyze_sender(sender):

    sender = sender.lower()

    if ".xyz" in sender:
        return "Suspicious sender domain (.xyz)"

    if "amaz0n" in sender:
        return "Possible fake Amazon sender"

    return "Sender appears normal"


# -----------------------------
# URL Analysis
# -----------------------------

def analyze_urls(urls):

    findings = []

    for url in urls:

        if url.startswith("http://"):
            findings.append("Uses HTTP")

        if ".xyz" in url:
            findings.append("Suspicious domain (.xyz)")

    return findings


# -----------------------------
# Attachment Analysis
# -----------------------------

def analyze_attachments(attachments):

    findings = []

    for attachment in attachments:

        attachment = attachment.lower()

        if attachment.endswith(".exe"):
            findings.append("Executable attachment")

        if ".pdf.exe" in attachment:
            findings.append("Double extension attachment")

    return findings