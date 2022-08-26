import requests
from bs4 import BeautifulSoup
import json 
import html
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class feedsClass(BaseModel):
    link:str
    title: str
    
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
    print(data)
    # dic = {"title":title , 'img' : data['2'], 'description':data['1']   }
    # jsonData = json.loads(json.dumps(data))
    return {"jsonData":data}








# from bs4 import BeautifulSoup
# import html
# import json
# from fastapi import FastAPI, File
# from pydantic import BaseModel
# import requests

# # description = "<h1>Header</h1><p>text</p>"   
# # values = dict(description='description',id=5)
# # response = requests.post(self.addr,data=values)

# # if response.ok:
# #     print response.json()

# app = FastAPI()

# class html2json(BaseModel):
#     # html: str
#     files: bytes = File(...)

# @app.post("/")
# async def sendJson(data: html2json):
#     soup = BeautifulSoup(data.html, 'html.parser')
#     text = soup.find_all('p')
#     img = soup.find_all('img')
#     data = {}
#     k=1
#     for i in text:
#         data[str(k)] = str(i.get_text())
#         img = html.unescape(i).find_all('img')
#         for j in img:
#             if len(j['src']) > 0:
#                 data[str(k)] = j['src']
#         k+=1
#     json_data = json.loads(json.dumps(soup))
#     return [{ "json_data": json_data}]

# # soup = BeautifulSoup((open('index.html')), 'html.parser')

# # text = soup.find_all('p')
# # img = soup.find_all('img')
# # data = {}
# # k=1
# # for i in text:
# #     data[str(k)] = str(i.get_text())
# #     img = html.unescape(i).find_all('img')
# #     for j in img:
# #         if len(j['src']) > 0:
# #             data[str(k)] = j['src']
# #     k+=1

# # with open('data.json', 'w') as outfile:
# #     json.dump(data, outfile)
