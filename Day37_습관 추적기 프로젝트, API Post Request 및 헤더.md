### [[HTTP Requests]]
GET 
[[requests.get()]]
외부 시스템에 특정한 데이터를 요청하고
그들이 응답으로 데이터를 줄  때 씀

POST
[[requests.post()]]
우리가 외부 시스템에 어떤 데이터를 주고
그것의 성공 유무를 제외하고 시스템으로부터 받는 응답에는 관심이 없음
ex) twitter API를 이용해 tweet 전송

PUT
[[requests.put()]]
외부 서비스에서 단순히 데이터를 업데이트함
ex) Google Sheets의 스프레드 시트에 있는 값을 업데이트

DELETE
[[requests.delete()]]
외부 서비스 데이터 삭제
ex) facebook 게시물


### [[HTTP Header]]
헤더
편지에서 헤더: 회사 전화번호, 웹사이트, 로고 등  관련 정보가 담겨 있는 부분 본문은 실제 메시지 부분

[[API Key]] -> 비밀 정보가 요청 자체에 있다, 훔칠 수 있음
![[Pasted image 20231212145552.png]]
이 API는 https를 통해 액세스 됨(http(s = secure)
암호화 돼있는 요청
그래도 브라우저에 뭔가를 설치해서 요청을 보거나 할 수 있음

HTTP header는
API 키가 로그나 요청 스니핑에서 타인에게 보이지 않게 함
따라서 일부 API 제공자들은 인증을 헤더에 제공하도록 요구하고 있음
![[Pasted image 20231212150033.png]]
![[Pasted image 20231212151909.png]]

#### [[strftime()]]
날짜 형식 포매팅 
![[Pasted image 20231212173224.png]]