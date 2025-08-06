# Code to extract text from resume

# PyMuPDF is the library for extracting text from PDF resume

import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    try:
        text = ""
        # Read the file content as bytes
        pdf_bytes = pdf_file.read()
        with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
