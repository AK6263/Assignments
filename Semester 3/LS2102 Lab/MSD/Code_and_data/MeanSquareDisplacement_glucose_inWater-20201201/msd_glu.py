dd# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:29:09 2020

@author: abhay

For 276K 
One for 30 molecules : 6000 and 4000
One for 25 molecules : 6000 and 4000
One for 20 molecules : 6000 and 4000

For 310K 
One for 30 molecules : 6000 and 4000
One for 25 molecules : 6000 and 4000
One for 20 molecules : 6000 and 4000

For 340K 
One for 30 molecules : 6000 and 4000 /
One for 25 molecules : 6000 and 4000 /
One for 20 molecules : 6000 and 4000 /
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import os
import pandas as pd
#%%

def f(x,m):
    return m*x
def fitter(x,y,m):
    popt,pcov = curve_fit(f, x, y)
    X = np.linspace(0,max(x)+100,100)
    Y = f(X,*popt)
    error = np.sqrt(np.sum((y - f(x,*popt))**2))
    plt.plot(X,Y,label = "m = {} , RMSE = {}, slope = {:e}".format(m,round(error),*popt))
    print(popt,error)
#%%
path = "276K"
t0 = "500_"
t0 = "1000"    
data = os.listdir(path)
for file in data:
    m = file[7:9]
    to = file[10:14]
    if to == t0:
        df =np.loadtxt(path + "/" + file, delimiter = " ")
        x,y = df[:,0],df[:,1]
        plt.scatter(x,y,s = 5,marker = ".",label = "m = " + m)
        fitter(x,y,m)
        plt.xlabel("tcor (1 unit = 0.1 ps)")
        plt.ylabel("MSD $<x^2>$ (Angstorm$^2$) ")
        plt.legend()
        plt.title("Temp = " + path)
        print(file,m,to)
plt.savefig(path +"_"+t0+"25" + ".png")

    

