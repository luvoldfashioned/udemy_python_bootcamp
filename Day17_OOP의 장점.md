
## [[Cases]]
PascalCase: 각 단어의 첫번째 글자 대문자(클래스 명)
camelCase: 두번째 단어부터 첫번째 글자 대문자(파이썬에서 별로 사용안함)
snake_case: 모든 단어 소문자, 단어를 _로 분리

## [[How create Class]]
```
class User:
    # pass 함수나 클래스를 비워두는 키워드
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username  # parameter 이름과 attribute 이름이 같은 것이 관행
        self.followers = 0    # 기본값 설정
        self.following = 0

# 메소드는 함수와 다르게 항상 첫 매개변수로 self 매개변수가 있어야 함
    def follow(self, user):
        user.followers += 1
        self.following += 1   
# self: 클래스 청사진 내부에서 클래스로부터 만들어지는 객체를 지칭

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
```

## [[How create attribute]]
```
user_1.id = "001"
user_1.username = "angela"
```



## [[Constructor]](생성자)
- 청사진의 일부, 객체가 생성될 때 무슨 일이 일어나야 하는지 명시할 수 있게 함
- 객체가 초기화 될 때 변수나 카운터의 시작값을 지정할 수 있음
- 생성자 생성 -> init 함수 사용
```
# class Car:

#     def __init__(self):

#     #initialise attributes(속성 초기화)
```

## Constructor에서 [[attribute]] 생성
```
class Car:
	def __init__(self, seats):    self: 만들어지고 있는, 또는 초기화되고 있는 실제 객체
		self.seats = seats        seats(parameter): 클래스로부터 객체가 생성될 때 전달됨,

# 데이터를 통해 객체의 속성값 설정 가능

# my_car = Car(5)    (== my_car.seats = 5)          call constructor

# 같은 속성을 가지는 객체를 많이 만들 때 이용하면 훨씬 더 빠르게 만들 수 있음
```

  
## [[method]](객체에 속하는 함수)
```
class Car:
	def enter_race_mode():
		self.seats = 2
my_car.enter_race_mode()
```
