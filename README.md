# Resume Matcher with Job Description

A NLP-powered web tool to evaluate how well a resume matches a job description using semantic similarity and keyword analysis.

### 🌐 Live Demo  
[Click here to try the app on Streamlit](https://resume-matcher-3008.streamlit.app/)

## 🚀 Tech Stack
- Python
- Streamlit
- Sentence-BERT
- Scikit-learn

## 💡 Features
- Upload resume & paste job description
- Get match score using SBERT embeddings
- See matched and missing keywords
- Get improvement suggestions

## 📦 Setup
pip install -r requirements.txt
streamlit run app.py

## ⚙️ How It Works

### 📝 Resume & JD Input
- The user uploads a resume (**PDF format**).
- The user pastes a job description (**JD**) into a text area.

### 🔍 Text Extraction
- The resume is parsed using `pdfplumber` to extract raw text.
- The JD is cleaned and tokenized for analysis.

### 🤖 Semantic Matching with SBERT
- Both the resume text and the JD are converted into **sentence embeddings** using **Sentence-BERT**.
- These embeddings capture the **contextual meaning** of the text (unlike TF-IDF which is just frequency-based).
- **Cosine similarity** is calculated between the two embeddings to generate a **match score** (0 to 1).

### 🧠 Keyword Analysis
- Important keywords from the JD are extracted.
- The tool checks which keywords are present or missing in the resume.
- It lists **matched keywords** and **missing keywords** to give insight into what’s covered.

### 💡 Improvement Suggestions
- Based on missing keywords, the app suggests which **skills/terms** to consider adding to the resume for better alignment.

### 🖥️ User Interface
- Built with **Streamlit** for a clean, interactive experience.
- **Upload → Paste JD → Get results instantly**    


## ✍️ Author
[Shreya](https://github.com/shreyaax30)


