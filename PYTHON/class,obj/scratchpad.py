class Person:
    def __init__(self,_name,_age):
        self.name = _name
        self.age = _age


    def greet(self,_time):
        print(f'Good {_time}, My name is {self.name}')

obj = Person('Karen',28)

print(obj.name)
print(obj.age)
print(obj.__dict__)
print(obj.__dict__['name'])
print(obj.greet('Evening'))
