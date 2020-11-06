# -*- coding: utf-8 -*-
"""
3 Nov 2020
Author: Xiandi Ooi

The Dasar Alam Sekitar is a bilingual document so further data cleaning proces
is necessary before we can start analysing the document.
"""
import nltk
import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
from sklearn.feature_extraction import text 
import pickle

def clean_dtm(corpus):
    """
    file: the corpus pandas dataframe
    output: the cleaned document-term matrix
    
    This function takes the given pdf file, extracts the image from each page,
    scan the words and output it as a corpus after performing a preliminary 
    text cleaning process.
    """
    # remove non-english words
    nltk.download("words")
    words = set(nltk.corpus.words.words())
    
    corpus_en = {}
    for i in range(1, 30):
        text_in = corpus["page_content"][i]
        text_out = " ".join(w for w in nltk.wordpunct_tokenize(text_in) if w.lower() in words or not w.isalpha())
        corpus_en[i] = text_out
    
    corpus_en_pd = pd.DataFrame.from_dict(corpus_en, orient = "index")
    corpus_en_pd.columns = ["page_content"] 
    
    """
    The following code is modified from the following source:
    Title: 2-Exploratory-Data-Analysis, NLP in Python Tutorial
    Author: Alice Zhao
    Date: 2018
    Availability: https://github.com/adashofdata/nlp-in-python-tutorial/blob/master/2-Exploratory-Data-Analysis.ipynb
    """
    # remove common stopwords
    cv = CountVectorizer(stop_words="english")
    data_cv = cv.fit_transform(corpus_en_pd.page_content)
    dtm = pd.DataFrame(data_cv.toarray(), columns=cv.get_feature_names())
    dtm.index = corpus_en_pd.index 
    dtm = dtm.transpose()
    
    # find the top 15 words in each page
    common = {}
    for pages in dtm.columns:
        top = dtm[pages].sort_values(ascending=False).head(15)
        common[pages]= list(zip(top.index, top.values))
    
    # pull out the top 15 words in each page
    words = []
    for pages in dtm.columns:
        top = [word for (word, count) in common[pages]]
        for t in top:
            words.append(t)
    
    # check the common words mannually because 
    # 1. the document has other malay words that we wish to remove for our analysis
    # 2. policy documents have little stop words and high-freq words may not be stop words
    most_common_words = Counter(words).most_common()
    
    new_stopwords = ["dan", "yang", "di", "serta", "shall", "environ", "baru", "surat", "strategi", "ay", "kos", "program", "la", "bandar", "da", "sam",
                  "ant", "masa", "gan", "aa", "sla", "sitar", "billy", "ta", "bahan", "mana", "massa", "badan", "ser", "dari", "stich", "en", "tera"]
    
    # create document-term matrix using the new stop words list
    stop_words = text.ENGLISH_STOP_WORDS.union(new_stopwords)
    cv2 = CountVectorizer(stop_words=stop_words)
    data_cv2 = cv2.fit_transform(corpus_en_pd.page_content)
    dtm_clean = pd.DataFrame(data_cv2.toarray(), columns=cv2.get_feature_names())
    dtm_clean.index = corpus_en_pd.index
    
    # output
    pickle.dump(cv2, open("cv_clean.pkl", "wb"))
    dtm_clean.to_pickle("das-dtm.pkl")
    corpus_en_pd.to_pickle("das-en-corpus.pkl")

def main():    
    os.chdir(r"filepath")
    corpus = pd.read_pickle("das-corpus.pkl")
    clean_dtm(corpus)

if __name__ == "__main__":
    main()
