
##  Sets, list and tuples##
my_list= list();
my_other_list=[];

my_tuples=tuple();
my_other_tuple=();

my_set= set();
my_other_set={}; # Inicialmente es un diccionario

print(type(my_set));  # Es un set no es una estructura ordenanda
print(type(my_other_set));  # Es un diccionario
print(type(my_tuples)); # Es una tupla

my_other_set={"KLips","KLips","KLips"};  # Es un set y solo acepta valores unicos
my_list_set= list(my_other_set);
print(my_list_set[0]);
# Creación de una lista con múltiples tipos de datos
mixed_list = [
    42,                          # Integer
    3.14159,                     # Float
    "Hola mundo",                # String
    True,                        # Boolean
    [1, 2, 3],                   # Lista anidada
    ("a", "b", "c"),             # Tupla
    {"nombre": "Python"},        # Diccionario
    {1, 2, 3},                   # Set
    None,                        # NoneType
    lambda x: x*2                # Función (lambda)
]

# Mostrando la lista completa
print("Lista completa:", mixed_list)

# Accediendo a elementos individuales
print("\nAlgunos elementos individuales:")
print("Elemento 0 (entero):", mixed_list[0])
print("Elemento 2 (string):", mixed_list[2])
print("Elemento 4 (lista):", mixed_list[4])
print("Elemento 5 (tupla):", mixed_list[5])
print("Elemento 6 (diccionario):", mixed_list[6])

# Usando la función lambda de la lista
print("\nResultado de la función lambda con entrada 5:", mixed_list[9](5))

##  Sets, list and tuples##
my_list = list()
my_other_list = []

my_tuples = tuple()
my_other_tuple = ()

my_set = set()
my_other_set = {}  # Inicialmente es un diccionario

print("\nTipos de datos:")
print(type(my_set))        # Es un set - no es una estructura ordenada
print(type(my_other_set))  # Es un diccionario
print(type(my_tuples))     # Es una tupla

my_other_set = {"KLips", "KLips", "KLips","","",0}  # Es un set y solo acepta valores únicos
my_list_set = list(my_other_set)
print("\nPrimer elemento de la lista convertida:", my_list_set[0])

# Corrección: intersection requiere un argumento o usar intersection_update
print("Elementos del set:", my_other_set)

print(my_other_set.issubset(my_other_set))# 

# slicing "Revanada" de listas

slicing = mixed_list[2:2]
print(slicing)

