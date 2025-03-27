##  Clases  ##

class Myclassempty:
    pass

print(Myclassempty)
print(Myclassempty())

class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


myperson = Person("Alex", "Salinas")
print(myperson.name)
print(myperson.lastname)

