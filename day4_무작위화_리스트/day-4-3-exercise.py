# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizonal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizonal - 1] = "X"

"""
selected_row = map[vertical - 1]   selected_row == row1 or row2 or row3
selected_row[horizonal - 1] = "X"
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
if position[1] == "1":
    if position[0] == "1":
        map[0][0] = "x"
    elif position[0] == "2":
        map[0][1] = "x"
    elif position[0] == "3":
        map[0][2] = "x"
elif position[1] == "2":
    if position[0] == "1":
        map[1][0] = "x"
    elif position[0] == "2":
        map[1][1] = "x"
    elif position[0] == "3":
        map[1][2] = "x"
elif position[1] == "3":
    if position[0] == "1":
        map[2][0] = "x"
    elif position[0] == "2":
        map[2][1] = "x"
    elif position[0] == "3":
        map[2][2] = "x"
"""

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")