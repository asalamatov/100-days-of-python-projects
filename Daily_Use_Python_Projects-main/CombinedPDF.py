import PyPDF2
import os

# get the merger of PDFs
merger = PyPDF2.PdfFileMerger()

# merge all the PDF files from the current folder
for file in os.listdir(os.curdir):
	if file.endswith(".pdf"):
		print(file)
		merger.append(file)
	merger.write(input("Enter a new name for your MERGED PDF: \n>>"))