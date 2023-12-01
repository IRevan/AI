# WEEK 3

### Vector Embedding, Database

> 벡터 임베딩은 데이터 점들의 집합으로, 그들의 기본적인 관계와 패턴을 수학적으로 표현한 것이다. 이미지, 텍스트, 오디오와 같은 복잡한 데이터 유형을 컴퓨터가 쉽게 처리할 수 있도록 표현하는데 임베딩이 자주 활용된다. 
> 
> 벡터 데이터베이스는 방대한 양의 벡터 임베딩을 저장하고 처리하기 위한 특수 데이터베이스이다.


### Chroma?

> Chroma는 오픈소스 벡터 데이터베이스이다.


### Code Explained

> 필요한 패키지들을 설치한다.

	!pip install langchain unstructured openai chromadb Cython tiktoken pypdf
	!pip install sentence-transformers gpt4all > /dev/null

> 필요한 모듈을 import한다.

	from langchain.text_splitter import RecursiveCharacterTextSplitter  
	from langchain.vectorstores import Chroma
	from langchain.embeddings import HuggingFaceEmbeddings
	from langchain.document_loaders import PyPDFLoader  
	from langchain.document_loaders import TextLoader  
	from langchain.document_loaders import DirectoryLoader

> 구글 코랩 환경에서 실행하므로 구글 드라이브를 마운트 시킨다.

	from google.colab import drive  
	drive.mount('/content/drive')

> 사용할 임베딩과 데이터 파일이 위치한 경로를 설정한다.

	HF = HuggingFaceEmbeddings()
	
	fn_dir = "/content/drive/My Drive/Colab Notebooks/data/데이터 저장 폴더 이름"

> AI기사에 대한 검색엔진을 만들기 위해 기사 내용을 1000자 단위로 쪼갠후 저장한다.

	loader = DirectoryLoader(fn_dir, loader_cls=TextLoader)  
	documents = loader.load()  
	  
	text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
	docs = text_splitter.split_documents(documents)  
	  
	len(documents), len(docs)

> 마지막으로 저장한 기사 내용울 Chroma를 이용하여 벡터화 시킨 후, 임베딩을 지정하면 검색엔진이 완성된다.

	db = Chroma.from_documents(docs, embedding=HF,  
	                                 persist_directory="HF_index_hf")  
	db.persist()

> 쿼리(검색어) "What is Generative AI?"에 대한 상위 2개 검색 결과는 다음과 같다.

	query = "What is Generative AI?"  
	docs = db.similarity_search(query)  
	
	docs[:2]

##### HuggingFaceEmbeddings

	'The regulator also points to its core mission — to support open, competitive markets — as another reason for taking a look at generative AI now. Notably, the competition watchdog is set to get additional powers to regulate Big Tech in the coming years, under plans taken off the back-burner by prime minister Rishi Sunak’s government last month, when ministers said it would move forward with a long-trailed (but much delayed) ex ante reform aimed at digital giants’ market power.'
	
	'The legal spats between artists and the companies training AI on their artwork show no sign of abating. Within the span of a few months, several lawsuits have emerged over generative AI tech from companies including OpenAI and Stability AI, brought by plaintiffs who allege that copyrighted data — mostly art — was used without their permission to train the generative models. Generative AI models “learn” to create art, code and more by “training” on sample images and text, usually scraped indiscriminately from the web. In an effort to grant artists more control over how — and where — their art’s used, Jordan Meyer and Mathew Dryhurst co-founded the startup Spawning AI. Spawning created HaveIBeenTrained, a website that allows creators to opt out of the training dataset for one art-generating AI model, Stable Diffusion v3, due to be released in the coming months.'

> 다음은 이력서 PDF파일 검색엔진이다. DirectoryLoader의 loader_cls를 PyPDFLoader로 바꿔주기만 하면 된다. 검색 결과는 다음과 같다.

##### HuggingFaceEmbeddings

	"Clients included: Bronx Museum of Arts, Cava Construction, Leftfield Pictures.\nIT Manager\n \nAugust 2010\n \nto \nMay 2012\n \nCompany Name\n \nï¼\u200b \nCity\n \n, \nState\nManaged a staff of ten IT support staff, which provided support for all users employed within Ogilvy North American offices.\nConstantly \ndeveloping new standards and IT policy's to improve support reaction time.\nKey Accomplishment: Lead architect for migrating all Lotus \nNotes and MS Exchange users to Cloud (Google) Mail.\nGathered and analyzed performance metric data.Â \nEducation and Training\nBS\n \n: \nPrint Production, Graphic Design Computer Science\n \n, \n1993\n \nSt. John's University\n \nPrint Production, Graphic Design Computer Science\nTechnical Skills\nActive Directory, premiere, ads, Advertising, IBM AIX, Apple, architect, Arts, catalog, color, com, Clients, digital photography, digital video,\ndirect mail, disaster recovery, eCommerce, Final \nCut Pro, SGI Irix, IT support, legal, Linux, Logic, loss prevention, Lotus"
	
	'part-time employees and consultants Webmaster and graphic designer for Internet and intranet sites, print advertising, multimedia, and\npresentation projects Maintained Mac desktop computers and software supporting DNA Sequencer and robotic systems.\nEducation and Training\nBachelor of Science\n \n: \nInformation Technology\n \n, \nJuly 2016\n \nUniversity of Phoenix\nInformation Technology[Number] GPA\nSkills\nACT!, Adobe, Acrobat, After Effects, Photoshop, Premiere, Apache, branding, business processes, C++, Cisco, Hardware, consultant,\nconsulting, CSS, client, clients, Database, Dell, disaster recovery, document management, Documentum, Dreamweaver, email, ERP, features,\nFireworks, Flash, FreeBSD, graphic designer, HP, HTML5, IBM, Illustrator, InDesign, information systems, Information technology, MS IIS,\nInternet communications, Java, JavaScript, Languages, Linux, logo, Mac, Apple Mac, marketing, market, access, MS Access, MS Exchange, MS'


### Conclusion

> 실행 결과를 확인해 보면 쿼리(검색어)에 대한 답을 주는 것이 아니기 검색어에 포함된 단어와의 관계만을 따지기 떄문에 사용자가 원하는 답을 챗봇처럼 얻을 수 없다.