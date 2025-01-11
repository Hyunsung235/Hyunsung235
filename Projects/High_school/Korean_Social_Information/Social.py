import requests
import tkinter
import tkinter.ttk as ttk
consumer_key = 'f5c8ab4b3a3447dcbdc7'
consumer_secret = '8911e9b21e164e768d74'
locatenum = {'서울특별시':0,'부산광역시':1,'대구광역시':2,'인천광역시':3,'광주광역시':4,'대전광역시':5,'울산광역시':6,'세종특별자치시':7,
             '경기도':8,'강원특별자치도':9,'충청북도':10,'충청남도':11,'전라북도':12,'전라남도':13,'경상북도':14,'경상남도':15,
             '제주특별자치도':16}
window = tkinter.Tk()
runcount = 0
Frame1 = tkinter.Frame(window, relief="solid", bd=1,width=400,height=130)
Frame1.place(x = 100,y = 100)
window.title("인구수 검색기")
window.geometry("600x300+100+100")

area = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시','세종특별자치시', '경기도', '강원특별자치도', '충청북도',
        '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도']
area_box = ttk.Combobox(values=area)
area_box.place(x = 150, y = 5, width = 200,height = 50)
area_box.set("지역을 선택하시오.")
def get_access_token():
    url = 'https://sgisapi.kostat.go.kr/OpenAPI3/auth/authentication.json'
    params = {
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['result']['accessToken']
    else:
        return None

def geocode(access_token):
    global data,runcount,label
    url = 'https://sgisapi.kostat.go.kr/OpenAPI3/stats/searchpopulation.json'
    params = {
        'accessToken': access_token,
        'year': 2022,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        data = data['result']
        area_data = area_box.get()
        temp = locatenum[area_data]
        printdata = data[temp]
        if runcount == 0:
            label = tkinter.Label(Frame1, text=area_data+"의 인구수 :"+printdata['population'] +"        "+ area_data+"의 평균연령"+printdata['avg_age'], width=55, height=5, fg="black", relief="solid")
            label.pack()
            runcount += 1
        else:
            label.config(text=area_data+"의 인구수 :"+printdata['population'] +"        "+ area_data+"의 평균연령"+printdata['avg_age'], width=55, height=5, fg="black", relief="solid")
        return data

def main():
    access_token = get_access_token()
    if access_token:
        geocode(access_token)

btn_play = tkinter.Button(window, overrelief="solid", width=15, command=main, repeatdelay=1000, repeatinterval=100,text="실행")
btn_play.place(x = 375, y = 5, width = 70, height=50)

window.mainloop()
