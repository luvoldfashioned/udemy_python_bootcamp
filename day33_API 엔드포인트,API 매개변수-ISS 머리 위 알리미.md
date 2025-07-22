## [[API]]
**Application Programming Interface**
- 일련의 명령, 함수, 프로토콜, 객체로 구성
- 이를 이용해 소프트웨어를 생성하거나 외부 시스템과 
    상호작용 할 수 있음
- API는 인터페이스이고, 프로그램과 외부 시스템 사이에 있는 장벽임
- API가 규정한 규칙들을 이용해서 외부 시스템에 데이터 요청
- 웹사이트=식당 / 데이터=주방 / 인터페이스(API)=메뉴
    메뉴는 주문할 수 있는 것과 없는 것을 알려줌

#### [[API Endpoint]]
특정한 외부 서비스에서 데이터를 얻으려면 그 데이터가 저장된 위치(location)을 알고 있어야 함
보통은 URL 
ex) 암호화페 데이터를 얻으려면 -> api.coinbase.com

#### [[API Request]]
- 마치 은행에 가서 돈을 인출하려는 것과 같다
- 은행 점원 ≒ API
- [[requests(python library)]]
	- requests.get() -> [[API Endpoint]]로 부터 원하는 데이터를 얻도록 도와줌
```
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
```
![[Pasted image 20231122153917.png]]

### [[response code]]
응답 코드
1XX : Hold On(진행중)
2XX: Here You Go(성공)
3XX: Go Away(권한 없음)
4XX: You Srewed Up
	(요청자가 잘못 됌 / 찾는 것이 존재하지않음)
5XX: I Screwed Up
	(서버가 잘못 됌 / 서버 다운 등 이슈)

응답 객체가 아닌 실제 상태 코드를 알고 싶을 때
`print(response.status_code)`
![[Pasted image 20231122154645.png]]
*invalid endpoint*
![[Pasted image 20231122154732.png]]
![[Pasted image 20231122154723.png]]


### [[requests(python library)]]
requests 모듈로 예외 생성 
`response.raise_for_status()`
![[Pasted image 20231122155632.png]]

[[JSON]] 데이터 받기
```
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
print(data)
```
![[Pasted image 20231122161834.png]]

파이썬 [[dictionary]]처럼 사용 가능
```
response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()["iss_position"]
print(data)
```
![[Pasted image 20231122163657.png]]
```
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
```
![[Pasted image 20231122163947.png]]

### [[API Parameters]]
- 은행원에게 개점 시간 같은 대략적인 질문 대신 {월요일}에는 몇 시에 문을 닫느냐고 물을 수 있음
- 모든 API에 parameter(매개변수)가 있는 건 아님
ex) 일출/일몰 시각 API -> 매개변수로 위치(위도/경도)를 제공

- URL 문자열에서 매개변수를 형식화
	Endpoint + ? + param_name=value +& + ...
```
	https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400
	https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=today
	https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&date=2023-11-23
	https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400&formatted=0
```
