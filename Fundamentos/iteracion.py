numbers = [1,2,3,4]

for number in numbers:
    print(number)

print([number ** 2 for number in range(1, 11)])


# Alias de una lista
countries = ["United States", "Canada", "Poland", "Germany", "Austria"]

nations = countries
print(id(countries) == id(nations))


countries[0] = "United States of America"

print(nations)

# Diccionario 
students = {
  "Alice": 89.5,
   "Bob": 76.0,
   "Charlie": 92.3,
     "Diana": 84.7,
   "Ethan": 88.9,
 }

for student in students:
     print(student, "->", students[student])


for student in students.keys():
     print(student)

for student in students.values():
      print(student)

# Declaracion break : La instrucción sale inmediatamente
# del bucle y salta a la primera instrucción después del bucle

numbers = [1, 3, 5, 7, 9]
target = 5

for number in numbers:
        print(f"Processing {number}...")
        if number == target:
           print(f"Target found {target}!")
           break

# Continue : La instrucción finaliza la iteración actual y continúa con la siguiente.
# Por ejemplo, si tiene una lista de números y solo desea procesar los pares, puede 
# usar una instrucción para omitir los números impares:

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
     print(f"{number = }")
     if number % 2 != 0:
          continue
     print(f"{number} is Even")

#Bucle anidado For :
for number in range(1, 11):
     for product in range(number, number * 11, number):
        print(f"{product:>4d}", end="")
        print()

my_tuple = (35 ,1.77 ,"Juan" ,"Alex")
print(type(my_tuple))