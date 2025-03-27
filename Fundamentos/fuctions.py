######  FUNCIONES #####

def suma(a, b):
    return a + b

print(suma(2,3))

#############################################

x = float(input("Ingresa el valor para x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)


###  FUNCIONES  ###
# Definición de la función
def calcular_y(x):
    return 1. / (x + 1. / (x + 1. / (x + 1. / x)))

# Creacion de un costructor
class Duck:
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    def quack(self):
        return print('Quack')

donald = Duck(height=1.35,weight=70,sex= "M")
print(donald.quack())
print(donald.height)
print(donald.weight)
print(donald.sex)
#######################3

def print_upper_texts(*texts):#*texts es un argumento de longitud variable
    print(type(texts))#<class 'tuple'>
    for text in texts:
        print(text.upper())#upper() convierte el texto a mayúsculas


print(print_upper_texts("hola", "mundo", "python"))