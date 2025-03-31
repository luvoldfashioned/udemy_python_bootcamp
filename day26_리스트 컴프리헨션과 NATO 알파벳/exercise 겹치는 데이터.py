with open("file.1.txt", "r") as f1:
    f1_list = f1.read().splitlines()
with open("file.2.txt", "r") as f2:
    f2_list = f2.read().splitlines()

result = [int(num) for num in f1_list if num in f2_list]

# Write your code above 👆
print(result)
