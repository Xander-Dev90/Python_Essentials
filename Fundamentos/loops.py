# Estructura de los bucles en Python

persona = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "correo": "juan.perez@ejemplo.com"
}
# Bucle 'for'
for i in persona:
    print("Clave:", i, "Valor:", persona[i])
    if i == "edad":
        print("Se ha encontrado la clave 'edad'")
        break

    else:
        print("No se ha encontrado la clave 'edad'")


# Bucle 'while'

contador = 0
while contador < 15:
    contador += 1
    if contador ==15:
        print("Se ha llegado al límite de 15 iteraciones")
        break

    print(f"Iteración {contador} en el bucle 'while'")
print("Fin del bucle 'while'")


x = [-5,-4,-3,-2,-1-0,1,2,3,4,5]
y = 1
fx = [] #Lista vacia

for element in x:
    fx.append(element**3 + y)

print(f" Fx = {fx}")
