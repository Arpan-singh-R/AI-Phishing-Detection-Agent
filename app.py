import streamlit as st
import tempfile
import os

from parser import parse_email, parse_email_text
from tools import calculate_risk
from agent import analyze_email, analyze_email_text
from report_generator import generate_report

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Phishing Detection Agent",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🛡️ AI Phishing Detection")

st.sidebar.info("""
This AI agent analyzes suspicious emails using:

• Email Parsing
• Rule-Based Detection
• Groq LLM
• AI Report Generation
""")

st.sidebar.markdown("---")

st.sidebar.subheader("🛡 Cyber Safety Tips")

st.sidebar.success("✔ Never click unknown links")
st.sidebar.success("✔ Check sender domain")
st.sidebar.success("✔ Avoid executable attachments")
st.sidebar.success("✔ Verify HTTPS websites")
st.sidebar.success("✔ Report phishing emails")

# -------------------------------
# Title
# -------------------------------
st.title("🛡️ AI Phishing Detection Agent")

st.write(
    "Analyze suspicious emails using AI-powered phishing detection."
)

# -------------------------------
# Paste Email
# -------------------------------
st.subheader("📋 Paste Email")

email_text = st.text_area(
    "Paste suspicious email here",
    height=220
)

st.markdown("### OR")

# -------------------------------
# Upload Email
# -------------------------------
uploaded_file = st.file_uploader(
    "📂 Upload Email (.txt)",
    type=["txt"]
)

# -------------------------------
# Analyze Button
# -------------------------------
if st.button("🚀 Analyze Email"):

    if not uploaded_file and not email_text.strip():
        st.warning("Please upload an email or paste email text.")
        st.stop()

    # ---------------------------
    # Uploaded File
    # ---------------------------
    if uploaded_file:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".txt"
        ) as tmp:

            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        email = parse_email(temp_path)

        analysis = calculate_risk(email)

        report = analyze_email(temp_path)

        pdf_file = generate_report(
            email,
            analysis,
            report
        )

        os.remove(temp_path)

    # ---------------------------
    # Pasted Email
    # ---------------------------
    else:

        email, analysis, report = analyze_email_text(email_text)

        pdf_file = generate_report(
            email,
            analysis,
            report
        )

    st.success("✅ Analysis Complete")

    # ---------------------------
    # Summary
    # ---------------------------
    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📧 Email Summary")

        st.write(f"**Sender:** {email['sender']}")
        st.write(f"**Subject:** {email['subject']}")
        st.write(f"**URLs Found:** {len(email['urls'])}")
        st.write(f"**Attachments:** {len(email['attachments'])}")

    with col2:

        st.subheader("🚨 Risk Assessment")

        st.metric(
            "Risk Score",
            f"{analysis['score']}/100"
        )

        st.progress(min(analysis["score"], 100) / 100)

        if analysis["risk"] == "HIGH":
            st.error("🔴 HIGH RISK")

        elif analysis["risk"] == "MEDIUM":
            st.warning("🟡 MEDIUM RISK")

        else:
            st.success("🟢 LOW RISK")

    # ---------------------------
    # Findings
    # ---------------------------
    st.divider()

    with st.expander("🔍 View Findings", expanded=True):

        for finding in analysis["findings"]:
            st.write("✅", finding)

    # ---------------------------
    # AI Analysis
    # ---------------------------
    st.divider()

    st.subheader("🤖 AI Analysis")

    st.write(report)

    # ---------------------------
    # Statistics
    # ---------------------------
    st.divider()

    st.subheader("📊 Email Statistics")

    c1, c2, c3 = st.columns(3)

    c1.metric("URLs", len(email["urls"]))
    c2.metric("Attachments", len(email["attachments"]))
    c3.metric("Findings", len(analysis["findings"]))

    # ---------------------------
    # Download PDF
    # ---------------------------
    st.divider()

    with open(pdf_file, "rb") as file:

        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="Phishing_Report.pdf",
            mime="application/pdf"
        )

    # ---------------------------
    # Footer
    # ---------------------------
    st.divider()

    st.caption(
        "Built by Arpan | AI Phishing Detection Agent | Agentic AI Internship Project"
    )