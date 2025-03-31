'''
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."


TRUE
LOVE
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
first_user_lowercase = name1.lower()    #"str".lower -> 소문자로 변환
second_user_lowercase = name2.lower()
add_name = first_user_lowercase + second_user_lowercase
print(add_name)

occur_true = add_name.count("t") + add_name.count("r") + add_name.count("u") + add_name.count("e")     #"str".connt -> 문자 개수 새기
occur_love = add_name.count("l") + add_name.count("o") + add_name.count("v") + add_name.count("e")
score = str(occur_true) + str(occur_love)

if int(score)>=90 or int(score)<=10:
    print(f"your score is {score}, you go together like coke and mentos.")
elif int(score)>=40 and int(score)<=50:
    print(f"your score is {score}, you are alright together")
else:
    print(f"your score is {score}.")    

