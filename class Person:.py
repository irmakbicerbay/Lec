class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(f"Hello my name is {self.name}")

p1= Person('Irmak', 19)
print(p1.myfunc)