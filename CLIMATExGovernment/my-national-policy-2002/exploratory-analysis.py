# -*- coding: utf-8 -*-
"""
6 Nov 2020
Author: Xiandi Ooi

This script is for performing exploratory analysis on the data, focusing on:
    1. number of words
    2. most common words via word clouds
This analysis is similar to the one we performed on the Malaysia Roadmap towards Zero Single-Use Plastic.

The following code is modified from the following source:
    Title: 2-Exploratory-Data-Analysis, NLP in Python Tutorial
    Author: Alice Zhao
    Date: 2018
    Availability: https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/2-Exploratory-Data-Analysis.ipynb
"""
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt 
import os

os.chdir(r"filepath")

# NUMBER OF ENGLISH WORDS
# load the document-term matrix
dtm = pd.read_pickle("das-dtm.pkl")
dtm = dtm.transpose()

# filter the document-term matrix to contain only non-zero items
freq = []
for pages in dtm.columns:
    words = dtm[pages].to_numpy().nonzero()[0].size
    freq.append(words)
# plot the graph
wordfreq = pd.Series(freq)
wordfreq.plot(kind="bar", title = "English Word Frequency for Dasar Alam Sekitar", 
              xlabel = "Page", ylabel = "Word Frequency")

# WORD CLOUD 
corpus = pd.read_pickle("das-en-corpus.pkl")
# select the pages that have substantial content
pages = []
for i in range(len(freq)):
    # here we assume that pages with more than one paragraph of English is worth looking into
    if freq[i] >= 120:
        pages.append(i)

# create the template for the word cloud object
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ="white", 
                min_font_size = 10, 
                max_font_size = 150,
                random_state=1)

# plot the word cloud
plt.rcParams["figure.figsize"] = [16, 16]
plt.subplots_adjust(hspace=0.2, wspace=0.2)
for index in range(len(pages)):
    page = pages[index]
    wordcloud.generate(corpus.page_content[page])
    
    plt.subplot(4,4,index+1)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Page {}".format(page))
# the results showed that we might have to clean the corpus again to remove the remaining stopwords and malay words

