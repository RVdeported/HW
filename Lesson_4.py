# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 10:58:11 2020

@author: Roman
"""
import random
import functools
import itertools
import math
from sys import argv




"""
1. Реализовать скрипт, в котором должна быть предусмотрена 
функция расчета заработной платы сотрудника. В расчете необходимо 
использовать формулу: (выработка в часах * ставка в час) + премия. 
Для выполнения расчета для конкретных значений необходимо запускать 
скрипт с параметрами.
"""
print("\n1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы..\n")

Script, name, hours, rate, premium = argv

if (hours.isdigit() and rate.isdigit() and premium.isdigit()):
    res = int(hours)*int(rate)+int(premium)
    print("Comrade ",name," is to be paid in amount of ",res)
else:
    print("Calculation data received are incorrect: ",hours," ",rate," ",premium)

"""
2. Представлен список чисел. Необходимо вывести элементы 
исходного списка, значения которых больше предыдущего элемента.
"""

init_list = random.sample(range(0,255),15)
out_list = []
for ind,t in enumerate(init_list):
    if ind>0:
        if t>init_list[ind-1]:
            out_list.append(t)

print("\n2. Представлен список чисел. Необходимо вывести элементы...\n")
print("Init list is: ",init_list,"\nOutput list i: ",out_list)

"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. 
Необходимо решить задание в одну строку.
"""

res = [i for i in range(20,240) if (i%20==0 or i%21==0)]

print("\n3. Для чисел в пределах от 20 до 240 найти числа...\n")
print("Result is: ",res)

"""
4. Представлен список чисел. Определить элементы списка, 
не имеющие повторений. Сформировать итоговый массив чисел, 
соответствующих требованию. Элементы вывести в порядке их 
следования в исходном списке. Для выполнения задания обязательно 
использовать генератор.
"""

init_list = [random.randrange(0,100) for i in [0]*100]
out_list = [i for i in init_list if init_list.count(i)==1]

print("\n4. Представлен список чисел. Определить элементы списка...\n")
print("Init list is: ",init_list,"\nOutput list is: ",out_list)

"""
5. Реализовать формирование списка, используя функцию range() 
и возможности генератора. В список должны войти четные числа 
от 100 до 1000 (включая границы). Необходимо получить результат 
вычисления произведения всех элементов списка.
"""

init_list = [random.randrange(100,1000) for i in [0]*4]
res = functools.reduce(lambda arg1, arg2: arg1*arg2, init_list)

print("\n5. Реализовать формирование списка, используя функцию range()...\n")
print("Init list is: ",init_list,"\nOutput is: ",res)

"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

arr1 = [3]
#iterator A
for i in itertools.cycle(arr1):
    if (len(arr1)<10):
        arr1.append(i+1)
    else: break
#iterator B
arr2 = []
arr1_len = len(arr1)
for i in itertools.cycle(arr1):
    if (len(arr2)<arr1_len):
        arr2.append(i)
    else:
        break
    
print("\n6. Реализовать два небольших скрипта...\n")
print("Result of simple iterator is: ",arr1,"\nResult if repeat itearator is: ",arr2)

"""
7. Реализовать генератор с помощью функции с ключевым словом yield, 
создающим очередное значение. При вызове функции должен создаваться 
объект-генератор. Функция должна вызываться следующим образом: 
for el in fact(n). Функция отвечает за получение факториала числа, 
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""

def fact (n=1):
    for el in range(1,abs(n)+1):
        yield math.factorial(el)
res = []
for el in fact(4):
    res.append(el)
    
print("\n7. Реализовать генератор с помощью функции с ключевым словом yield...\n")
print("Factorial list result is: ",res)






