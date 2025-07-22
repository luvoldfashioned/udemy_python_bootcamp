
## [[Scope]]
```
enemies = 1

  

def increase_enemies():

  enemies = 2

  print(f"enemies inside function: {enemies}")

  

increase_enemies()

print(f"enemies outside function: {enemies}")
```
  

## Local Scope
```
def drink_potion():

  potion_strength = 2             #local var

  print(potion_strength)

  

drink_potion()

#print(potion_strength)
```
  

## Global Scope
```
player_health = 10                  #namespace: 이름을 지정한 대상이 특정 범위 안에서 유효

  

def game():  

  def drink_potion():            #game 함수 내부에 지역 범위를 가짐

    potion_strength = 2

    print(player_health)

  

drink_potion()

print(player_health)
```
  
  

## There is no Block Scope
```
# if 3 > 2:

# a_variable = 10  
#if, while, for 내부의 변수, 들여 쓰기 한 모든 코드의 블록이라면 울타리로 치지 않음.

game_level = 3

enemies = ["skeleton", "Zombie", "Alien"]

if game_level < 5:

  new_enemy = enemies[0]

  

print(new_enemy)

  

game_level = 3

def create_enemy():

  enemies = ["skeleton", "Zombie", "Alien"]

  if game_level < 5:

    new_enemy = enemies[0]

  

  print(new_enemy)

# print(new_enemy)          -> error, 함수 내부에는 지역 범위가 있다
```
  
  

## Modifying Global Scope
```python
enemies = 1

  

def increase_enemies():

  global enemies                #전역 변수를 가지고 있다고 명시

  enemies += 1                  #전역 변수를 수정

  print(f"enemies inside function: {enemies}")

  

increase_enemies()

print(f"enemies outside function: {enemies}")

  

#전역 범위를 가진 무언가를 수정하기 까다로움

#전역 범위를 가진 변수는 코드 안 어디서든 만들 수 있으며 코드를 작성한 시기 사이에 며칠이 걸렸을 수도 있기 때문에 버그와 오류가 잘 생김

#전역 범위를 수정해서 읽을 수 있다면 문제가 없지만, 지역 범위를 가진 함수 내부에서 수정하지 말 것
```
  

## solution
```
enemies = 1

  

def increase_enemies():

  print(f"enemies inside function: {enemies}")

  return enemies+1                                   #return을 이용

  

enemies = increase_enemies()

print(f"enemies outside function: {enemies}")

  
  

#전역 범위를 가진 변수를 다룰 때는 주의를 기울여야 함

#전역 범위를 쓰면 안되는건 아님

#정수를 정의할 때 전역 범위는 특히 유용함
```
  
## 상수를 구별할 때 대문자로 명명
```
PI = 3.14159           

URL = "https://www.google.com"
```