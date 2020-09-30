#import this library for the audio conversion
import pyttsx3

#this library is responsible for the pdf reading
import PyPDF2



book = open('ankur.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

#initialise the library
speaker = pyttsx3.init()

# getting details of current speaking rate
rate = speaker.getProperty('rate')   

#changing the current speaking rate to 155
speaker.setProperty('rate', 155)


#taking the very first page as an input
page = pdfReader.getPage(1)


text = page.extractText()

#now the speaking begins
speaker.say(text)
speaker.runAndWait()