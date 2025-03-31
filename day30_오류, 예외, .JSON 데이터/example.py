# # FileNotFound

# try:
#     file = open("a_file.txt")  # FileNotFound
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])  # keyerror
# # except:   모든 에러 무시
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist.")
# # 예외가 없을 때
# else:
#     content = file.read()
#     print(content)
# # 어떤 일이 일어나도 실행
# finally:
#     raise KeyError("This is an error that I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
