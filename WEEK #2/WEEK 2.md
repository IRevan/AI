# WEEK 2

### 1. What is this?

	자신이 원하는 네이버 뉴스의 테마에 해당하는 헤드라인 뉴스의 제목과 내용을 가져와 전처리를 통해 명사만 추출하여 워드클라우드를 만듭니다.

### 2. Code Explained


**1) Web Crawling**

> 먼저 웹 크롤링에 필요한 모듈을 가져온다

	from selenium import webdriver
	from selenium.webdriver.common.by import By
	from selenium.webdriver.edge.options import Options

> 원하는 테마를 선택한다.

![capture4](https://github.com/IRevan/AI/assets/62048967/425b76b3-2afa-46f9-a000-91e9b9bcab1b)

	i = int(input('테마를 선택하세요\n100: 정치, 101: 경제, 102: 사회, 103: 생활/문화, 104: 세계, 105: IT/과학\n')

> 각 테마의 주소를 살펴보면 공통된 부분과 다른 부분(마지막 세 자리 숫자)이 존재한다.

	/
	정치: https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100
 	/
	경제: https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101
	/
 	사회: https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=102
	/
 	생활/문화: https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103
	/
 	IT/과학: https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105
	/
 	세계: https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104
	
> 이제 각 테마의 주소로 들어가 보자. 뉴스를 크롤링하기 위해선 먼저, 뉴스의 링크가 필요하다. 그러나 여기도 테마의 링크처럼 HTML문서의 속성의 공통된 부분과 다른 부분이 존재한다. 다음은 뉴스의 링크와 제목이 속한 클래스의 이름이다. 

	/
	정치: class="sh\_text\_headline nclicks(cls_pol.clsart)"
	/
 	경제: class="sh\_text\_headline nclicks(cls_eco.clsart)"
	/
 	사회: class="sh\_text\_headline nclicks(cls_nav.clsart)"
	/
 	생활/문화: class="sh\_text\_headline nclicks(cls_lif.clsart)"
	/
 	IT/과학: class="sh\_text\_headline nclicks(cls_sci.clsart)"
	/
 	세계: class="sh\_text\_headline nclicks(cls_wor.clsart)"
	
> 우리가 크롤링 하고자 하는 헤드라인 뉴스가 있는 영역을 살펴보면 5개의 뉴스와 더 보기 버튼이 있다. 모든 뉴스를 크롤링 하기 위해 버튼을 클릭하여 숨겨진 뉴스를 드러내야 한다. 

![capture2](https://github.com/IRevan/AI/assets/62048967/7fce94a6-f7d4-4df0-9b46-67bec4c15a68)


> 테마에 따라 클래스 이름이 다르므로 이 부분을 바꿔줘야 한다. 코드는 다음과 같다.

	j = {100: 'pol', 101: 'eco', 102: 'nav', 103: 'lif', 104: 'wor', 105: 'sci'} 
 	
	url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={}'.format(i)  
	css_selector1 = '[class="sh_text_headline nclicks(cls_{}.clsart)"]'.format(j[i])  
	css_selector2 = '[class="cluster_more_inner _news_cluster_more_btn nclicks(cls_{}.clsmore)"]'.format(j[i])

> 옵션을 이용하여 셀레늄을 실행시켰을 때 브라우저가 뜨지 않도록 설정했다.

	options = Options()  
	options.add_argument("--headless")


> Edge 드라이버를 가져와 선택한 테마로 접속한다. 셀레늄의 find_element(s) 함수와 
CSS_SELECTOR를 이용하여 버튼을 클릭하여 숨겨진 뉴스를 표시하고 제목과 링크가 속한 클래스를 가져온다.

	driver = webdriver.Edge(options=options)  
	driver.get(url)  
	driver.find_element(By.CSS_SELECTOR, css_selector2).click()  
	elements = driver.find_elements(By.CSS_SELECTOR, css_selector1)  
	driver.implicitly_wait(20)

> elements를 출력 해 보자.

	[<selenium.webdriver.remote.webelement.WebElement (session="ecae2ef580296fe4df9c85f0dc79ac72", element="40721DAF62F7804D4EF6E56E2BB20126_element_101")>, ...]

> 리스트의 각 요소는 셀레늄 객체이므로 객체 내부에 저장되어 있는 뉴스의 제목과 링크만 가져온다.

	titles = []  
	for i in elements:  
	    titles.append(i.text)  

	links = []  
	for i in elements:  
		links.append(i.get_attribute("href"))

> 마지막으로 뉴스의 링크로 접속해서 내용을 가져와야 한다. 이제 필요한 데이터는 전부 가져왔다.

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
	
> 기사 내용을 담은 TXT파일이 data 폴더에 생성되었다. 

![capture3](https://github.com/IRevan/AI/assets/62048967/56c7d04d-3087-427c-8c0a-f0c84be7acc3)

**2) Preprocessing**

> 필요한 모듈을 불러온다.

	from konlpy.tag import Okt  
	from collections import Counter  
	from wordcloud import WordCloud  
	import matplotlib.pyplot as plt  
	import pandas as pd  
	import itertools

> 저장한 기사 내용 텍스트 파일들을 차례대로 읽어 들인 다음, Okt와 pandas를 이용해 각 기사의 명사를 담은 CSV파일을 생성한다.

	okt = Okt()  
	for i in range(1, 9):  
	    with open('./data/article{}.txt'.format(i), 'r', encoding='utf-8') as file:  
	        article = file.read()  
	        
	    noun = okt.nouns(article)  
	    list_o = list(dict.fromkeys(noun))  
	    
	    sr_o = pd.Series(list_o)  
	    sr_o.to_csv('./data/noun{}.csv'.format(i), index=False, encoding='utf-8')

> data 폴더에 CS V파일이 생성된 것을 확인할 수 있다.

![capture](https://github.com/IRevan/AI/assets/62048967/65b93cf9-ff63-4c66-93c9-99ccdacd90d3)


> 생성한 CSV파일들을 읽어 온 후 하나로 합친다. 

	noun1 = pd.read_csv('data/noun1.csv')  
	noun2 = pd.read_csv('data/noun2.csv')  
	noun3 = pd.read_csv('data/noun3.csv')  
	noun4 = pd.read_csv('data/noun4.csv')  
	noun5 = pd.read_csv('data/noun5.csv')  
	noun6 = pd.read_csv('data/noun6.csv')  
	noun7 = pd.read_csv('data/noun7.csv')  
	noun8 = pd.read_csv('data/noun8.csv')  
	
	noun = pd.concat([noun1, noun2, noun3, noun4, noun5, noun6, noun7, noun8], sort=False) 
	noun = noun.drop_duplicates()  
	noun.columns = ['noun']

> 최종적으로 워드클라우드를 출력한다.

	Data = noun['noun'].values.tolist()  
	
	r = len(Data)  
	a = []  
	for i in range(r):  
	    a.append(okt.nouns(Data[i]))  
	  
	c = []  
	for i in range(r):  
	    c.append(Counter(a[i]))  
	  
	target_list = list(itertools.chain(*a))  
	tl2 = Counter(target_list)  
	tl = Counter({x: tl2[x] for x in tl2 if len(x) > 1})  
	  
	wc = WordCloud(font_path='data/NanumBarunGothic.ttf', background_color='white', max_font_size=60)  
	cloud = wc.generate_from_frequencies(dict(tl))  
	  
	plt.figure(figsize=(30, 10))  
	plt.axis('off')  
	plt.imshow(cloud)  
	plt.show()

**3) Result**

![result 1](https://github.com/IRevan/AI/assets/62048967/2a1dd6c4-60ee-4e09-ae93-4dcd224b4ead)
