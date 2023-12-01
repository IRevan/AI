from bs4 import BeautifulSoup
import requests

query = input('검색어를 입력하세요')
page = int(input('검색할 페이지를 입력하세요'))
url = 'https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}&start{}'.format(query, page*10-9)

original_html = requests.get(url)
html = BeautifulSoup(original_html.text, "html.parser")
articles = html.select("div.group_news > ul.list_news > li div.news_area > a")

print(articles)
print(len(articles))

news_title = []
for i in articles:
    news_title.append(i.attrs['title'])

news_link = []
for i in articles:
    news_link.append(i.attrs['href'])

news = []
for i in range(len(news_title)):
    news.append([news_title[i], news_link[i]])

print(news)
