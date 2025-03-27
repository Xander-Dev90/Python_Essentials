# Description: List methods in Python
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[1:5])  # [2, 3, 4, 5]
print(list[1:9:2]) # [2, 4, 6, 8]
print(list[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Metodos en listas

list.append("1")
list.insert(0, "@")
print(list)

#recorrer una lista
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0
for i in range(len(list2)):
    i += 1
 

print(i)

# Comprension de listas( List Comprehension)
animales=["perro","gato","loro","pez"]
animales_mayus=[animales.upper() for animales in animales] # 
print(animales_mayus)


