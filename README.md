
## Web-Crawler [![Build Status](https://travis-ci.org/fabianaboldrin/web-crawler.svg?branch=master)](https://travis-ci.org/fabianaboldrin/web-crawler.svg?branch=master)

This program has been designed to work only with Wikipedia sites. It searches for the first link in the page and stops when it gets to a specific page (ex. philosophy)

# Installation
  Currently working in Python 3.x

  *Clone the git*

  *pip install -r requirements.txt*

# Example of usage

```bash
python WebCrawler.py -s https://pt.wikipedia.org/wiki/Python -t https://en.wikipedia.org/wiki/Scrapy -m 40
```
  
# List of arguments

  | Argument      | Meaning          | Default value |
  | ------------- | -----------------| --------------|
  | -s            | start url        | Random article|
  | -t            | target url       | Philosophy    |
  | -m            | number of steps  | 30            |
