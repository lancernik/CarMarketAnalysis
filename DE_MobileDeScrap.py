# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:50:16 2019
 
@author: lancernik
"""
 
from __future__ import division, unicode_literals
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import string
import re
from itertools import groupby
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde
from scipy.stats import kde
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import codecs
import requests
 
 
 
 
 
 
 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
 
 
 
 
 
def ScrapPage(marka,model,pg_num):
   
    #DriverSet
#        dr.get("https://www.mobile.de/pl/samochod/volkswagen-passat/vhc:car,pgn:{},pgs:50,ms1:25200_25_".format(marka,model,pg_num))
#     https://www.mobile.de/pl/samochod/opel-vectra/vhc:car,pgn:%7B%7D,pgs:50,ms1:19000_10_
    dr = webdriver.Chrome(executable_path=r'C:\Users\lancernik\Desktop\chromedriver_win32\chromedriver.exe')
    dr.get("https://www.mobile.de/pl/samochod/skoda-fabia/vhc:car,pgn:{},pgs:50,ms1:22900_6_".format(pg_num))
#    dr.get("https://suchen.mobile.de/fahrzeuge/search.html?isSearchRequest=true&makeModelVariant1.makeId=25200&makeModelVariant1.modelId=g37&maxPowerAsArray=KW&minPowerAsArray=KW&pageNumber={}&scopeId=C&sfmr=false".format(pg_num))
    bs = BeautifulSoup(dr.page_source,'html.parser')
    dr.quit()
   
   
    #Scrapuje date produkcji
   
   
    #Stage 2 - Usuwa spacje z tekstu
    #Stage 3 - Usuwa niewidzialne spacje z tekstu
    #Stage 4 - Zmienia wiek z niczego na 2019 rok dla nowych
    #Stage 5 - Znajduje wszystkie wartosci liczbowe
    age_stage1 = str(bs.find_all(class_="u-text-bold"))
    age_stage2 = age_stage1.translate({ord(c): None for c in string.whitespace})
    age_stage3 = re.sub(r"\s+", '', age_stage2)
    age_stage4 = re.sub(r'>0km<', '05/2019,1km,', age_stage3)
    age_stage5 = [int(s) for s in re.findall(r'\b\d+\b',age_stage4)]
    #Stage 6 - Usuwa numer miesiaca z daty
    age_from_page = [i for i in age_stage5 if i >= 1700 and i<= 2020]
   
   
   
   
    #Scrapuje przebieg
   
   
    #Stage 1 - usuwanie dekodowania, bez tego nie mozna sub'owac
    #Stage 2 - Podmiana 0 km, aby nowe samochody byly w datasecie
    #Stage 3 - usuwanie wyszukujemy wartosci miedzy kilometrami
    mileage_stage1 = str(bs.decode('UTF-8'))
    mileage_stage2 = re.sub(r' 0 km', '05/2019,1km,', mileage_stage1)
    mileage_stage3 = [s for s in re.findall(",(.*)km", mileage_stage2)]
    #Stage 4 - usuwnie spalania w litrach na 100 km
    ztemp=[]
    for i in mileage_stage3:
        ztemp.append(re.sub(r"\s+", '', i))
        mileage_from_page = [int(i) for i in ztemp if i.isdigit()]
   
   
   
    #Scrapuje cene
       
       
    #Stage 2 - usuwa spacje
    #Stage 3 - usuwa niewidzialne spacje (&nbsp;)
    #Stage 4-8 usuwa zbedna tresc
    #Stage 9 - Tworzy liste
    price_stage1 = str(bs.find_all(class_="seller-currency u-text-bold"))
    price_stage2 = price_stage1.translate({ord(c): None for c in string.whitespace})
    price_stage3 = re.sub(" ",'',price_stage2)
    price_stage4 = re.sub('<pclass="seller-currencyu-text-bold">','',price_stage3)
    price_stage5 = re.sub('</p>','',price_stage4)
    price_stage6 = price_stage5.replace('[', "")
    price_stage7 = price_stage6.replace(']', "")
    price_stage8 = price_stage7.replace('EUR(brutto)', "")
    price_stage9 = price_stage8.replace(u'\xa0', u'')
    
    price_stage10 = price_stage9.split (",")
    #price_stage9 = price_stage8.split (",")
    #Stage 10 - mnozy przez wartosc euro
    try:
        price_from_page = [round(int(x)*4.28) for x in price_stage10]

   
   
   
   
    #Tworzy dict z poszczegolnej strony
   
        datadict = {'Marka':'Marka','Model':'Model','Milage':[0],'Age':[0],'Price':[0]}
        dataset = pd.DataFrame(data=datadict)
        marka_out=["{}".format(marka)] * len(age_from_page)
        model_out=["{}".format(model)] * len(age_from_page)
        if len(mileage_from_page) == len(age_from_page) == len(price_from_page) ==len(model_out) == len(marka_out):
            df = pd.DataFrame(
            {'Milage':mileage_from_page,
             'Age': age_from_page,
             'Price': price_from_page,
             'Marka':marka_out,
             'Model':model_out})
       
            dataset = dataset.append(df,ignore_index=True)
    except:
        return None
    return dataset
 
def ScrapModel(marka,model,start,stop):
 
    datadict = {'Milage':[0],'Age':[0],'Price':[0]}
    dataset_out = pd.DataFrame(data=datadict)
   
    for i in range(start,stop):
        TempData = ScrapPage(model,marka,i)
        dataset_out = dataset_out.append(TempData,ignore_index=True)
        print(dataset_out)
       
    dataset_out.to_csv('{}-{}-mobile.csv'.format(marka,model))
    return dataset_out
 
 
 
test = ScrapModel("skoda","octavia",1,150)
#print(test)
    






#
#marka = "opel"
#model = "corsa"
#pg_num = 1
#dr = webdriver.Chrome(executable_path=r'C:\Users\lancernik\Desktop\chromedriver_win32\chromedriver.exe')
#dr.get("https://www.mobile.de/pl/samochod/{}-{}/vhc:car,pgn:{},pgs:50,ms1:19000_10_".format(marka,model,pg_num))
#bs = BeautifulSoup(dr.page_source,'html.parser')
##dr.quit()
#   
#   
##Scrapuje date produkcji
#   
#
#
#   
##Stage 2 - usuwa spacje
##Stage 3 - usuwa niewidzialne spacje (&nbsp;)
##Stage 4-8 usuwa zbedna tresc
##Stage 9 - Tworzy liste
#price_stage1 = str(bs.find_all(class_="seller-currency u-text-bold"))
#price_stage2 = price_stage1.translate({ord(c): None for c in string.whitespace})
#price_stage3 = re.sub(" ",'',price_stage2)
#price_stage4 = re.sub('<pclass="seller-currencyu-text-bold">','',price_stage3)
#price_stage5 = re.sub('</p>','',price_stage4)
#price_stage6 = price_stage5.replace('[', "")
#price_stage7 = price_stage6.replace(']', "")
#price_stage8 = price_stage7.replace('EUR(brutto)', "")
#
#price_from_page = price_stage8.replace(u'\xa0', u'')
#price_from_page = price_from_page.split (",")
#
#
#print(price_from_page)
#
#print(price_from_page1)