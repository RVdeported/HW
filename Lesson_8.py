# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:22:15 2021

@author: Roman
"""


"""
1. Реализовать класс «Дата», функция-конструктор которого должна 
принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, 
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной 
структуры на реальных данных.
"""

print("\n1. Реализовать класс «Дата», функция-конструктор которого должна...\n")

class Data():
    date = "00-00-0000"
    def __init__(self, date):
        self.date = date
    
    @classmethod
    def get_date(cls, date):
        """
        return date in days
        """
        if (cls.validate(date)):
            splitted = date.split("-")
            print("Total days:")
            return int(int(splitted[2]) * 365 + 
                       int(splitted[1]) * 30.5 + 
                       int(splitted[0]))
        else: 
            return False
    
    @staticmethod
    def validate(date):
        if (date.count("-") != 2):
            print("Error. Wrong format")
            return False
        
        splitted = date.split("-")
        if (not(splitted[0].isdigit()) or
            not(splitted[1].isdigit()) or
            not(splitted[2].isdigit())):
            print("Error. There some non-numeric characters")
            return False
        
        if (int(splitted[0]) < 1 or
            int(splitted[1]) < 1 or
            int(splitted[2]) < 0):
            print("Error. There zero or negative values")
            return False
        
        if (int(splitted[0]) > 31 or
            int(splitted[1]) > 12):
            print("Error. There too large numbers")
            return False
        
        return True
    
test = ["24-12-2003", "40-12-2003",
        "10-0-2004", "10-03-20g0"]
for n in test:
    print("Testing " + n)
    data = data= Data(n)
    print("Output:")
    print(str(data.get_date(data.date)) + "\n")


"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию 
деления на нуль. Проверьте его работу на данных, вводимых пользователем. 
При вводе пользователем нуля в качестве делителя программа должна 
корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

print("\n2. Создайте собственный класс-исключение, обрабатывающий ситуацию...\n")

class null_del_exept(Exception):
    def __init__(self, txt):
        self.txt = txt

while True:
    inp = input("Please, enter divider and dilimetr via space or '-1' to exit:\n")
    if (inp == '-1'):
        break
    inp = inp.split(" ")
    if (not(inp[0].isdigit()) or 
        not(inp[1].isdigit())):
        print("Error. Some of the integers are not numbers, returning...")
    else:
        inp[0] = int(inp[0])
        inp[1] = int(inp[1])
        try:
            if (inp[1] == 0):
                raise null_del_exept("Error! Zero division")
            print(inp[0] / inp[1])
  
        except null_del_exept as err:
            print(err)

"""
3. Создайте собственный класс-исключение, который должен проверять 
содержимое списка на наличие только чисел. Проверить работу 
исключения на реальном примере. Необходимо запрашивать у пользователя 
данные и заполнять список. Класс-исключение должен контролировать типы 
данных элементов списка.
"""

class StringExeption(Exception):
    def __init__(self, txt):
        self.txt = txt

array = []
while True:
    inp = input("Enter a number to add to list. Enter 'stop' to exit\n")
    if (inp == 'stop'):
        break
    try:
        if (not(inp.isdigit())):
            raise StringExeption("Error! Non-numeric value entered")
        array.append(int(inp))
    except StringExeption as err:
        print(err)
        
print("\nTotal lsit: " + str(array))


"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, 
описывающий склад. А также класс «Оргтехника», который будет базовым 
для классов-наследников. Эти классы — конкретные типы оргтехники 
(принтер, сканер, ксерокс). В базовом классе определить параметры, 
общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, 
отвечающие за приём оргтехники на склад и передачу в определенное 
подразделение компании. Для хранения данных о наименовании и количестве 
единиц оргтехники, а также других данных, можно использовать любую 
подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
"""

print("\n4. Начните работу над проектом «Склад оргтехники»...\n")
print("\n5. Продолжить работу над первым заданием...\n")
print("\n6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых...\n")

class Storage():
    _header = ["id", "Department", "tech_type", "tech"] # data fields. 'tech' saves Tech object itself
    _items = []
    _cur_id = 0
    def store_item(self, tech, department = "Default", quantity = 1):
        """
        function fill items[] according to header[] structure
        'id' field fills automatically
        """
        if (type(quantity) != int):
            print("Error! Passed quantity " + str(quantity) + " is non-numeric value. Aborting...")
            return False
        to_store = [self._cur_id, department, tech.tech_type, tech]
        for n in range(0,quantity):    
            to_store[0] = self._cur_id
            self._cur_id += 1
            self._items.append(to_store)
            print("Storing item " + str(to_store))
    
    def get_count(self,criteria_arr, value_arr):
        """
        Accepts array of header criteria and array of corresponding values.
        Returns count of items found if ALL criteria meet the data.
        """
        counter = 0
        #transferring inputs to lists
        inp = [criteria_arr, value_arr]
        for ind, n in enumerate(inp):
            if (type(n) != list):
                inp[ind] = [n]
        
        # entry validation
        if (len(inp[0]) != len(inp[0])):
            print("Lengh of input arr don't match. Aborting...")
            return False       

        for i, n in enumerate(criteria_arr):
            try:
                criteria_arr[i] = self._header.index(n) 
            except ValueError:
                print("Criteria " + criteria_arr[i] + " not found, aborting...")
                return False
        
        #counting
        for item in self._items:
            for cr_ind, criteria in enumerate(criteria_arr):
                if value_arr[cr_ind] != item[criteria_arr[cr_ind]]:
                    break
                if (cr_ind == len(criteria_arr) - 1):
                    counter += 1
        return counter
    
    def get_tech_by_id(self,ind):
        """
        return Tech object by index in _items[]
        """
        if (type(ind) != int):
            print("Passed value is not Int. Aborting...")
            return False
        
        for n in self._items:
            if (n[0] == ind):
                return n[3]
        print("Item with id " + ind + " not found")
        return False


class Tech():
    name = "Default"
    office = False
    weight = 10
    tech_type = "Default"
    def __init__(self, name = "Default", office = False, weight = 10):
        self.name = name
        self.office = office
        self.weight = weight

class printer(Tech):
    wifi = False
    def __init__(self, name = "Default", office = False, weight = 10,
                 wifi = False):
        super().__init__(name, office, weight)
        self.wifi = wifi   
        self.tech_type = "Printer"

class shovel(Tech):
    for_winter = False
    def __init__(self, name = "Default", office = False, weight = 10,
                 for_winter = False):
        super().__init__(name, office, weight)
        self.for_winter = for_winter
        self.tech_type = "Shovel"

# initialization and storing
st = Storage()
pr = printer(name = "HP print", wifi = True)
sh = shovel(name = "Kristina", weight = 5)
st.store_item(pr)
st.store_item(pr, "1")
st.store_item(pr, "2", 2)
st.store_item(pr, "1")
st.store_item(sh, "2")
st.store_item(sh, "2")
st.store_item(sh, "1")

# extracting
print("\nGetting count of printers from '1' department:")
print(st.get_count(["Department", "tech_type"],["1", "Printer"]))
print("\nGetting object with '1' index:")
obj = st.get_tech_by_id(1)
print(obj.name + "\ntype: " + obj.tech_type + "\nhave wifi feature: " + str(obj.wifi))
print("\nGetting object with '5' index:")
obj = st.get_tech_by_id(5)
print(obj.name + "\ntype: " + obj.tech_type + "\nis for winter: " + str(obj.for_winter))

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""

print("\n7. Реализовать проект «Операции с комплексными числами»...\n")

class Complex_num():
    a = 1
    b = 1
    def __init__(self, a = 1, b = 1):
        if (type(a) != int or
            type(b) != int):
            print("Error! Inputs are incorrect. Aborting...")
            return
        self.a = a
        self.b = b
    
    def __add__(self, right):
        if (type(right) == Complex_num):
            a = self.a + right.a
            b = self.b + right.b
            return Complex_num(a, b)
        
        elif (type(right) == int):
            a = self.a + right
            b = self.b
            return Complex_num(a, b)
        
        else:
            print("Error! Value " + right + " cannot be added. Aborting...")
            return False
    
    def __sub__(self, right):
        if (type(right) == Complex_num):
            a = self.a - right.a
            b = self.b - right.b
            return Complex_num(a, b)
        
        elif (type(right) == int):
            a = self.a - right
            b = self.b
            return Complex_num(a, b)
        
        else:
            print("Error! Value " + right + " cannot be subtracted. Aborting...")
            return False
    
    def __mul__(self, right):
        if (type(right) == Complex_num):
            a = self.a * right.a + (-self.b) * right.b
            b = self.b * right.a + self.a * right.b
            return Complex_num(a, b)
        
        elif (type(right) == int):
            a = self.a * right
            b = self.b * right
            return Complex_num(a, b)
        
        else:
            print("Error! Value " + right + " cannot be multiplied. Aborting...")
            return False
        
        
        return Complex_num(a, b)
    
    def __str__(self):
        return str(self.a) + " + " + str(self.b)+ "*i"

print("Creating two Complex numbers:\n")
num1 = Complex_num(4, 5)
num2 = Complex_num(2, 3)
print(str(num1) + "\n" + str(num2))
print("\nAdding the numbers")
print(num1 + num2)
print("\nSubtracting the numbers")
print(num1 - num2)
print("\nMultiplicating bumbers")
print(num1 * num2)






