from bs4 import BeautifulSoup
import html
import json

soup = BeautifulSoup((open('index.html')), 'html.parser')

text = soup.find_all('p')
img = soup.find_all('img')
data = {}
k=1
src_=[]

codes = { 
    "\u2019" : "'",
    "\u2018" : "'",
    "\u201c" : '"',
    "\u201d" : '"',
    "\u2013" : '-',
    "\u2014" : '-',
    "\u2026" : '...',
    "\u00a0" : ' '
}

for i in text:
    data[str(k)] = str(i.get_text())
    img = html.unescape(i).find_all('img')
    for j in img:
        if len(j['src']) > 0:
            data[str(k)] = j['src']
            src_ = j['src']
    k+=1

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
