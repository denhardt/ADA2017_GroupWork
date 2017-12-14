# coding: utf-8

# need to specify the following params before running:
    # start_date =  datetime(1990, 1, 1)
    # end_date = datetime(1990, 1, 31)
    # json_filename = 'test2.json'

import os
import re
import json
import spacy
import enchant
import pandas as pd
import fr_core_news_sm

from lxml import etree
from datetime import datetime

from gensim.models import Phrases
from gensim.models.word2vec import LineSentence
from gensim.models.ldamulticore import LdaMulticore
from gensim.corpora import Dictionary, MmCorpus

import pyLDAvis
import pyLDAvis.gensim
import warnings
#import cPickle as pickle

from data_retrieval import *
from data_reduction import *
from data_cleaning import *
from lda_helper import *

path = '/Users/robin/GIT/ADA/'
project_path = '/Users/robin/GIT/ADA/ADA2017_GroupWork/Project/'
articles_path = os.path.join(path, 'JDG/')

# Time consuming
if 1 == 1:
    corpus = get_articles(articles_path, start_date, end_date)

# defines keywords that should be contained in articles
# to consider them votations
# keywords = ['votation']
# todo: check if notebook file .ipynb encoded in UTF
keywords = ['votation','voter','référendum',' élection','Élection','initiative populaire',
            # careful with 'élection': includes all articles with sélection
            # adding a space fixes this: ' élection'
            'grand conseil','plébiscite','scrutin','suffrage']
# todo: add removing of keywords from articles
# get articles related to votations
corpus = filter_articles(corpus, keywords)

# summarize articles about votations
corpus = summarize_articles(corpus, keywords)


# Time consuming !!

# For each publication ee keep only words that occupy one of
# the listed grammatical positions in the sentence
pos=['VERB', 'PROPN', 'NOUN', 'ADJ', 'ADV']
if 1 == 1:
    get_ipython().run_line_magic('time', '')
    cleaned = [(date, lemmas) for date, lemmas in clean(corpus, pos)]

    # retrieve dates
    dates = [pair[0] for pair in cleaned]

    # retrieve articles
    corpus = [pair[1] for pair in cleaned]


# In[ ]:

# Storing the articles we lemmatized before in '.json' file.
with open(os.path.join(project_path, json_filename), 'w') as file:
    json.dump(corpus, file)


# In[ ]:


# Loading articles from .json file
# with open(os.path.join(project_path, json_filename), 'r') as file:
#     lemmatized_corpus = json.load(file)
