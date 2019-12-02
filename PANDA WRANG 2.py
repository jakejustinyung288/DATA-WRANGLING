# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 00:47:09 2019

@author: jakecool
"""
#DATA WRANGLING PROBLEM 2
import pandas as pd
DATA = {'Box': ['Box1','Box1','Box1','Box2','Box2','Box2'],
         'Dimension':['Length','Width','Height','Length','Width','Height'], 
         'Value':[6,4,2,5,3,4]}
messyDATA = pd.DataFrame(DATA, columns = ['Box','Dimension','Value'])
tidyDATA= messyDATA.pivot_table(index='Box', columns ='Dimension', values = 'Value')

tidyDATA['Volume']= tidyDATA.Length * tidyDATA.Width * tidyDATA.Height





