```
def my_function():

    result = 3*2

    return result
```
  

## ==Return as an early exit
```
def format_name(f_name, l_name):

    #docstrings

    """Take a first and last name and format it

    to return the title case version of the name."""              #여러줄로 작성 가능

    if f_name == "" or l_name == "":

        return "You didn't provide valid inputs."     #조기리턴 -> 함수 조기에 종료 시키기

    formated_f_name = f_name.title()

    formated_l_name = l_name.title()

  

    return f"{formated_f_name} {formated_l_name}" #return -> 함수의 마지막으로 인지

  

print(format_name(input("What is your first name? "), input("What is your last name? ")))
```
  
## ctrl + /로 여러 줄 주석처리