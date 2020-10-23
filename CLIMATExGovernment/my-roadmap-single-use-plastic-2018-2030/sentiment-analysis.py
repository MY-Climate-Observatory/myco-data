# -*- coding: utf-8 -*-
"""
23 Oct 2020
Author: Xiandi Ooi

This script is for performing sentiment analysis on the data.

The following code is modified from the following source:
    Title: 3-Sentiment-Analysis, NLP in Python Tutorial
    Author: Alice Zhao
    Date: 2018
    Availability: https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/3-Sentiment-Analysis.ipynb
"""
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

corpus = pd.read_pickle("data_clean.pkl")

pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

corpus["polarity"] = corpus["page_content"].apply(pol)
corpus["subjectivity"] = corpus["page_content"].apply(sub)

fig, ax = plt.subplots()
ax.plot(corpus.index, corpus["polarity"])
ax.plot(corpus.index, corpus["subjectivity"])
ax.set_title("Sentiment Analysis")
ax.legend(["Polartiy","Subjectivity"])
ax.xaxis.set_label_text("Pages")
ax.yaxis.set_label_text("Polarity and Subjectivity")
plt.show()

# Polarity: How positive or negative a word is. -1 is very negative. +1 is very positive.
# Subjectivity: How subjective, or opinionated a word is. 0 is fact. +1 is very much an opinion.

# The results are quite surprising since the document is predicted to be mostly negative and somewhat opinionated.
# Subjectivity: We see that as a policy paper it is somewhat opinionated, but it is overall positive in tone.
# Polartiy: We see that some times the paper is a little negative, but overall the tone is centered around zero.
# The main problem with our challenge here is that our data size is very small, so the predicted values is very likely to be inaccurate.
