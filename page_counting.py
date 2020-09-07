# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:05:06 2020

@author: Melody
"""
from win32com import client as wc

word = wc.Dispatch('Word.Application')



doc = word.Documents.Open("C:/Users/86158/Desktop/新建文件夹/14年三网融合项目专项审计修改+-1.docx")



doc.Repaginate()

num_of_sheets = doc.ComputeStatistics(2)

#doc.Page(1).Range
print(num_of_sheets)

doc.Close() #关闭原来word文件