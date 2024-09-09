# CerveraTronx 3000
***
![python](https://img.shields.io/badge/Python-green)
![jupyter](https://img.shields.io/badge/Jupyter_notebooks-orange)
![Calculus](https://img.shields.io/badge/Calculus-purple)

Este proyecto consiste en un programa que recibe del usuario una función de 1 o 2 variables y permite realizar operaciones de cálculo infinitesimal simbólico y numérico sobre la función. El programa también grafica las funciones y los resultados de las operaciones aplicadas, en 2 o 3 dimensiones, según la función ingresada.

El programa puede realizar 4 operaciones de cálculo:
- Derivada simbólica
- Integral simbólica
- Derivada numérica
- Integral numérica

A excepción de la derivada numérica, el resto utiliza métodos de `sympy`para obtener las operaciones requeridas. La derivada numérica se calcula mediante diferenciales centrales del valor de la función desde el punto de interés.
