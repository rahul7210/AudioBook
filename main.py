import pyttsx3
import PyPDF2

book=open('oop.pdf','rb')
Reader=PyPDF2.PdfFileReader(book)
pages=Reader.numPages

speaker = pyttsx3.init()
speaker.say(" Hello Rahul Sir, As always, a great pleasure watching you work")
for num in range(7,pages):
    pg=Reader.getPage(num)
    text=pg.extractText()
    speaker.say(text)
    speaker.runAndWait()

