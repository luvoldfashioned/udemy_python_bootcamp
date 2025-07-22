### [[BeautifulSoup]]
개발자가 웹사이트를 이해할 수 있도록 도와주는 모듈
 [[html]] 파일 파싱

```python
from bs4 import BeautifulSoup

with open(file="index.html") as file:
    contents = file.read()
    print(contents)

soup = BeautifulSoup(contents, 'html.parser') # 문서 형식 명시
```

![[Pasted image 20240118125012.png]]


작업 중인 웹사이트에 따라 html.parser가 작동하지 않는 경우가 있으며
lxml 파서를 이용해야 할 수도 있음
파싱이나 Beautiful Soup에 보내는 콘텐츠를 이해하는 다른 방식
![[Pasted image 20240118125411.png]]
```python
from bs4 import BeautifulSoup
import lxml

with open(file="index.html") as file:
    contents = file.read()
    print(contents)
    
soup = BeautifulSoup(contents, 'lxml')
```


<em>HTML 코드인 객체를 파이썬 객체로 불러오기</em>
```python
print(soup.title)
```
%%output%%
![[Pasted image 20240118130204.png]]

```python
print(soup.title.name)
```
%%output%%
![[Pasted image 20240118131238.png]]

```python
print(soup.title.string)
```
![[Pasted image 20240118131423.png]]

```python
print(soup.prettify()) # indent
```
![[Pasted image 20240118131546.png]]

가장 첫 번째 앵커 태그 불러오기
```python
 print(soup.a)
```

모든 태그 불러오기(find_all())
```python
all_anchor_tags = soup.find_all(name="a") # 모든 앵커 태그
print(all_anchor_tags)
```
![[Pasted image 20240118132903.png]]

앵커 태그에서 텍스트만 가져오기
```python
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
	print(tag.getText())
```

앵커 태그에서 링크만 가져오기
```python
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
	tag.get("href")
```
![[Pasted image 20240118134030.png]]

[[id selector]]로 찾기
```python
heading = soup.find(name="h1", id="name")
```
![[Pasted image 20240118134953.png]]

[[class selector]]로 찾기
![[Pasted image 20240118135315.png]]
([[class]]는 [[reserved keyword]](예약어)임)

따라서 \_(underscore)를 붙임
```python
section_heading = soup.find(name="h3", class_="heading")
```
![[Pasted image 20240118135818.png]]


복잡한 웹사이트에서는 모든 앵커 태그 리스트에서 어떤 링크가 원하는 링크인지 알기가 어려움
따라서 특정 요소를 드릴 다운할 수 있는 방법이 필요함

CSS selector
find 대신 select_one 사용
```python
company_url = soup.select_one(selector="p a")
```
p 태그 안의 a태그 찾기
select_one ➡️ 처음으로 일치하는 항목을 가져옴
select ➡️ 일치하는 모든 항목을 리스트로 가져옴


(원본 html 코드)
![[Pasted image 20240130143344.png]]
CSS select로 파싱 결과
![[Pasted image 20240130143307.png]]

```python
name = soup.select_one(selector="#name")
print(name)
```
![[Pasted image 20240130143847.png]]

![[Pasted image 20240130144651.png]]


#### 웹 스크래핑 합법/불법
1. 저작권이 있는 콘텐츠를 상업화할 수 없다
2. 인증을 거쳐야 하는 데이터를 스크랩해서는 안된다

CAPTCHA(구불구불 글자), reCAPTCHA(체크박스)를 통해 웹사이트의 데이터 스크랩 방지

#### 웹 서핑 윤리
1. 공공 API가 있는 경우 항상 API를 사용해라
2. 웹사이트의 소유자를 존중해라

어떤 웹사이트는 스크랩 가능한 항목과 불가능한 항목을 확인할 수 있음
/robots.txt
![[Pasted image 20240130173759.png]]
3. 반복 간격 제한해 서버 과부하 시키지 말기

