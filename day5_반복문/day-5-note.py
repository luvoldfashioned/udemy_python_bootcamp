fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)

"""
range
for number in range(a, b):
    print(number)
"""

for number in range(1, 10):       
    print(number)                   #출력값은 1~9

for number in range(1, 11, 3):      #3은 증가 크기
    print(number)           

total = 0
for number in range(1, 101):
    total += number

