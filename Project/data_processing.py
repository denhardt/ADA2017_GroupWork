# coding: utf-8

# General packages:
import os
import re
import json
import pandas as pd
from lxml import etree
from datetime import datetime
from dateutil import parser
# NLP tools used:
import fr_core_news_sm
import spacy
import enchant
# from gensim.models import Phrases
# from gensim.models.word2vec import LineSentence
# from gensim.models.ldamulticore import LdaMulticore
# from gensim.corpora import Dictionary, MmCorpus
# import pyLDAvis
# import pyLDAvis.gensim
import warnings
# Helper functions written for various stages of data retrieval, reduction,
# cleaning and processing
from data_retrieval import *
from data_reduction import *
from data_cleaning import *
# from lda_helper import *

def process_data(start_date, end_date, newsp):
    """
    Inputs:
        start_date - a datetime.datetime object specifying the start date of articles
                     to be parsed.
        end_date - a datetime.datetime object specifying the end date of articles
                   to be parsed.
        newsp - list of strings corresponding to folders to be processed
    Example:
        start_date =  datetime(1990, 1, 1)
        end_date = datetime(1990, 1, 31)
        newsp = ['JDG', 'GDL']
    """
    for np in newsp:
        path = '/Users/robin/GIT/ADA/'
        project_path = '/Users/robin/GIT/ADA/ADA2017_GroupWork/Project/'
        articles_path = os.path.join(path, np+'/')
        print('starting parsing')
        # Time consuming
        if 1 == 1:
            corpus, dates = get_articles(articles_path, start_date, end_date)
        print('# of articles parsed:', len(corpus))


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
        print('# of articles after filtering', len(corpus))

        # Time consuming !!

        # For each publication ee keep only words that occupy one of
        # the listed grammatical positions in the sentence
        pos=['VERB', 'PROPN', 'NOUN', 'ADJ', 'ADV']

        # get_ipython().run_line_magic('time', '')
        cleaned = [(date, lemmas) for date, lemmas in clean(corpus, pos)]

        # retrieve dates
        dates = [pair[0] for pair in cleaned]

        # retrieve articles
        corpus = [pair[1] for pair in cleaned]

        print('done cleaning, lemmatizing')
        # In[ ]:
        print('Creating DataFrame')
        df = pd.DataFrame(columns=['date', 'newspaper', 'text'])
        df.text, df.date = corpus, dates
        df.newspaper = np
        df.date = df.date.apply(lambda x: parser.parse(x))
        df.date = df.date.apply(lambda x: datetime.strftime(x, '%Y-%d-%m %H:%M:%S'))
        df.date = df.date.apply(lambda x: parser.parse(x))
        df.set_index('date', inplace=True)
        df.to_csv('df_'+np+'.csv')
        print('DataFrame written to file:'+'df_'+np+'.csv')
        # Selection of articles between dates can be done like so:
        # df.date = df.date.apply(lambda x: parser.parse(x))
        # df.set_index=('date', inplace=True)
        # df[datetime(1851,1,24):datetime(1852,8,22)]

        # Storing the articles we lemmatized before in '.json' file.
        # with open(os.path.join(project_path, json_filename), 'w') as file:
        #     json.dump(corpus, file)
        #
        # print('done corpus to json', json_filename)

        # Loading articles from .json file
        # with open(os.path.join(project_path, json_filename), 'r') as file:
        #     lemmatized_corpus = json.load(file)
