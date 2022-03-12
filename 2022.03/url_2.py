
import requests
from bs4 import BeautifulSoup
import streamlit

def book(url):
    b = []
    response = requests.get(url)
    if response.status_code == 200:
        print("Success")
        source = response.text
        soup = BeautifulSoup(source, 'html.parser')

        print(soup.findAll('div'))
        exs = soup.findAll('div', {"class": "thumb_type thumb_type2"}, )

        for ex in exs:
            b.append(ex.find('img')['alt'])

        return b

    else:
        print(response.status_code)


a = book('https://book.naver.com/category/index.naver?cate_code=100010010')


for i in range(len(a)):
    streamlit.text(a[i])