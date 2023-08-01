import matplotlib.pyplot as plt
from numpy import *
import numpy as np
import pandas as pd
from scipy.constants import c
# data input
gal_lon,gal_lat,Temperature,cos_theta,sigma=np.loadtxt('/home/soumadip/Documents/Motion-of-solar-system/Code/final-data.csv',delimiter=',',unpack=True)

def deg_rad(deg):
    rad = np.pi * deg/180
    return rad

def costheta(l1,b1,l2,b2):
    l1=deg_rad(l1)
    b1=deg_rad(b1)
    l2=deg_rad(l2)
    b2=deg_rad(b2)
    a,b,c = np.zeros(len(l1)), np.zeros(len(l1)), np.zeros(len(l1))
    for i in range(len(l1)):
        a[i]=np.cos(b1[i])*np.cos(l1[i])*np.cos(b2)*np.cos(l2)
        b[i]=np.cos(b1[i])*np.sin(l1[i])*np.cos(b2)*np.sin(l2)
        c[i]=np.sin(b1[i])*np.sin(b2)
    return a+b+c

a=386867/c
chisq=np.zeros(100)
lon=np.linspace(250,275,num=chisq.size)-360

coos=np.zeros((100,4005))
for i in range(100):
    coos[i]=costheta(gal_lon,gal_lat,lon[i],gal_lat[2157])

for i in range(chisq.size):
    k_flag = Temperature - 2.727755*(1+a*coos[i])
    che=(k_flag/sigma)**2
    dhe=np.sum(che)
    chisq[i]=dhe

plt.plot(lon+360,chisq)
plt.show()
#print(costheta(gal_lon,gal_lat,lon[20],gal_lat[2157]).size)
#print(Temperature.size)'''