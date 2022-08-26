import requests
from bs4 import BeautifulSoup
import json 
import html
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
class feedsClass(BaseModel):
    link:str
    title:str
    
@app.post("/")
def rssFeed(feeds:feedsClass):
    url = requests.get(feeds.link)
    htmltext = url.text

    file_html = open("index.html", "w")
    file_html.write(htmltext)
    file_html.close()
    
    soup = BeautifulSoup( (open("index.html"))  , 'html.parser')
    text = soup.find_all('p')
    dateTime = soup.find('div', class_='ReleaseDateSubHeaddateTime').get_text().strip().split('Posted On:')[1].strip().split('by')[0].strip().split(" ")
    dateTime[1]= dateTime[1].lower()
    # locale.setlocale(locale.LC_ALL, 'en_IN')
    # date = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')
    # date = date.strftime('%d-%m-%Y')
    print(dateTime)
    # datetime.datetime.strptime("11/12/98","%dd/%d/%y")
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
    # monthDict={1:'jan', 2:'feb', 3:'mar', 4:'apr', 5:'may', 6:'jun', 7:'jul', 8:'aug', 9:'sep', 10:'oct', 11:'nov', 12:'dec'}
    monthDict = {
        'jan':'00',
        'feb':'01',
        'mar':'02',
        'apr':'03',
        'may':'04',
        'jun':'05',
        'jul':'06',
        'aug':'07',
        'sep':'08',
        'oct':'09',
        'nov':'10',
        'dec':'11'
    }
    dateTime[1] = dateTime[1].replace(dateTime[1],monthDict[dateTime[1]])
    dateString = dateTime[1]+'/'+dateTime[0]+'/'+dateTime[2] +" "+ dateTime[3][:-2]
    
    # dic = {"title":title , 'img' : data['2'], 'description':data['1']   }
    # jsonData = json.loads(json.dumps(data))
    # locale.setlocale(locale.LC_ALL, 'fr_FR')
    # test_date = datetime.datetime.strptime(date, '%d %b %Y')
    # iso_date = test_date.isoformat()
    # print(iso_date)
    return {"jsonData":data, "title":feeds.title, "createdAt":dateString}








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
