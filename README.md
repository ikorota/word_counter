# Wiki Word Counter App

A simple and efficient application that counts the number of words and word frequency from a Wikipedia article.

## Features

- Extracts paragraphs and counts words in Wikipedia articles.
- Simple and intuitive user interface.
- Performs word frequency calculation.

## Installation

### Prerequisites

- Docker client (tested using Docker Desktop on Windows)
- A web browser (for the web-based app version)

### Steps

```bash
git clone https://github.com/ikorota/word_counter.git
cd .\word_counter\
docker build --tag 'word_counter' .
docker run -p 8000:8000 -it word_counter python main.py
```

## Testing

The application can be tested in swagger UI http://127.0.0.1:8000/docs or by executing curl commands, e.g.:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/word-frequency?article=Pet%20door&depth=0' -H 'accept: application/json'
```

```bash
curl -X 'POST' 'http://127.0.0.1:8000/keywords' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"article": "Pet door", "depth": 0, "ignore_list": ["a"], "percentile": 0}'
```

Unit tests can be executed while the previously started Docker container is running:

```bash
docker run -it pytest
