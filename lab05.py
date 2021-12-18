#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:05:25 2021

@author: dawid
"""

# %%

import pandas
import names
import random


table = []


def get_random_mark():
    return random.randint(2, 5)


for i in range(0,60):
    student = [names.get_first_name(), names.get_last_name(), 
               random.randint(10000, 99999), random.choice(['II','I']),
               get_random_mark(),get_random_mark(),get_random_mark()]
    table.append(student)
    
data = pandas.DataFrame(table)
data.columns = ['FirstName', 'LastName', 'AlbumNr', 'GrName','Kol1Note', 'Kol2Note', 'ProjectNote' ]

#data.sort_values("FirstName", inplace=True)

print(data['Kol1Note'].corr(data['Kol2Note']))
print(data)

print("Maksymalną ocenę z kol1 zdobyło: " + str(data['Kol1Note'][data['Kol1Note'] > 4].count()))
print("Maksymalną ocenę z kol2 zdobyło: " + str(data['Kol2Note'][data['Kol2Note'] > 4].count()))

print(str(data['Kol2Note'][data['Kol2Note'] < 3].count()) + " osób nie zdało kolokwium nr 2.")


print("Mediana ocen w grupie II z kol 2: " + str(data[data['GrName']=='II']['Kol2Note'].median()))

print("Średnia ocen w grupie I z kol 1: " + str(data[data['GrName']=='I']['Kol1Note'].mean()))
print("Mediana ocen w grupie II z kol 1:: " + str(data[data['GrName']=='II']['Kol1Note'].mean()))

series = [data[data['GrName']=='I']['Kol1Note'],data[data['GrName']=='I']['Kol2Note']]

result = pandas.concat(series)


print("Mediana ocen w grupie II z pierwszego i drugiego kolokwium: " + str(result.median()))

# %%

import pandas
import numpy.random

data = pandas.read_csv('abalone.csv')
#print(data.dtypes)
#data.drop(columns=['Sex'], inplace=True)
#data2 = data.drop(columns=['Length'])

#data.rename(columns={'Sex':'Type'}, inplace=True)
#print(data.isnull().sum())
#print(data['Length']-data['Diameter'])

#data.replace(0.365,0.667, inplace=True)


#data['Diameter'].plot()
#print(data)
#data.plot(x='Diameter', y='Length').plot()

#series = pandas.Series(3 * numpy.random.rand(5),
 #                     index=['3.0','3.5','4.0','4.5', '5,0'],
  #                    name='Prawdopodobny rozkład ocen z przedmiotu :)')

#series.plot.pie()

print(data['Length'].get(3))



# %%

