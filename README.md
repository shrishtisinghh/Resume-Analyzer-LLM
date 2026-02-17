# 🤖 AI Resume Analyzer

An AI-powered Resume Analyzer that extracts candidate skills, identifies strengths and weaknesses, and recommends suitable job roles using Large Language Models (LLMs).

This project helps students, job seekers, and recruiters quickly evaluate resumes with intelligent insights.

---

## 🚀 Features

✅ Upload Resume in PDF format  
✅ Automatic text extraction  
✅ AI-based skills detection  
✅ Strengths and weaknesses analysis  
✅ Job role recommendations  
✅ Clean and interactive Streamlit UI  
✅ Works for multiple domains (IT, Marketing, Commerce, Healthcare, etc.)

---

## 🧠 How It Works

1. User uploads a resume (PDF)
2. Text is extracted from the document
3. Resume content is sent to an LLM API
4. AI analyzes the profile and returns:
   - Skills
   - Strengths
   - Weaknesses
   - Recommended Job Roles

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LLM API (OpenRouter / OpenAI Compatible)
- PDFPlumber
- Prompt Engineering
- REST API Integration

---
##⚙️ Installation
pip install -r requirements.txt

--▶️ Run Project
streamlit run app.py

--
🔑 API Key Setup
Create .env file:
OPENROUTER_API_KEY=your_key_here

📂 Project Structure
AI-Resume-Analyzer/
│── app.py
│── requirements.txt
│── .env
│── README.md

Screenshot
<img width="654" height="523" alt="Screenshot 2026-02-17 194828" src="https://github.com/user-attachments/assets/bcf8e353-a0d9-486e-91df-aace53e2355a" />


⭐ Future Improvements

Resume score prediction
Job description matching
ATS compatibility check
Multi-file upload support

