"""Basic word2vec example."""
import numpy as np
import pandas as pd
import gensim #open-source achine learning framework
from gensim import corpora
from gensim import models
from gensim.parsing.preprocessing import strip_non_alphanum
from gensim.parsing.preprocessing import strip_numeric
import pickle

#import favorite text dataset for analysis
import pickle
def file_read_csv(path,txt_column=[]):
    print("Pickle File I/O Example - text Read")
    myfile = open(path, "r")
    text = myfile.read()
    text = strip_non_alphanum(text)
    text = strip_numeric(text)
    return [text]

print('Task 1: Read-in a text-based document, aka "establishing the corpus')
documents = file_read_csv(r"C:\\Python\\Data\\Text8") #single-line text

print('Task 2a: Preprocessing dataset, including stoplist, word frequencies & filters')
stoplist = set('for a of the and to in'.split())
# Lowercase each document, split it by white space and filter out stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]
print(texts)

import os
try:
    user_paths = os.environ['PYTHONPATH'].split(os.pathsep)
except KeyError:
    user_paths = []