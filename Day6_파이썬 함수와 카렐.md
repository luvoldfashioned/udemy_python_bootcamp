
- ## 함수뒤엔 ()가 붙음
```
print() 
```


```
def my_function():

    print("Hello")

    print("Bye")

  

my_function()
```
  

- ## 전체 블록을 들여쓰기 하는 법: ctrl + ] or ctrl + [

  

- ## [[indentation]]

spaces vs tabs

4 spaces


```
While something_is_true:

    #do this

    #then do this

    #then do this
```
  

## [[for vs while]]

- for: 어떤 것을 반복하고 반복하는 각 아이템에 대해 뭔가를 해야 할 때 유용
```
fruits = ["Apple", "Pear", "Orange"]
	for fruit in fruits:
		print(fruit)
```
  

- while: 특정 작업을 설정한 조건에 도달할 때 까지 수없이 반복수행할 때

- ==for는 실행 횟수를 사전에 설정해놓지만, while은 조건이 거짓으로 전환될 때 까지 무한반복