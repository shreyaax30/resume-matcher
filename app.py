#Main app logic

import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_parser import clean_text
from matcher import calculate_similarity, find_keyword_matches, calculate_bert_similarity

st.set_page_config(page_title="Resume Matcher", layout="centered")

st.title("📄 Resume Matcher with Job Description")

# Upload resume PDF
resume_file = st.file_uploader("Upload your Resume (PDF only)", type=["pdf"])

# Text area for job description
jd_text = st.text_area("Paste the Job Description here")


# Match button
if st.button("🔍 Match Resume"):

    if not resume_file or not jd_text.strip():
        st.warning("Please upload a resume and paste the job description.")
    else:
        # Extract and clean
        resume_raw = extract_text_from_pdf(resume_file)
        resume_clean = clean_text(resume_raw)
        jd_clean = clean_text(jd_text)

        # Match score
        score = calculate_bert_similarity(resume_clean, jd_clean)
        st.success(f"✅ Match Score: {score}%")

        # Keywords
        matched, missing = find_keyword_matches(resume_clean, jd_clean)

        st.markdown("### ✔️ Matched Keywords")
        st.write(', '.join(sorted(matched)) if matched else "None")

        st.markdown("### ❌ Missing Keywords")
        st.write(', '.join(sorted(missing)) if missing else "None")

        # Suggestions
        if missing:
            st.markdown("### 💡 Suggestions")
            st.info(f"Consider adding keywords like: {', '.join(sorted(missing))} to improve your resume.")