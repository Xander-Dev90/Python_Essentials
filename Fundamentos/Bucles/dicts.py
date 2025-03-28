
# Creación de un diccionario sencillo
mi_diccionario = {
    "nombre": "Juan",
    "edad": 28,
    "profesion": "Desarrollador",
    "lenguajes": ["Python", "JavaScript", "Java"],
    "activo": True,
    "direccion": {
        "calle": "Calle Principal",
        "numero": 123,
        "ciudad": "Madrid"
    }
}

# Mostrar el diccionario completo
print("Diccionario completo:")
print(mi_diccionario["nombre"])

# Acceder a valores individuales
print("\nAcceso a valores individuales:")
print("Nombre:", mi_diccionario["nombre"])
print("Edad:", mi_diccionario["edad"])
print("Lenguajes:", mi_diccionario["lenguajes"])

# Acceder a un valor dentro de una lista en el diccionario
print("\nPrimer lenguaje:", mi_diccionario["lenguajes"][0])

# Acceder a un valor dentro de un diccionario anidado
print("\nCiudad:", mi_diccionario["direccion"]["ciudad"])

# Modificar un valor
mi_diccionario["edad"] = 29
print("\nEdad actualizada:", mi_diccionario["edad"])

# Añadir una nueva clave-valor
mi_diccionario["experiencia"] = 5
print("\nNueva clave añadida - Experiencia:", mi_diccionario["experiencia"])

# Eliminar una clave-valor
del mi_diccionario["activo"]
print("\nDiccionario después de eliminar 'activo':")
print(mi_diccionario)

# Verificar si una clave existe
if "nombre" in mi_diccionario:
    print("\nLa clave 'nombre' existe en el diccionario")

# Obtener todas las claves
print("\nTodas las claves:", list(mi_diccionario.keys()))

# Obtener todos los valores
print("\nTodos los valores:", list(mi_diccionario.values()))

# Obtener todos los pares clave-valor como tuplas
print("\nTodos los pares clave-valor:")
for clave, valor in mi_diccionario.items():
    print(f"  {clave}: {valor}")


print(mi_diccionario.keys())
print(mi_diccionario.items())
print(mi_diccionario.values())
print(mi_diccionario.pop())
print(mi_diccionario.fromkeys())
