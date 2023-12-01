from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd

query = input('검색어를 입력하세요 ')
page = int(input('검색할 페이지의 갯수를 입력하세요 '))
page_num = [i*10-9 for i in range(1, page+1)]

news_dict = {}

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
for i in page_num:
    url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&start={}'.format(query, i)

    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    news = soup.select(".news_tit")

    for k in news:
        news_dict[k.attrs["title"]] = k.attrs["href"]

sr = pd.Series(news_dict)
print(sr)
