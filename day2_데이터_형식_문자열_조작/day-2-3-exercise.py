# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆
# 1year=365days 52weeks 12month
#Write your code below this line 👇

left_year = 90-int(age)
left_day = left_year*365
left_week = left_year*52
left_month = left_year*12
print(f"You have {left_day} days, {left_week} weeks and {left_month} months left.")
"""
message = f"You have {left_day} days, {left_week} weeks and {left_month} months left."
print(message)
"""