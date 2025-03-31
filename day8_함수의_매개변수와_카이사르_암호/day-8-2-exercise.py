#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number-1):
        if number%i == 0:
            #not a prime
            is_prime = False
    #is a prime
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



