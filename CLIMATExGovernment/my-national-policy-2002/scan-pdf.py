# -*- coding: utf-8 -*-
"""
2 Nov 2020
Author: Xiandi Ooi

We will convert the pdf into image page by page. 
The source link of the pdf can be found in the README.md.

"""
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import os
import pandas as pd
import re
import string

def scan_pdf(inputfile):
    """
    inputfile: the pdf document
    output: the cleaned corpus
    
    This function takes the given pdf file, extracts the image from each page,
    scan the words and output it as a corpus after performing a preliminary 
    text cleaning process.
    """
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
    pdf_dict = {}
    for i in range(1, counter):
        imagename = "page_" + str(i) + ".jpg"
        text = str(((pytesseract.image_to_string(Image.open(imagename))))) 
        text = text.replace("-\n", "")
        file.write(text)
        pdf_dict[i] = text
    
    # finalize the outputs
    file.close()
    
    # transform the dictionary into pandas dataframe
    data = pd.DataFrame.from_dict(pdf_dict, orient = "index")
    data.columns = ["page_content"] 
    
    # clean the data
    data_clean = pd.DataFrame(data.page_content.apply(lambda x:clean(x)))
    
    # save the text objects aside
    data_clean.to_pickle("das-corpus.pkl")
    
    # export the dataframe 
    data_clean.to_csv("DAS-corpus.csv")
    
    return data_clean

def clean(text):
    """
    text: a string object
    output: the cleaned string object
    
    The function performs basic text cleaning operations including making text
    lower case, removing non-sensical text, removing puctuation, and
    removing words containing numbers.
    """
    """
    The data cleaning process is modified from the following source:
        Title: 1-Data-Cleaning, NLP in Python Tutorial
        Author: Alice Zhao
        Date: 2018
        Availability: https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/1-Data-Cleaning.ipynb
    """    
    text = text.lower()
    text = re.sub("\n", "", text)
    text = re.sub("\[.*?\]", " ", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = re.sub("[‘’“”…ł]", " ", text)
    text = re.sub("[˜˚˛˝˙œ™]", "", text)
    return text

def main():    
    os.chdir(r"C:\Users\Xiandi\Desktop\Python")
    inputfile = "dasar_as.pdf"
    scan_pdf(inputfile)

if __name__ == "__main__":
    main()
