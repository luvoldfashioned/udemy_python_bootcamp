
# [[File]]
파일
## [[open()]]
```
file = open("my_file.txt")
contents = file.read()
print(contents)

file.close() -> 파일을 열면 기본적으로 컴퓨터 자원을 차지해서 닫아줘야 함
```

## [[with]] 키워드
with 키워드는 파일을 직접 관리하기 때문에 파일을 수동적으로 닫지 않아도 됨
```
with open("my_file.txt") as file:  # f로 써도 됨
    contents = file.read()
    print(contents)
```

## [[write()]]
- r(read)->읽기 모드 / w(write)->파일에 있는 것 지우고 쓰기 / a(append)->추가하기
- 쓰기 모드에서 파일을 열려고 하는데 파일이 존재하지 않으면 파일을 만듦
```
with open("my_file.txt", mode='w') as file: 
	file.write("new text.")
```

# [[Paths]]
경로

## [[Absolute File Path(절대 파일 경로)]]
루트(/)를 기준으로 시작
>/
>/Work
>/Work/report.ppt
>/Work/Project
>/Work/Project/talk.ppt

## [[Relative File path(상대 파일 경로)]]
working directory(현재 작업하고 있는 디렉토리나 폴더)
%%
working directory가 /Work/Project
>./talk.ppt

working directory가 /Work
>./Project/talk.ppt

working directory가 /Work/Project에서 상위 폴더 내 report.doc
>../report.doc

같은 working directory 내 파일에 접근할 때
>./report.doc  = report.doc

%%

## [[windows와 mac의 파일 경로 차이]]
window -> 각각의 폴더들이  \\(슬래시)로 구분 됨
mac -> 각각의 폴더들이 /(슬래시)로 구분 됨
python -> OS 상관없이 /(슬래시)