# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:47:30 2020

@author: Roman
"""

"""

1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. Элементы списка 
можно не запрашивать у пользователя, а указать явно, в программе.

"""

print("\n","1. Создать список и заполнить его элементами различных типов данных....\n")

var_list = ["Var",100,["test","inner","list"],"100"]
print("My various types list is ",var_list," with type ",type(var_list),"\n")
for i in range(0,len(var_list)):
    var_list[i] = type(var_list[i])
print("Types of the list variables are: ",var_list,"\n")

"""

2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().

"""

print("2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элемен...","\n")

input_list = []
while True:
    var_to_append = input("Enter var to recond in the list or enter 'Done' to finish the list\n")
    if (var_to_append == 'Done'):
        break
    input_list.append(var_to_append)

print("Initial input list is as follows:\n",input_list)
for i in range(0,len(input_list)):
    if (i % 2 == 1):
        temp = input_list[i - 1]
        input_list[i - 1] = input_list[i]
        input_list[i] = temp
print("Processed input list is as follows:\n",input_list,"\n")

"""

3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict.

"""

print("3. Пользователь вводит месяц в виде целого числа от 1 до 12....","\n")

while True:
    inp = input("Please, enter month num: ")
    try:
        inp = int(inp)
        if (inp>12 or inp<1):
            print("The num can't be interpreted as a month, returning...")
        else:
            break
    except ValueError:
        print("Entered value is not a num, returning...")
        

seasons_dict = {
        "Winter":[12,1,2],
        "Autumn":[3,4,5],
        "Summer":[6,7,8],
        "Fall":[9,10,11]
        }

seasons_list = [
        ["Winter",12,1,2],
        ["Autumn",3,4,5],
        ["Summer",6,7,8],
        ["Fall",9,10,11]
        ]

for i in seasons_dict:
    if seasons_dict[i].count(inp) > 0:
        print("Search in dictionary shows: ",i)
        break

for i in seasons_list:
    if i.count(inp)>0:
        print("Search in list shows: ",i[0])
        break

"""

4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове.

"""

print("4. Пользователь вводит строку из нескольких слов, разделённых пробелами...","\n")
inp = input("Enter the words:\n")
print("\nCompleted list is below:")
word_list = inp.split(" ")
for i in word_list:
    print(i[0:min(10,len(i))])

"""

5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий 
набор натуральных чисел. У пользователя необходимо запрашивать новый 
элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми 
значениями, то новый элемент с тем же значением должен 
разместиться после них.

"""

rating_list = [6,3,1]
print:("Initial list is as follows:\n",rating_list)
while True:
    while True:
        inp = input("Please, enter prime num or 'Done' to exit: ")
        if (inp =='Done'):
            break
        try:
            inp = int(inp)
            if (inp>9 or inp<0):
                print("The num can't be interpreted as a prime num, returning...")
            else:
                break
        except ValueError:
            print("Entered value is not a num, returning...")
    if (inp =='Done'):
        break
    rating_list.append(inp)
    rating_list.sort(reverse=True)
    print("Current sorted list is as follows:\n",rating_list)
    
"""

6. * Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с 
параметрами (характеристиками товара: название, цена, количество, 
единица измерения). Структуру нужно сформировать программно, т.е. 
запрашивать все данные у пользователя.

Необходимо собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, 
например название, а значение — список значений-характеристик, 
например список названий товаров.
    
"""

print("6. * Реализовать структуру данных «Товары»...\n")

Goods = []
#receive command
command_list =["Add","Get","Done"]
while True:
    inp = input("Please enter command:\nAdd: add a merchandise\nGet: get info about merchandise via index\nDone: Exit the program\n")
    if (command_list.count(inp)<1):
        print("Command not found, returning...")
    elif (inp == 'Done'):
        break        
    # Add command
    if (inp=="Add"):
        index = len(Goods)+1
        dict_to_add = dict()
        while True:
            dict_key = input("Please enter good parametr or 'Done' to finish adjust parametrs:\n")
            if (dict_key=="Done"):
                break
            dict_description = input("Please enter description:\n")
            dict_to_add.update({dict_key : dict_description})
        set_to_add = (index,dict_to_add)
        Goods.append(set_to_add)
        print(set_to_add)
    # Get command
    if(inp == "Get"):
        general_dict = dict()
        #forming keys
        for i in Goods:
            general_dict.update(i[1])
        #forming descriptions
        for n in list(general_dict.keys()):
            desc_list = []
            for i in Goods:
                try:
                    desc_list.append(i[1][n])
                except KeyError:
                    desc_list
            general_dict.update({n:desc_list})
        print("Goods analytics presented below:\n",general_dict)




