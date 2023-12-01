import requests
from bs4 import BeautifulSoup
import pandas as pd

query = input('검색어를 입력하세요')
page = int(input('검색할 페이지를 입력하세요'))
url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&start={}".format(query, str(page*10-9))


webpage = requests.get(url)
soup = BeautifulSoup(webpage.text, "html.parser")
news = soup.select(".news_tit")

news_dict = {}
for i in news:
    news_dict[i.attrs['title']] = i.attrs['href']

series = pd.Series(news_dict)

print(series)
