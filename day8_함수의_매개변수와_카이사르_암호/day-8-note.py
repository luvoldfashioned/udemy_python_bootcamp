# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("hello")
    print("hello")
    print("hello")

greet()

#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do? {name}")

greet_with_name("Angela")
#name = parameter / Angela = argument

#Functions with more than 1 input   
def greet_with(name, location):
    print(f"hello {name}")
    print(location)

greet_with("ysb", "jinjeop")
greet_with(name="ysb", location="jinjeop ") #Keyword Arguments my_function(a=1, b=2, c=3)


