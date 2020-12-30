# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 12:47:17 2020

@author: Roman
"""



"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку 
конструктора класса (метод __init__()), который должен 
принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, 
расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() 
для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации 
операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — 
первый элемент первой строки первой матрицы складываем с 
первым элементом первой строки второй матрицы и т.д.
"""

print("\n1. Реализовать класс Matrix (матрица)...\n")

class Matrix:
    __matrix = []
    def __init__(self, list_of_lists):
        self.__matrix = list_of_lists
        self.__normalize()
        
    def __normalize(self):
        self.lenght = max([len(n) for n in self.__matrix])
        for n in self.__matrix:
            while len(n) < self.lenght:
                n.append(0)
    
    def __str__(self):
        res = ""
        for n in self.__matrix:
            res += "\n" + str(n)
        return res
    
    def __add__(self, other):
        if isinstance(other, Matrix):
            if (self.Get_dimensions(self) == self.Get_dimensions(other)):
                self.matrix_list = []
                for i1, n in enumerate(self.__matrix):
                    self.matrix_list.append([])
                    for i2, t in enumerate(self.__matrix[i1]):
                        self.matrix_list[i1].append(
                                self.__matrix[i1][i2] + other.__matrix[i1][i2])
                return Matrix(self.matrix_list)
            else:
                print("Error! Matricies are of different dimentions")
                return self
        else:
            print("Error! Matrix can be added only to another matrix")
            return self
    
    def Get_dimensions(self, matrix):
        return [len(matrix.__matrix[0]),len(matrix.__matrix)]
        


test_list_1 = [
        [1,2,3],
        [1,2,3,4],
        [1,2]
        ]
test_list_2 = [
        [2,2,4,8],
        [1,4,3,],
        [1,2,2]
        ]
test_list_3 = [
        [2,2,4],
        [1,4,3],
        [1,2,2]
        ]

m1 = Matrix(test_list_1)
m2 = Matrix(test_list_2)
m3 = Matrix(test_list_3)
print("\nThere three lists for matricies:")
print(test_list_1)
print(test_list_2)
print(test_list_3)
print("\nFrom the lists, three matricies were created:")
print(m1)
print(m2)
print(m3)
print("\nAdding matrix 1 and 2:")
print(m1 + m2)
print("\nTrying to add matricies 1 and 3. They are of different dimensions:")
print(m1 + m3)

"""
2. Реализовать проект расчета суммарного расхода ткани 
на производство одежды. Основная сущность (класс) 
этого проекта — одежда, которая может иметь определенное 
название. К типам одежды в этом проекте относятся пальто 
и костюм. У этих типов одежды существуют параметры: 
размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды 
использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3). Проверить работу этих методов 
на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на 
практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных 
классов проекта, проверить на практике работу декоратора 
@property.
"""

from abc import ABC

print("\n2. Реализовать проект расчета суммарного расхода ткани...\n")

class Cloth (ABC):
    __V = 0
    __H = 0
    def __init__(self, V, H):
        self.__V = V
        self.__H = H
    
    def Get_dimensions(self):
        return [self.__V, self.__H]
    
    @property
    def Get_cloth_consumption(self):
        return self.Get_dimensions[0] * self.Get_dimensions[1]

class Coat (Cloth):
    @property
    def Get_cloth_consumption(self):
        return self.Get_dimensions()[0] / 6.5 + 0.5

class Suit (Cloth):
    @property
    def Get_cloth_consumption(self):
        return self.Get_dimensions()[1] * 2 + 0.3


c = Coat(13, 5)
s = Suit(3, 6)
print("Created Coat with dimensions ", c.Get_dimensions(), 
      " cloth consumption is ", c.Get_cloth_consumption)
print("Created Suit with dimensions ", s.Get_dimensions(), 
      " cloth consumption is ", s.Get_cloth_consumption)

"""
3. Реализовать программу работы с органическими клетками. 
Необходимо создать класс Клетка. В его конструкторе 
инициализировать параметр, соответствующий количеству 
клеток (целое число). В классе должны быть реализованы 
методы перегрузки арифметических операторов: сложение 
(__add__()), вычитание (__sub__()), умножение (__mul__()), 
деление (__truediv__()).Данные методы должны применяться 
только к клеткам и выполнять увеличение, уменьшение, 
умножение и обычное (не целочисленное) деление клеток, 
соответственно. В методе деления должно осуществляться 
округление значения до целого числа.
"""

print ("\n3. Реализовать программу работы с органическими клетками...\n")
class Cell:
    _cell_num = 0
    def __init__(self, num):
        self._cell_num = num
    
    def __add__(self, other):
        if (isinstance(other, Cell)):
            return Cell(self._cell_num + other._cell_num)
        else:
            print("Error! Other side is not Cell.")
            return self
        
    def __sub__(self, other):
        if (isinstance(other, Cell)):
            self.__delta = self._cell_num - other._cell_num
            if (self.__delta >= 0):   
                return Cell(self.__delta)
            else:
                print("Delta is below zero. returning 0...")
                return Cell(0)
        else:
            print("Error! Other side is not Cell.")
            return self
        
    def __mul__(self, other):
        if (isinstance(other, Cell)):
            return Cell(self._cell_num * other._cell_num)
        else:
            print("Error! Other side is not Cell.")
            return self
    
    def __truediv__(self, other):
        if (isinstance(other, Cell)):
            return Cell(int(self._cell_num / other._cell_num))
        else:
            print("Error! Other side is not Cell.")
            return self
    
    def make_order(self, row_num):
        self.res = ""
        for n in range(0, int(self._cell_num / row_num)):
            self.res += ("*" * row_num) + "\n"
        self.res += ("*" * (self._cell_num % row_num) + "\n")
        return self.res

c1 = Cell(3)
c2 = Cell(5)
print("Created 2 cells: c1 with ",c1._cell_num," cells, c2 with ", c2._cell_num)
c1 = c1 + c2
print("c1 after addition ", c1._cell_num)
c1 = c1 - c2
print("c1 after subtraction ", c1._cell_num)
c1 = c1 * c2
print("c1 after multiplication ", c1._cell_num)
c1 = c1 / c2
print("c1 after divide ", c1._cell_num)
print("Cell with 16 cells ordered by 5-item rows:\n")
print(Cell(16).make_order(5))







