# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 00:34:47 2019

@author: jakecool
"""
#DATA WRANGLING PROBLEM 1
import pandas as pd

MATH = {'Student': ['Ice Bear','Panda','Grizzly'], 'Math':[80,95,79]}
ELECTRONICS = {'Student': ['Ice Bear','Panda','Grizzly'], 'Electronics':[85,81,83]}
M = pd.DataFrame(MATH, columns = ['Student','Math'])
E = pd.DataFrame(ELECTRONICS, columns = ['Student','Electronics'])

X = pd.merge (M,E)


GEAS = {'Student': ['Ice Bear','Panda','Grizzly'], 'GEAS':[90,79,83]}
ESAT = {'Student': ['Ice Bear','Panda','Grizzly'], 'ESAT':[93,89,88]}
G = pd.DataFrame(GEAS, columns = ['Student','GEAS'])
ES = pd.DataFrame(ESAT, columns = ['Student','ESAT'])

Y = pd.merge (X,G)

Z = pd.merge (Y,ES)

long_format = pd.melt(Z, id_vars = 'Student', 
                      value_vars = ['Math','Electronics','GEAS','ESAT'])

long_format_final = long_format.rename(columns = {'variable':'Subjects','value':'Grades'})

