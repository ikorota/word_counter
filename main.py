from fastapi import FastAPI
import uvicorn
from collections import Counter
from pydantic import BaseModel
from typing import List
from utils import get_article, get_statistics, analyze_article
import logging


app = FastAPI()


class Keywords:
    article: str
    depth: int
    ignore_list: List[str]
    percentile: int

    def __init__(self, article, depth, ignore_list, percentile):
        self.article = article
        self.depth = depth
        self.ignore_list = ignore_list
        self.percentile = percentile


class KeywordsRequest(BaseModel):
    article: str
    depth: int
    ignore_list: List[str]
    percentile: int


@app.get('/word-frequency')
def get_word_frequency(article: str, depth: int):
    analyzed_articles = []
    word_counter = Counter()
    word_counter = analyze_article(article, depth, analyzed_articles, word_counter)
    word_count = get_statistics(word_counter, [], 0)
    return word_count


@app.post('/keywords')
def get_word_frequency(request_body: KeywordsRequest):
    analyzed_articles = []
    word_counter = Counter()
    logging.info("Request body:")
    logging.info(request_body)
    logging.info(request_body.model_dump())
    keywords = Keywords(**request_body.model_dump())
    article = keywords.article
    depth = keywords.depth
    ignore_list = keywords.ignore_list
    percentile = keywords.percentile
    word_counter = analyze_article(article, depth, analyzed_articles, word_counter)
    word_count = get_statistics(word_counter, ignore_list, percentile)
    return word_count


@app.get('/healthy')
def health_check():
    return {'status': 'healthy'}
    

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
