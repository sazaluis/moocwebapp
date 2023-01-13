#from funciones import una_funcion
import sys
import os
sys.path.append(os.path.abspath("/mooc/U3/app"))
from funciones import *
a=10
b=13
print(a)
variable = 'texto variable'
variable = 'cambio texto variable'
print(variable)

CONSTANTE = 'texto constante por tener mayusculas'
CONSTANTE = 'te puedo cambiar, pero esta feo. los programadores no te respetarán'
print(CONSTANTE)

"""
comentarios·Con
SALTO
DE Linea
"""


una_funcion(a,b)
sentenciaif(a,b)
sentenciawhile(a)