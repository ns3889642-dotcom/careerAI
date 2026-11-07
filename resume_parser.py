from pypdf import PdfReader
from io import BytesIO

def extract_resume_text(pdf_file):

    reader = PdfReader(BytesIO(pdf_file.getvalue()))

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text