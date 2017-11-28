import numpy as np 

key_word = ['votation','voter','référendum','bernois','populaire','constitution','élection','fédéral','initiative',
'citoyenne','alémanique','cantonale','stipulant','grand conseil','accepté','consultation','jurassien','plébiscite',
'scrutin','suffrage','voix','élection','majorité','socialiste','majoritaire','campagne']

def article_selection(articles,keywords):
    
    articles_votation = []

    for i in range(len(articles)):
        if any(word in articles[i].split() for word in keywords): 
            articles_votation.append(articles[i])
    return articles_votation            