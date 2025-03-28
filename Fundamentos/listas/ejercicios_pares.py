
import cProfile

# Muestre los numeros pares de mi lista

#num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#pares = [i for i in num if i % 2 == 0]

#print(pares)

# Ordenas una lista 
def ordenar_lista():
    my_list = [8, 10, 6, 2, 4]  # lista a ordenar
    swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
    while swapped:
         swapped = False  # no hay intercambios hasta ahora
         for i in range(len(my_list) - 1):
              if my_list[i] > my_list[i + 1]:
                 swapped = True  # ¡ocurrió el intercambio!
                 my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

    return my_list
print(ordenar_lista())

cProfile.run('ordenar_lista()')