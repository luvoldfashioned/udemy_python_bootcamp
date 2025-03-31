# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
add = 0
persons = 0

for i in student_heights:
    add += i
    persons += 1

print(add/persons)

"""
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height/number_of_students)   round(number [, ndigits]) -> 소수점 자리에서 반올림
print(average_height)
"""