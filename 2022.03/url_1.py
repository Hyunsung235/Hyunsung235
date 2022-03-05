import requests
from bs4 import BeautifulSoup

#url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
url = 'https://pubg.game.daum.net/pubg/ranking/leaderboards.daum'
response = requests.get(url)


# 200은 성공을 뜻함
if response.status_code == 200:
    print("Success")
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    print("soup", soup)


 #hi 태그 출력
    print("soup hi", soup.h1)

# 하위 목록 뽑기
    for ch in soup.h1.children:
        print(ch)


# findAll 찾고자 하는 것을 전체에서 list 형태로 return 한다
    ex = soup.findAll("hi", {"class":"title"})
    print("ex", ex)
    print("before", soup.findAll('div'))
    top_list = soup.findAll("div", {"class":"tit3"})
    print("top list", top_list)
    p = soup.find_all('p')
    top_list = soup.find_all(attrs={'class':'tit3'})

    index = 1


# stri은 공백을 제거하는 역할
    for i in top_list:
        print(index, i.text.strip())
        index += 1

else:
    print(response.status_code)