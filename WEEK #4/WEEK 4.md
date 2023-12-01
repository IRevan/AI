# WEEK 4

### Code Explained

> 데이터는 네이버 뉴스이며 크롤링 코드는 2주차에 작성한 것을 사용했다.

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

> 검색엔진에 필요한 패키지들을 설치한다.

	!pip install langchain unstructured openai chromadb Cython tiktoken pypdf
	!pip install sentence-transformers gpt4all > /dev/null

> 필요한 모듈을 import한다.

	from langchain.text_splitter import RecursiveCharacterTextSplitter  
	from langchain.vectorstores import Chroma  
	from langchain.embeddings import GPT4AllEmbeddings  
	from langchain.embeddings import SentenceTransformerEmbeddings
	from langchain.document_loaders import PyPDFLoader  
	from langchain.document_loaders import TextLoader  
	from langchain.document_loaders import DirectoryLoader

> 구글 코랩 환경에서 실행하므로 구글 드라이브를 마운트 시킨다.

	from google.colab import drive  
	drive.mount('/content/drive')

> 사용할 임베딩과 뉴스 텍스트 데이터 파일이 위치한 경로를 설정한다.

	G4A = GPT4ALLEmbeddings()
	ST = SentenceTransformerEmbeddings()
	
	fn_dir = "/content/drive/My Drive/Colab Notebooks/data/데이터 저장 폴더 이름"

> 크롤링한 네이버 IT/과학 뉴스에 대한 검색엔진을 만들기 위해 기사 내용을 1000자 단위로 쪼갠 후 저장한다.

	loader = DirectoryLoader(fn_dir, loader_cls=TextLoader)  
	documents = loader.load()  
	  
	text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
	docs = text_splitter.split_documents(documents)  
	  
	len(documents), len(docs)

> 마지막으로 저장한 기사 내용울 Chroma를 이용하여 벡터화 시킨 후, 임베딩을 지정하면 검색엔진이 완성된다.

	db = Chroma.from_documents(docs, embedding=시용할 임베딩,  
	                                 persist_directory="index_hf")  
	db.persist()

> 쿼리(검색어) "AI"에 대한 각 임베딩의 상위 5개 검색 결과는 다음과 같다.

	query = "AI"  
	docs = db.similarity_search(query)  
	
	docs[:5]

##### GPT4ALLEmbeddings

	'온디바이스 AI 전략과 관련해서는 강점인 개인화를 강조했다. 그는 "대규모 언어 모델은 개인화된 정보에서 얻은 정보를 추가해 이용자에게 훨씬 더 최적화된 답변을 제공할 수 있다"며 "그런 이유로 시간이 지나면 클라우드의 일반적인 경험보다 디바이스에서의 AI와 생성된 사용자 경험이 훨씬 더 좋아질 것"이라고 덧붙였다. 하와이(=미국)'
	
	"우선 주요국과 국제기구들이 인공지능 신뢰성 확보를 산업 발전의 전제로 인식해 가이드라인 등 자율 실천방안을 제시하는 상황에서 '국가 인공지능 윤리기준'의 구체적 실천수단으로 채용, 생성형 인공지능 기반 서비스 등 분야별 가이드라인을 마련·확대하고, 민간 자율 신뢰성 검·인증을 다음달부터 추진할 계획이다. 특히 AI 사업 중 고위험 영역 인공지능 개발·실증 사업을 수행하는 기업을 일부 선정해 오는 12월 시범 인증을 추진할 예정이다.\n\n또한 인공지능 자체가 내포하는 편향성, 불투명성 등 기술적 한계와 인공지능 오작동 등에 따른 인공지능의 잠재 위험요인에 대응하기 위해 기존 인공지능의 한계를 극복하고 초거대 인공지능의 신뢰성을 확보하기 위한 기술개발을 내년부터 신규로 추진할 예정이다."
	
	'퀄컴, 생성형 AI 시대 자신감…"개인 맞춤형 서비스로 차별화"\n\n\n지아드 아즈가 퀄컴 제품관리 수석 부사장이 취재진들의 질문에 답변하고 있다. 공동취재단 제공\n퀄컴이 \'생성형 AI(인공지능)\'에 대한 자신감을 보였다.\n\n지아드 아즈가 퀄컴 제품관리 수석 부사장은 24일(현지시간) 미국 하와이 마우이에서 열린 \'스냅드래곤 서밋 2023\'에서 한국 기자들과 만나 이날 공개한 온디바이스 AI 기반 제품이 생성형 AI 분야에서 경쟁력을 얻을 수 있다고 밝혔다.\n\n그는 "\'스냅드래곤X 엘리트\'와 \'스냅드래곤8 3세대\' 모두 현재 다른 어떤 기기보다 훨씬 더 많은 기능을 갖추고 있다고 말씀드릴 수 있다"고 자신감을 내비쳤다. 퀄컴은 이날 열린 행사에서 온디바이스 AI 시장 재편에 관해 강조했다. 생성형 AI 등장 이후 클라우드 기반 AI가 주인공으로 부상한 가운데 개인화에 강점이 있는 온디바이스 AI 시장을 자사 기술력과 경쟁력으로 본격 공략하겠다는 전략이다.'
	
	"정부, AI 창작물에 '워터마크' 도입 추진\n\n\n민간 자율 검·인증제도 내달 시행\n위험 요인 평가하고 신뢰성 확보\n내달부터 인공지능(AI) 서비스에서 발생할 수 있는 위험 요인 등을 민간 자율로 평가하는 검·인증 체계와 AI 생성물에 대한 워터마크 표시 제도가 추진된다.\n\n과학기술정보통신부 이종호 장관은 25일 개인정보보호위원회 고학수 위원장, 인공지능 분야 민간 최고위 관계자들과 함께 '제4차 인공지능 최고위 전략대화'를 열고 이 같은 내용을 발표했다."

##### SentenceTransformerEmbeddings

	'퀄컴, 생성형 AI 시대 자신감…"개인 맞춤형 서비스로 차별화"\n\n\n지아드 아즈가 퀄컴 제품관리 수석 부사장이 취재진들의 질문에 답변하고 있다. 공동취재단 제공\n퀄컴이 \'생성형 AI(인공지능)\'에 대한 자신감을 보였다.\n\n지아드 아즈가 퀄컴 제품관리 수석 부사장은 24일(현지시간) 미국 하와이 마우이에서 열린 \'스냅드래곤 서밋 2023\'에서 한국 기자들과 만나 이날 공개한 온디바이스 AI 기반 제품이 생성형 AI 분야에서 경쟁력을 얻을 수 있다고 밝혔다.\n\n그는 "\'스냅드래곤X 엘리트\'와 \'스냅드래곤8 3세대\' 모두 현재 다른 어떤 기기보다 훨씬 더 많은 기능을 갖추고 있다고 말씀드릴 수 있다"고 자신감을 내비쳤다. 퀄컴은 이날 열린 행사에서 온디바이스 AI 시장 재편에 관해 강조했다. 생성형 AI 등장 이후 클라우드 기반 AI가 주인공으로 부상한 가운데 개인화에 강점이 있는 온디바이스 AI 시장을 자사 기술력과 경쟁력으로 본격 공략하겠다는 전략이다.\n\n지아드 아즈가 부사장은 "퀄컴은 지난 10년 이상 AI에 투자해오면서 HW(하드웨어)를 포함해 소프트웨어(SW) 측면에서도 근본적인 연구를 수행해왔다"며 "이런 측면에서 다른 경쟁사들과 진정으로 차별화한다고 생각한다"고 언급했다.\n\n가령 레스토랑을 예약하고 싶다고 하면, 추천 앱 \'옐프(Yelp)\'에 들어가 그 지역에서 가장 높은 평점을 받은 레스토랑을 확인했지만, 지금 위치한 거리에서 가장 가까운 식당을 확인하고 다시 옐프 앱으로 가서 예약하고 이 과정을 처음부터 기기가 한번에 해주는 식이다. PC의 경우 일상적 업무에서도 활용할 수 있다. 가상 현실 영역에서는 "날아다니는 비행기를 생성해줘"라고 말하면 실제 개인 데이터를 염두에 두고 해당 이미지를 생성하고 가상 사물이나 주변 장소를 생성할 수 있다. 디바이스가 이용자를 더 잘 이해하기 때문에 각 개개인에게 맞춤화 된 서비스를 제공할 수 있다.'
	
	"정부, AI 창작물에 '워터마크' 도입 추진\n\n\n민간 자율 검·인증제도 내달 시행\n위험 요인 평가하고 신뢰성 확보\n내달부터 인공지능(AI) 서비스에서 발생할 수 있는 위험 요인 등을 민간 자율로 평가하는 검·인증 체계와 AI 생성물에 대한 워터마크 표시 제도가 추진된다.\n\n과학기술정보통신부 이종호 장관은 25일 개인정보보호위원회 고학수 위원장, 인공지능 분야 민간 최고위 관계자들과 함께 '제4차 인공지능 최고위 전략대화'를 열고 이 같은 내용을 발표했다.\n\n우선 주요국과 국제기구들이 인공지능 신뢰성 확보를 산업 발전의 전제로 인식해 가이드라인 등 자율 실천방안을 제시하는 상황에서 '국가 인공지능 윤리기준'의 구체적 실천수단으로 채용, 생성형 인공지능 기반 서비스 등 분야별 가이드라인을 마련·확대하고, 민간 자율 신뢰성 검·인증을 다음달부터 추진할 계획이다. 특히 AI 사업 중 고위험 영역 인공지능 개발·실증 사업을 수행하는 기업을 일부 선정해 오는 12월 시범 인증을 추진할 예정이다.\n\n또한 인공지능 자체가 내포하는 편향성, 불투명성 등 기술적 한계와 인공지능 오작동 등에 따른 인공지능의 잠재 위험요인에 대응하기 위해 기존 인공지능의 한계를 극복하고 초거대 인공지능의 신뢰성을 확보하기 위한 기술개발을 내년부터 신규로 추진할 예정이다.\n\n아울러 챗GPT와 같은 초거대 인공지능의 확산으로 안전에 대한 위험성 우려가 확대되는 상황에서 인공지능이 생성한 결과물에 대한 워터마크 도입의 제도화를 검토하고, 고위험 인공지능에 대한 해설서를 내년 1·4분기에 마련하는 등 신뢰성 확보를 위한 제도 정립 과제를 추진할 방침이다. 민간에서는 김유철 LG AI 연구원 부문장이 '인공지능 윤리원칙 실행을 위한 기업의 노력'을 발표하고, JLK 김동민 대표가 '고위험 인공지능 분야에 대한 신뢰성 검·인증의 필요성'을 소개했다."
	
	'그는 향후 자사 생성형 AI 기능을 결합한 플랫폼을 결합한 디바이스에 대한 기대감을 내비치기도 했다. \'스냅드래곤8 3세대\'에 접목된 생성형 AI 기능 탑재로 기대하는 효과에 대해 "OEM(주문자표생산) 파트너들은 기본적으로 카메라 개인화에 대한 새 사용 사례를 기대한다"며 "PC 분야에서도 AI 관점에서 우리가 할 수 있는 것을 결합하면 아무도 근접하지 못할 것으로 본다"고 자신감을 내비쳤다. 타사 중에서 70억개의 매개변수(파라미터) 모델을 초당 20개의 토큰으로 처리할 수 있는 곳이 없으며, 6초 만에 스테이블 디퓨전을 빠르게 수행할 수 있는 기업도 아직 없다는 부연 설명이다.\n\n온디바이스 AI 전략과 관련해서는 강점인 개인화를 강조했다. 그는 "대규모 언어 모델은 개인화된 정보에서 얻은 정보를 추가해 이용자에게 훨씬 더 최적화된 답변을 제공할 수 있다"며 "그런 이유로 시간이 지나면 클라우드의 일반적인 경험보다 디바이스에서의 AI와 생성된 사용자 경험이 훨씬 더 좋아질 것"이라고 덧붙였다. 하와이(=미국)'
	
	"포스코DX '비전 AI 솔루션'…야생동물 로드킬 막는다\n\n\n포스코DX는 인공지능(AI) 기반 야생동물 ‘로드킬’ 예방 시스템을 개발했다고 25일 밝혔다.\n\n이 시스템은 도로 일정 구간에 라이다 센서와 CCTV를 설치해 도로로 뛰어드는 야생동물을 감지한다. 고라니, 고양이 등 어떤 동물인지도 판독해 해당 구간 전광판에 띄워 운전자에게 알려준다. 영상 내 행동을 인식하고 객체를 탐지·분석하는 포스코DX의 ‘비전AI 솔루션’ 기술이 들어갔다.\n\n포스코DX는 경남에서 전남 여수까지 걸쳐 있는 한려해상국립공원 상주~금산지구 350m 구간에서 이 시스템 성능을 시험하고 있다. 회사 관계자는 “시험 결과를 바탕으로 환경부 산하 국립공원공단과 협력해 다른 공원으로 확대할 것”이라고 말했다."


### Conclusion

###### GPT4ALLEmbeddings 

> 1. 뉴스의 내용 중 불필요한 내용은 제거하고 핵심만 가져와 사용자가 훨신 알아보기 쉽개 보여준다.
> 2. 실행 속도가 매우 빠르다. 

###### SentenceTransformerEmbeddings

> 1. 뉴스의 텍스트 데이터 전체를 가져와 한 눈에 알아보기 어렵다.   
> 2. 실행 속도가 상대적으로 많이 느려 성능차이가 체감된다.