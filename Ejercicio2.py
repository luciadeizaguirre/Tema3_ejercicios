#De forma iterativa
import numpy as np
from typing import Any
def construccion(matriz):
    matriz=np.array([[4,3,2,5,6] , [1,2,7,8,3], [3,8,9,3,1], [2,3,5,6,1], [1,3,4,6,4]])
    determinante=np.linalg.det(matriz)
    return determinante
#De forma recursiva
class Matriz():
    def __init__(self, filas: list[list[int]]):
        self.filas = filas
        self.filas = []

    def columns(self, columnas: list[list[int]]):
        self.columnas=columnas
        return [[fila[i] for fila in self.filas] for i in range(len(self.filas[0]))]

    def numero_filas(self):
        return len(self.filas)

    def numero_columnas(self):
        return len(self.filas[0])

    def orden(self):
        return (self.numero_filas, self.numero_columnas)

    def determinante(self):
        if self.orden == (0, 0):
            return 1
        if self.orden == (1, 1):
            return int(self.filas[0][0])
        if self.orden == (2, 2):            
            return int((self.filas[0][0] * self.filas[1][1])
                - (self.filas[0][1] * self.filas[1][0]))
        else:
           return int((self.filas[0][0] * self.filas[1][1] * self.filas [2][2]) + (self.filas[0][1] * self.filas[1][2] * self.filas [2][0])
                    + (self.filas[1][0] * self.filas[2][1] * self.filas [0][2]) - (self.filas[0][2] * self.filas[1][1] * self.filas [2][0]) 
                    - (self.filas[0][1] * self.filas[1][0] * self.filas [2][2]) - (self.filas[1][2] * self.filas[2][1] * self.filas [0][0]) )
