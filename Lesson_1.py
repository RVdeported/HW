# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:56:21 2020

@author: Roman
"""

"""

1. Поработайте с переменными, создайте несколько, выведите на экран, 
запросите у пользователя несколько чисел и строк и сохраните в 
переменные, выведите на экран.

"""

var1 = "100"
var2 = 100

print("1. Поработайте с переменными...\n")
print("My values are ",var1," ",str(var2),"\n with types ",
      type(var1)," ",type(var2),"\n")

print("...запросите у пользователя несколько чисел и строк...\n")

while True:
    var1 = input("Please, enter number: ")
    try:
        var1 = int(var1)
        break
    except ValueError:
        print("Variable is not int, returning...")
    
var2 = input("Please, enter string: ")
print("Entered ",var1," ",str(var2),"\n","with types ",
      type(var1)," ",type(var2),"\n")

"""

2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды и выведите в 
формате чч:мм:сс. Используйте форматирование строк.

"""

print("\n","2. ...Переведите время в часы, минуты и", 
      "секунды и выведите в формате чч:мм:сс","\n")

inp = 0
while True:    #yeah yeah, double code...
    inp = input("Please, enter number: ")
    try:
        inp = int(inp)
        break
    except ValueError:
        print("Variable is not int, returning...")

h = min(inp//3600,99)
if (h<10):
    h = "0"+str(h)
else:
    h = str(h)

m = inp%3600//60
if (m<10):
    m = "0"+str(m)
else:
    m = str(m)

s = inp%60
if (s<10):
    s = "0"+str(s)
else:
    s = str(s)


print("Result is: ",h,":",m,":",s,"\n")
        
"""

3. Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. 
Считаем 3 + 33 + 333 = 369.

"""

print("\n","3. Узнайте у пользователя число n.", 
      "Найдите сумму чисел n + nn + nnn.")

inp = 0
while True:    #yeah yeah, double code...
    inp = input("Please, enter number: ")
    try:
        inp = int(inp)
        if (abs(inp)>9):
            print("Variable is bigger than 9, returning...")
        else:
            break
    except ValueError:
        print("Variable is not int, returning...","/n")
    
print("Result is ",str(inp+inp*11+inp*111))       
        

"""

4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.

"""

print("/n","4. Пользователь вводит целое положительное число.", 
      "Найдите самую большую цифру в числе. ")

inp = 0
while True:    #yeah yeah, double code...
    inp = input("Please, enter number: ")
    try:
        inp = int(inp)
        if (inp<1):
            print("Variable is negative or zero, returning...")
        else:
            break
    except ValueError:
        print("Variable is not int, returning...","\n")

num_of_int = 1
while inp // (10 ** num_of_int) > 1:
    num_of_int = num_of_int + 1

res = 0
while num_of_int>0:
    temp = inp % (10 ** num_of_int) // (10 ** (num_of_int-1))
    if (temp > res):
        res = temp
    num_of_int = num_of_int - 1

print("Highest int is ",res,"\n")

"""

5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма 
(прибыль — выручка больше издержек, или убыток — издержки больше 
выручки). Выведите соответствующее сообщение. 
Если фирма отработала с прибылью, вычислите рентабельность 
выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите 
прибыль фирмы в расчете на одного сотрудника.

"""

print("5. Запросите у пользователя значения выручки и издержек фирмы.... \n")

rev = 0
while True:    #yeah yeah, double code...
    rev = input("Please, enter revenue: ")
    try:
        rev = int(rev)
        if (rev<0):
            print("Variable is negative, returning...")
        else:
            break
    except ValueError:
        print("Variable is not int, returning...","\n")

exp = 0
while True:    #yeah yeah, double code...
    exp = input("Please, enter expenses: ")
    try:
        exp = int(exp)
        if (exp<0):
            print("Variable is negative, returning...")
        else:
            break
    except ValueError:
        print("Variable is not int, returning...","\n")

fin_res = "profit"
if (rev - exp < 0):
    fin_res = "loss"

print("The company have ",fin_res," in amount ",str(rev-exp))
if (fin_res == "profit"):
    print("Profit margin is ",round(float(rev / exp - 1),2)*100,"%","\n")
    
    empl = 0
    while True:    #yeah yeah, double code...
        empl = input("Please, enter employee count: ")
        try:
            empl = int(empl)
            if (empl<1):
                print("Variable is negative or zero, returning...")
            else:
                break
        except ValueError:
            print("Variable is not int, returning...","\n")
    print("Profit per headcount is ",int((rev - exp)//empl),"\n")
    
"""

6. Спортсмен занимается ежедневными пробежками. 
В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % 
относительно предыдущего. Требуется определить номер дня, 
на который общий результат спортсмена составить не менее b 
километров. Программа должна принимать значения параметров 
a и b и выводить одно натуральное число — номер дня.

"""

print("\n","6. Спортсмен занимается ежедневными пробежками.", 
      "В первый день его результат составил a километров.... ","\n")

a = 0
while True:    #yeah yeah, double code...
    a = input("Please, enter a parametr: ")
    try:
        a = int(a)
        if (a<1 or a>9):
            print("Variable is not prime num, returning...")
        else:
            break
    except ValueError:
        print("Variable is not int, returning...","\n")
b = 0
while True:    #yeah yeah, double code...
    b = input("Please, enter b parametr: ")
    try:
        b = int(b)
        if (b<1 or b>9):
            print("Variable is not prime num, returning...")
        else:
            break
    except ValueError:
        print("Variable is not int, returning...","\n")

run_dist = a
day = 0
while (run_dist<b):
    run_dist = run_dist * 1.1
    day = day+1
    print ("Day ",day,": ", round(run_dist,2))
print("\n","Answer is: on the Day ",day," the sportman achieved result of at least ",b," km","\n")

