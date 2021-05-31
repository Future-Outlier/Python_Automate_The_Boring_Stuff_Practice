import requests, bs4
res = requests.get("http://nostarch.com")
res.raise_for_status()
# todo we need to put a parser to tell bs4 which parser to parse
noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))