import fitz  # PyMuPDF

doc = fitz.open("sample.pdf")

print("총 페이지 수:", len(doc))

for page in doc:
    text = page.get_text()
    print(text)

doc.close()
