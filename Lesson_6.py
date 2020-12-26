# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 17:10:55 2020

@author: Roman
"""

"""
1. Создать класс TrafficLight (светофор) и определить у него 
один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать 
переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке 
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и 
вызвав описанный метод.
"""

print("\n1. Создать класс TrafficLight (светофор)...\n")

import time

class TrafficLight:
    def __init__(self):
        self.__color = "red"
    def running(self):
        self.__time_interwals = [7,2,4]
        self.__colors = ["red","yellow","green"]
        self.__cur_time= time.time()
        self.__i = 0
        print("Now color is "+self.__color)
        while True:
            self.__delta = time.time()-self.__cur_time
            if self.__delta >= self.__time_interwals[self.__i]:
                if (self.__i == len(self.__colors)-1):
                    print("Ending the cycle, time elapsed: ",round(self.__delta,0))
                    break
                self.__i += 1
                self.__color = self.__colors[self.__i % len(self.__time_interwals)]
                self.__cur_time= time.time()
                print("Now color is ",self.__color,"time elapsed: ",round(self.__delta,0))

tr = TrafficLight()
tr.running()

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: 
length (длина), width (ширина). Значения данных атрибутов должны 
передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия 
всего дорожного полотна. Использовать формулу: длина * ширина * масса 
асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * 
чи сло см толщины полотна. Проверить работу метода.
"""

print("\n2. Реализовать класс Road (дорога), в котором определить атрибуты...\n")
class Road:
    def __init__(self, l=1000, w=15):
        self._lenght = l
        self._width = w
    def calc_road_mass(self, mass_1sm_road = 25, thickness_road = 5):
        return(self._width * self._lenght * mass_1sm_road * thickness_road / 1000)

road = Road(1000, 15)
print("Road mass is ",road.calc_road_mass(25, 5))

"""
3. Реализовать базовый класс Worker (работник), 
в котором определить атрибуты: name, surname, position (должность), 
income (доход). Последний атрибут должен быть защищенным и ссылаться 
на словарь, содержащий элементы: оклад и премия, например, 
{"wage": wage, "bonus": bonus}. Создать класс Position (должность) 
на базе класса Worker. В классе Position реализовать методы получения 
полного имени сотрудника (get_full_name) и дохода с учетом премии 
(get_total_income). Проверить работу примера на реальных данных 
(создать экземпляры класса Position, передать данные, проверить 
значения атрибутов, вызвать методы экземпляров).
"""
print("\n3. Реализовать базовый класс Worker (работник)...\n")

class Worker:
    def __init__(self, name = "Ivan", surname = "Petrov", position = "DataScientist", wage = 20000, bonus = 5000):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus":bonus}
    
class Position(Worker):
    def get_full_name(self):
        return self.name
    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]
    
pos = Position()
print("Employee ",pos.get_full_name(),"has an income of ",pos.get_total_income())


"""
4. Реализуйте базовый класс Car. У данного класса должны быть 
следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда). Опишите несколько 
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать 
текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите 
метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. Выполните вызов 
методов и также покажите результат.
"""
print("\n4. Реализуйте базовый класс Car. У данного класса...\n")

class Car:
    def __init__(self, speed = 40, color = "red", 
                 name = "Pobeda", is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return "Car "+ self.name +" is moving"
    def stop(self):
        return "Car "+ self.name + " is stopping"
    def turn(self,direction):
        return "Car "+ self.name + " turned to " + direction
    def show_speed(self):
        return "Current speed of "+ self.name + " is " + str(self.speed)

class TownCar(Car):
    def __init__(self, speed = 40, color = "red", 
                 name = "Pobeda"):
        super().__init__(speed, color, name)
        self.is_police = False
        
    def show_speed(self):
        res = str("Current speed of "+self.name+" is "+str(self.speed))
        if self.speed > 60:
            res = str("Speed limit is breached! "+res)
        return res
            
class SportCar(Car):
    def __init__(self, speed = 40, color = "red", 
                 name = "Pobeda"):
        super().__init__(speed, color, name)
        self.is_police = False

class WorkCar(Car):
    def __init__(self, speed = 40, color = "red", 
                 name = "Pobeda"):
        super().__init__(speed, color, name)
        self.is_police = False
    def show_speed(self):
        res = str("Current speed of "+self.name+" is "+str(self.speed))
        if self.speed > 40:
            res = str("Speed limit is breached! "+res)
        return res
        
class PoliceCar(Car):
    def __init__(self, speed = 40, color = "red", 
                 name = "Pobeda", is_police = False):
        super().__init__(speed, color, name)



PC = PoliceCar(name = "PoliceCar")
TC = TownCar(speed = 70, name = "TownCar")
WC = WorkCar(speed = 45, name = "WorkCar")
SC = SportCar(name = "SportCar")
print(PC.go())
print(SC.stop())
print(WC.turn("south"))
print(SC.show_speed())
print(WC.show_speed())
print(TC.show_speed())

"""
5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса 
Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов 
реализовать переопределение метода draw. Для каждого из классов методы 
должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
 что выведет описанный метод для каждого экземпляра.
"""

print("\n5. Реализовать класс Stationery (канцелярская принадлежность)...\n")

class Stationery:
    def __init__(self, title = "Komus"):
        self.title = title
    def draw(self):
        print("Draw start...")
    
class Pen(Stationery):
    def draw(self):
        Stationery.draw(self)
        print("Pen draw\n")

class Pencil(Stationery):
    def draw(self):
        Stationery.draw(self)
        print("Pencil draw\n")

class Handle(Stationery):
    def draw(self):
        Stationery.draw(self)
        print("Handle draw\n")



pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()



