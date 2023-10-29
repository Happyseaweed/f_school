import PyPDF2
import io
import requests

headers = {'User-Agent': 'Mozilla/5.0 (X11; Windows; Windows x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36'}


class PDFTextExtractor:
    def __init__(self, url):
        self.response = requests.get(url=url, headers=headers, timeout=120)
        self.file = io.BytesIO(self.response.content)

    def extract_text(self):
        text = ""
        reader = PyPDF2.PdfReader(self.file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page_obj = reader.pages[page_num]
            page_text = page_obj.extract_text()
            text += page_text

        return text

pdf_extractor = PDFTextExtractor("https://ocw.mit.edu/courses/18-s997-high-dimensional-statistics-spring-2015/aedae8ecc50403ef5af2d2438764993e_MIT18_S997S15_Assignment1.pdf")
extracted_text = pdf_extractor.extract_text()



print(extracted_text)
