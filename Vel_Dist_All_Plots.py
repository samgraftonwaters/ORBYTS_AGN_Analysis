import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model
import math
import pandas as pd
import glob
from matplotlib.pyplot import cm
from matplotlib.cm import get_cmap
import scipy.stats as ss

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
Vel_Err_Std = np.std(np.sqrt(Velocity_Error))

Dist_Avg = np.mean(Distance)
Dist_Err_Avg = np.mean(Distance_Error)
Dist_Std = np.std(Distance)
Dist_Err_Std = np.std(Distance_Error)

agn = ['MRK3', 'NGC1365', 'NGC424', 'NGC5643', 'CIRCINUS', 'NGC4151', 'NGC4507', 'NGC5506', 'NGC7582']
c = ['red', 'blue', 'green', 'magenta', 'purple', 'cyan', 'orange', 'black', 'brown', 'pink']

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
        Spec = open(f'/Path/to/your/directory/{AGN}/{YEAR}/{AGN}_{YEAR}.dat') #Open the file

        Spec = np.recfromtxt(Spec, names=['Wave', 'Wave_E', 'Wave_e', 'Flux', 'Flux_E', 'Flux_e', 'Model', 'Back'])

        X = Spec.Wave
        Y = Spec.Flux

        NGCspreadsheetfile=glob.glob(f'/Path/to/your/directory/{AGN}/*.xls*')
        df=pd.ExcelFile(NGCspreadsheetfile[0])

        NGCdict={}
        sheetlist=[]
        for sheet in df.sheet_names:
              NGCdict[sheet]=df.parse(sheet, skiprows=3)
              sheetlist.append(sheet)
        NGCdict[YEAR]
        df=NGCdict[YEAR]

        for i in range(len(df[df.columns[1]])):

            cen=df[df.columns[1]]*Z #Observed wavelength (A)
            cen_err=df[df.columns[2]] #Error on the Observed wavelength

            velocity=df[df.columns[9]] #Measured velocity (m/s)
            velocity_err=df[df.columns[10]] #Error on the measured velocity (m/s)

            distance=df[df.columns[11]] #Distance from the central black hole (m)
            distance_err=df[df.columns[12]]

            plt.errorbar(cen, velocity/1E3, xerr=cen_err, yerr=velocity_err/1E3, color=colors, fmt='o', markersize=10)
    plt.errorbar([], [], xerr=1, yerr=1, fmt='o', markersize=10, color=colors, label=AGN)
plt.fill_between([7, 37], [Vel_Avg/1E3 - 1*Vel_Std/1E3],    [Vel_Avg/1E3 + 1*Vel_Std/1E3], facecolor="blue",  color='blue', alpha=0.6)
plt.fill_between([7, 37], [Vel_Avg/1E3 - 2*Vel_Std/1E3],    [Vel_Avg/1E3 + 2*Vel_Std/1E3], facecolor="blue", color='blue', alpha=0.4)
plt.fill_between([7, 37], [Vel_Avg/1E3 - 3*Vel_Std/1E3],    [Vel_Avg/1E3 +3*Vel_Std/1E3], facecolor="blue", color='blue', alpha=0.2)
plt.hlines(Vel_Avg/1E3, 7, 37, linestyles='dashed', lw=5, color='red')
#plt.fill_between([7, 37], [Vel_Avg/1E3 - Vel_Err_Avg/1E3],    [Vel_Avg/1E3 + Vel_Err_Avg/1E3], facecolor="red", color='red', alpha=0.6)
plt.xlim(10, 35)
plt.xticks(np.arange(10, 35, 2), fontsize=18)
plt.yticks(fontsize=18)
plt.xlabel(r'Wavelength ($\AA$)', fontsize=20)
plt.ylabel(r'Velocity (km s$^{-1}$)', fontsize = 25)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
#plt.ylim(-6000, 6000)
plt.legend(loc='upper right', ncol=3, fontsize=15)
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
        Spec = open(f'/Path/to/your/directory/{AGN}/{YEAR}/{AGN}_{YEAR}.dat') #Open the file

        Spec = np.recfromtxt(Spec, names=['Wave', 'Wave_E', 'Wave_e', 'Flux', 'Flux_E', 'Flux_e', 'Model', 'Back'])

        X = Spec.Wave
        Y = Spec.Flux

        NGCspreadsheetfile=glob.glob(f'/Path/to/your/directory/{AGN}/*.xls*')
        df=pd.ExcelFile(NGCspreadsheetfile[0])

        NGCdict={}
        sheetlist=[]
        for sheet in df.sheet_names:
              NGCdict[sheet]=df.parse(sheet, skiprows=3)
              sheetlist.append(sheet)
        NGCdict[YEAR]
        df=NGCdict[YEAR]

        for i in range(len(df[df.columns[1]])):

            cen=df[df.columns[1]]*Z #Observed wavelength (A)
            cen_err=df[df.columns[2]] #Error on the Observed wavelength

            distance=df[df.columns[11]] #Distance from the central black hole (m)
            distance = np.array(distance, dtype=float)
            distance_err=df[df.columns[12]]
            distance_err = np.array(distance_err, dtype=float)

            plt.errorbar(cen, distance, xerr=cen_err, yerr=distance_err, color=colors, fmt='o', markersize=10)
    plt.errorbar([], [], xerr=1, yerr=1, fmt='o', markersize=10, color=colors, label=AGN)
plt.yscale('log')
plt.xlabel(r'Wavelength ($\AA$)', fontsize=20)
plt.ylabel(r'Distance (m)', fontsize = 25)
plt.xlim(10, 35)
plt.xticks(np.arange(10, 35, 2), fontsize=18)
plt.yticks(fontsize=18)
plt.ylim(1E14, 6E23)
plt.legend(loc='upper left', ncol=3, fontsize=15)
plt.show()
