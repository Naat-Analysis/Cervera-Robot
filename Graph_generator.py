import matplotlib.pyplot as plt
import sympy as spy
import numpy as npy

def grapher(k,F,F2=None):
    Fxs=spy.sympify(F)
    x=spy.symbols(k)
    Fxl=spy.lambdify(x,F,'numpy')
    xvar=npy.linspace(-10,10,200)
    yvar=Fxl(xvar)
    plt.plot(xvar,yvar,label=f'{F}')
    if F2 is not None:
        F2xs=spy.sympify(F2)
        F2xl=spy.lambdify(x,F2,'numpy')
        y2var=F2xl(xvar)
        plt.plot(xvar,y2var,label=f'{F2}')
    plt.xlabel('x')
    plt.ylabel(f'F(x)')
    #plt.legend()
    plt.title(f'Gráfico de la función {F}')
    plt.grid(True)
    plt.show()
