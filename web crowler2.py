#!/usr/bin/env python

import time
import bs4
import urllib
import requests
import argparse


def find_first_link(url):
    # get the HTML of the url, using requests framework and
    # inserting the HTML at Beautiful Soup
    response = requests.get(url)
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

    return urllib.parse.urljoin('https://en.wikipedia.org/', article_link)


def continue_crawl(search_history, target_url, max_steps=30):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long; aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen; aborting search!")
        return False
    return True


def get_arg_parser():
    """
    Sets up the argument parser
    """
    parser = argparse.ArgumentParser(
        description="Wikipedia Web Crawler",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '-s', help='Start URL (e.g. https://en.wikipedia.org/wiki/Special:Random)', dest='start_url')
    parser.add_argument(
        '-t', help='Target URL (e.g. https://en.wikipedia.org/wiki/Philosophy', dest='target_url')
    return parser


def process_arguments():
    """
    Process the arguments
    """
    arg_parser = get_arg_parser()
    arguments = arg_parser.parse_args()

    if arguments.start_url is None:
        arg_parser.error('Start URL (-s) is required')
    if arguments.target_url is None:
        arg_parser.error('Target URL (-t) is required')
    return arguments

if __name__ == '__main__':
    args = process_arguments()
    article_chain = [args.start_url]

    while continue_crawl(article_chain, args.target_url):
        print(article_chain[-1])
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        if not first_link:
            print("We've arrived at an article with no links, aborting search!.")
            break
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        time.sleep(2)
