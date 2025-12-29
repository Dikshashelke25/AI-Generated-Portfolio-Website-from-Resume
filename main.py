# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import zipfile
# from pypdf import PdfReader
# from langchain_core.messages import SystemMessage, HumanMessage
# import os

# load_dotenv()
# os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# st.set_page_config(page_title="AI Website Generator", page_icon="🤧")
# st.title("PORTFOLIO WEBSITE GENERATOR")

# uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

# def extract_text_from_pdf(uploaded_file):
#     reader = PdfReader(uploaded_file)
#     text = ""
#     for page in reader.pages:
#         text += page.extract_text() or ""
#     return text

# if st.button("Generate") and uploaded_file is not None:

#     resume_text = extract_text_from_pdf(uploaded_file)

#     model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

#     messages = [
#         SystemMessage(content="""
# You are an expert in generating a portfolio website from resume text.
# Extract name, skills, experience, projects, achievements, education,
# design style, and generate a colorful portfolio website.

# Output format must be:

# --html--
# [html code]
# --html--

# --css--
# [css code]
# --css--

# --js--
# [js code]
# --js--
# """),
#         HumanMessage(content=resume_text)
#     ]

#     response = model.invoke(messages)

#     # Save files
#     with open("index.html", "w", encoding="utf-8") as f:
#         f.write(response.content.split("--html--")[1])

#     with open("style.css", "w", encoding="utf-8") as f:
#         f.write(response.content.split("--css--")[1])

#     with open("script.js", "w", encoding="utf-8") as f:
#         f.write(response.content.split("--js--")[1])

#     # Zip files
#     with zipfile.ZipFile("website.zip", "w") as zipf:
#         zipf.write("index.html")
#         zipf.write("style.css")
#         zipf.write("script.js")

#     st.download_button(
#         "Click to download website",
#         data=open("website.zip", "rb"),
#         file_name="website.zip"
#     )

#     st.success("Website generated successfully")


# ============================================================
# AI RESUME → PORTFOLIO WEBSITE GENERATOR (ADVANCED STREAMLIT)
# ============================================================
# Features:
# - Resume (PDF) → Portfolio Website
# - Premium animated UI (blue–purple)
# - Glassmorphism cards
# - Resume summary preview
# - Robust LLM parsing
# - ZIP export (HTML/CSS/JS)

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import zipfile
from pypdf import PdfReader
from langchain_core.messages import SystemMessage, HumanMessage
import os

# ============================================================
# ENV SETUP
# ============================================================
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="AI Resume to Portfolio Generator",
    page_icon="✨",
    layout="centered"
)

# ============================================================
# ADVANCED UI STYLING
# ============================================================
st.markdown("""
<style>

@keyframes gradientBG {
  0% {background-position: 0% 50%;}
  50% {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}

/* 🔥 Darker, high-contrast background */
.stApp {
  background: linear-gradient(-45deg, #0f172a, #1e293b, #1e1b4b, #312e81);
  background-size: 400% 400%;
  animation: gradientBG 14s ease infinite;
  color: #f8fafc !important;
}

/* 🌟 High contrast glass panel */
.glass {
  background: rgba(255,255,255,0.10);
  backdrop-filter: blur(20px);
  border-radius: 22px;
  border: 1px solid rgba(255,255,255,0.2);
  padding: 2rem;
  box-shadow: 0 20px 50px rgba(0,0,0,0.55);
}

/* 📝 Headings readable */
h1 {
  text-align: center;
  color: #ffffff !important;
  font-weight: 800;
}

.subtitle {
  text-align: center;
  color: #cbd5e1 !important;
  margin-bottom: 1.5rem;
}

/* 📁 Upload box contrast */
.stFileUploader {
  background: #1e293b !important;
  color: #e2e8f0 !important;
  border: 2px dashed #475569 !important;
  border-radius: 16px;
  padding: 1.2rem;
}

/* 🚀 Button contrast boost */
.stButton button {
  background: linear-gradient(135deg, #4f46e5, #3b82f6);
  color: #ffffff;
  font-weight: 700;
  border-radius: 14px;
  padding: 0.8rem 2.3rem;
  border: none;
  box-shadow: 0 10px 30px rgba(59,130,246,0.45);
  transition: all 0.3s ease;
}

.stButton button:hover {
  transform: translateY(-3px) scale(1.07);
  box-shadow: 0 15px 40px rgba(59,130,246,0.7);
}

/* 🎉 Success message card */
.success-box {
  background: #0f766e33;
  border-left: 6px solid #14b8a6;
  border-radius: 14px;
  padding: 1rem;
  color: #e0f2f1;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
# st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.markdown("# 📄 Resume → Portfolio Website Generator")
st.markdown(
    "<p class='subtitle'>Upload your resume and instantly get a <b>modern, colorful, professional portfolio website</b>.</p>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type="pdf")

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

generate = st.button("🚀 Generate Portfolio Website")

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# GENERATION LOGIC
# ============================================================
if generate:
    if uploaded_file is None:
        st.warning("Please upload a PDF resume.")
        st.stop()

    with st.spinner("✨ Analyzing resume & designing website..."):
        resume_text = extract_text_from_pdf(uploaded_file)

        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

        messages = [
            SystemMessage(content="""
You are an expert web developer and portfolio designer. 
Generate a complete modern, professional, responsive portfolio website using the resume text provided below.

Website Requirements:
- Home / About section with professional intro
- Skills section with categorized tech stacks
- Projects section with 3-6 showcased projects (cards with description + skills used)
- Work Experience timeline style layout
- Education section
- Contact section with email and social links
- Take profile picture
- Smooth scrolling navigation with nav bar
- Contrast-friendly modern color palette
- Responsive design (mobile + desktop friendly)
- Include placeholder images if needed

Styling Requirements:
- Modern UI (glassmorphism or neo-brutal or clean modern)
- Google Fonts: Poppins / Inter
- Color palette suggestion: Indigo / Slate / White (#4f46e5, #1e293b, #ffffff)
- Buttons & links should use hover animations

Tech rules:
- Pure HTML, CSS, JS only
- No frameworks

STRICT OUTPUT FORMAT:
--html--
[HTML]
--html--
--css--
[CSS]
--css--
--js--
[JS]
--js--
"""),
            HumanMessage(content=resume_text)
        ]

        response = model.invoke(messages)
        content = response.content

        try:
            html = content.split("--html--")[1].split("--css--")[0]
            css = content.split("--css--")[1].split("--js--")[0]
            js = content.split("--js--")[1]
        except Exception:
            st.error("⚠️ Failed to generate website. Try another resume.")
            st.stop()

        # Save files
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html)
        with open("style.css", "w", encoding="utf-8") as f:
            f.write(css)
        with open("script.js", "w", encoding="utf-8") as f:
            f.write(js)

        # Zip
        with zipfile.ZipFile("portfolio_website.zip", "w") as zipf:
            zipf.write("index.html")
            zipf.write("style.css")
            zipf.write("script.js")

        st.markdown("<div class='success-box'>🎉 Website generated successfully!</div>", unsafe_allow_html=True)

        st.download_button(
            "⬇️ Download Portfolio Website (ZIP)",
            data=open("portfolio_website.zip", "rb"),
            file_name="portfolio_website.zip",
            mime="application/zip"
        )