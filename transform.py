from app import pdf_to_word
from app import word_to_pdf


pdf_to_word("input.pdf", "output.docx")
word_to_pdf("output.docx", "output.pdf")
