#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 12:12:59 2021

@author: dawid
"""


# %%
#-------------------ZADANIE 1----------------------
import csv
def count_quantity_of_signs_in_file(filePath):
    quantity_of_signs = 0
    file = open(filePath)
    for row in csv.reader(file):
        quantity_of_signs = quantity_of_signs + len(row[0])
    return quantity_of_signs


    
print(count_quantity_of_signs_in_file('/home/dawid/Documents/studia/II rok/III semestr/python/workspace/lab03.csv'))


# %%
#-------------------ZADANIE 2----------------------
import csv

def seach_file_for_palindrome(filePath):
    file = open(filePath)
    newFile = '/home/dawid/Documents/studia/II rok/III semestr/python/workspace/palindrome.csv'
    lp = 1;
    for row in csv.reader(file):
        if (checkIfPalindrome(row[0])):
            saveWordToFile(newFile, lp, row,'true')
            lp = lp + 1
        else:
            saveWordToFile(newFile, lp, row,'false')
            lp = lp + 1

def checkIfPalindrome(row):
    return row == row[::-1]
        
    
def saveWordToFile(filePath, lp, row, isPalindrome):
    file = open(filePath,'a',newline='')
    rowforFile = [lp, row[0], isPalindrome]
    csv.writer(file).writerow(rowforFile)
    file.close()
    
seach_file_for_palindrome('/home/dawid/Documents/studia/II rok/III semestr/python/workspace/lab03words.csv')
    

# %%
#-------------------ZADANIE 3----------------------
import csv

setOfYearsWithMonths = set()

def createGroupsForAverage(filePath):
    file = open(filePath)
    for row in csv.reader(file, delimiter=' '):
        yearWithMonth = f"{row[0]} {row[2]}"
        setOfYearsWithMonths.add(yearWithMonth);

def prepareData(filePath):
    file = open(filePath)
    dic = {}
    for row in csv.reader(file, delimiter=' '):
        yearWithMonth = f"{row[0]} {row[2]}"
        if(dic.get(yearWithMonth) == None):
            dic.update({yearWithMonth : [row[4], 1]})
        else:
            dic.get(yearWithMonth)
            curentAgregateValue = float(dic.get(yearWithMonth)[0])
            curentNumberOfValues = int(dic.get(yearWithMonth)[1])
            dic.update({yearWithMonth : [curentAgregateValue + float(row[4]), curentNumberOfValues+1]})
    return dic
 

def calculateAveragePerMonth(dic):
    dicOfAverages = {}
    for item in dic.items():
        average = item[1][0] / item[1][1]
        dicOfAverages.update({item[0]:average})
    return dicOfAverages
        
def saveToFile(dictionary, filePath):
    file = open(filePath,'a',newline='')
    for item in dictionary.items():
        rowforFile = [item[0], ":", round(item[1],2)]
        csv.writer(file, delimiter=' ').writerow(rowforFile)
    file.close()



        
createGroupsForAverage('/home/dawid/Documents/studia/II rok/III semestr/python/workspace/lab03.csv')
saveToFile(calculateAveragePerMonth(prepareData('/home/dawid/Documents/studia/II rok/III semestr/python/workspace/lab03.csv')),'/home/dawid/Documents/studia/II rok/III semestr/python/workspace/result.csv')  
 
# %%
#-------------------ZADANIE 4----------------------

month = input("Podaj rozmiar miesiąc: ")
year = input("Podaj rok: ")

def findData(filePath):
    file = open(filePath)
    for row in csv.reader(file, delimiter=' '):
        data = str(month) + " " + str(year)
        if(data == row[0]):
            print(row[2])
            
findData('/home/dawid/Documents/studia/II rok/III semestr/python/workspace/result.csv');

    





# %%
    