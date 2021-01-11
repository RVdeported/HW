# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 11:24:54 2020

@author: Roman
"""

import json

"""
1. Создать программно файл в текстовом формате, записать 
в него построчно данные, вводимые пользователем. 
Об окончании ввода данных свидетельствует пустая строка.
"""

print("\n1. Создать программно файл в текстовом формате, записать...\n")

with open("File_1.txt","w") as file:
    while True:
        inp = input("Please, enter string:\n")
        if inp == "":
            print("Finishing writing...")
            break
        print(inp,file = file)
with open("File_1.txt","r") as file:
    print("Outcome file content:\n",file.read())
    

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

print("\n2. Создать текстовый файл (не программно), сохранить в нем несколько...\n")

with open("Lesson_5_1.txt","r") as file:
    lines = file.readlines()
    words = []
    for i in lines:
        words.append(len(i.split(" ")))
    lines = len(lines)
    print("\nLines count: ",lines,", words count in each line ",words)

"""
3. Создать текстовый файл (не программно), построчно записать 
фамилии сотрудников и величину их окладов. Определить, кто из 
сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

print("\n3. Создать текстовый файл (не программно), построчно записать...\n")
with open("Lesson_5_2.txt","r") as file:
    content = file.readlines()
    print("File content:\n",content)
salary_arr = []
for i in content:
    name, salary = i.split(":")
    salary_arr.append([name,int(salary)])
average_salary = sum([i[1] for i in salary_arr])/len(salary_arr)
low_salary = [i[0] for i in salary_arr if i[1]<20000]
print("\nAverage salary is ",average_salary," Low earniers:",low_salary)


"""
4. Создать (не программно) текстовый файл со следующим содержимым:
Необходимо написать программу, открывающую файл на чтение и 
считывающую построчно данные. При этом английские числительные 
должны заменяться на русские. Новый блок строк должен записываться 
в новый текстовый файл.
"""

print("\n4. Создать (не программно) текстовый файл со следующим...\n")
numbers={
        "One":"Один",
         "Two":"Два",
         "Three":"Три",
         "Four":"Четыре",
         }

with open("Lesson_5_3.txt","r") as file:
    lines = file.readlines()
res = []
for i in lines:
    temp = i.split(" ")
    temp[0] = numbers[temp[0]]
    line = temp[0]+" "+temp[1]+" "+temp[2]
    res.append(line)

with open("File_2.txt","w",encoding="UTF-8") as file:
    file.writelines(res)

with open("File_2.txt","r",encoding="UTF-8") as file:
    print("Result of transformation:\n",file.read())
    
    
"""
5. Создать (программно) текстовый файл, записать в него программно 
набор чисел, разделенных пробелами. Программа должна подсчитывать 
сумму чисел в файле и выводить ее на экран.
"""
print("\n5. Создать (программно) текстовый файл, записать в него...\n")

numbers = "3 5 3 6 3 10 32 10 95 34"
with open("File_3.txt","w") as file:
    file.writelines(numbers)

with open("File_3.txt","r") as file:
    file_sum = sum([int(i) for i in file.read().split(" ")])
    file.seek(0)
    print("Input text in file is:\n",
          file.read(), 
          "\n File sum is ",
          file_sum
          )

"""
6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее 
количество занятий по нему. Вывести словарь на экран.
"""
lines = []

with open("Lesson_5_4.txt","r") as file:
    lines = file.readlines()
lines_splitted = [i.split(":") for i in lines]
names = [i[0] for i in lines_splitted]
numbers = [i[1].split(" ") for i in lines_splitted]
for ind, item in enumerate(numbers):  
    numbers[ind].remove("")
summary_time = []
for ind, item in enumerate(numbers):    
    temp = 0
    for i in item:
        temp += int(i[0:i.find("(")])
    summary_time.append(temp)

result = {}
for i, item in enumerate(names):
    result.update({names[i]:summary_time[i]})

print("\n6. Необходимо создать (не программно) текстовый файл...\n")
with open("Lesson_5_4.txt","r") as file:
    print("Input file content:\n",file.read(),"\n",
          "Output dictionary:\n",result)

"""
7. Создать (не программно) текстовый файл, в котором каждая строка 
должна содержать данные о фирме: название, форма 
собственности, выручка, издержки.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчет 
средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и 
их прибылями, а также словарь со средней прибылью. Если фирма 
получила убытки, также добавить ее в словарь (со значением убытков).

Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""

print("\n7. Создать (не программно) текстовый файл, в котором...\n")

with open("Lesson_5_5.txt","r",encoding="UTF-8") as file:
    lines = file.readlines()
company_dataset = []
"""
in company_dataset:
    [0-3] - initial data
    [4] - income

"""
for_avg = [0,0]
for i in lines:
    temp = i.split(" ")
    temp[2:4] = [int(temp[2]),int(temp[3])]
    temp.append(temp[2]-temp[3])
    for_avg[0] += temp[4] * int(temp[4] >= 0)
    for_avg[1] += int(temp[4] >= 0)
    company_dataset.append(temp)

avg = for_avg[0] / for_avg[1]
out_list = []
company_dict = {}
for i in company_dataset:
    company_dict.update({i[0]:i[4]})
avg_dict = {'average_profit':avg}
out_list.append(company_dict)
out_list.append(avg_dict)

with open("File_4.json","w") as file:    
    json.dump(out_list,file)
    print("Result is saved in ",file.name)
    



