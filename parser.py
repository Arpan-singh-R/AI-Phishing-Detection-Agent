import re


def parse_email(file_path):
    """
    Parse an email from a text file.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return parse_email_text(content)


def parse_email_text(content):
    """
    Parse an email directly from pasted text.
    """

    sender = ""
    subject = ""

    # Extract sender
    sender_match = re.search(r"From:\s*(.*)", content, re.IGNORECASE)
    if sender_match:
        sender = sender_match.group(1).strip()

    # Extract subject
    subject_match = re.search(r"Subject:\s*(.*)", content, re.IGNORECASE)
    if subject_match:
        subject = subject_match.group(1).strip()

    # Extract URLs
    urls = re.findall(r"https?://[^\s]+", content)

    # Extract attachments
    attachments = re.findall(
        r"Attachment:\s*(.*)",
        content,
        re.IGNORECASE
    )

    return {
        "sender": sender,
        "subject": subject,
        "body": content,
        "urls": urls,
        "attachments": attachments
    }