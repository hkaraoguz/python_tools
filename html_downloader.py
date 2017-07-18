#!/usr/bin/env python
import urllib2


def get_html_content(url):
    """
    Get the html content of an url
    """

    response = urllib2.urlopen(url)

    return response.read()
