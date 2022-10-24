print('##############  3-5강  ##############')
print('파이썬 기초(1)')
print('--------------- (1) 리스트  ---------------')
a_list = ['사과','배','감']

print(a_list[2])

a_list.append('귤')

print(a_list)

print('---------------  (2) 딕셔너리  ---------------')
a_dict = {
    'name' : 'bob',
    'age' : 27
}

print(a_dict['name'])

print('---------------  (3) 함수  ---------------')

def sum(a,b):
    print('더하자!')
    return a+b

result = sum(1,2)
print(result)
print('##############  3-5강  ##############')

print('---------------  (1) 조건문  ---------------')
def is_adult(age):
    if age > 20 :
        print('성인입니다.')
    else :
        print('청소년입니다.')

is_adult(25)
is_adult(15)

print('---------------  (2) 반복문  ---------------')

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for aaa in fruits:
    if aaa == '배':
        count += 1
print(count)
print('---------------  (2) 반복문2  ---------------')
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for ppp in people:
    if ppp['age'] > 20:
        print(ppp['name'])


print('##############  3-7강  ##############')
print('---------------  requests 패키지 써보기  ---------------')

import requests # requests 라이브러리 설치 필요

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

print(rjson)
print(rows)

for row in rows:
    gu_name = row['MSRSTE_NM']
    gu_mise = row['IDEX_MVL']

    if gu_mise < 40:
        print(gu_name)

print('##############  3-8강  ##############')
print('---------------  크롤링 기본 세팅  ---------------')
import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.aik73au.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20221024',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

# 코딩 시작

for movie in movies:
    a = movie.select_one('td.title > div > a')
    a_rank = movie.select_one('td:nth-child(1) > img')
    a_star = movie.select_one('td.point')

    if a is not None:
        print('------------------')
        print(a_rank['alt'] + '위')
        print(a.text)
        print(a_star.text)


