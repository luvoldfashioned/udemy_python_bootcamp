weather_c = eval(input())
# 🚨 Don't change code above 👆

# Write your code 👇 below:
weather_f = {week: (c*9/5)+32 for (week, c) in weather_c.items()}


print(weather_f)
