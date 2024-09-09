from . import Function_class as fc
import sympy as sp
from . import Graph_generator as gf
print('===========================================')
print('==== C E R B E R A - T R O N X 3 0 0 0 ====')
print('===========================================')

k=1
while k==1:   
    F=input('Ingrese la función a analizar (f(x) o f(x,y)): ')
    x=input('Ingrese la variable de interés: ')
    dimen=int(input('¿Cuántas variables independientes tiene la función?: '))
    Fs=sp.sympify(F)
    xs=sp.symbols(x)
    Fx=fc.funcion(Fs,xs)
    d=1
    while d==1:
        i=int(input('Indique el número de la operación a realizar:\n 1. Derivada simbólica\n 2. Integral simbólica\n 3. Derivada numérica\n 4. Integral numérica\n'))
        if i==1:
            print(f'La derivada simbólica de {Fx.expr} es\n {Fx.sderiv()}')
            gf.grapher(x,F,dimen,str(Fx.sderiv()))
        elif i==2:
            print(f'La integral simbólica de {Fx.expr} es\n {Fx.sinteg()}')
            gf.grapher(x,F,dimen,str(Fx.sinteg()))
        elif i==3:
            a=float(input('Ingrese punto dónde calcular la derivada:\n'))
            h=float(input('Ingrese el incremento para la derivada numérica:\n'))
            print(f'La derivada numérica de {Fx.expr} en {a} con delta {h} es\n {Fx.nderiv(a,h)}')
            gf.grapher(x,F,dimen)
        elif i==4:
            a=float(input('Ingrese punto inicial de integración:\n'))
            b=float(input('Ingrese punto final de integración:\n'))
            print(f'La integral numérica de {Fx.expr} desde {a} hasta {b} es\n {Fx.ninteg(a,b)}')
            gf.grapher(x,F,dimen)
        d=int(input('¿Desea realizar otra operación sobre la función? 1=Sí, 0=No: '))    
    k=int(input('¿Desea agregar otra función? 1=Sí, 0=No: '))
print('Proceso finalizado')