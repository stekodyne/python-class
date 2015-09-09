"""
NewsFeedParser is an abstract base class for concrete news parser classes.

Adapted from examples in "Learning Python Design Patterns Code"
by Gennadiy Zlobin.

Converted to Python 3 by running:
    python PYTHON_HOME/Tools/Scripts/2to3.py -w news_parser.py
"""

from abc import ABCMeta, abstractmethod
import urllib.request
from xml.dom import minidom
from ticketmanor.rest_services.feed_reader import (
    NewsType,
    FeedReaderException,
)


# BONUS TODO: make NewsFeedParser an abstract base class
# HINT: see slide 2-13
class NewsFeedParser:

    # TODO: note the definition of the NewsFeedParser __init__() method.
    # (no code changes required)
    def __init__(self, news_item_element_name):
        self.item_element_name = news_item_element_name

    # TODO: paste methods from rss_news_feed_parser here


    # BONUS TODO: define get_url() as an abstract method

    # BONUS TODO: define parse_item() as an abstract method

    # BONUS TODO 2: convert parse_xml_content() into a generator function that yields
    # a single parsed item each time it's called.
    # HINT: delete the parse_content list completely. Instead of appending
    # each parsed item to a list, yield it from the generator.


# Run news_feed_parser to verify NewsFeedParser is abstract
if __name__ == '__main__':
    try:
        parser = NewsFeedParser(None)
        import sys
        print("ERROR: NewsFeedParser is not abstract", file=sys.stderr)
    except TypeError:
        print("Success: NewsFeedParser is abstract")
