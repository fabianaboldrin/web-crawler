
## Web-Crawler [![Build Status](https://travis-ci.org/fabianaboldrin/web-crawler.svg?branch=master)](https://travis-ci.org/fabianaboldrin/web-crawler.svg?branch=master)

Program designed to be used in Wikipedia sites only. It searches for the first link in the page and stop when it gets to a specific page (ex. philosophy)

# Installation
  * Currently working in Python 3.x
  
### Steps to install
  1. [Fork this repository](https://github.com/fabianaboldrin/web-crawler) (Click the Fork button in the top right of this page, click your Profile Image)
  2. Clone your fork down to your local machine.
  `git clone https://github.com/<your_username>/projecteuler.git`
  3. Get inside the `web-crawler` directory.
  `cd projecteular`
  4. Create a virtual environment.
  `virtualenv -p python3 venv`
  5. Activate the environment.
  `source activate venv` or `source venv/bin/activate`
  6. Install the requirements.
  `pip3 install -r requirements.txt`

# Example of usage

  python WebCrawler.py -s https://pt.wikipedia.org/wiki/Python -t https://en.wikipedia.org/wiki/Scrapy -m 40
  
# List of arguments
  
  | Argument      | Meaning          | Default value |
  | ------------- | -----------------| --------------|
  | -s            | start url        | Random article|
  | -t            | target url       | Philosophy    |
  | -m            | number of steps  | 30            |
  
  
