"""
*****윤년 조건*****
1. 4로 나뉘어지는 해
2. 100으로 나뉘어지는 경우 제외
3. 100으로 나뉘어지는 경우 중 400으로 나뉘어지는 해
"""

year = int(input("Which year do you want to check?"))

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(f"{year}년은 윤년입니다.")
        else:
            print(f"{year}년은 윤년이 아닙니다.")
    else:
        print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 윤년이 아닙니다.")