import pdfplumber
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

pdf_path = r"C:\Users\82314\Desktop\IS5940 Innovation and Technology Entrepreneurship\00 Group Project\Group6_Data to billionaires_interim_Plantpal_plan.pdf"

with pdfplumber.open(pdf_path) as pdf:
    print(f"Total pages: {len(pdf.pages)}")
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        print(f"\n{'='*60}")
        print(f"PAGE {i+1}")
        print('='*60)
        if text:
            print(text)
        else:
            print("[No text extracted from this page]")
