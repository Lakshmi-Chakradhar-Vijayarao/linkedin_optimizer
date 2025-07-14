import io
from docx import Document
import fitz  # PyMuPDF

def extract_text_from_file(uploaded_file):
    file_type = uploaded_file.name.split('.')[-1].lower()

    try:
        if file_type == "txt":
            return uploaded_file.read().decode("utf-8").strip()

        elif file_type == "docx":
            doc = Document(uploaded_file)
            return "\n".join(p.text.strip() for p in doc.paragraphs if p.text.strip())

        elif file_type == "pdf":
            with fitz.open(stream=uploaded_file.read(), filetype="pdf") as pdf:
                return "\n".join(page.get_text().strip() for page in pdf)

    except Exception as e:
        return f"\u26a0\ufe0f Failed to extract text: {str(e)}"

    return "\u26a0\ufe0f Unsupported file type."

def extract_university_name(resume_text):
    """
    Attempt to extract a university, college, or institute name from resume text.
    Returns the first line containing related keywords.
    """
    for line in resume_text.splitlines():
        if any(keyword in line.lower() for keyword in ["university", "college", "institute", "polytechnic"]):
            return line.strip()
    return None

def extract_company_name(resume_text):
    """
    Attempt to extract a company name based on common patterns in experience section.
    Returns the first plausible company name found.
    """
    for line in resume_text.splitlines():
        if any(keyword in line.lower() for keyword in ["intern", "software engineer", "developer", "worked at", "experience at"]):
            words = line.strip().split("at")
            if len(words) > 1:
                company = words[-1].strip()
                if 2 <= len(company) <= 60:
                    return company
    return None
