import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model
import math
import pandas as pd
import glob
from matplotlib.pyplot import cm
from matplotlib.cm import get_cmap

#Defining our simple Gaussian model
def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (np.sqrt(2*np.pi) * wid)) * np.exp(-(x-cen)**2 / (2*wid**2))


# NGC1365, MRK3, NGC4507, NGC7582, NGC5506, NGC424, NGC5643, CIRCINUS, NGC1068, NGC4151
AGN = input('Which AGN are you looking at? ')

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

c = ['red', 'blue', 'green', 'magenta', 'purple'] #colors for the data points, in order of observation year

for YEAR, colors in zip(year, c):
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

    plt.errorbar(cen, velocity/1E3, xerr=cen_err, yerr=velocity_err/1E3, color=colors, fmt='o', markersize=10, label=YEAR)

plt.xlabel(r'Wavelength ($\AA$)', fontsize=20)
plt.ylabel(r'Velocity (km s$^{-1}$)', fontsize = 25)
plt.title(AGN+': Velocity vs Wavelength', fontsize=30, loc='center')
plt.xticks(np.arange(10, 35, 2), fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(10, 35)
plt.legend(loc='best', fontsize=18)
plt.show()
