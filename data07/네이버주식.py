import requests
import pandas as pd
from bs4 import BeautifulSoup
import mysql_movie.stock_crud as db
url = "https://finance.naver.com/sise/lastsearch2.nhn"
result = requests.get(url)
#print(result.content)
# result

content = BeautifulSoup(result.content, "html.parser")

# content
name = content.findAll("a", {"class": "tltle"})
print(len(name))
name_list = []

# 종목명 추출
for i in range (len(name)):
    name_list.append(name[i].text)
print(name_list)

# 현재가 추출

cost = content.findAll("td", {"class":"number"})
print(cost[1])
print(cost[11])
cost_list = []
for i in range(1, len(cost), 10): # 10의 간격으로 추출됨
    cost_list.append(cost[i].text.replace(",", ""))
print(cost_list)

name_list2 = tuple(name_list)
cost_list2 = tuple(cost_list)

total_list = list(zip(name_list2, cost_list2))
print(total_list)
total = tuple(total_list)
#print(total)
#db.create(total)