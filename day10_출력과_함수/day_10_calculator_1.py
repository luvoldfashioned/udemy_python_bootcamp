#Calculator

#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}


num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
calculation_funciton = operations[operation_symbol]
num2 = int(input("What's the second number?: "))
first_answer = calculation_funciton(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")


operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
calculation_funciton = operations[operation_symbol]
second_answer = calculation_funciton(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}") 


# print vs return
# return -> 또 다른 함수의 입력으로 넣을 수 있음 