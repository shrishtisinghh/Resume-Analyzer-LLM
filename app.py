import streamlit as st
import pdfplumber
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume and get AI-powered career insights")

# -----------------------------
# OpenRouter API Configuration
# -----------------------------
OPENROUTER_API_KEY = "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"

API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}


# -----------------------------
# Extract Text from PDF
# -----------------------------
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


# -----------------------------
# AI Resume Analysis
# -----------------------------
def analyze_resume(text):

    prompt = f"""
You are an expert HR professional and career coach.

Analyze the resume and provide:

Skills:
(bullet points)

Strengths:
(bullet points)

Weaknesses:
(bullet points)

Recommended Job Roles:
(bullet points)

Important:
- Understand the candidate domain properly.
- Do NOT assume technical roles if resume is non-technical.
- Keep response concise and professional.

Resume:
{text}
"""

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    data = response.json()

    if "choices" in data:
        return data["choices"][0]["message"]["content"]

    return str(data)


# -----------------------------
# Streamlit UI
# -----------------------------
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:

    with st.spinner("Analyzing Resume... Please wait ⏳"):

        resume_text = extract_text(uploaded_file)

        result = analyze_resume(resume_text)

        st.subheader("📊 Analysis Result")

        st.write(result)
