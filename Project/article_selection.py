import numpy as np 

key_word = ['votation','voter','référendum','bernois','populaire','constitution','élection','fédéral','initiative',
'citoyenne','alémanique','cantonale','stipulant','grand conseil','accepté','consultation','jurassien','plébiscite',
'scrutin','suffrage','voix','élection','majorité','socialiste','majoritaire','campagne']

def article_selection(articles,keywords):
    
    articles_votation = []

    for art in articles:
        if any(word in art.split() for word in keywords):
            articles_votation.append(art)
    return articles_votation
