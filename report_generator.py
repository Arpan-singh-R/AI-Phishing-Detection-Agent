from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    email,
    analysis,
    ai_report,
    output_file="Phishing_Report.pdf"
):
    """
    Generate a PDF report for the phishing analysis.
    """

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(output_file)

    story = []

    # -------------------------
    # Title
    # -------------------------
    story.append(
        Paragraph(
            "AI Phishing Detection Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 12))

    # -------------------------
    # Email Information
    # -------------------------
    story.append(
        Paragraph(
            f"<b>Sender:</b> {email['sender']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Subject:</b> {email['subject']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Score:</b> {analysis['score']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Risk Level:</b> {analysis['risk']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 15))

    # -------------------------
    # Findings
    # -------------------------
    story.append(
        Paragraph(
            "<b>Findings</b>",
            styles["Heading2"]
        )
    )

    for finding in analysis["findings"]:
        story.append(
            Paragraph(
                f"• {finding}",
                styles["BodyText"]
            )
        )

    story.append(Spacer(1, 15))

    # -------------------------
    # AI Report
    # -------------------------
    story.append(
        Paragraph(
            "<b>AI Analysis</b>",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            ai_report.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return output_file