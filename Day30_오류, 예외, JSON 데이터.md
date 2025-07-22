## [[Catching Exceptions]]
예외 포착하기

#### [[try(Catching Exceptions)]]: Something that might cause an exception
	예외를 유발할 수 있는 뭔가를 실행하는 코드 블록

#### [[except(Catching Exceptions)]]: Do this if there was an exception
	만약에 예외가 있었다면 컴퓨터가 실행하게 하려는 블록
##### "'except'를 단독으로 사용하지 마시오'"
![[Pasted image 20231115151844.png]]
- KeyError를 무시하고 계속 진행해서 'a_file.txt' 생성
```
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdf"])  # KeyError

# 모든 에러 무시
except:
    file = open("a_file.txt", "w")
    file.write("Something")
```

###### 특정한 상황 잡기
```
try:
    file = open("a_file.txt")  # FileNotFound
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdf"])  # keyerror

# except:   모든 에러 무시
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
```
![[Pasted image 20231115152933.png]]
%%KeyError%%

###### 다수의 예외
```
try:
    file = open("a_file.txt")  # FileNotFound
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdf"])  # keyerror

# except:   모든 에러 무시
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError:
    print("That key does not exist.")
```
![[Pasted image 20231115152834.png]]
###### 예외를 잡고 여전히 오류 메시지를 받으려면
```
try:
    file = open("a_file.txt")  # FileNotFound
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdf"])  # keyerror
    
# except:   모든 에러 무시
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_message:
    print(f"the key {error_message} does not exist.")
```
![[Pasted image 20231115153500.png]]


#### [[else(Catching Exceptions)]]: Do this if there were no exceptions
	예외가 없었을 때 실행할 코드
```
# 예외가 없을 때
else:
    content = file.read()
    print(content)
```

#### [[finally(Catching Exceptions)]]: Do this no matter what happens
	기본적으로 어떤 일이 일어나더라도 실행해야 할 블록
```
# 어떤 일이 일어나도 실행
finally:
    file.close()
    print("File was closed.")
```

#### [[raise(Catching Exceptions)]]
자신만의 예외 만들기
```
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
```
![[Pasted image 20231115160719.png]]


### [[JSON]]
JavaScript Object Notation
- 데이터 전송 방법으로 널리 사용
- 네스티드 리스트와 딕셔너리들로 구성
- #### Write
	[[json.dump()]]
```
	new_data = {
        website: {
            "email": email,
            "password": passwor
        }
    }
	with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
```
![[Pasted image 20231115211653.png]]

- #### Read
	[[json.load()]]
	- json데이터를 취해서 파이썬 딕셔너리로 변환
```
with open("data.json", "r") as data_file:
	data = json.load(data_file) -> type = dict
	print(data)
```
![[Pasted image 20231115213054.png]]

- Update
	[[json.update()]]
```
with open("data.json", "r") as data_file:
	# Reading old data
	data = json.load(data_file)
	# Updating old data with new data
	data.update(new_data)

with open("data.json", "w") as data_file:
	# Saving update data
	json.dump(data, data_file, indent=4)
```

##### 파일이 없거나 내부에 데이터가 없다면
```
try:
	with open("data.json", "r") as data_file:
		# Reading old data
		data = json.load(data_file)

except FileNotFoundError:
	with open("data.json", "w") as data_file:
		json.dump(new_data, data_file, indent=4)

else:
	data.update(new_data)
	with open("data.json", "w") as data_file:
		# Saving update data
		json.dump(data, data_file, indent=4)

finally:
	website_entry.delete(0, END)
	password_entry.delete(0, END)
```

#### 다른 쉬운 대안이 없을 때만 예외 처리
==쉽게 할 수 있다면 가급적 if와 else 사용==
- exception -> 아주 드물게 발생하는 뭔가
- if, else -> 아주 드물게 발생하는 뭔가 
```
try:
	with open("data.json") as data_file:
		data = json.load(data_file)
		
except FileNotFoundError:
	messagebox.showinfo(title="Error", message="No Data File Found.")
	
else:

	if website in data:
		email =data[website]["email"]
		password = data[website]["password"]
		messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
		
	else:
		messagebox.showinfo(title="error", message=f"No details for {website} exists")
```