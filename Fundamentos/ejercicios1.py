
import time

inicio1 = time.time()
class Person:

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


myperson = Person("Alex", "Salinas")
print(myperson.name)
print(myperson.lastname)
fin1 = time.time()



inicio2 = time.time()
class persa:
    def __init__(self,name,lastname):
        self.full_name = f"{name} {lastname}" #public
        self.__name = name #private

    def walk(self):
       return print(f"{self.full_name}   {self.__name} is Walking")

persa = persa("Alex", "Salinas")
print(persa.full_name)
correr = persa.walk()
#print(correr)
fin2 = time.time()

print(f"Tiempo de ejecución de la clase Person: {fin1 - inicio1}")
print(f"Tiempo de ejecución de la clase persa: {fin2 - inicio2}")

x = 1 / 2 + 3 // 3 + 4 ** 2

print(x)



