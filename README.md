# SearchPackage
#### 네이버 검색을 파이썬으로, 간편하게

# How to Use
1. **파이썬 3** 이상 필요
2. cmd창에 ```pip install SearchPackage``` 입력
3. 모듈을 사용할 파이썬 파일 내에서 ```from naver import naver_searcher``` 로 모듈 임포트

# Functions
```
  블로그:naver_searcher.blog("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치)   
    뉴스:    ''        .news("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 
      책:    ''       .book("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 
백과사전:    ''        .encyc("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 
    영화:    ''        .movie("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 
    카페:    ''        .cafe("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 
  지식in:    ''        .kin("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 
  이미지:    ''        .image("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 
전문자료:    ''        .doc("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치) 

위 검색 유형 전부 포함: naver_searcher.find_everything("검색할 문자열", display=검색 결과 출력 건수, start=검색 시작 위치)
                      
```

# Example

#### test.py
```py
#import module
from naver import naver_searcher
output = naver_searcher.news("네이버", display=3, start=1)

print(type(output))

print(type(output[0]))

print(output[0]['title'])

print(output)
```

#### output
```
<class 'list'>
<class 'dict'>
&quot;'내돈내산' 리뷰만 따로 본다&quot;…<b>네이버</b>, '쇼핑 스마트블록' 도입
[{'title': "&quot;'내돈내산' 리뷰만 따로 본다&quot;…<b>네이버</b>, '쇼핑 스마트블록' 도입", 'originallink': 'http://www.newsis.com/view/?id=NISX20220711_0001937995&cID=13006&pID=13100', 'link': 'https://n.news.naver.com/mnews/article/003/0011296393?sid=105', 'description': "기자 = <b>네이버</b>가 직접 구매 인증한 사용자의 상품평, 날씨∙시즌별 추천 아이템 정보 등을 손쉽게 확인할 수 있는 쇼핑 스마트블록을 선보였다고 11일 밝혔다. <b>네이버</b>는 지난해 AI(인공지능) 검색 '에어서치'를 선보이고... ", 'pubDate': 'Mon, 11 Jul 2022 10:12:00 +0900'}, {'title': "<b>네이버</b>, 인공지능 검색 서비스 '쇼핑 스마트블록' 도입", 'originallink': 'https://www.yna.co.kr/view/AKR20220711039500017?input=1195m', 'link': 'https://n.news.naver.com/mnews/article/001/0013301390?sid=105', 'description': "<b>네이버</b>가 인공지능(AI) 중심 검색 브랜드 '에어서치'(AiRSearch)로 제공하는 사용자 맞춤형  검색 결과 '스마트블록'을 쇼핑에도 확대 적용한다고 11일 밝혔다. 스마트블록은 <b>네이버</b>가 지난해 10월 통합검색을 대체하는... ", 'pubDate': 'Mon, 11 Jul 2022 09:30:00 +0900'}]
```

#### test.py
```py
from naver import naver_searcher
output = naver_searcher.find_everything("네이버", display=2, start=1)

print(type(output))

print(type(output['blog']))

print(output)

```

#### output
```
<class 'dict'>
<class 'list'>
{'blog': [{'title': '<b>네이버</b> 블로그 애드포스트 승인 3배 빨리 받기', 'link': 'https://blog.naver.com/resumet?Redirect=Log&logNo=222798927611', 'description': '물론 그 뒤로 광주고와 <b>네이버</b>, 그리고 블로거간의  복잡한 관계가 숨어있지만 그것까지 알 필요는... 사실 <b>네이버</b>에서 공식적으로 알리는 조건은 아닙니다. 참고만 하시면 되구요. 문제는 포스팅이 50개가 넘고... ', 'bloggername': '블루래더 - 경제적 자유를 향한 푸른 사다리', 'bloggerlink': 'https://blog.naver.com/resumet', 'postdate': '20220704'}, {'title': '<b>네이버</b> 메모 활용 방법 편리해요', 'link': 'https://blog.naver.com/bookey3?Redirect=Log&logNo=222806963021', 'description': '세상 편리한 <b>네이버</b> 메모 메모장 잘 활용하고 계시나요? 생각의 조각들이 흩어지지 않도록 중요한 일정... 하지만 <b>네이버</b> 메모장이 편리한 이유 중 하나는 자동으로 컴퓨터와 연동이 되어서 핸드폰으로 쓰든 pc로... ', 'bloggername': '우쿠리 우쿨렐레', 'bloggerlink': 'https://blog.naver.com/bookey3', 'postdate': '20220711'}], 'news': [{'title': "&quot;'내돈내산' 리뷰만 따로 본다&quot;…<b>네이버</b>, '쇼핑 스마트블록' 도입", 'originallink': 'http://www.newsis.com/view/?id=NISX20220711_0001937995&cID=13006&pID=13100', 'link': 'https://n.news.naver.com/mnews/article/003/0011296393?sid=105', 'description': "기자 = <b>네이버</b>가 직접 구매 인증한 사용자의 상품 평, 날씨∙시즌별 추천 아이템 정보 등을 손쉽게 확인할 수 있는 쇼핑 스마트블록을 선보였다고 11일 밝혔다. <b>네이버</b>는 지난해 AI(인공지능) 검색 '에어서치'를 선보이고... ", 'pubDate': 'Mon, 11 Jul 2022 10:12:00 +0900'}, {'title': "<b>네이버</b>, 인공지능 검색 서비스 '쇼핑 스마트블록' 도입", 'originallink': 'https://www.yna.co.kr/view/AKR20220711039500017?input=1195m', 'link': 'https://n.news.naver.com/mnews/article/001/0013301390?sid=105', 'description': "<b>네이버</b>가 인공지능(AI) 중심 검색 브랜드 '에어서치'(AiRSearch)로 제공하는 사용자 맞춤형 검색 결과 '스마트블록'을 쇼핑에도 확대 적용한다고 11일 밝혔다. 스마트블록은 <b>네이버</b>가 지난해 10월 통합 검색을 대체하는... ", 'pubDate': 'Mon, 11 Jul 2022 09:30:00 +0900'}], 'book': [{'title': '<b>네이버</b>쇼핑 스마트스토어로 상위노출 하라 (무조건 1페이지에 올려라, 그래야 산다!)', 'link': 'http://book.naver.com/bookdb/book_detail.php?bid=15768781', 'image': 'https://bookthumb-phinf.pstatic.net/cover/157/687/15768781.jpg?type=m1&udate=20211126', 'author': '김도균', 'price': '22000', 'discount': '19800', 'publisher': '휴먼하우스', 'pubdate': '20211015', 'isbn': '1185455175 9791185455174', 'description': '<b>네이버</b>쇼핑 1페이지 1위 상위노출 전략<b>네이버</b>쇼핑에서 ‘칫솔’, ‘핫팩’, ‘선풍기’를 비롯한 주요 대표키워드에서 1페이지 1위에 상품을 노출하면서... 이론이 아니라 적용하는 순간 바로 순위가 상승하는 스마트스토어 상위노출의 실전 기법을 다룬 책으로, 스마트스토어 초보셀러와 <b>네이버</b>쇼핑... '}, {'title': '<b>네이버</b> 블로그로 돈 벌기 (1년에 5,000만 원 버는 수익 확장 노하우)', 'link': 'http://book.naver.com/bookdb/book_detail.php?bid=20941046', 'image': 'https://bookthumb-phinf.pstatic.net/cover/209/410/20941046.jpg?type=m1&udate=20220104', 'author': '아빠동동', 'price': '16000', 'discount': '14400', 'publisher': '한빛미디어', 'pubdate': '20210928', 'isbn': '1162244771 9791162244777', 'description': '<b>네이버</b> 블로그 상위 0.1% 탑 블로거가 알려주는 12가지 블로그 수익화 전략퇴사 없이 경제적 자 유를 획득하라!<b>네이버</b> 블로그를 운영하는 사람이라면 누구나 블로그를 통해 수익을 창출하고 유명해지길 원합니다. 하지만 꾸준히 한다고 블로그가 무조건 성장하는 것은 아닙니다. <b>네이버</b> 블로그로 단기간에 수익을... '}], 'encyc': [{'title': '<b>네이버</b>(주)', 'link': 'https://terms.naver.com/entry.naver?docId=652054&cid=43167&categoryId=43167', 'description': " 1999년 6월에 설립된 대한민국 대표 인터넷 회사. 인터넷 포털 '<b>네이버</b>(NAVER)'와 글로벌 모바일 메신저 '라인(LINE)' 등을 운영하는 글로벌 기업.  <b>네이버</b>는 1999년 6월 이해진 글로벌투자책임자를 비롯한... ", 'thumbnail': 'http://openapi-dbscthumb.phinf.naver.net/2315_000_1/20180503120708313_7U0BCOA3X.jpg/company_2383_i1.jpg?type=m160_160'}, {'title': '<b>네이버</b>', 'link': 'https://ko.wikipedia.org/wiki/%EB%84%A4%EC%9D%B4%EB%B2%84', 'description': '<b>네이버</b> ( 영어: NAVER )는 1999년 6월에 출시된  대한민국의 포털사이트이다. 또한 <b>네이버</b>는 1997년 2월 26일 이해진, 권혁일, 김보경, 구창진, 오승환, 최재영, 강석호 등으로 구성된 삼성SDS의 사내 벤처에서... ', 'thumbnail': ''}], 'movie': [{'title': '루스 <b>네이버</b>', 'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=213066', 'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/2130/213066_P01_100736.jpg', 'subtitle': 'Lou’s Neighbour', 'pubDate': '2021', 'director': ' 빅토리아 라파우리|헥터 앨버커|', 'actor': '', 'userRating': '0.00'}, {'title': '마이 <b>네이버</b>, 미구엘', 'link': 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=203935', 'image': 'https://ssl.pstatic.net/imgmovie/mdi/mit110/2039/203935_P01_171245.jpg', 'subtitle': 'My Neighbor, Miguel', 'pubDate': '2021', 'director': '대니 나바로|', 'actor': '', 'userRating': '0.00'}], 'cafe': [{'title': '<b>네이버</b> 로직 변화- <b>네이버</b>의 의도는?', 'link': 'http://cafe.naver.com/jihosoccer123/1563603', 'description': '얼마전, <b>네이버</b> 노출 로직 변화에 대해, 스타트업 코너에 글을 올렸는데, 여기 쇼핑몰 코너에 업로드... 1년 전부터는 SEO에 많은 투자를 하여 저의 사이트를 <b>네이버</b> 첫장 웹사이트 부분 2위로 노출을 시켰습니다.(물론 1위는... ', 'cafename': '아프니까 사장이다 [소상공인·자영업...', 'cafeurl': 'https://cafe.naver.com/jihosoccer123'}, {'title': '<b>네이버</b> 공동인증서 발급하려면 어떻게 해야 할까?', 'link': 'http://cafe.naver.com/masanmam/6096446', 'description': '<b>네이버</b> 공동인증서 발급하려면 어떻게 해야 할까? 안녕하세요. 기존에 공인인증서라는 이름으로 통용되던...  그 중 대표적인 것이 바로 ‘<b>네이버</b> 공동인증서 발급’인데요. 어떻게 발급받을 수 있고, 기존과는 어떤... ', 'cafename': '창원 줌마렐라 [경남,마산,진해,함안,...', 'cafeurl': 'https://cafe.naver.com/masanmam'}], 'kin': [{'title': '<b>네이버</b>맵버십확인', 'link': 'https://kin.naver.com/qna/detail.naver?d1id=1&dirId=10601&docId=422357818&qb=64Sk7J2067KE&enc=utf8&section=kin.qna&rank=1&search_sort=0&spq=0', 'description': '저의 <b>네이버</b> 플러스 멤버십 결재 잘된것인지확인 하는 방법 좀... <b>네이버</b> 플러스 멤버십 결재 된것인지 확인 할수가 없어서 문의 드립니다 안녕하세요. <b>네이버</b> 지식파트너입니다. 현재 이용 중인 <b>네이버</b>플러스 멤버십은... '}, {'title': '<b>네이버</b> 페이 사용', 'link': 'https://kin.naver.com/qna/detail.naver?d1id=1&dirId=1060115&docId=422171847&qb=64Sk7J2067KE&enc=utf8&section=kin.qna&rank=2&search_sort=0&spq=0', 'description': '<b>네이 버</b> 페이는 무슨 방법으로 사용하는건가요? <b>네이버</b>페이 포인트 사용법에 대한 질문인가요? 기본적으로 <b>네이버</b>페이는 간편결제 서비스입니다. <b>네이버</b>Id 로 기본적인 이용약관 동의절차를 거치면 <b>네이버</b>페 이 이용이 가능해집니다.... '}], 'image': [{'title': '네이버·카카오 공공문서 전자증명서 출시한다!', 'link': 'http://post.phinf.naver.net/MjAyMjA0MjBfMjU1/MDAxNjUwNDIzNTA3MjM1.DN4sOFz9Hng7Pb8MK9SbnlDEHJKD71A73yIxRBUSpbwg.UnQtZliVQvpVwBy0NYx0MHHZpiGZ5QN0G12KsMDncr0g.PNG/IdrthDgLZAVzquIADAlVK21k_iVM.jpg', 'thumbnail': 'https://search.pstatic.net/common/?src=http://post.phinf.naver.net/MjAyMjA0MjBfMjU1/MDAxNjUwNDIzNTA3MjM1.DN4sOFz9Hng7Pb8MK9SbnlDEHJKD71A73yIxRBUSpbwg.UnQtZliVQvpVwBy0NYx0MHHZpiGZ5QN0G12KsMDncr0g.PNG/IdrthDgLZAVzquIADAlVK21k_iVM.jpg&type=b150', 'sizeheight': '560', 'sizewidth': '800'}, {'title': '네이버 라인, 일본서 NFT마켓 열어...인기캐릭터IP 등 확보', 'link': 'http://imgnews.naver.net/image/014/2022/04/13/0004819592_001_20220413153004683.jpg', 'thumbnail': 'https://search.pstatic.net/common/?src=http://imgnews.naver.net/image/014/2022/04/13/0004819592_001_20220413153004683.jpg&type=b150', 'sizeheight': '320', 'sizewidth': '560'}], 'doc': [{'title': '한국지리 지형단원 수업에서의 인터넷 위성사진 활용 - <b>네이버</b> 지도를 ', 'link': 'http://academic.naver.com/article.naver?doc_id=57612644', 'description': 'Classroom application of satellite pictures in the topography unit of Korean Geography - Based on Naver Map - 인터넷에서 제공되'}, {'title': '<b>네이버</b>의 글로벌 경영 사례 연구 - 기 술을 통한 세계 정복을 꿈꾸는 네이', 'link': 'http://academic.naver.com/article.naver?doc_id=887651118', 'description': 'A Case Study on Naver’s Global Management - Naver Dreams of Conquering the World Through Technology <b>네이버</b>는 그동안 축적한 '}]}

```
