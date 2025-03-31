# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #split() 문자열을 특정 기호로 구분하여 리스트에 저장하는 함수
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
parameter = len(names)-1
print(parameter)
random_num = random.randint(0,parameter)
print(random_num)
pay_name = names[random_num]
print(f"{pay_name} is going to buy the meal today!")

"""
pay_name = random.choice(names)
print(f"{pay_name} is going to buy the meal today!")
"""