from resume_parser import extract_text_from_pdf
from jd_parser import clean_text
from matcher import calculate_similarity, find_keyword_matches

# Load and clean resume
resume_text = extract_text_from_pdf("myResume.pdf")
resume_clean = clean_text(resume_text)

# Sample JD
sample_jd = """
We are looking for a flutter developer with experience in Django, REST APIs, dart.
Knowledge of SQL and Git is a plus. Strong communication and problem-solving skills required.
"""
jd_clean = clean_text(sample_jd)

# Calculate similarity
score = calculate_similarity(resume_clean, jd_clean)

print(f"✅ Resume matches the job description by {score}%")

# Find keyword matches
matched, missing = find_keyword_matches(resume_clean, jd_clean)

print("\n🔍 Matched Keywords:", matched)
print("❌ Missing Keywords:", missing)
