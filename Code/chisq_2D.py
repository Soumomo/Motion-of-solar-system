import matplotlib.pyplot as plt
from numpy import *
import numpy as np
import pandas as pd
from scipy.constants import c
# data input
gal_lon,gal_lat,Temperature,cos_theta,sigma=np.loadtxt('/home/soumadip/Documents/Motion-of-solar-system/Code/final-data.csv',delimiter=',',unpack=True)
y = Temperature 
x = 2.727755*cos_theta/c
yerr= sigma
'''
x=array([0.1,
 0.6,
 1.1,
 1.6,
 2.1,
 2.6,
 3.1,
 3.6,
 4.1,
 4.6,
 5.1,
 \
5.6,
 6.1,
 6.6,
 7.1,
 7.6,
 8.1,
 8.6,
 9.1,
 9.6])
y=array([34.1329,
 98.7892,
 121.0725,
 180.3328,
 236.3683,
 \
260.5684,
 320.9553,
 380.3028,
 407.3759,
 453.7503,
 506.9685,
 \
576.9329,602.0845,
 699.0915,
 771.2271,
 796.6707,
 787.8436,
 \
877.0763,
 915.3649,
 1000.7312])
yerr=array ([5.8423,
 9.9393,
 11.0033,
 13.4288,
 15.3743,
 16.1421,
 \
17.9152,
 19.5014,
 20.1836,
 21.3014,
 22.516,
 24.0194,
 \
24.5374,
 26.4403,
 27.771,
 28.2254,
 28.0686,
 29.6155,
 30.255,
 \
31.6343] )
'''
# calculate sums needed to obtain chi-square
s_yy=sum (y**2/yerr**2)
s_xx=sum(x**2/yerr**2)
s_0=sum(1/yerr**2)
s_xy=sum( (y*x) /yerr**2)
s_y=sum(y/yerr**2)
s_x=sum(x/yerr**2)
# by completing the square, we rewrite chi-squared as
# sum((y_i - A x_i - B)*2/sigma_i*2
# = (A-A**)*2/sigma_A*2
# + (B-B**) *2/sigma_B*2
# + 2*rho* (A-A**) (B-B**) /sigma_A*Sigma_A
# + \chi*2_{min}
A_best = (s_0*s_xy - s_x*s_y)/(s_0*s_xx - s_x**2)
sigma_A = 1/sqrt(s_xx);
B_best = (s_y*s_xx - s_x*s_xy)/(s_0*s_xx - s_x**2)
sigma_B = 1/sqrt(s_0);
rho = s_x/sqrt(s_xx*s_0);
minchi2 = (s_0*s_xy**2 - 2*s_x*s_y*s_xy + s_y**2*s_xx)/(s_x**2 - \
s_0*s_xx) + s_yy
# create parameter grid
A_interval = 1.1* (sqrt (6.17*sigma_A**2/(1-rho**2)));
B_interval = 1.1* (sqrt (6.17*sigma_B**2/(1-rho**2)));

# create parameter grid
'''a = np.linspace(A_best-A_interval, A_best+A_interval)
b = np.linspace(B_best-B_interval, B_best+B_interval)'''
a=np.linspace(385*1e3,390*1e3)
b=np.linspace(2.72771,2.72779)
A,B = np.meshgrid(a,b)
# calculate chi-square over parameter grid
# chi2=(S1)+ (A**2)*(S2) + (B**2)*(S3) - 2*A*S4 - 2*B*S5 + 2*A*B*S6
chi2 = s_yy + (A**2)*s_xx + (B**2)*s_0 - 2*A*s_xy - 2*B*s_y + 2*A*B*s_x;
# plot data with errorbars
print(yerr[0])
'''
plt.figure (1)
plt.plot (x,A_best*x)
plt.errorbar (x,y, yerr, linestyle='None',fmt='.k')
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.grid(True)
plt.title("y vs x data with y-error bars")
'''
#plot chi-square in A-~b parameter plane with 68% and 95% contours
'''plt.figure (2)
levels= [minchi2,minchi2+2.3,minchi2+6]
Z=plt.contour(B,A,chi2,levels)
plt.clabel(Z,inline=1, fontsize=10)
plt.plot(B_best,A_best,'+')
plt.xlabel('T_cmbr (intercept)',fontsize=16)
plt.ylabel('v/c ',fontsize=16)
plt.title('Chi-square 68% and 95% contours in A-B plane')
plt.show()'''