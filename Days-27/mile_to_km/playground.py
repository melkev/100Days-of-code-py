def add(*args):
    print(*args)
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 6, 7, 8))

def calculate(n, **kwargs):
    # print(type(kwargs))
    # for key, val in kwargs.items():
    #     print(key)
    #     print(val)
        
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2, add= 3 , multiply=5)

class Car:
    
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        
        
my_car = Car( model="gt-r")
print(my_car.make)