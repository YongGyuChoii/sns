import requests
from bs4 import BeautifulSoup

url = 'https://www.goodchoice.kr/product/detail?ano=62375&adcno=3&sel_date=2021-09-25&sel_date2=2021-09-26'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']

print(title,image,desc)


