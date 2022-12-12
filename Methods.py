import sys
sys.path.append('C:\\Users\\gubis\\projects\\MAP_codes')
from Interpol.Methods import Spline2, Lagrange

import numpy as np
from time import time
import matplotlib.pyplot as plt


#=====================================================================
#=====================================================================


def Simps(x_data: np.ndarray, y_data: np.ndarray, interval: list=None, step: float=0.01, interpol: bool=False) -> float:
    if interval==None:
        b = x_data[-1]
        a = x_data[0]
    
    if interpol==True:
        if len(x_data)<=15:
            f = Lagrange(x_data,y_data)
            x = np.arange(a,b+step,step)
            y = f.at(x)
        else:
            x,y = Spline2(x_data,y_data,step=step)
    else:
        x,y = x_data,y_data

    s = y[0] + y[-1]
    for i in range(1,len(y)-1):
        if i%2:
            s+=4*y[i]
        else:
            s+=2*y[i]
    I = step*s/3

    print(f"\nIntegration at Interval= [{a},{b}] is:\nI={I}\n")
    return I


#=====================================================================
#=====================================================================


def Trapz(x_data: np.ndarray, y_data: np.ndarray, interval: list=None, step: float=0.01, interpol: bool=False) -> float:
    if interval==None:
        b = x_data[-1]
        a = x_data[0]
    
    if interpol==True:
        if len(x_data)<=15:
            f = Lagrange(x_data,y_data)
            x = np.arange(a,b+step,step)
            y = f.at(x)
        else:
            x,y = Spline2(x_data,y_data,step=step)
    else:
        x,y = x_data,y_data
    
    y_mean = (y[1:]+y[:-1])/2

    I = sum(y_mean*step)

    print(f"\nIntegration at Interval= [{a},{b}] is:\nI={I}\n")
    return I