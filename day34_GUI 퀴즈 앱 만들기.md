`tkinter` 모듈에서 `Label` 위젯과 `Canvas` 위젯의 `create_text` 메서드를 사용하여 텍스트를 생성하는 두 가지 주요 차이점이 있습니다.

1. **위치 지정 방법:**
   - **Label:** `Label` 위젯을 사용하면 텍스트의 위치를 `pack`, `grid`, 또는 `place` 메서드를 통해 부모 위젯 내에서 조절합니다. `pack` 및 `grid`의 경우, 부모 위젯의 레이아웃 관리자에 따라 위치가 결정됩니다.
   
     ```python
     label = Label(root, text="Hello, Tkinter!")
     label.pack()  # 또는 label.grid(), label.place()
     ```

   - **Canvas:** `Canvas` 위젯에서는 `create_text` 메서드를 사용하여 텍스트의 좌표를 직접 지정합니다.

     ```python
     canvas = Canvas(root, width=200, height=100)
     canvas.create_text(100, 50, text="Hello, Tkinter!")
     canvas.pack()
     ```

   각각의 방식은 텍스트를 표시하는 위치를 다르게 지정합니다.

2. **기능 및 확장성:**
   - **Label:** `Label` 위젯은 단순한 텍스트 표시 위젯이며, 주로 간단한 텍스트를 표시하기 위해 사용됩니다. `Label`에는 텍스트 이외의 다양한 옵션이 있지만, 일반적으로 복잡한 그래픽 렌더링이나 상호 작용을 위한 확장적인 기능은 제한적입니다.

   - **Canvas:** `Canvas` 위젯의 `create_text` 메서드는 그래픽 요소를 그리는 범용적인 기능을 제공합니다. 이를 사용하면 텍스트뿐만 아니라 다양한 그래픽 요소를 표시하고 조작할 수 있습니다. `Canvas`는 그림, 도형, 애니메이션 등 다양한 기능을 지원하여 더 많은 제어와 확장성을 제공합니다.

따라서 간단한 텍스트 표시가 목적이라면 `Label`을 사용하는 것이 간단하고 편리하며, 더 복잡한 그래픽 요소를 그리고 제어해야 할 경우에는 `Canvas`와 `create_text` 메서드를 사용하는 것이 더 적합합니다.



### [[Type hints]]

`age: int`
변수의 데이터형을 선언하고 그대로 둘 수 있다

```
def police_check(age: int):
	if age > 18:
		can_drive = True
	else:
		can_drive = False
	return can_drive

...

if police_check("twelve"):
	print("You may pass")
else:
	print("Pay a fine")

```
![[Pasted image 20231205192429.png]]

#### 리턴 유형 지정
```
def greeting(name: str) -> str:
	return 'Hello' + name
```
