import matplotlib.pyplot as plt
import sympy as spy
import numpy as npy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D

def grapher(k,F,dimen,F2=None):
    if dimen==1:
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
        plt.legend()
        plt.title('Gráfico 2D de la función')
    elif dimen==2:
        x = spy.symbols('x')
        y = spy.symbols('y')
        Fxl_3d = spy.lambdify((x, y), F, 'numpy')
        xvar_3d = npy.linspace(-10, 10, 80)
        yvar_3d = npy.linspace(-10, 10, 80)
        xvar_3d, yvar_3d = npy.meshgrid(xvar_3d, yvar_3d)
        zvar_3d = Fxl_3d(xvar_3d, yvar_3d)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_wireframe(xvar_3d, yvar_3d, zvar_3d, alpha=0.8, color='orange')
        if F2 is not None:
            F2xl_3d = spy.lambdify((x, y), F2, 'numpy')
            z2var_3d = F2xl_3d(xvar_3d, yvar_3d)
            ax.plot_wireframe(xvar_3d, yvar_3d, z2var_3d, alpha=0.8, color='blue')
        custom_lines = [
            Line2D([0], [0], color='orange', lw=4, label=f'{F}'),
            Line2D([0], [0], color='blue', lw=4, label=f'{F2}') if F2 is not None else None
        ]
        custom_lines = [line for line in custom_lines if line is not None]  # Filtrar líneas no utilizadas
        ax.legend(handles=custom_lines)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.title(f'Gráfico 3D de la función')
        ax.grid(True)
        ax.view_init(elev=20, azim=60)
    plt.show()