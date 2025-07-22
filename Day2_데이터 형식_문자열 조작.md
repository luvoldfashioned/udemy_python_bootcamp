
- ##  **sub_script**
```
print("Hello"[4])
```
- ## string
```
print("123"+"345")  
```
- ## **integer**
```
print(123+345)  
```
  
- ## **파이썬에서 큰 숫자의 반점을 '_'로 표시 가능**
```
print(123_456_789)  
```

- ## **float**
```
3.14159 
```

- ## **boolean**
```
True / False   
```

- ## ==Ctrl + / 를 통해 한 줄 주석 처리 가능
```
num_char = len(input("what is your name?"))  
```

- ## **TypeError: can only concatenate str**
```
print("your name has " + num_char + " characters.")
(not "int") to str



num_char = str(len(input("what is your name?")))

print("your name has " + num_char + " characters.")
```

  
- ## ==type함수로 데이터 형식 확인 가능
```
print(type(num_char)) 
```
  
- ## ==나누면 값은 float형태로 반환
```
print(6/3)
```

- ## 거듭제곱
```
print(2**3)
```
  
- ## ==round함수로 반올림, 콤마를 통해 반올림할 자릿수 지정
```
print(round(8 / 3, 2)) 
```
  
```
result = 4/2

result /= 2

print(result)

  

score = 0

score += 1

print(score)
```
  

- ## [[F-string]]
```
score = 0

height = 1.8

isWinning = True

# f-string 문자열 앞에 f를 붙이고 다른 형식의 데이터를 {}안에 넣으면 알아서 변환
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
```