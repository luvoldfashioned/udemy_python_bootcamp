
## [[Import]]

### Basic import (한 두 번 사용할 때)
```
import turtle
tim = turtle.Turtle()
```
### from ... import...   (모듈에 포함된 무언가를 여러번 사용할 때)
```
from turtle import Turtle
tim = Turtle()
```
##### from turtle import * (모듈 안의 모든 것을 현재 파일 내에 있는 것처럼 사용
단점: 클래스 또는 메소드가 어디서 왔는 지 확인하기 어려움
`forward(100)

### 모듈([[Module]]) 별칭 지정
```
# import turtle as t
# tim = t.Turtle()
```

### Python [[tuple]]
`my_tuple = (1, 3, 8)`
tuple은 값을 변경할 수 없다

### 변경하기를 원하면 리스트로 변환
`list(my_tuple)`