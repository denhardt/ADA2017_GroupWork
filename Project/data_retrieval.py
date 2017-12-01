# -*- coding: utf-8 -*-
"""some helper functions.

Those functions help in getting articles stored in xml file.
"""
from lxml import etree
from datetime import datetime

def month_dates(start_date, end_date):
    """
    defines a list of dates in the mm/yyyy format in the range [start_date, end_date]
    """
    f = lambda date: date.month + 12 * date.year

    res = []
    for tot_m in range(f(start_date)-1, f(end_date)):
        y, m = divmod(tot_m, 12)
        res.append(str(y) + '/' + '%02d' % (m+1))
    
    return res
 
def get_date(article):
    """
    This method returns the date of the given article
    in the dd/mm/yyyy format
    """
    str_date = article.find('entity').find('meta').find('issue_date').text
    return datetime.strptime(str_date, '%d/%m/%Y')

def get_articles_in_file(file, start_date, end_date):
    """
    Retrieves all the articles in the file and store them into a list of strings.
    """
    articles = []  
    for article in file.iter('article'):
        if article.find('entity') is not None:
            a = ''
            date = get_date(article)
            if start_date <= date <= end_date:
                for entity in article.iter('entity'):
                    a += entity.findtext('full_text') + ' '
                articles.append(date.strftime('%d/%m/%Y') + ' ' + a)
    return articles

def get_articles(path, start_date, end_date):
    """
    Iterates through the file hierarchy specified by the path and 
    retrieves the articles published between start_date and end_date included
    """
    articles = []
    for m_date in month_dates(start_date, end_date):
        try:
            file = etree.parse(path + m_date + '.xml')
            articles.append(get_articles_in_file(file, start_date, end_date))
        except (FileNotFoundError, IOError):
            pass
    return [a for file in articles for a in file]

def get_entity_text(file, box_id):
    """
    Retrieves the text associated to a box_id in the file.
    An empty list is returned if the box_id is not found
    """
    res = []
    for article in file.iter('article'):
        if article.find('entity') is not None:
            date = get_date(article)
            for entity in article.iter('entity'):
                if   box_id == entity.find('meta').find('box').text:
                    res = date.strftime('%d/%m/%Y') + ' ' + entity.findtext('full_text')
                    break
    return res