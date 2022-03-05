import requests
from bs4 import BeautifulSoup

url = 'https://pubg.game.daum.net/pubg/ranking/leaderboards.daum'
response = requests.get(url)

if response.status_code == 200:
    print("Success")
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    print("soup", soup)

    #print("soup hi", soup.h1)
    print()
    print(soup)

#    for ch in soup.h1.children:
#        print(ch)

#    ex = soup.findAll("hi", {"class":"title"})
#    print("ex", ex)
#    print("before", soup.findAll('div'))
#    top_list = soup.findAll("div", {"class":"tit3"})
#    print("top list", top_list)
#    p = soup.find_all('p')
#    top_list = soup.find_all(attrs={'class':'tit3'})

#    index = 1


#    for i in top_list:
#        print(index, i.text.strip())
#        index += 1

else:
    print(response.status_code)