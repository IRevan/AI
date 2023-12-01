# WEEK 1

### 1. 목표 사이트

네이버 뉴스

### 2. 공부한 크롤링 기법들

1) BeautufulSoup을 이용한 웹 크롤링

    ![image](https://github.com/IRevan/AI/assets/62048967/0d856b37-16e4-48af-af1d-a4ea4881bd87)
    
    원하는 검색어와 페이지를 입력하면 입력한 페이지의 모든 기사 제목과 각각의 링크를 차례대로 가져와
    리스트에 저장하고 가져온 기사의 갯수를 출력한다.
    
    ![image](https://github.com/IRevan/AI/assets/62048967/d0ce3fd7-2a96-4d17-9332-a9bdd458a7b1)
    
    ![image](https://github.com/IRevan/AI/assets/62048967/821a7fe2-0c7c-49e0-bbdf-a66abbb61fb7)
    
    ![image](https://github.com/IRevan/AI/assets/62048967/1bbf90d0-c72a-49ab-a912-7f3d8d598bfe)
    
    ![image](https://github.com/IRevan/AI/assets/62048967/285efb60-8133-4844-8bbe-2edff1f7d0bc)
    
    ![image](https://github.com/IRevan/AI/assets/62048967/7773e4c7-19a4-4e23-b2ac-1c6ea20fa274)
    
    ![image](https://github.com/IRevan/AI/assets/62048967/fba27cb6-6046-4bc4-acae-a43f04a7821f)
    
    ![image](https://github.com/IRevan/AI/assets/62048967/d99eb3c6-15d4-427c-b93a-65fdac439b4f)
  
    알아보기 쉽게 타이틀과 링크만으로 이루어진 리스트를 각각 만든다.
  
    ![image](https://github.com/IRevan/AI/assets/62048967/f5428267-db69-4208-a024-95261d5f7f80)
  
    ![image](https://github.com/IRevan/AI/assets/62048967/01173ab1-4050-4b78-b63d-a318f2f2df39)
  
    최종적으로 [타이틀, 링크]를 하나의 요소로 가지는 하나의 리스트를 만들어 더 알아보기 쉽게 만든다.
    
    ![image](https://github.com/IRevan/AI/assets/62048967/aea6d6ef-1e57-4e94-9436-39075e19c283)
  
    ![image](https://github.com/IRevan/AI/assets/62048967/00753027-d43d-4b05-8f2a-c9e0fcc00c69)
  
    ![image](https://github.com/IRevan/AI/assets/62048967/8ad40bc3-d4f5-4ddb-abde-b70cc49766a9)
  
    위의 코드는 너무 난잡해 보이고 실행했을 때 최종적으로 나오는 리스트가 보기 너무 불편하여 코드를
    간략하게 하고 직관적으로 알아볼 수 있는 자료형을 찾아보던 중 판다스의 '시리즈'를 알게 되었다.
    판다스란 파이썬 데이터 분석 라이브러리이며 시리즈는 판다스가 사용하는 2개의 자료형 중 하나이다.
    시리즈는 딕셔너리와 유사하며 Key를 이용하여 Value를 찾는다. 그러나 딕셔너리는 가로인 반면 시리즈는
    세로이기에 딕셔너리보다 훨씬 알아보기 쉽다. 나는 시리즈에 대하여 추가적으로 공부하여 최종적으로 뉴스
    제목을 Key로, 뉴스 링크를 Value로 가지는 시리즈를 출력하는 코드를 작성했다.
  
    ![image](https://github.com/IRevan/AI/assets/62048967/2b3e2ebe-5582-49ae-99f3-a78239082106)
  
    ![image](https://github.com/IRevan/AI/assets/62048967/c32acce7-d076-4e37-aefc-032e00ee8074)
  
3) selenium을 활용한 웹 크롤링

   ![image](https://github.com/IRevan/AI/assets/62048967/9cc12747-a1b9-440f-a5e7-115de1c2809f)

   BeautifulSoup과는 다른 방법으로 웹 크롤링을 할 수 있는지를 찾아보다가 selenium을 알게 되었다.
   그래서 나는 selenium을 최대한 활용하기 위해 공식 문서, 유튜브, 온라인 문서, 개발자 커뮤니티 등을 찾아보며
   추가적으로 공부를 하였서 Options에 대해서 배웠다. Options모듈은 selenium을 어떤 브라우저에서 실행했을 때
   브라우저에 내릴 수 있는 명령이다. 예를 들어 접속 시 음악이 나오는 사이트를 음소거 할 수 있고, 창의 크기를
   임의로 지정하는 등의 액션을 취할 수 있다.
   
   ![image](https://github.com/IRevan/AI/assets/62048967/c33a3fd8-8c82-44e5-be0f-7eae9622a12a)

   위의 코드는 사용자가 입력한 검색어와 연관된 네이버 뉴스의 제목과 링크를 크롤링히여 Series로 출력하는 코드이다.

   ![image](https://github.com/IRevan/AI/assets/62048967/67ae51ac-887a-4347-ad7b-84ab63dae43e)

   먼저 필요한 모듈을 가져온다.

   ![image](https://github.com/IRevan/AI/assets/62048967/507418ce-007e-4010-a109-4ee55f617b76)

   다음으로는 검색어와 검색결과의 페이지 갯수를 입력받고 제목과 링크를 저장 할 딕셔너리를 만든다.
   page_num의 원소를 저렇게 설정해 옿은 이유는 뒤에서 설명하겠다.

   ![image](https://github.com/IRevan/AI/assets/62048967/f5c7c337-230d-4022-a46e-f626ef102f4a)

   이 옵션을 추가하면 파일을 실행했을 때 브라우저 창이 뜨지 않는다. options.add_experimental_option("detach", True)를
   주면 창이 꺼지지 않는다. options.add_argument("--mute-audio")를 주면 사이트에서 나오는 오디오를 음소거 한다.
   options.add_argument("window-size = x,y")를 주면 창의 사이즈를 임의로 조정할 수 있다. options.add_argument("incognito")를
   주면 브라우저의 시크릿 모드로 selenium을 실행한다.

   ![image](https://github.com/IRevan/AI/assets/62048967/956daebd-7570-4267-a192-5a9cc3f580ff)

   driver에 옵션이 활성화 된 webdriver를 저장한다.

   ![image](https://github.com/IRevan/AI/assets/62048967/3423a331-7356-4190-9aab-cc4af151f741)

   page_num의 원소를 특이하게 정한 이유가 바로 여기에 있다. 네이버에 AI를 검색하고 뉴스 탭에 들어가 가장 아래로 스크롤 하여
   1페이지를 눌러보면 다음과 같은 URL이 뜬다.

   https://search.naver.com/search.naver?where=news&sm=tab_pge&query=AI&sort=0&photo=0&field=0&pd=0&ds=&de=
   &cluster_rank=20&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:all,a:all&start=1

   2페이지를 눌러 보면 다음과 같이 뜬다.
   
   https://search.naver.com/search.naver?where=news&sm=tab_pge&query=AI&sort=0&photo=0&field=0&pd=0&ds=&de=
   &cluster_rank=40&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:all,a:all&start=11

   3페이지

   https://search.naver.com/search.naver?where=news&sm=tab_pge&query=AI&sort=0&photo=0&field=0&pd=0&ds=&de=
   &cluster_rank=54&mynews=0&office_type=0&office_section_code=0&news_office_checked=&office_category=0&service_area=0&nso=so:r,p:all,a:all&start=21

   위 세 링크들의 공통점은 다음과 같다.

   https://search.naver.com/search.naver?where=news&sm=tab_pge&query={}...&start={}

   여기서 query는 검색어를 의미하고 start는 페이지를 의미한다. 그런데 여기서 이상한 점은 1페이지는 1로 표시되나 2페이지와 3페이지는
   2와 3으로 표시되지 않고 다른 숫자로 표시된다. 규칙을 살펴보면 화면에 보이는 페이지*10-9를 링크상의 페이지로 가진다는 것이다.
   page_num의 원소를 저렇게 설정한 이유가 바로 여기에 있다.

   ![image](https://github.com/IRevan/AI/assets/62048967/bbbee2e0-38b3-4f50-9ca1-43e213516e7c)

   이후로는 get()을 사용하여 url을 가져오고 변수 html에 page source를 저장한다. BeautifulSoup을 이용하여 클래스 이름으로 news_tit 
   을 찾고 그 안에 있는 title과 href(링크)만 가져와 딕셔너리에 저장한다.

   ![image](https://github.com/IRevan/AI/assets/62048967/f6d1e459-69fe-4af9-a084-5325e2a41288)

   최종적으로 판다스를 이용하여 시리즈로 변환한 후 출력한다.

   ![image](https://github.com/IRevan/AI/assets/62048967/42ebf052-6a2d-4108-8d70-da6999f50e20)
