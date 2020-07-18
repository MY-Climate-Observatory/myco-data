# -*- coding: utf-8 -*-
"""
18 July 2020
Author: Xiandi Ooi

We will extract the text from the pdf page by page. 
The source link of the pdf can be found in the README.md.

Credits to "Automate the Boring Stuff with Python, automatetheboringstuff.com"

Note: 
This method is suitable only if you are extracting only the text from a text-based pdf.
If your pdf is a scanned document, then you would have to convert the pdf into some image file
and perform OCR on it.

Also, we can't get local issuer certificate when fetching the source using the request library,
so we manually downloaded it to local and run it.

"""
import PyPDF2

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
    return pdf_dict

def main():    
    file_name = r"filepath\Malaysia-Roadmap-Towards-Zero-Single-Use-Plastics-2018-20302.pdf"
    extract_pdf(file_name)

if __name__ == "__main__":
    main()
