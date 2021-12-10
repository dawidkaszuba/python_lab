#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:59:20 2021

@author: dawid
"""

# %%
#-------------------ZADANIE 1----------------------
import csv
import datetime
import calendar

day = int(input("Podaj dzień: "))
month = int(input("Podaj miesiąc: "))
year = int(input("Podaj rok: "))

date = datetime.datetime(year, month, day)


def how_many_exams(date):
    file = open('/home/dawid/Documents/studia/II rok/III semestr/python/workspace/sesjaEgzaminacyjna.csv')
    exams_list = []
    counter = 0
    for row in csv.reader(file, delimiter = ' '):
        e_day = int(row[0])
        e_month = list(calendar.month_abbr).index(row[1])
        e_year = int(row[2])
        e_date = datetime.datetime(e_year, e_month, e_day)
        exams_list.append(e_date)  
    file.close()
    
    for date_of_exam in exams_list:
        if date_of_exam > date:
            counter = counter+1
    print("Liczba pozostałych egzaminów: " +  str(counter))
    
how_many_exams(date)
# %%

import re

from datetime import date

today = date.today()
date_format = input("Podaj format daty: ")


if(re.search('[d]{2}', date_format) != None):
    date_format = re.sub('[d]{2}', str(today.day), date_format)
else:
    print("Niepoprawny format dnia!")
    
if(re.search('[m]{2}', date_format) != None):
    date_format = re.sub('[m]{2}', str(today.month), date_format)
else:
    print("Niepoprawny format miesiąca!")
    
if(re.search('[y]{4}', date_format) != None):
   date_format = re.sub('[y]{4}', str(today.year), date_format)
elif(re.search('[y]{2}', date_format) != None):
   date_format = re.sub('[y]{2}', today.strftime('%y'), date_format)
else:
    print("Niepoprawny format roku!")
    
print(date_format)
    



 
        

    

# %%