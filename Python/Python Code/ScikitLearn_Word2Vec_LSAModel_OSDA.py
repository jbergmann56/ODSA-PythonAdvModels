#Goal - Refactor and Improve the Gensim Word2Vec LSI NLP model using Scikit-learn, adhering to the CRISP-DM Process

#LSI Overview: LSA is technique in natural language processing of analyzing relationships between a set of documents 
#and the terms they contain by producing a set of concepts related to the documents and terms. 
#i.e. LSA assumes that words that are close in meaning will occur in similar pieces of text 

#global variable that work as model parameters - adjust for model performance "fine-tuning"
n_samples = 2000 #sample size
n_features = 1000 #name/entity recgonition & group selection (vectors)
n_components = 5 #themes
n_top_words = 10 #words per theme

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
#data pre-processing tools from gensim package
from gensim.parsing.preprocessing import strip_non_alphanum 
from gensim.parsing.preprocessing import strip_numeric
from gensim.parsing.preprocessing import strip_punctuation
from gensim.parsing.preprocessing import strip_multiple_whitespaces
from gensim.parsing.preprocessing import strip_short
#import scikit-learn & graphical libraries
# Any results you write to the current directory are saved as output.
from sklearn import preprocessing #data prep - module includes scaling, centering, normalization, binarization and imputation methods.
from sklearn.feature_extraction import text #used for removing stop words and obtaining feature extraction from text
import matplotlib.pyplot as plt
import seaborn as sns #Seaborn is a Python data visualization library based on matplotlib. 
sns.set(style="white") #white background style for seaborn plots
sns.set(style="whitegrid", color_codes=True)

#import sklearn libraries to NLP model bilding & validation
from sklearn.metrics import accuracy_score  #used for model evaluation - https://scikit-learn.org/stable/modules/model_evaluation.html#model-evaluation
from sklearn.feature_extraction.text import CountVectorizer  #bag-of-words vectorication for LDA model
from sklearn.decomposition import LatentDirichletAllocation #model for NLP topic extraction, similar to gensim LDA
from sklearn.datasets import make_multilabel_classification #create random test dataset
from sklearn.model_selection import train_test_split

#CRISP-DM Task: Data Preparation 
#import favorite text-based dataset for analysis using pandas dataframe - compatible w/scikit-learn
def read_text(path):
    print("Pandas File I/O Example - csv read")
    text=pd.read_csv(path) #import to pandas DataFrame
    return text #return pandas dataframe type

#preprocess data for use in text mining/NLP - refactored for pandas dataframe
def preprocess_text(corpus,field_name = 'Comment'):
    print("Preprocessing Corpus from pandas data frame")
    for index, row in corpus.iterrows():  #iterate through rows in dataframe
        line = row['Comment'].strip('\n')
        line = strip_punctuation(line)
        line = strip_non_alphanum(line)
        line = strip_numeric(line)
        line = strip_multiple_whitespaces(line)
        line = strip_short(line)
        #add cleaned text line to new dataframe
        corpus.at[index,field_name] = line #set value at row/column in corpus dataframet            
    return corpus

print('CRISP-DM Task: Data Preparation')
print('Task 1: Read-in a text-based document, aka "establishing the corpus')
documents = read_text(r"C:\\Python\\Data\\Text_Mining_Sample_CSV.csv") #single-line text
#print(documents.head())

print('Task 2: Preprocessing dataset, including stoplist, word frequencies & filters')
print('Task 2a: Remove punctuation, non-alphanumeric and numeric characters')
raw_corpus = preprocess_text(documents,field_name = 'Comment')

print('Task 2b: remove english stopwords and add additional to remove from text document')
#set stopword list - see here for set of english "stop words": https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/feature_extraction/stop_words.py
#scikit-learn uses a stoplist "frozenset" - immutable python set" - to add additional stopwords, neded to union additional set  
stop_words = text.ENGLISH_STOP_WORDS.union({"have", "with", "are", "JBergmann"})
#print(stop_words)

print('Task 2b: create a BOW vector for Latent-Dirichlet-Allocation (LDA) Model, using assigned stop words')
#Convert a collection of text documents to a matrix of token counts - "bag-of-words", unless otherwise specified
bow_vector = CountVectorizer(stop_words=stop_words)
#"Comment" column is the 6th column in the dataset - index "5" in dataframe
value_list = [row[5] for row in raw_corpus.itertuples(index=False, name=None)]
#print(value_list[0:3])
#create term-document matrix and and place all relevant terms in vocabulary/dictionary
bow = bow_vector.fit_transform(value_list)
#dictionary stored in the vocabulary_ variable of the bow object 
#print(bow_vector.vocabulary_)

print('CRISP-DM Task: Data Understanding')
print('Task 1: print information about bow verctor and/or corpus')
print(bow_vector.vocabulary_.get('atm')) #get dictionary index of "get" keyword
counts = np.asarray(bow.sum(axis=0)) 
count_words = counts[0]
freq = count_words[109] #get word count of all terms in dictionary, using retured "get" word id - ex atm = 109
print(freq) #print frequency

print('Task 2: use pandas and data viz libraries to explore & understand the columns and values in the text dataset')
print(documents.head())  #get first 5 observations in pandas dataframe
# Check data types for each variable
print(documents.info())
#assess data quailty - null values 
print(documents.isnull().sum())
#describe dataset values 
print(documents.describe())
#view histograp of categorical variables 
#summarize & plot pandas column using "groupby" function
summary = documents.groupby(['Comment Type'])["ID"].count().reset_index(name="count")
print(summary)
y = summary['count']
x = summary['Comment Type']   #iterate list to transfor dates for graphical use
data = pd.DataFrame({'Freq':y, 'Comment Type':x}).set_index(x) 
data.plot(kind='bar')
#plt.show()  #uncomment to show - otherwise holds execution until closed

print('CRISP-DM Task: Model Building')
print("Fitting LDA models with tf features, "
      "n_samples=%d and n_features=%d..."
      % (n_samples, n_features))
lda = LatentDirichletAllocation(n_components=n_components, max_iter=5,
                                learning_method='online',
                                learning_offset=50.,
                                random_state=0)
lda.fit(bow)
print("\nTopics in LDA model:")
bow_feature_names = bow_vector.get_feature_names()

def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()

print_top_words(lda, bow_feature_names, n_top_words)

print('CRISP-DM Task: Model Evaluation')
print('Step 1: get test topics then score them vs. current LDA model')
train, test = train_test_split(list(documents['Comment'].values), test_size = 0.2)
test_vector = bow_vector.fit_transform(test)
test_lda = lda.fit(test_vector)  #fit text vector within existing model - transpose to work
#Calculate approximate log-likelihood as score.
print(test_lda.score(test_vector))

print('Step 2: Use formal model evaluation stats "perplexity") 
# create test/train text documents to evaluate model 
vectoriser = CountVectorizer(stop_words = 'english', max_features=500)  #max features must be less that "n_features" variable!
doc_train = vectoriser.fit_transform(train)
features = vectoriser.get_feature_names()
doc_test = vectoriser.fit_transform(test)
news_lda = lda.fit(doc_train)
print(news_lda.perplexity(doc_test)) # lower the perplexity, the better

print('Task 3: Compare vs. Gensim word2vec topic output')
#class exercise - what is the difference? 

print('CRISP-DM Task: Model Deployment')
#gensim contains ablility to save and update models with future iterations
#lecture is TBD