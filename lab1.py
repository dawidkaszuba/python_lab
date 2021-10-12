#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 21:21:35 2021

@author: dawid
"""
# %%
#-------------------ZADANIE 1----------------------
import random
from statistics import mean
import math


list = []

arraySize = input("Podaj rozmiar tablicy: ")
arraySizeAsInt = int(arraySize)

for number in range(arraySizeAsInt):
    list.append(random.random())

avg = sum(list)/len(list)
avgEmbedded = mean(list)
print("Średnia: ", avg)
print("Średnia (wbudowna funkcja): ", avgEmbedded)

list.sort()
print("Posortowana lista: ", list)


if(len(list) % 2 == 0):
    mediana = list[math.ceil(len(list)/2)] + list[math.floor(len(list)/2)] / 2
else:
    mediana = list[(math.floor(len(list)/2))]

print("Mediana: ", mediana)    
    
#%%
#-------------------ZADANIE 2----------------------
import random

arraySize = input("Podaj rozmiar tablicy: ")
arraySizeAsInt = int(arraySize)

tempSize = arraySizeAsInt


def generate_list_mltp_types():
    list = []
    listOfStrings = generate_random_string(generate_quantity_of_strings())
    listOfInts = generate_random_integer(generate_quantity_of_int())
    listOfBoolens = generate_random_boolean(generate_quantity_of_boolens())
    listOfFloats = generate_random_float(generate_quantity_of_float())
    list.extend(listOfStrings)
    list.extend(listOfInts)
    list.extend(listOfBoolens)
    list.extend(listOfFloats)
    return list
    
   
def generate_quantity_of_strings():
    global tempSize
    value = random.randint(1, tempSize-3)
    tempSize = tempSize - value
    return value

def generate_quantity_of_int():
    global tempSize
    value = random.randint(1, tempSize-2)
    tempSize = tempSize - value
    return value

def generate_quantity_of_boolens():
    global tempSize
    value = random.randint(1, tempSize-1)
    tempSize = tempSize - value
    return value

def generate_quantity_of_float():
    global tempSize
    value = random.randint(1, tempSize)
    tempSize = tempSize - value
    return value



def generate_random_string(quantityofStrings):
    word = []
    list12 = []
    sizeOfString = random.randint(1, 20)
    
    for s in range(quantityofStrings):
        for x in range(sizeOfString):
            char = chr(random.randint(97, 122))
            word.append(char)
        b = ''.join(word)
        word = []
        list12.append(b)
        b = " "
    return list12
        
def generate_random_boolean(quantityOfBoolens):
    list2 = []
    for y in range(quantityOfBoolens):
        list2.append(random.choice([True,False]))
    return list2

def generate_random_integer(quantityOfIntegers):
    list3 = []
    for z in range(quantityOfIntegers):
        list3.append(random.randint(1, 100))    
    return list3
    
def generate_random_float(quantityOfFloats):
    list4 = []
    for w in range(quantityOfFloats):
        list4.append(random.uniform(1, 100))    
    return list4

def generate_four_lists(list):
    listOfInts = []
    listOfFloats = []
    listOfBoolens = []
    listOfStrings = []
    for x in list:
        if type(x) == int:
            listOfInts.append(x)
        if type(x) == float:
            listOfFloats.append(x)
        if type(x) == bool:
            listOfBoolens.append(x)
        if type(x) == str:
            listOfStrings.append(x)
    print(listOfInts)
    print(listOfFloats)
    print(listOfBoolens)
    print(listOfStrings)
            

generate_four_lists(generate_list_mltp_types())

#%%
#-------------------ZADANIE 3----------------------

list1 = [1,2,3,4,5,6,7,8,9]


def aaa(list1):
    list = []
    list1.reverse()
    for i in range(0,len(list1)):
        if i % 2 ==0:
            list.append(list1[i])
    return list

print(aaa(list1))        
    

#%%
#-------------------ZADANIE 4----------------------

from collections import deque
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c','d','e','f','g','h','i','j','k','l']
list3 = []

def merge(list1, list2):
    flag = 1
    list1a = deque(list1)
    list1b = deque(list2)
    while(bool(list1a) | bool(list1b)):
        if flag == 1:
            if bool(list1a):
                list3.append(list1a.popleft())
            flag = 2
        else:
            if bool(list1b):
                list3.append(list1b.popleft())
            flag = 1
    return list3
            
print(merge(list1, list2))
#%%
#-------------------ZADANIE 5----------------------

list = [1,2,"asd", 4,"xcx", -1, 'asda']

def sortList(list):
    list1 = []
    list2 = []
    list3 = []
    for x in list:
        if type(x) == str:
            list1.append(x)
        else:
            list2.append(x)
    list3.extend(sorted(list2))
    list3.extend(sorted(list1))
    return list3
print(sortList(list))
    
#%%




