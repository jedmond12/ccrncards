#!/usr/bin/env python3
import PyPDF2

pdf_path = "Chapters/Chapter 1 Cardiovascular Concepts.pdf"

with open(pdf_path, 'rb') as file:
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"

with open("cardiovascular_chapter.txt", "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extracted {len(text)} characters from {len(pdf_reader.pages)} pages")
