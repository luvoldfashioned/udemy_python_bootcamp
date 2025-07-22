## [[TKinter]]
파이썬 내장 GUI 모듈
```
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# keep the window on screen
window.mainloop()
```

### [[TKinter widget]]
###### [[tkinter.Label]]
###### [[tkinter.Button]]
###### [[tkinter.Entry]]
###### [[tkinter.Text]]
###### [[tkinter.Spinbox]]
###### [[tkinter.Scale]]
###### [[tkinter.Checkbutton]]
###### [[tkinter.Radiobutton]]
###### [[tkinter.Listbox]]

### [[TKinter 레이아웃 매니저]]
##### [[pack()]]
- place it in to the screen, automaticaly center it on the screen
- The Packer -> 배치 관리 시스템(geometry-management mechanisms)
- https://docs.python.org/3/library/tkinter.html#the-packer
- 단점: 위치를 정확하게 명시하기 어렵다

##### [[place()]]
- 정확한 위젯 위치선정(x, y값 제공)
- 단점: 여러개의 위젯을 정확한 위치를 구상해 배치하는 것이 어려움
`my_label.place(x=0, y=0)`

##### [[Grid()]]
- 다른 컴포넌트와 연관이 있음
- 원하는 위젯을 왼쪽 윗부분에서부터 배치
- ==gird와 pack은 같은 프로그램에서 쓸 수 없음

```
# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(row=0, column=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# Entry
input = Entry(width=10)
input.grid(row=2, column=2)
```

|Label |      |     |
|------|------|------|
|      | Button | |
|      |        | Entry|

![[Pasted image 20231107123426.png]]

### [[padding]]
여유 공간을 추가
`window.config(padx=20, pady=20)`
![[Pasted image 20231107125453.png]]
(가장자리에 여유가 생김)

- 특정 위젯 주위에만 패딩을 추가
`my_label.config(padx=50, pady=50)`

## [[Advanced Python Arguments]]
더 다양한 범위의 입력을 구체적으로 명시

#### [[Arguments with Default Values]]
기본 값을 갖는 인수, 함수 선언 시 디폴트 값 설정
선택적 인수에 대해 디폴트 값을 제공하는 방법
```
def my_function(a=1, b=2, c=3)
	# Do this with a
	# Then do this with b
	# Finally do this with c
```
![[Pasted image 20231106162101.png]]
(optional) -> 실제로 디폴트 값을 갖고 있기 때문

### [[아스테리스크 arg]]
\*args(argument, 인수)
- Unlimited Arguments(무제한 위치 인자)
- Unlimited Positional Arguments -> `arg[0]`
- 여러 개의 인수를 취할 수 있는 함수를 만드는 법
- 함수 add가 **몇개의 인수라도 허용한다는 뜻**
- type(args) -> [[Tuple]]
```
def add(*args):
	for n in args:
			print(n)
```


## [[이중 아스테리스크 kwargs]]
\*\*kwargs(keyword argument, 키워드 인수)
- 위치(positional)가 아니라 이름(keyword)으로 인수를 언급
- 무제한 키워드 인자
- type(kwargs) -> [[dictionary]]
```
def calculate(**kwargs):
	print(type(kwargs))

calculate(add=3, multiply=5)
```

```
def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculator(2, add=3, multiply=5)
```

#### [[tkinter.Lable()과 turtle.write( )의 작동방식]]
`tkinter.Lable()`
![[Pasted image 20231106172915.png]]
- TKinter 모듈은 파이썬의 문법과 많이 다른 TK라고 불리는 다른 기술에서 복제됨
- 작동하기 위해 기본적으로 TK명령을 사용
- 모든 선택 사항들을 취해서 \*\*kwargs나 선택적 키워드 인수로 바꿈
- 때문에 TKinter모듈에서 레이블을 생성하거나 
	pack 메소드를 호출할 때 \*\*kw 외에 수정할 수 있는 
	어떤 프로퍼티도 나타나지 않음

`turtle.write()`
![[Pasted image 20231106172854.png]]
turtle: 파이썬에서 생성 -> 디폴트 형태를 갖고 visible boolean을 갖고 있어서 프롬포트에서 볼 수 있는
모든 프로퍼티들을 설정할 수 있음

## [[많은 선택적 키워드 인수를 갖는 클래스를 생성하는 법]]

```
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        
my_car = Car(make="Nissan")
print(my_car.model)
```
- 인수들 중 하나를 구체적으로 명시하지 않았을 때
- `my_car = Car(make="Nissan")`  model 명시X
![[Pasted image 20231106173238.png]]
%%error%%

해결법: kw.get()
get함수는 딕셔너리 안에 키가 존재하지 않으면 ==아무 것도 반환하지 않고 오류가 발생하지 않음==.
```
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.colour)
```
![[Pasted image 20231106175310.png]]
명시하지 않은 인수에 대해서 `None` 반환