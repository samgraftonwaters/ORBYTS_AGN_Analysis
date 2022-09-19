import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model
import math
import pandas as pd
import glob
from matplotlib.pyplot import cm
from matplotlib.cm import get_cmap
import scipy.stats as ss
from statsmodels.stats.weightstats import ztest as ztest

All_Vel = open(f'/Path/to/your/directory/Wave_Vel_Table.txt') #Open the file

All_Vel = np.recfromtxt(All_Vel, names=['Wave', 'Wave_E', 'Vel', 'Vel_Err'])

All_Dist = open(f'/Path/to/your/directory/Wave_Dist_Table.txt') #Open the file

All_Dist = np.recfromtxt(All_Dist, names=['Wave', 'Wave_E', 'Dist', 'Dist_Err'])

Wavelength = All_Vel.Wave
Wavelength_Error = All_Vel.Wave_E
Velocity = All_Vel.Vel
Velocity_Error = All_Vel.Vel_Err
Distance = All_Dist.Dist
Distance_Error = All_Dist.Dist_Err

Vel_Avg = np.mean(Velocity)
Vel_Err_Avg = np.mean(Velocity_Error)
Vel_Std = np.std(Velocity)
Vel_Err_Std = np.std(Velocity_Error)
print('mu', Vel_Avg/1000, Vel_Err_Avg/1000)
print('sig', Vel_Std/1000, Vel_Err_Std/1000)

Dist_Avg = np.mean(Distance)
Dist_Err_Avg = np.mean(Distance_Error)
Dist_Std = np.std(Distance)
Dist_Err_Std = np.std(Distance_Error)


def gaussian(x, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (np.exp(-(x-cen)**2 / (2*wid**2)))

Gaus_Vel = gaussian(Velocity, cen = Vel_Avg, wid=Vel_Std)
plt.plot(Velocity/1E3, Gaus_Vel, 'o', color='black')
plt.xlabel(r'Velocity (km s$^{-1}$)', fontsize = 20)
plt.ylabel(r'Prob. Density', fontsize = 25)
plt.fill_between([Vel_Avg/1E3 + 1*Vel_Std/1E3, Vel_Avg/1E3 - 1*Vel_Std/1E3], -0.02, 1.02, facecolor="blue", color='blue', alpha=0.6)
plt.fill_between([Vel_Avg/1E3 + 2*Vel_Std/1E3, Vel_Avg/1E3 - 2*Vel_Std/1E3], -0.02, 1.02, facecolor="blue", color='blue', alpha=0.4)
plt.fill_between([Vel_Avg/1E3 + 3*Vel_Std/1E3, Vel_Avg/1E3 - 3*Vel_Std/1E3], -0.02, 1.02, facecolor="blue", color='blue', alpha=0.2)
plt.vlines(Vel_Avg/1E3, -0.02, 1.02, linestyles='dashed', lw=5, color='red')
plt.ylim(-0.02, 1.02)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()

for AGN, colors in zip(agn, c):
    if AGN == str('NGC1365'):
      z = 0.005457
      y = 3
      year = ['2004', '2012', '2013']
    elif AGN == str('MRK3'):
      z = 0.013509
      y = 5
      year = ['2000', '2001', '2002', '2012', '2015']
    elif AGN == str('NGC4507'):
      z = 0.011801
      y = 3
      year = ['2001', '2010']
    elif AGN == str('NGC7582'):
      z = 0.005254
      y = 5
      year = ['2001', '2005', '2016']
    elif AGN == str('NGC5506'):
      z = 0.00589
      y = 5
      year = ['2004', '2008', '2009', '2015']
    elif AGN == str('NGC5643'):
      z = 0.003999
      y = 3
      year = ['2009']
    elif AGN == str('CIRCINUS'):
      z = 0.001448
      y = 5
      year = ['2001']
    elif AGN == str('NGC4151'):
      z = 0.003262
      y = 30
      year = ['2020']
    elif AGN == str('NGC424'):
      z = 0.011840
      y = 5
      year = ['2001', '2008']

    Z = 1+z

    for YEAR in year:

        NGCspreadsheetfile=glob.glob(f'/Path/to/your/directory/{AGN}/*.xls*')
        df=pd.ExcelFile(NGCspreadsheetfile[0])

        NGCdict={}
        sheetlist=[]
        for sheet in df.sheet_names:
            NGCdict[sheet]=df.parse(sheet, skiprows=3)
            sheetlist.append(sheet)
        NGCdict['ALL']
        df=NGCdict['ALL']

        for i in range(len(df[df.columns[1]])):

            velocity=df[df.columns[1]] #Measured velocity (m/s)
            velocity_err=df[df.columns[2]] #Error on the measured velocity (m/s)

            # Vel_Avg = np.mean(np.sqrt(velocity**2))
            Vel_Avg = np.mean(velocity)
            Vel_Err_Avg = np.mean(velocity_err)
            Vel_Std = np.std(np.sqrt(velocity**2))
            Vel_Err_Std = np.std(np.sqrt(velocity_err))

        Gaus_Vel = gaussian(velocity, cen = Vel_Avg, wid=Vel_Std)
    print(AGN, Vel_Avg/1000, Vel_Std/1000)
    plt.plot(velocity/1E3, Gaus_Vel, '-o', lw=2, color=colors)
    plt.plot([], [], 'o', markersize=10, color=colors, label=AGN)
    plt.vlines(Vel_Avg/1E3, -0.02, 1.02, linestyles='dashed', lw=2, color=colors)

plt.xlabel(r'Velocity (km s$^{-1}$)', fontsize = 20)
plt.ylabel(r'Prob. Density', fontsize = 25)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.ylim(-0.02, 1.02)
#plt.ylim(-6000, 6000)
plt.legend(loc='upper left', ncol=1, fontsize=15)
plt.show()
