import PyPDF3
import pyttsx3
import pdfplumber


file = "Lorem.pdf"

book = open(file, "rb")
pdfReader = PyPDF3.PdfFileReader(book)

pages = pdfReader.numPages

final_text = ""

with pdfplumber.open(file) as pdf:
	for i in range(0, pages):
		page = pdf.pages[i]
		text = page.extract_text()
		final_text += text

engine = pyttsx3.init()
engine.say(final_text)
engine.save_to_file(final_text, "Lorem.mp3")
engine.runAndWait()

