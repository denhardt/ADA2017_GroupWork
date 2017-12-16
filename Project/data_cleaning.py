# -*- coding: utf-8 -*-
"""some helper functions.

Those functions help to clean the data before applying the lda model
"""

import spacy
import enchant
import fr_core_news_sm

nlp = fr_core_news_sm.load()

def punct_space(token):
    """
    helper function to eliminate tokens
    that are pure punctuaiton or whitespace
    """
    
    return token.is_punct or token.is_space


def is_french(word):
    """
    helper function to eliminate tokens that
    are not french words.
    """
    d = enchant.Dict('fr_FR')
    return d.check(word)


def clean(corpus, pos):
    """
    generator function to use spaCy to parse articles,
    lemmatize the text, and yield sentences. Removes all words that aren't
    french, don't occupy one of the grammatical positions in pos, are stopwords,
    digits, punctuation, whitespaces, and are like numbers (spacy's like_num)
    """
    
    for parsed_article in nlp.pipe(corpus, 
                                   batch_size=100, n_threads=5):
        # save the date
        date = parsed_article[0].text
        
        yield (date, ' '.join([token.lemma_ for token in parsed_article if token.pos_ in pos
                and not punct_space(token) and is_french(token.text) and not token.is_stop
                and not token.is_digit and not token.like_num]))
