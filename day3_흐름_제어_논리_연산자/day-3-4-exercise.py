"""
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries\n")
size = input("What size pizza do you want? S, M, or L\n ")
add_pepperoni = input("Do you want pepperoni? Y or N\n ")
extra_cheese = input("Do you want extra cheese? Y or N\n ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = 15 + 2 + 1
        elif extra_cheese == "N":
            bill = 15 + 2
    
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = 15 + 1
        elif extra_cheese == "N":
            bill = 15

elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = 20 + 3 + 1
        elif extra_cheese == "N":
            bill = 20 + 3
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = 20 + 1
        elif extra_cheese == "N":
            bill = 20

elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            bill = 25 + 3 + 1
        elif extra_cheese == "N":
            bill = 25 + 3
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            bill = 25 + 1
        elif extra_cheese == "N":
            bill = 25
else:
    print("error")

print(f"Your final bill is: ${bill}.")