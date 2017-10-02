#!/usr/bin/env python

import argparse
import time
import urllib
import bs4
import requests


class WebCrawler:
    """Class to find first article in Wikipedia in chain until it finds a target url"""

    def __init__(self,
                 start_url=None,
                 target_url=None):
        if start_url is None:
            start_url = "https://en.wikipedia.org/wiki/Special:Random"
            print("Using default start url")
        if target_url is None:
            target_url = "https://en.wikipedia.org/wiki/Philosophy"
            print("Using default target url")
        self.start_url = start_url
        self.target_url = target_url
        self.article_chain = [start_url]

    def last_article_in_chain(self):
        """This function will return the last article in the article_chain list"""
        return self.article_chain[-1]

    def find_first_link(self):
        """Get the HTML of the url, using requests framework and
           inserting the HTML at Beautiful Soup"""
        response = requests.get(self.last_article_in_chain())
        html = response.text
        soup = bs4.BeautifulSoup(html, 'html.parser')

        # The div with the main of the article
        content_div = soup.find(class_="mw-parser-output")

        for element in content_div.find_all('p', recursive=False):
            if element.find('a', recursive=False):
                article_link = element.find('a', recursive=False).get('href')
                break

        if not article_link:
            return

        first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

        self.article_chain.append(first_link)
        return first_link

    def continue_crawl(self, max_steps=30):
        """This function will return True if it can continue finding articles"""
        if self.last_article_in_chain() == self.target_url:
            print("We've found the target article!")
            return False
        elif len(self.article_chain) > max_steps:
            print("The search has gone on suspiciously long; aborting search!")
            return False
        elif self.last_article_in_chain() in self.article_chain[:-1]:
            print("We've arrived at an article we've already seen; aborting search!")
            return False
        else:
            return True


def get_arg_parser():
    """
    Sets up the argument parser
    """
    parser = argparse.ArgumentParser(
        description="Wikipedia Web Crawler",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s', 
        help='Start URL (e.g. https://en.wikipedia.org/wiki/Special:Random)', 
        dest='start_url'
    )
    parser.add_argument(
        '-t', 
        help='Target URL (e.g. https://en.wikipedia.org/wiki/Philosophy', 
        dest='target_url'
    )
    return parser


def process_arguments():
    """
    Process the arguments
    """
    arg_parser = get_arg_parser()
    arguments = arg_parser.parse_args()

    return arguments


def main():
    """This is the main function which will run if this is the main script"""
    args = process_arguments()
    web_crawler = WebCrawler(start_url=args.start_url, target_url=args.target_url)
    print('Start url: %s' % web_crawler.start_url)
    print('Target url: %s' % web_crawler.target_url)
    while web_crawler.continue_crawl():
        print(web_crawler.last_article_in_chain())
        # download html of last article in article_chain
        # find the first link in that html
        first_link = web_crawler.find_first_link()
        if not first_link:
            print("We've arrived at an article with no links, aborting search!.")
            break
        # delay for about two seconds
        time.sleep(2)
    print("This chain contains %s links!" % len(web_crawler.article_chain))

if __name__ == "__main__":
    main()
