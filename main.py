import requests
from bs4 import BeautifulSoup
#1

response=requests.get('https://example.com/')
if response.status_code==200:
    soup=BeautifulSoup(response.content, "html.parser")
    title=soup.find('title').text
    print(title)
else:
    print("error", response.status_code)

#2
response=requests.get('https://en.wikipedia.org/')
if response.status_code==200:
    soup=BeautifulSoup(response.content, "html.parser")
    img=soup.find_all('img')
    for i in img:
        print("https://" + i["src"])


#3
response=requests.get('https://example.com/')
if response.status_code==200:
    soup=BeautifulSoup(response.content, "html.parser")
    soup_list=soup.find_all('a')
    for link in soup_list:
        href=link.get('href')
        if href.startswith('https://'):
            print(href)


#4
response=requests.get('https://example.com/')
if response.status_code==200:
    soup=BeautifulSoup(response.content, "html.parser")
    for script in soup.find_all(["style", "script"]):
        script.extract()
    text=' '.join(soup.stripped_strings)
    words=len(text.split())
    print(words)