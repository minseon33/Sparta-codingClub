import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music = soup.select('#body-content > div.newest-list > div > table > tbody > tr')


for music_info in music:
    num = music_info.select_one('td.number')
    title = music_info.select_one('td.info > a.title.ellipsis')
    singer = music_info.select_one('td.info > a.artist.ellipsis')

    # if num is not None and title is not None and  singer is not None:
    num_a = num.text[0:2]
    title_a = title.text.split()
    singer_a = singer.text
    print(num_a,"".join(title_a),singer_a)




