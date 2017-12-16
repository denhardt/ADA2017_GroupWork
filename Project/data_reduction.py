# -*- coding: utf-8 -*-
"""some helper functions.

Those functions help to reduce the corpus and documents size
"""
import re

def filter_articles(corpus, keywords=['votation']):
    """
    Selects articles in the corpus that contain
    at least one of the keywords.
    """
    votations = []
    for article in corpus:
        if any(word in article for word in keywords): 
            votations.append(article)
    return votations

def summarize_articles(corpus, keywords=['votation'], delimiter='.'):
    """
    For each publication retains only sentences 
    containing at least one of the keywords 
    together with its closest neighboors, namely
    the preceding and following sentences. 
    
    Any sequence of character between the delimiter
    is considered a sentence. 
    """
    new_corpus = []
    for article in corpus:
        date = re.findall(r'^([^\s]+)', article)[0]

        sent = ''
        phrases = article.split(delimiter)
        for i, phrase in enumerate(phrases):
            if any(keyword in phrase for keyword in keywords):
                if len(phrases) < 2:
                    sent += phrase
                elif i == 0:
                    sent += phrase[phrase.index(' ') + 1:] + ' '  + phrases[i+1]
                elif i == len(phrases) - 1:
                    sent += ' ' + phrases[i-1] + ' ' + phrase
                elif 0 < i < len(phrases) - 1:
                    sent += ' ' + phrases[i-1] + ' ' + phrase + ' ' + phrases[i+1]
        new_corpus.append(date + ' ' + sent)

    return new_corpus
