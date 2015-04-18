import urllib
import re
import sys
import HTMLParser
from referenties import convert_month
from referenties import date

def main():
	htmlurl = sys.argv[1]
	html1 = urllib.urlopen(htmlurl)
	html = html1.read()
	title = re.search(r'itemprop="headline">([^<]+)<', html).group(1)
	author = re.search(r'itemprop="author">([^<]+)<', html).group(1)
	pubdate = "{0}, {1} {2}".format(re.search(r'content="([0-9]+)-[0-9]+-[0-9]+T', html).group(1), re.search(r'content="[0-9]+-[0-9]+-([0-9]+)T', html).group(1), convert_month(re.search(r'content="[0-9]+-([0-9]+)-[0-9]+T', html).group(1)))
	viewdate = date("het bekijken")
	url = html1.geturl()
	print("Bij deze bron kun je de volgende bronvermelding gebruiken:")
	print("{0}. ({1}). {2}. Geraadpleegd op {3} van {4}.".format(author, pubdate, HTMLParser.HTMLParser().unescape(title), viewdate, url))

if __name__ == '__main__':
	main()

