#! python3
#  searchpypi.py - Opens several search results.
# todo to learn HTML, CSS Selector Parser of beautiful soup
import requests, sys, webbrowser, bs4
print("Searching...") # display text while downloading the search result page
res = requests.get("http://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
print(res.raise_for_status())

# todo: Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, features='html.parser') # TODO HTML Knowledge
# todo: Open a browser tab for each result.
linkElems = soup.select(".package-snippet") # TODO CSS Selector
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")# a kind of attribute.
    print("Opening", urlToOpen)
    webbrowser.open(urlToOpen)

'''command line
python searchpypi.py boring stuff
'''

#todo
# try to search goods on Amazon  (learn css selector and html first)