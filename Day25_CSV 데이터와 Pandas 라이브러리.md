
## [[CSV]]
콤마로 분류된 값
표 형태로 된 데이터를 대표하는 일반적인 방식
스프레드 시트같은 표들에 적합한 데이터
```
import csv      # 내장 라이브러리  

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)  # object 생성
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
```

## [[Pandas]]
데이터 분석 라이브러리
```
import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"]) # 첫번째 줄을 열의 제목으로 사용하면 자동식별
```
%%
//////output//////
         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny
___________________________
0    12
1    14
3    14
4    21
5    22
6    24
%%

## [[Pandas datatype]]
```
type(data)              # DataFrame
type(data["temp"])      # Series
```

## [[DataFrame]]
- 전체 표와 같은 것
- 엑셀 파일이나 구글 시트에 있는 각각의 시트들은 DataFrame으로 간
![[Pasted image 20231023121820.png]]

## [[Series]]
- 리스트와 같은 것, 표에서 한 열과 같은 것
![[Pasted image 20231023121838.png]]

## [[get Data in Columns]]

`print(data["condition"])`
- 거의 딕셔너리로 취급
- 열에 있는 이름과 똑같아야 함
-  대소문자 구분 주의

`data.condition`
- Pandas가 각각의 열과 칼럼명을 가져가서 attribute로 변환
- 좀 더 객체(object)에 가깝게 취급

%%출력 값은 동일함%%

## [[get Data in Rows]]

`print(data[data.day == "Monday"])`

```
# Print the row of data which had the highest temperature.
print(data[data.temp == data.temp.max()])
```

```
# Convert Monday's temperature to Fahrenheit
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 1.8 + 32
print(monday_temp_F)
```

## [[Create a Dataframe from scratch]]
```
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
```

## [[Create csv file]]
`data.to_csv("new_data.csv")`