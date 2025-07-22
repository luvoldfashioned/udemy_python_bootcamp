
## [[Higher Order Function(고차함수)]]

- 다른 함수와 함께 작동하는 함수
```
def calculator(n1, n2, func):
   return func(n1, n2)

result = calculator(2, 3, add)
```


## [[Instance]]

- 하나의 [[Class]]를 통해 생성한 n개의 객체를 별개의 인스턴스라고 부름
- 각 개체가 어느 한 순간에 다른 속성을 지닐 수 있으며, 각기 다른 메소드를 수행할 수 있다는 사실을 객체의 [[상태(State)]] 라고 부름

-  예) turtle 클래스의 객체([[Object]]) timmy의 색상 속성 상태는 초록색이고, tommy의 색상 속성은 보라색

- 두 객체가 속성([[attribute]]) 즉 모양 면에서 다른 [[상태(State)]]를 지니고 있음
`screen.listen()


### 직접 생성하지 않은 메소드를 사용할 때에는 position argument보다 keyword argument를 사용하는게 좋음

`screen.onkey(key="space", fun=move_forwards)  # 함수의 인수로 함수를 전달할 때에는 () 붙이지 않음


`screen.exitonclick()