from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

i = int(input('주제를 선택하세요\n100: 정치, 101: 경제, 102: 사회, 103: 생활/문화, 104: 세계, 105: IT/과학\n'))

j = {100: 'pol', 101: 'eco', 102: 'nav', 103: 'lif', 104: 'wor', 105: 'sci'}
url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={}'.format(i)
css_selector1 = '[class="sh_text_headline nclicks(cls_{}.clsart)"]'.format(j[i])
css_selector2 = '[class="cluster_more_inner _news_cluster_more_btn nclicks(cls_{}.clsmore)"]'.format(j[i])

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get(url)
driver.find_element(By.CSS_SELECTOR, css_selector2).click()
elements = driver.find_elements(By.CSS_SELECTOR, css_selector1)
driver.implicitly_wait(20)

titles = []
for i in elements:
    titles.append(i.text)

links = []
for i in elements:
    links.append(i.get_attribute("href"))

k = 1
for i in links:
    driver.get(i)
    article = driver.find_element(By.CSS_SELECTOR, '[class="go_trans _article_content"]')
    driver.implicitly_wait(20)

    text = article.text
    with open('./data/article{}.txt'.format(k), 'w', encoding='utf-8') as f:
        f.write('{}\n\n\n'.format(titles[k-1]))
        f.write(text)

    k += 1

driver.quit()