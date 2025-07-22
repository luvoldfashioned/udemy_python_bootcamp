
## [[List Comprehension]]

`new_list = [new_item for item in list]`
- 파이썬에 있는 아주 독특한 특징
- 코드를 훨씬 더 짧게 쓸 수 있으며 읽기도 더 쉽다

%% 
For Loop
```
numbers = [1,  2, 3]
new_list = []
for n in numbers:
	add_1 = n + 1
	new_list.append(add_1)
```
=List Comrehension
```
numbers = [1, 2, 3]
new_list = [n+1 for n in numbers]
```
%%

```
name = "Angela"
new_list = [letter for letter in name]
```

![[Pasted image 20231101162712.png]]

### [[Python Sequnences]]
- [[list]], [[range]], [[string]], [[tuple]] 등
- 명확하게 순서를 갖고있음

### [[Conditional List Comprehension]]
`new_list = [new_item for item in list if test]`

```
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", " Freddie"]
short_names = [name for name in names if len(name)<5]
```
## [[Dictionary Comprehension]]
`new_dict = {new_key:new_value for item in list}`
`students_scores = {student: random.randint(0, 100) for student in names}**`
`new_dict = {new_key:new_value for (key, value) in dict.items()`

### [[Conditional Dictionary Comprehension]]
`new_dict = {new_key:new_value for (key, value) in dict.items() if test}`
```
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
```

### [[Pandas DataFrame에서 반복하는 방법]]

```
student_dict = {
    "student": ["Angela", "James", "lily"],
    "score": [56, 76, 98]
}
```

##### Loop through dictionaries:
```
for (key, value) in student_dict.items():
    print(value)
```

```
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
```

##### Loop through a [[dataframe]]
- 단지 열의 이름을 반복하여 열에 있는 데이터를 보여주는 것이기 때문에 유용하지 않음
```
for (key, value) in student_data_frame.items():
    print(key)
    print(value)
```

![[Pasted image 20231105204633.png]]

##### Loop through rows of a [[dataframe]]
- [[iterrows()]]
- 각 열 대신에 [[DataFrame]]에 있는 각 행을 반복 실행할 수 있게 해줌
- 각각의 행들은 [[Pandas]] [[Series]]의 [[object]]임
- 행을 이용할 수 있고 점 표기법을 사용해서 특정 열 아래에 있는 값을 구할 수 있음
```
for (index, row) in student_data_frame.iterrows():
    print(index)
```

```
for (index, row) in student_data_frame.iterrows():
	print(row)
```
![[Pasted image 20231105204841.png]]

```
if row.student == "Angela":
	print(row.score)
```
![[Pasted image 20231105204913.png]]
       