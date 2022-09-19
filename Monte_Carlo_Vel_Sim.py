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

LEN = 1000

All_Vel = open(f'/Path/to/your/directory/Wave_Vel_Table.txt') #Open the file

All_Vel = np.recfromtxt(All_Vel, names=['Wave', 'Wave_E', 'Vel', 'Vel_Err'])

Wavelength = All_Vel.Wave
Wavelength_Error = All_Vel.Wave_E
Velocity = All_Vel.Vel
Velocity.sort()
Velocity_Error = All_Vel.Vel_Err

Vel_Avg = np.mean(Velocity)
Vel_Err_Avg = np.mean(Velocity_Error)

Vel_Std = np.std(Velocity)
Vel_Err_Std = np.std(Velocity_Error)

def gaussian(x, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (np.exp(-(x-cen)**2 / (2*wid**2)))
Average_large_range = []
vel_large_range = []
Delta_Large = []
for i in range(LEN):
    y = np.random.randint(low=min(Velocity), high = max(Velocity), size=167)

    AVG = np.mean(y)
    SIG = Vel_Std #np.std(y) #

    y.sort()

    GAUS = gaussian(y, AVG, SIG)
    plt.plot(y/1E3, GAUS, '-o', lw=2, color='red')

    delta = y - Velocity
    Delta_Large.extend(delta)
    vel_large_range.extend(y)
    Average_large_range.append(AVG)

Average_annom_range = []
vel_annom_range = []
Delta_annom = []
for i in range(LEN):
    y = np.random.randint(low=min(Velocity), high = Velocity[165], size=167)

    AVG = np.mean(y)
    SIG = Vel_Std #np.std(y) #

    y.sort()

    GAUS = gaussian(y, AVG, SIG)
    plt.plot(y/1E3, GAUS, '-o', lw=2, color='blue')

    delta = y - Velocity
    Delta_annom.extend(delta)
    vel_annom_range.extend(y)
    Average_annom_range.append(AVG)

vel_STD_range = []
Average_STD_range = []
Delta_STD = []

for i in range(LEN):
    # y = np.random.randint(low=-2000E3, high = 2000E3, size=167)
    y = np.random.randint(low=(Vel_Avg- 3*Vel_Std), high = (Vel_Avg + 3*Vel_Std), size=167)
    AVG = np.mean(y)
    SIG = Vel_Std #np.std(y) #

    y.sort()

    GAUS = gaussian(y, AVG, SIG)
    plt.plot(y/1E3, GAUS, '-o', lw=2, color='magenta')

    vel_STD_range.extend(y)
    Average_STD_range.append(AVG)
    delta = y - Velocity
    Delta_STD.extend(delta)

Gaus_Vel = gaussian(Velocity, cen = Vel_Avg, wid=Vel_Std)
plt.plot(Velocity/1E3, Gaus_Vel, '-o', color='black')

plt.plot([], [], '-o', lw=3, markersize=10, color='red', label = 'Full Velocity Range')
plt.plot([], [], '-o', lw=3, markersize=10, color='blue', label = 'Removing Largest Velocity')
plt.plot([], [], '-o', lw=3, markersize=10, color='magenta', label = r'$3 \sigma$ Velocity Range')
plt.plot([], [], '-o', lw=3, markersize=10, color='black', label = 'Observed Data')

plt.xlabel(r'Velocity (km s$^{-1}$)', fontsize = 20)
plt.ylabel(r'Prob. Density', fontsize = 25)


plt.xlabel(r'Velocity (km s$^{-1}$)', fontsize = 20)
plt.ylabel(r'Simulation Prob. Density', fontsize = 25)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.ylim(-0.02, 1.02)
plt.xlim(-2000, 4000)
plt.legend(loc='upper right', ncol=1, fontsize=15)
plt.show()

plt.hist(np.array(Average_large_range)/1E3, bins=25, range=None, color='red')
plt.hist(np.array(Average_STD_range)/1E3, bins=25, range=None, color='magenta')
plt.hist(np.array(Average_annom_range)/1E3, bins=25, range=None, color='blue')
plt.vlines(Vel_Avg/1E3, 0, 40, linestyles='solid', lw=8, color='cyan')

plt.plot([], [], '-', lw=10, color='red', label = 'Full Velocity Range')
plt.plot([], [], '-', lw=10, color='blue', label = r'Removing Largest Velocity')
plt.plot([], [], '-', lw=10, color='magenta', label = r'$3 \sigma$ Velocity Range')
plt.plot([], [], '-', lw=10, color='cyan', label = 'Observed Data Average')

plt.legend(loc='best', fontsize=12)
plt.xlabel(r'Average Velocity (km s$^{-1}$)', fontsize = 20)
plt.ylabel('N', fontsize = 25)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.show()
