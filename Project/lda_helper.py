# -*- coding: utf-8 -*-
"""some helper functions.

Those functions help to prepare and analyse the lda model
"""
from gensim.models.ldamulticore import LdaMulticore
from gensim.corpora import Dictionary, MmCorpus

def bow_generator(corpus, dico):
    """
    generator function to construct the
    bag-of-words matrix.
    """
    for article in corpus:
        yield dico.doc2bow(article.split())
        
def explore_topic(lda, topic_number, topn=10):
    """
    accept a user-supplied topic number and
    print out a formatted list of the top terms
    """
    
    print(u'{:20} {}'.format(u'term', u'frequency') + u'\n')
    
    for term, frequency in lda.show_topic(topic_number, topn):
        print(u'{:20} {:.3f}'.format(term, round(frequency, 3)))
        
def articles_from_topic(lda, bow_corpus, corpus, topic):
    """
    return the list of articles associated
    with a given topic.
    """
    assert len(bow_corpus) == len(corpus)
    nb_topics = lda.num_topics

    documents = []
    if 0 <= topic < nb_topics:
        k = 0
        for bow_article in bow_corpus:
            dist = lda.get_document_topics(bow_article, minimum_probability=0)
            dist = [p[1] for p in dist]
            idx_max = dist.index(max(dist)) # what?! this isn't the ID of the topic
            # the id of the topic was the fist value of each tuple in dist (cf
            # documentation get_document_topics() ), which has been discarded
            # on line 41
            if idx_max == topic:
                documents.append(corpus[k])
            k += 1
    return documents
