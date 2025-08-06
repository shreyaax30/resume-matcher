from jd_parser import clean_text

sample_jd = """
We are looking for a Python developer with experience in Django, REST APIs, and cloud services like AWS.
Knowledge of SQL and Git is a plus. Strong communication and problem-solving skills required.
"""

cleaned = clean_text(sample_jd)

print("----- Cleaned JD -----")
print(cleaned)
