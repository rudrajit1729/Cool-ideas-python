# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:41:40 2019

@author: RUDRAJIT
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

file='data_file.xlsx'
xl=pd.ExcelFile(file)#reaing from excel file
dfs=xl.parse(xl.sheet_names[0])#parsing Excel sheet to data frame

dfs=list(dfs['Timeline'])
#print(dfs[20:50])
sid=SentimentIntensityAnalyzer()
str1="Name of the person"
str2="Updated"
str3="Years active"
str4="Years active"
dfs=dfs[:265]
for data in dfs:
    a=data.find(str1)
    b=data.find (str2)
    c=data.find(str3)
    d=data.find(str4)
    if a==-1 and b==-1 and c==-1 and d==-1:
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
