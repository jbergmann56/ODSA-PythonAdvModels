#Gensim Docs: http://pandas.pydata.org/pandas-docs/stable/
#Description: https://en.wikipedia.org/wiki/Word2vec
#Tutorials/Code Example:  https://github.com/RaRe-Technologies/gensim/blob/develop/gensim%20Quick%20Start.ipynb
#Library Purpose: Gensim Word2vec is a two-layer neural net that dataprocesses text.
#Its input is a text corpus and its output is a set of vectors: feature vectors for words in that corpus
#it can be applied just as well to genes, code, likes, playlists, social media graphs and 
#other verbal or symbolic series in which patterns may be discerned.

import os
import tempfile
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))
"""Basic word2vec example."""
import numpy as np
import pandas as pd
import gensim #open-source achine learning framework
from gensim import corpora
from gensim import models
from gensim.parsing.preprocessing import strip_non_alphanum
from gensim.parsing.preprocessing import strip_numeric
import pickle

'''#import favorite text dataset for analysis
def file_read_csv(path,txt_column=[]):
    print("Pickle File I/O Example - text Read")
    myfile = open(path, "r")
    text = myfile.read()
    text = strip_non_alphanum(text)
    text = strip_numeric(text)
    return [text]

print('Task 1: Read-in a text-based document, aka "establishing the corpus')
documents = file_read_csv(r"C:\\Python\\Data\\Text8") #single-line text
'''

#use text example from genism website
raw_corpus = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",              
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

print('Task 2: Preprocessing dataset, including stoplist, word frequencies & filters')
stoplist = set('for a of the and to in'.split())
print('Task 2a: Lowercase each document')
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in raw_corpus]

print('Task 2b:  create a list list of non-distinct parsed words from doc') 
# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

print('Task 2c: Only keep words that appear more than once')
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
#long list of distinct words

print('Task 2d: Create dictionary/term-document matrix')
#associate each word in the processed corpus with a unique integer ID, using the gensim.corpora.Dictionary class. 
#This dictionary defines the vocabulary of all words that our processing knows about.
dictionary = corpora.Dictionary(processed_corpus)
print(dictionary)

print('Task 3:  Extract Knowledge by vectorizing corpus, then applying NLP methodology')
# create a "new" test document as a plain Python list, then vectorize into a "bag of words"
new_doc = "system minors"
new_vec = dictionary.doc2bow(new_doc.lower().split())
#Note that this vector only contains entries for words that actually appeared in the document. 

#To infer the latent structure in our training corpus we need a way to represent documents
#that we can manipulate mathematically. One approach is to represent each document as a vector. 
print('Task 3a: convert training document into id-driven vectors, using dictionary data structure')
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

print('Task 3b: Apply NLP model to vector space')
#The tf-idf model transforms vectors from the bag-of-words representation to a vector space,
#where the frequency counts are weighted according to the relative rarity of each word in the corpus.
tfidf = models.TfidfModel(bow_corpus) #initalize & train model on vectorized data
tfidf2 = tfidf[new_vec] #use tf-idf "trained" model to transform the "new" document vector
print(tfidf2)

#Calling model[corpus] only creates a wrapper around the old corpus document stream
#need to apply model/transformation to uncover topic insights - Here we transformed our Tf-Idf corpus
#via Latent Semantic Indexing into a latent 2-D space
print('Task 3d: apply word2vec transformation algorithom to vectors, then output resulting topics')
#lsi = models.LsiModel(tfidf2, id2word=dictionary) # initialize an LSI transformation
#corpus_lsi = lsi[tfidf2] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
#lsi.print_topics(3)