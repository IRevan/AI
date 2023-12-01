from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

x = 0
while(x<=220):
    url = "https://www.kumoh.ac.kr/ko/sub01_04.do?mode=list&&articleLimit=10&article.offset={}".format(x)
    driver.get(url)
    driver.implicitly_wait(10)

    links = []
    for i in range(1, 11):
        css_selector = ".board-list01 > table:nth-child(1) > tbody:nth-child(3) > tr:nth-child({}) > td:nth-child(2) > a:nth-child(1)".format(i)
        href = driver.find_element(By.CSS_SELECTOR, css_selector)
        links.append(href)

    href = []
    for i in links:
        href.append(i.get_attribute("href"))

    for i in href:
        driver.get(i)
        driver.implicitly_wait(20)
        driver.find_element(By.CSS_SELECTOR, '[class="file-down-btn hwp"]').click()

    x += 10
