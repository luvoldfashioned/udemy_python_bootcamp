 
- ## 0~1사이의 부동 소수점 난수 생성
```
random_float = random.random()

print(random_float)

  

print(random_float * 5) #random.random 부동 소수점 난수의 범위를 0~1 에서 ~5로 확장
```
  



- ## [[Module]]

한 스크립트에 방대한 코드,개별 모듈로 나눔

가져다 쓸 수 있는 코드

random -> 파이썬 팀이 난수를 생성할 수 있도록 개발한 모듈



  
- ## list는 순서가 있다
```
states_of_america = ["Delaware", "Pennsylavania"] 

  

print(states_of_america[0]) #Delaware

print(states_of_america[-1]) #Pennsylaania, 인덱스는 음수도 가능
  

states_of_america[1] = "Pencilvania" #리스트 내 항목 인덱스로 지정해 수정 가능

states_of_america.append("Angelaland") #리스트 마지막 항목으로 추가

states_of_america.extend(["Angelaland", "Jack Nauer Land"]) #여러개의 항목 추가 states_of_america.extend([])
```
  

- 함수를 암기할 필요 없다. 비효율적, 자료를 읽은 후 어떤 작업이 가능할 지 생각해보기. 프로그래밍은 오픈 북 시험이다.

  
```
num_of_states = len(states_of_america)

print(states_of_america[num_of_states - 1]) #print(states_of_america[num_of_states]) -> off-by-one error

  

fruits = ["strawberries", "nectarines", "apples", "Peaches", "Cherries", "Pears"]

vegetables = ["Spinach", "kale", "tomatoes", "celery", "potatoes"]

  

dirty_dozen = [fruits, vegetables]

  

print(dirty_dozen)
```