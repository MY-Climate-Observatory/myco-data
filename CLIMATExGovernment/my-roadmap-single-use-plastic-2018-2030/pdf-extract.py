# -*- coding: utf-8 -*-
"""
16 Oct 2020
Author: Xiandi Ooi

We will extract the text from the pdf page by page. 
The source link of the pdf can be found in the README.md.

Credits to automatetheboringstuff.com and Alice Zhao from https://github.com/adashofdata/nlp-in-python-tutorial

Note: 
This method is suitable only if you are extracting only the text from a text-based pdf.
If your pdf is a scanned document, then you would have to convert the pdf into some image file
and perform OCR on it.

Also, we can't get local issuer certificate when fetching the source using the request library,
so we manually downloaded it to local and run it.

"""
import PyPDF2
import pandas as pd
import re
import string
from sklearn.feature_extraction.text import CountVectorizer
import pickle

# Read the pdf from its source
def extract_pdf(file_name):
    """
    file_name: the downloaded pdf file of the Roadmap
    output: a dictionary of the extracted text organized by page
    
    This function takes the given pdf file and extract the text from each page then store it in the 
    form of dictionary.
    
    """
    # Read the pdf file
    pdf_object = open(file_name, "rb")
    read_pdf = PyPDF2.PdfFileReader(pdf_object)
    
    pdf_dict = {}
    
    # Iterate across each page and extract the text file, organized by page
    for i in range(read_pdf.numPages):
        pdf_page = read_pdf.getPage(i)
        pdf_dict[i] = pdf_page.extractText()
    # now we have a dictionary of page number: one large chunk of text in a list
    
    # transform the dictionary into pandas dataframe
    data = pd.DataFrame.from_dict(pdf_dict, orient = "index")
    data.columns = ["page_content"]     
    
    # clean the data
    data_clean = pd.DataFrame(data.page_content.apply(lambda x:clean(x)))
    # we now have a corpus for the whole roadmap
    
    # transforming the corpus into a document-term matrix
    cv = CountVectorizer(stop_words="english")
    data_cv = cv.fit_transform(data_clean.page_content)
    dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
    dtm.index = data_clean.index  
    
    # save the text objects aside
    dtm.to_pickle("dtm.pkl")
    data_clean.to_pickle("data_clean.pkl")
    pickle.dump(cv, open("cv.pkl", "wb"))
    return dtm
    
def clean(text):
    text = text.lower()
    text = re.sub("\n", "", text)
    text = re.sub("\[.*?\]", " ", text)
    text = re.sub("[%s]" % re.escape(string.punctuation), "", text)
    text = re.sub("\w*\d\w*", "", text)
    text = re.sub("[‘’“”…]", " ", text)
    text = re.sub("[˜˚˛˝˙œł]", " ", text)
    return text

def main():    
    file_name = r"C:\Users\Xiandi\Desktop\Python\Malaysia-Roadmap-Towards-Zero-Single-Use-Plastics-2018-20302.pdf"
    extract_pdf(file_name)

if __name__ == "__main__":
    main()
