
## Web-Crawler [![Build Status](https://travis-ci.org/fabianaboldrin/web-crawler.svg?branch=master)](https://travis-ci.org/fabianaboldrin/web-crawler.svg?branch=master)

Program designed to be used in Wikipedia sites only. It searches for the first link in the page and stop when it gets to a specific page (ex. philosophy)

# Installation
  Currently working in Python 3.x
  
  *Clone the git*
  
  *pip install -r requirements.txt*

# Example of usage

  python WebCrawler.py -s https://pt.wikipedia.org/wiki/Python -t https://en.wikipedia.org/wiki/Scrapy -m 40
  
# List of arguments
  
  | Argument      | Meaning          | Default value |
  | ------------- | -----------------| --------------|
  | -s            | start url        | Random article|
  | -t            | target url       | Philosophy    |
  | -m            | number of steps  | 30            |
  
  
