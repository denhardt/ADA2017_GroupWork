# -*- coding: utf-8 -*-
"""
some helper functions.
These functions help in getting articles that are stored in xml file.
"""
from lxml import etree
from datetime import datetime

def month_dates(start_date, end_date):
    """
    defines a list of dates in the yyyy/mm format in the range [start_date, end_date]
    Outpus:
        res - a list of strings
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
    Inputs:
        article - an lxml.etree._Element
    Outputs:
        a datetime.datetime object specifying the age of the article
    """
    str_date = article.find('entity').find('meta').find('issue_date').text
    return datetime.strptime(str_date, '%d/%m/%Y')

def get_articles_in_file(file, start_date, end_date):
    """
    Retrieves all the articles in the xml file and store them into a list of strings.

    Inputs:
        file - an lxml.etree._ElementTree object specifying the xml files to be parsed
        start_date - a datetime.datetime object specifying the start date of articles
                     to be parsed
        end_date - a datetime.datetime object specifying the end date of articles
                   to be parsed
    Outputs:
        articles - A list of strings containing the raw text of all articles parsed
    """
    articles = []
    dates = []
    for article in file.iter('article'):
        if article.find('entity') is not None:
            a = ''
            date = get_date(article)
            if start_date <= date <= end_date:
                for entity in article.iter('entity'):
                    a += entity.findtext('full_text') + ' '
                articles.append(date.strftime('%d/%m/%Y') + ' ' + a)
                dates.append(date)
    return articles, dates

def get_articles(path, start_date, end_date):
    """
    Iterates through the file hierarchy specified by the path and
    retrieves the articles published between start_date and end_date included

    Inputs:
        path - path of the files to be parsed, ex: /path/to/files/JDG/
        start_date - a datetime.datetime object specifying the start date of articles
                     to be parsed
        end_date - a datetime.datetime object specifying the end date of articles
                   to be parsed
    Outputs:
        A list of strings containing the raw text of all articles parsed
    """
    articles = []
    dates = []
    for m_date in month_dates(start_date, end_date):
        try:
            file = etree.parse(path + m_date + '.xml')
            article, art_dates = get_articles_in_file(file, start_date, end_date)
            articles = articles + article
            dates = dates + art_dates
        except (FileNotFoundError, IOError):
            pass
    return articles, dates

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
