# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:29:09 2020

@author: abhay

For 295K 
2000 and 1000

For 310K 
2000 and 1000

For 325K 
2000 and 1000
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import os
import pandas as pd
#%%
def f(x,m,c):
    return m*x + c
def fitter(x,y,path):
    popt,pcov = curve_fit(f, x, y)
    X = np.linspace(0,max(x)+300,100)
    Y = f(X,*popt)
    error = np.sqrt(np.sum((y - f(x,*popt))**2))
    plt.plot(X,Y,label = "Temp = {} , RMSE = {}, slope = {:e}".format(path,round(error),popt[0]))
    print(popt,error)
#%%
f_ = ["295K","310K","325K"]
tcor = ["1000","2000"]
path = f_[0]

data = os.listdir(path)
for file in data:
    #m = file[7:9]
    to = file[7:11]
    #if to == t0:
    df =np.loadtxt(path + "/" + file, delimiter = " ")
    x,y = df[:,0],df[:,1]
    plt.scatter(x,y,s = 5,marker = ".",label = "tcor = " + to)
    fitter(x[400:],y[400:],to)
    plt.xlabel("time (ps)")
    plt.ylabel("MSD $<x^2>$")
    plt.legend()
    plt.title("Temp = " + path)
    print(file,to)

plt.savefig(path +"_1000_2000"+".png")


#%%

t0 = tcor[1]
f_ = ["295K","310K","325K"]

for path in f_:
    data = os.listdir(path)
    for file in data:
        #m = file[7:9]
        to = file[7:11]
        if to == t0:
            df =np.loadtxt(path + "/" + file, delimiter = " ")
            x,y = df[:,0],df[:,1]
            #plt.scatter(x,y,s = 5,marker = ".",label = "tcor = " + to)
            fitter(x[400:],y[400:],path)
            plt.xlabel("time (ps)")
            plt.ylabel("MSD <x>")
            plt.legend()
            plt.title("TCor = " + t0)
            print(file,to)
plt.savefig(t0+".png")
