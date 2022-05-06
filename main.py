import numpy as np
from matplotlib import pyplot

# Variables de control de datos
swa = 0
swb = 0
swc = 0

# Control de la variable a
while swa == 0:
    try:
        a = float(input("Ingrese el valor de (a):\n"))
        if a == 0:
            raise Exception("a no puede ser zero")
    except:
        print("!!! Numero no valido !!!\n Vuelva a ingresarlo")
    else:
        swa = 1

# Control de la variable b
while (swb == 0):
    try:
        b = float(input("Ingrese el valor de (b):\n"))
    except:
        print("!!! Numero no valido !!!\n Vuelva a ingresarlo")
    else:
        swb = 1

# Control de la variable c
while (swc == 0):
    try:
        c = float(input("Ingrese el valor de (c):\n"))
    except:
        print("!!! Numero no valido !!!\n Vuelva a ingresarlo")
    else:
        swc = 1

print("La ecuación de la forma: ", a, "x² {0:+} x".format(b), "{0:+}".format(c), " :")

# Calculo del Discriminante
disc = (b ** 2) - (4 * a * c)

# Verificacion del valor del discriminante
if disc >= 0:
    raiz = (disc) ** (0.5)
else:
    raiz = (disc * -1) ** (0.5)

# Calculo de las raices de la ecuacion
if (disc > 0):
    print("Raices reales: ")
    x1 = ((-b) + raiz) / (2 * a)
    x2 = ((-b) - raiz) / (2 * a)
    print("x1= ", "{:.3f}".format(x1))
    print("x2= ", "{:.3f}".format(x2))
elif (disc == 0):
    print("Raiz unica")
    x1 = ((-b) + raiz) / (2 * a)
    x2 = ((-b) - raiz) / (2 * a)
    print("x1= ", "{:.3f}".format(x1))
else:
    print("Raices imaginarias:")
    x1 = (-b) / (2 * a)
    x2 = (-b) / (2 * a)
    print("x1= ", "{:.3f}".format(x1), "+ ", "{:.3f}".format(raiz), "i")
    print("x2= ", "{:.3f}".format(x2), "- ", "{:.3f}".format(raiz), "i")

x = np.arange(-20, 20, 0.1)
y = (a * (x ** 2)) + (b * x) + c

pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Calculo del vertice de la parabola
xv = ((-b) / (2 * a))
yv = (a * (xv ** 2)) + (b * xv) + c
# Forma canonica f(x) = a(x-xv)²+yv


if a > 0:
    pyplot.ylim(yv - 2, yv + 15)
else:
    pyplot.ylim(yv - 15, yv + 2)

pyplot.xlim(xv - 5, xv + 5)

pyplot.plot(x, y)
pyplot.plot(xv, yv, marker="o", color="black")

pyplot.savefig("output.png")
pyplot.show()