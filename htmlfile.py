
import requests
from bs4 import BeautifulSoup
import json 
import html
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class feedsClass(BaseModel):
    link:str
    
@app.post("/")
def rssFeed(feeds:feedsClass):
    url = requests.get(feeds.link)
    htmltext = url.text

    file_html = open("index.html", "w")
    file_html.write(htmltext)
    file_html.close()

    soup = BeautifulSoup( (open("index.html"))  , 'html.parser')
    text = soup.find_all('p')
    title = soup.find(property="og:title")
    title = (title["content"])

    img = soup.find_all('img') 
    data = {}
    k=1
    for i in text:
        data[str(k)] = str(i.get_text()).replace("\xa0","")
        img = html.unescape(i).find_all('img')
        for j in img:
            if len(j['src']) > 0:
                data[str(k)] = j['src']
        k+=1
    # print(data)
    dic = {"title":title , 'img' : data['2'], 'description':data['1']  }
    # jsonData = json.loads(json.dumps(data))
    return {"jsonData":dic}