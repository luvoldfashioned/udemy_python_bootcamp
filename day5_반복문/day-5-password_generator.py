#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡmy codeㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
password = []

for l in range(1, nr_letters+1):
    rand_letter = random.randint(0, len(letters)-1)
    password.append(letters[rand_letter])
for s in range(1, nr_symbols+1):
    rand_symbol = random.randint(0, len(symbols)-1)
    password.append(symbols[rand_symbol])
for n in range(1, nr_numbers+1):
    rand_num = random.randint(0, len(numbers)-1)
    password.append(numbers[rand_num])

print("".join(password))
"""


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡsolution codeㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
password = ""

for char in range(1, nr_letters+1):
    password += random.choice(letters)                 #몰랐던 부분
for char in range(1, nr_symbols+1):
    password += random.choice(symbols) 
for char in range(1, nr_numbers+1):
    password += random.choice(numbers)     

print(password)






#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"""
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡmy codeㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

password = []

for l in range(1, nr_letters+1):
    rand_letter = random.randint(0, len(letters)-1)
    password.append(letters[rand_letter])
for s in range(1, nr_symbols+1):
    rand_symbol = random.randint(0, len(symbols)-1)
    password.append(symbols[rand_symbol])
for n in range(1, nr_numbers+1):
    rand_num = random.randint(0, len(numbers)-1)
    password.append(numbers[rand_num])

random.shuffle(password)  #list 변수 랜덤정렬
print("".join(password))
"""

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡsolution codeㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
password_list = []

for char in range(1, nr_letters+1):
    password_list += random.choice(letters)                 #  == password_list.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols) 
for char in range(1, nr_numbers+1):
    password_list += random.choice(numbers)     

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(password)