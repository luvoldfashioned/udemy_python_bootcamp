# def add(*args):
#     result = 0
#     for n in args:
#         result += n
#     return result


# print(add(5, 6, 1, 4))

# def calculator(**kwargs):
#     print(type(kwargs))


# calculator(add=3, multiply=5)

def calculator(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculator(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.colour)
