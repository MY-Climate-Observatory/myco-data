# -*- coding: utf-8 -*-
"""
25 Oct 2020
Author: Xiandi Ooi

We will convert the pdf into image page by page. 
The source link of the pdf can be found in the README.md.

"""
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import os

def scan_pdf(inputfile):
    # converting the pdf file to image
    pages = convert_from_path("dasar_as.pdf", 500)
    counter = 1
    for page in pages:
        filename = "page_" + str(counter) + ".jpg"
        page.save(filename, "JPEG")
        counter += 1
        
    # scanning the text using OCR
    # note that the document is a little old so there might be some inaccuracies 
    file = open("dasar_as.txt", "a")
    for i in range(1, counter):
        imagename = "page_" + str(i) + ".jpg"
        text = str(((pytesseract.image_to_string(Image.open(imagename))))) 
        text = text.replace("-\n", "")
        file.write(text) 
    file.close()
    return file

def main():    
    os.chdir(r"filepath")
    inputfile = "dasar_as.pdf"
    scan_pdf(inputfile)

if __name__ == "__main__":
    main()
