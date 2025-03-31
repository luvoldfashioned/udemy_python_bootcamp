# Day 20
# 1. Create a snake body
# 2. Move the snake
# 3. Control the snake

# Day 21
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with tail

# Class Inheritance(클래스 상속)
# 기존 클래스에서 행동과 외형을 상속받는 과정
# Inherit Appearance, Inherit Behaviour
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()    super는 상위 클래스를 나타냄
class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale.")


class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
