import matplotlib.pyplot as plt

x = [-5,-4,-3,-2,-1,-0,1,2,3,4,5]
y = 1
fx = [] #Lista vacia

for element in x:
    fx.append(element**2 + y)

print(f" Fx = {fx}")

plt.figure(figsize=(10,5))
plt.title('Grafico de una funcion parabola')
plt.style.use('ggplot')
plt.plot(
           x, fx,
        )
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.legend(['f(x) = x^2 + 1'])



plt.show()