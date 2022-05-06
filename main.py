import numpy as np
from matplotlib import pyplot


def leerNumero(id):
    try:
        num = float(input("Ingrese el valor de " + id + "\n"))
        if id == "a" and num == 0:
            raise Exception("a no puede ser cero")
        return num
    except Exception as e:
        print(str(e))
        return None


def calcularDiscriminate(a, b, c):
    return (b ** 2) - 4 * a * c


def calcularRaizPositiva(a, b, det):
    return ((-b) + (det ** 0.5)) / (2 * a)


def calcularRaizNegativa(a, b, det):
    return ((-b) - (det ** 0.5)) / (2 * a)


def formatoEcuacion(a, b, c):
    if a == 1:
        title = "x²"
    else:
        title = str(a) + "x²"
    if b != 0:
        title = title + str("{:+}".format(b)) + "x"
    if c != 0:
        title = title + str("{:+}".format(c))
    return title


def graficar(a, b, c):
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

    if 0 < a < 1:
        pyplot.xlim(xv - 15, xv + 15)
    else:
        pyplot.xlim(xv - 5, xv + 5)

    pyplot.plot(x, y)
    pyplot.plot(xv, yv, marker="o", color="black")

    pyplot.xlabel('x')
    pyplot.ylabel('y')

    pyplot.title(formatoEcuacion(a, b, c))

    pyplot.savefig("output.png")
    pyplot.show()


def main():
    while True:
        a = leerNumero("a")
        if a is not None:
            break

    while True:
        b = leerNumero("b")
        if b is not None:
            break

    while True:
        c = leerNumero("c")
        if c is not None:
            break

    disc = calcularDiscriminate(a, b, c)

    x1 = calcularRaizPositiva(a, b, disc)
    x2 = calcularRaizNegativa(a, b, disc)

    print("La ecuación de la forma: ", formatoEcuacion(a, b, c))

    if disc > 0:
        print("Raices reales: ")
        print("x1= ", "{:.3f}".format(x1))
        print("x2= ", "{:.3f}".format(x2))
    elif disc == 0:
        print("Raiz unica")
        print("x1= ", "{:.3f}".format(x1))
    else:
        print("Raices imaginarias:")
        print("x1=", "{:.3f}".format(x1.real), "{0:+.3f}".format(x1.imag), "i")
        print("x2=", "{:.3f}".format(x2))

    graficar(a, b, c)


if __name__ == "__main__":
    main()
