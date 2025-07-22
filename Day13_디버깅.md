

[[How to Debugging]]
## 1. Describe Problem(문제 그려보기)
```
def my_function():
   for i in range(1, 21):          # (1, 20) x
     if i == 20:
       print("You got it")

my_function()
```
  

## 2. Reproduce the Bug(버그 재현하기)
```
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])
```
  

## 3. Play Computer(컴퓨터 입장에서 생각해보기)
```
year = int(input("What's your year of birth?"))

if year > 1980 and year <= 1994:
	print("You are a millenial.")
elif year > 1994:
	
print("You are a Gen Z.")
```
  

## 4. Fix the Errors(오류 수정하기 -빨간 줄 주목)
```
age = int(input("How old are you?"))

if age > 18:
	print(f"You can drive at age {age}.")
```
## 5. Print is Your Friend(print() 구문 사용)
```
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page

print(total_words)
```
  

## 6. Use a Debugger(디버거 활용)
```
def mutate(a_list):
   b_list = []
   for item in a_list:
	   new_item = item * 2
	   b_list.append(new_item)
	   print(b_list)

mutate([1,2,3,5,8,13])
```
  
  

## 7. Take a Break

## 8. Ask a Friend

## 9. Run Often(코드를 자주 실행)

## 10. Ask StackOverflow