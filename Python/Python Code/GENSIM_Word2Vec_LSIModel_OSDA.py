#Goal - Implement and Evaluate the LSI NLP model, using the CRISP-DM Process

#LSI Overview: LSI is technique in natural language processing of analyzing relationships between a set of documents 
#and the terms they contain by producing a set of concepts related to the documents and terms. 
#i.e. LSA assumes that words that are close in meaning will occur in similar pieces of text 

#import libraries for data structures and Gensim Word2Vec API
import os
import tempfile
TEMP_FOLDER = tempfile.gettempdir()
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))
import numpy as np
import pandas as pd
import gensim #open-source achine learning framework
from gensim import corpora
from gensim import models
from gensim.parsing.preprocessing import strip_non_alphanum 
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_punctuation

#CRISP-DM Task: Data Preparation 
#import favorite text dataset for analysis 
def read_text(path):
    print("Python File I/O Example - text Read")
    with open(path, "r") as f:
    	line = f.readlines()
    return line

#preprocess data for use in text mining/NLP
def preprocess_text(corpus=[]):
    print("Preprocessing Corpus from list data structure")
    for i, val in enumerate(corpus):  #iterate through list
	    corpus[i] = corpus[i].strip('\n')
	    corpus[i] = strip_punctuation(corpus[i])
	    corpus[i] = strip_non_alphanum(corpus[i])
	    corpus[i] = strip_numeric(corpus[i])
    return corpus

print('CRISP-DM Task: Data Understanding')
#place vord2vec functions here:  https://rare-technologies.com/word2vec-tutorial/

print('CRISP-DM Task: Data Preparation')
print('Task 1: Read-in a text-based document, aka "establishing the corpus')
documents = read_text(r"C:\\Python\\Data\\Text8") #single-line text
#documents = read_text(r"C:\\Python\\Data\\text_mining_sample") #single-line text

print('Task 2: Preprocessing dataset, including stoplist, word frequencies & filters')
print('Task 2a: Remove punctuation, non-alphanumeric and numeric characters')
raw_corpus = preprocess_text(documents)

print('Task 2b: Remove words in stoplist and Lowercase each document')
#stoplist = set('for a of the and to in i they it my me that have with are was is t s ve he re is'.split())
stoplist = set('for a of the and to in i they it my me that have with are was'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in raw_corpus]

print('Task 2c: create a list list of non-distinct parsed words from doc') 
# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

print('Task 2d: Only keep words that appear more than once')
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
#print(processed_corpus) #long list of distinct words

print('Task 3: Transform Data - Create dictionary/term-document matrix')
#associate each word in the processed corpus with a unique integer ID, using the gensim.corpora.Dictionary class. 
#This dictionary defines the vocabulary of all words that our processing knows about.
dictionary = corpora.Dictionary(processed_corpus)
print(dictionary.token2id)

print('CRISP-DM Task: Model Building')
#To infer the latent structure in our training corpus we need a way to represent documents
#that we can manipulate mathematically. One approach is to represent each document as a vector. 
print('Task 1: convert training document by vectorizing processed corpus into "bag-of-words" vectors,' 
	  + 'using dictionary data structure')
bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]

print('Task 2: Train Model by Applying NLP methodology to vectorized "bag of words" corpus')
#LSI is being used in a variety of information retrieval and text processing applications, 
#although its primary application has been for concept searching and automated document categorization
modelLsi = models.LsiModel(bow_corpus, id2word=dictionary, num_topics=10) #initalize & train model on vectorized data
print('output Lsi Training Model')
#Cosine measure returns similarities in the range <-1, 1> (the greater, the more similar).
print(modelLsi.print_topics(-1))

print('CRISP-DM Task: Model Evaluation')
#key for text analytics is interpretability - does it make sense?  
print('Task 1: Test model by creating a topic via a Python list of keywords, then vectorize into a "bag of words" vector')
new_doc = "human computer interaction"
#new_doc = "branch bank service"
print('Test Theme: ' + new_doc)
new_vec = dictionary.doc2bow(new_doc.lower().split())
#Calling modelLsi[new_vec] creates a wrapper around the old corpus document stream
modelLsi_test = modelLsi[new_vec] #use "testing" data to transform the "new" document vector
print(modelLsi_test) #if model isn't high quality, continue to iterate

print('Task 2: formal tests of model accuracy')
#include if find

print('CRISP-DM Task: Model Deployment')
#gensim contains ablility to save and update models with future iterations
#lecture is TBD