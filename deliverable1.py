#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:15:55 2023

@author: annareeder
"""
##loading in module 
import pandas as pd
##loading in data 

repo='https://github.com/reederan/DropsOfJupyter/raw/main/'
csvfile1='annual-number-of-deaths-by-cause.csv'
csvfile2='distribution-human-rights-vdem.csv'
csvfile3='water-and-sanitation.csv'
deathscsv=pd.read_csv(repo + csvfile1)
humanrightscsv=pd.read_csv(repo + csvfile2)
sanitationcsv=pd.read_csv(repo + csvfile3)

##cleaning and formatting

