# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:59:15 2020

@author: Roman
"""

"""
1. Реализовать функцию, принимающую два числа 
(позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть 
обработку ситуации деления на ноль.
"""

print("1. Реализовать функцию, принимающую два числа...\n")

def divide (dividend,divisor):
    if divisor==0:
        return float('inf')
    else:
        return dividend/divisor
    

while True:
    nums = str(input("Enter dividend and divisor via space: ")).split(" ")
    if (len(nums)==2):    
        try:
            div1 = int(nums[0])
            div2 = int(nums[1])
            print("Result of division of ",div1," by ",div2," is ",divide(div1,div2))
            break
        except ValueError:
            print("Nums enetered incorrectly, returning...")
    else:
        print("Please, enter 2 nums, returning...")
        

"""
2. Реализовать функцию, принимающую несколько параметров, 
описывающих данные пользователя: имя, фамилия, год рождения, 
город проживания, email, телефон. 
Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
"""

print("\n2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя...\n")

def user_data(name = "absent",
              surname = "absent",
              year_birth = "absent",
              city = "absent",
              email = "absent",
              phone = "absent"):
    params = dict(
    {
     "name" : name,
     "surname": surname,
     "year_birth": year_birth,
     "city":city,
     "email":email,
     "phone":phone
     })
    print("\nEntered user parametrs:")
    for n in params: print(n,": ",params[n])
        

inp = str(input("Please, enter user data via space:\n")).split(" ")
while len(inp)<6:
    inp.append("absent")

user_data(name = inp[0],
              surname = inp[1],
              year_birth = inp[2],
              city = inp[3],
              email = inp[4],
              phone = inp[5])

"""
3. Реализовать функцию my_func(), которая принимает 
три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""

print("\n3. Реализовать функцию my_func(), которая принимает...\n")

def my_func(arg1, arg2, arg3):
    arr = [arg1,arg2,arg3]
    max_num = -999
    while True:
        for i, n in enumerate(arr):
            if (i>0):
                temp = arr[0]+arr[i]
                if (temp > max_num):
                    max_num = temp
        if (len(arr)<3):
            break
        arr = arr[1:len(arr)]
    return max_num

inp = [30,20,50]
print("Function inputs are ",inp,". Result is:\n",my_func(inp[0],inp[1],inp[2]))

"""
4. Программа принимает действительное положительное 
число x и целое отрицательное число y. Необходимо выполнить 
возведение числа x в степень y. Задание необходимо реализовать 
в виде функции my_func(x, y). При решении задания необходимо 
обойтись без встроенной функции возведения числа в степень.
"""

print ("4. Программа принимает действительное положительное число x и целое отрицательное число y...\n")

def my_func(x,y):
    return x**y

def my_func_2(x,y):
    num = 1
    for n in range(0,abs(y)):
        num *= x
    if (y<0):
        num = 1/num
    return num


while True:
    nums = str(input("Enter two nums via space: ")).split(" ")
    if (len(nums)==2):    
        try:
            nums[0] = float(nums[0])
            nums[1] = int(nums[1])
            if (div1>0 and div2 <0):
                break
            else:
                print("First num should be positive and second num should be negative, returning...")
        except ValueError:
            print("Nums enetered incorrectly, returning...")
    else:
        print("Please, enter 2 nums, returning...")

print("Result with ** functions is: ",my_func(nums[0],nums[1]),
      "\nResult with custom function is: ",my_func(nums[0],nums[1]),"\n")

"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных 
пробелом и снова нажать Enter. Сумма вновь введенных чисел 
будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, 
выполнение программы завершается. Если специальный символ введен 
после нескольких чисел, то вначале нужно добавить сумму этих чисел 
к полученной ранее сумме и после этого завершить программу.
"""

print("5. Программа запрашивает у пользователя строку чисел...\n")

num_sum = 0
End = False
while End==False:
    nums = str(input("Enter nums via space. Enter 'Done' to finish:\n")).split(" ")
    for i, n in enumerate(nums):
        if (n=="Done"):
            nums = nums[0:i]
            End = True
            break
        try:
            nums[i] = int(n)
        except ValueError:
            nums.remove(n)
    num_sum += sum(nums)
    print("Done!, current sum is ",num_sum)
print("End of program")

"""
6. Реализовать функцию int_func(), принимающую слово из 
маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text.
"""

def int_func(string):
    return string.capitalize()

words = str(input("Enter words via space.\n")).split(" ")
res = ""
for i, n in enumerate(words): 
    res += int_func(n) + " "
res = res[0:len(res)-1]

print("Result is:\n"+res)
    
    
    
            
