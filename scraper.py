import PyPDF2
import cv2
import tika
import pytesseract
from tika import parser, unpack

homepath = "/Users/peteraltamura/Documents/fun/plunkett/pages/"
fname = "warDiary_mar7-31-42.pdf"
fname = "0258.pdf"
tika.initVM()
#print("VM Started")
print("Getting results")
print(homepath+fname)
results = unpack.from_file(homepath+fname)


print(results.keys())
c = results['content']
print("Printing content below:")
print(c[:10000].strip())

import sys
sys.exit()


#img = cv2.imread(homepath+fname)
#pytesseract.pytesseract.tesseract_cmd = r"/usr/local/bin/tesseract"
#print('here')
#t = pytesseract.image_to_string(img, config='-l eng --oem 1 --psm 6')
#print(t)

#pdfObj = open(homepath+fname, "rb")
#pdfReader = PyPDF2.PdfFileReader(pdfObj)
#print("No. pages: ", pdfReader.numPages)
