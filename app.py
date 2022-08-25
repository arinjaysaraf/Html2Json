from bs4 import BeautifulSoup
import html
import json
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class html2json(BaseModel):
    html: str

@app.post("/")
def sendJson(data: html2json):
    soup = BeautifulSoup(data.html, 'html.parser')
    text = soup.find_all('p')
    img = soup.find_all('img')
    data = {}
    k=1
    for i in text:
        data[str(k)] = str(i.get_text())
        img = html.unescape(i).find_all('img')
        for j in img:
            if len(j['src']) > 0:
                data[str(k)] = j['src']
        k+=1
    json_data = json.loads(json.dumps(soup))
    return [{ "json_data": json_data}]

# soup = BeautifulSoup((open('index.html')), 'html.parser')

# text = soup.find_all('p')
# img = soup.find_all('img')
# data = {}
# k=1
# for i in text:
#     data[str(k)] = str(i.get_text())
#     img = html.unescape(i).find_all('img')
#     for j in img:
#         if len(j['src']) > 0:
#             data[str(k)] = j['src']
#     k+=1

# with open('data.json', 'w') as outfile:
#     json.dump(data, outfile)
