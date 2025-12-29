# AI-Generated-Portfolio-Website-from-Resume

An AI-powered Streamlit application that converts your resume (PDF) into a fully functional, modern, and visually stunning portfolio website using LangChain and Google Gemini (gemini-2.5-flash-lite).

Upload your resume → Download a complete portfolio website (HTML, CSS, JS) 🚀

📌 Project Overview
Feature	Description
Project Name	Resume to Portfolio Website Generator
Description	Converts a resume PDF into a modern portfolio website using AI
Input	Resume (PDF)
Output	HTML, CSS, JavaScript (ZIP file)
UI Framework	Streamlit
AI Model	Google Gemini (gemini-2.5-flash-lite)
Frontend Tech	Pure HTML, CSS, JavaScript
Deployment	Local / Browser-ready

✨ Key Highlights
📄 Upload PDF Resume
🧠 AI-powered resume analysis using Google Gemini
🎨 Generates a modern, gradient-based portfolio website
💎 Card-based UI with smooth hover animations
📱 Fully responsive design
🧾 Clean separation of HTML, CSS & JavaScript
📦 One-click ZIP download
⚡ No frontend frameworks — pure HTML, CSS, JS

🛠️ Tech Stack
Category	Technologies
Frontend Generator	HTML, CSS, JavaScript
Backend / UI	Streamlit
AI / LLM	LangChain + Google Gemini
Model Used	gemini-2.5-flash-lite
PDF Processing	PyPDF
Environment Variables	python-dotenv

⚙️ Application Workflow
Step	Process
1	Setup Google API using .env
2	Upload Resume (PDF)
3	Extract text from PDF
4	Send text to Gemini model
5	Apply system prompt (UI/UX + frontend rules)
6	Generate HTML, CSS, JS
7	Split files correctly
8	Zip all files
9	Download & open index.html

🧠 How It Works (Architecture)
Environment Setup

Uses python-dotenv to securely load the Google API key from .env
Resume Upload

User uploads a PDF resume via Streamlit UI
Text Extraction

Resume text is extracted using PyPDF
AI Processing

Resume text is sent to ChatGoogleGenerativeAI
Model analyzes and extracts:
Name
Role
Summary
Skills
Experience
Projects
Education
Achievements
System Prompt Engineering

AI is instructed to behave as a Senior UI/UX Designer & Frontend Expert
Strict output format enforced for clean file separation
Website Generation

AI generates:
index.html
style.css
script.js
ZIP Packaging

All files are compressed into a single downloadable ZIP
Instant Deployment

Open index.html in any browser to view your portfolio 🎉

📦 Requirements
Library	Purpose
streamlit	Web UI
pypdf	PDF text extraction
langchain	LLM orchestration
langchain_google_genai	Gemini integration
python-dotenv	Secure API key storage
zipfile	File compression

🚀 Getting Started

1️⃣ Clone the Repository
git clone  https://github.com/shubham132004/Resume-To-Portfolio-AI.git
cd portfolio
cd Scripts
activate
streamlit run main.py

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   

3️⃣ Install Dependencies
pip install -r req.txt

4️⃣ Setup Environment Variables
Create a .env file in the root directory:

gemini=YOUR_GOOGLE_API_KEY

🔐 API keys are kept secure using dotenv.

5️⃣ Run the Application
streamlit run main.py
📥 Usage
Open the Streamlit app in your browser

Upload your resume PDF

Click Generate Portfolio Website

Download the ZIP file

Open index.html → Your portfolio is live 🎉

🌟 Use Cases
Students building first portfolios

Professionals upgrading resumes

Freelancers showcasing projects

Rapid personal website generation

AI + Prompt Engineering demos

🔮 Future Enhancements
Multiple design themes

Live preview before download

Custom domain deployment

Hosting integration (GitHub Pages / Netlify)

Resume quality scoring
