from resume_parser import extract_text_from_pdf

pdf_path = "myResume.pdf"  # Replace with your own resume filename
resume_text = extract_text_from_pdf(pdf_path)

print("----- Resume Text Start -----")
print(resume_text[:1000])  # Print first 1000 characters
print("----- Resume Text End -----")