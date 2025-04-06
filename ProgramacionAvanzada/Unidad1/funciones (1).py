import numpy as np
# Definición 
def f(x):
    return x**2

def g(x, y):
    X, Y = np.meshgrid(x, y)
    return np.sin(X) * np.cos(Y)

def h(x, y, z):
    X, Y, Z = np.meshgrid(x, y, z)
    return X * Y * Z

# Clases
class Funcion:
    def __init__(self, nombre, funcion): #iniciacion
        self.nombre = nombre
        self.funcion = funcion
    
    def evaluar(self, *valores): #evaluacion
        return self.funcion(*valores)
