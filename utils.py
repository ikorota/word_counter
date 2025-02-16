import requests
from bs4 import BeautifulSoup as bs
import re
import logging


def get_article(title):
    ''' Function for fetching wiki article '''
    logging.info(f'Requesting {title}')
    try:
        response = requests.get(
            'https://en.wikipedia.org/w/api.php',
            params={
                'action': 'parse',
                'page': title,
                'format': 'json',
            }
        ).json()
    except Exception as err:
        logging.info('Request was not successful')
        logging.info(err)
    raw_html = response['parse']['text']['*']
    return raw_html


def analyze_article(title, depth, analyzed_articles, word_counter):
    ''' Function for analyzing html document. It extracts <p> tags and words within them. It also extracts <a> tags 
        within p tags and gets titles of referenced articles'''
    logging.info(f'Analyzing article {title}')
    logging.info(f'Current depth is {depth}')
    if (depth < 0 or title in analyzed_articles):
        return
    raw_html = get_article(title)
    soup = bs(raw_html, "html.parser")
    paragraphs = soup.find_all("p")
    analyzed_articles.append(title)

    next_titles = []
    for paragraph in paragraphs:
        words = re.findall(r'\b[a-zA-Z]+\b', paragraph.text.strip().lower())
        word_counter.update(words)
        for anchor in paragraph.find_all("a"):
            if (anchor.get("title", "/") != '/'):
                next_title = anchor.get("title", "/")
                print(next_title)
                next_titles.append(next_title)
    
    for next_title in next_titles:
        analyze_article(next_title, depth-1, analyzed_articles, word_counter)
    
    return word_counter


def get_statistics(word_counter, exclude_words, percentile):
    ''' Function for counting words and calculating percentage frequency '''
    logging.info('Gathering statistics...')
    exclude_words = [word.lower() for word in exclude_words]
    word_sum = sum(word_counter.values())
    indicator = (percentile / 100) * word_sum
    word_count = {word: {'count': count, 'percentage': (count / word_sum) * 100} for word, count in word_counter.items()
                  if word not in exclude_words and count >= indicator}
    return word_count
