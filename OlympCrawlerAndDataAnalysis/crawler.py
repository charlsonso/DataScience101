'''
Web Crawler to grab olympic medal data from Wikipedia.org and export to csv

@pre: requires url lib >1.17 and beautiful soup
@post:

Tutorial Used : https://www.dataquest.io/blog/web-scraping-tutorial-python/
				http://gawron.sdsu.edu/python_for_ss/course_core/book_draft/web/HTMLParser.html


'''

import urllib
from bs4 import BeautifulSoup

thisurl = "https://en.wikipedia.org/wiki/2014_Winter_Olympics"

handle = urllib.urlopen(thisurl)

html_gunk = handle.read()

print(html_gunk)
