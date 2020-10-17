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
    output: dataframes of corpus and document-term matrix
    
    This function takes the given pdf file, extracts the text from each page,
    and organizes them into word corpus and document-term matrix.    
    """
    
    """
    The pdf extraction code is modified from the following source:
        Title: Chapter 15 Working with PDF and Word Documents, Automate the Boring Stuff with Python 
        Author: Al Sweigart
        Date: 2015
        Availability: https://automatetheboringstuff.com/2e/chapter15/
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
    
    """
    The data cleaning process is modified from the following source:
        Title: 1-Data-Cleaning, NLP in Python Tutorial
        Author: Alice Zhao
        Date: 2018
        Availability: https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/1-Data-Cleaning.ipynb
    """
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
    file_name = r"filepath\Malaysia-Roadmap-Towards-Zero-Single-Use-Plastics-2018-20302.pdf"
    extract_pdf(file_name)

if __name__ == "__main__":
    main()
