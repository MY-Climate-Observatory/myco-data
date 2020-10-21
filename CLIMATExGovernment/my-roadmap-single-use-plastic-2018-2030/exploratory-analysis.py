# -*- coding: utf-8 -*-
"""
21 Oct 2020
Author: Xiandi Ooi

This script is for performing exploratory analysis on the data, focusing on:
    1. most common words via word clouds
    2. number of words

The following code is modified from the following source:
    Title: 2-Exploratory-Data-Analysis, NLP in Python Tutorial
    Author: Alice Zhao
    Date: 2018
    Availability: https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/2-Exploratory-Data-Analysis.ipynb
"""
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt 

# loading the document-term matrix after cleaning
dtm = pd.read_pickle("dtm.pkl")
dtm = dtm.transpose()

# creating a dictionary of most common words in each page
common = {}
for page in dtm.columns:
    top = dtm[page].sort_values(ascending=False).head(10)
    common[page]= list(zip(top.index, top.values))
common_df = pd.DataFrame.from_dict(common, orient = "index")
# the good thing about policy papers is that the language is quite clean, no additional cleaning is necessary

# pages 0, 3, 7, 8, 9, 11, 13 has very little wordings, so we will not dive into much of it
pages = [1,2,4,5,6,10,12,14,15]

# WORD CLOUD
# loading the corpus for word cloud plotting
corpus = pd.read_pickle("data_clean.pkl")

# create the template for the word cloud object
wordcloud = WordCloud(width = 800, height = 800, 
                background_color ="white", 
                min_font_size = 10, 
                max_font_size = 150,
                random_state=1)

# plot the word cloud
plt.rcParams["figure.figsize"] = [6, 6]
plt.subplots_adjust(hspace=0.2, wspace=0.2)
for index in range(len(pages)):
    page = pages[index]
    wordcloud.generate(corpus.page_content[page])
    
    plt.subplot(3,3,index+1)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Page {}".format(page))
    
plt.show()
# since it is a policy paper, its vocabularies are mainly scientific, but words that implies shared values are also used to emphasize citizen participation.

# NUMBER OF WORDS  
# filter the document-term matrix to contain only non-zero items
freq = []
for pages in dtm.columns:
    words = dtm[pages].to_numpy().nonzero()[0].size
    freq.append(words)

wordfreq = pd.Series(freq)

wordfreq.plot(kind="bar", title = "Word Frequency for Malaysia Roadmap towards Zero Single-Use Plastic", 
              xlabel = "Page", ylabel = "Word Frequency")
