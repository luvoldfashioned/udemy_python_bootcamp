import pandas

student_dict = {
    "student": ["Angela", "James", "lily"],
    "score": [56, 76, 98]
}

# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Loop through a dataframe
# # 단지 열의 이름을 반복하여 열에 있는 데이터를 보여준것이기 때문에 유용하지 않음
# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of a data frame
# iterrows() 각 열 대신에 데이터 프레임에 있는 각 행을 반복 실행할 수 있게 해줌
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # 각각의 행들은 판다스 시리즈의 객체임
    # 행을 이용할 수 있고 점 표기법을 사용해서 특정 열 아래에 있는 값을 구할 수 있음
    # print(row)
    if row.student == "Angela":
        print(row.score)
