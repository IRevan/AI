from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# user_data = "C:\Selenium_py\user_data"  # 기존에 쓰던 유저 데이터가 아니라 완전히 새로운 데이터를 만들어 셀레늄 실행, 새로운 데이터가 새로운 프로필에 누적된다.
# user_data = "C:\Users\tride\AppData\Local\Google\Chrome\User Data"  # 기존의 내 프로필을 사용한다.
# options.add_argument(f"user-data-dir = {user_data}")  # 유저 데이터 사용 여부를 결정, 모든 프로필에 해당
# options.add_argument("--profile-directory=여기에 입력")  # 다른 프로필을 사용하고 싶을 때 프로필 경로 확인 후 가장 마지막에 있는 폴더의 이름 입력

options.add_experimental_option("detach", True)  # 창을 닫지 않으면 프로그램이 계속 실행된다.(이 옵션을 추가하지 않으면 창이 바로 꺼진다.)

options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")  # fullscreen = F11
# options.add_argument("window-size = x,y")  # 창 크기 지정 가능

# options.add_argument("--headless")  # 창이 보이지 않게 한다
# options.add_argument("--disable-gpu")

# options.add_argument("--mute-audio")  # 오디오가 자동적으로 나오는 사이트를 뮤트
# options.add_argument("incognito")  # 시크릿 모드 실행

# add_argument()의 인자들을 확인할 수 있는 사이트 https://peter.sh/experiments/chromium-command-line-switches/#aggressive-cache-discard

url = 'https://www.naver.com/'

driver = webdriver.Chrome(options=options)
driver.get(url)

# print(type(driver.page_source))  # html 문서를 텍스트 형태로 가져온다. 슬라이싱으로 원하는 만큼 가져올 수 있다.
