import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model
import math
import pandas as pd
import glob
plt.rcParams['figure.figsize'] = [10, 8]

#Defining our simple Gaussian model
def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (np.sqrt(2*np.pi) * wid)) * np.exp(-(x-cen)**2 / (2*wid**2))

#Details for the model and LMFIT package can be found here: https://lmfit.github.io/lmfit-py/model.html

# NGC1365, MRK3, NGC4507, NGC7582, NGC5506, NGC424, NGC5643, CIRCINUS, NGC1068, NGC4151
AGN = input('Which AGN are you looking at? ')

#2000, 2001, 2002 ... 2015
YEAR = input('Which Year are you looking at? ')

Spec = open(f'/Path/to/your/directory/{AGN}/{YEAR}/{YEAR}.dat') #Open the file

Spec = np.recfromtxt(Spec, names=['Wave', 'Wave_E', 'Wave_e', 'Flux', 'Flux_E', 'Flux_e', 'Model', 'Back'])
#Read the file and set the names of the columns

#Once AGN and year are selected, code takes the AGN redshift (z), black hole mass (MBH) and flux scale limit (y) for the rest of the code.
if AGN == str('NGC1365'):
  z = 0.005457
  y = 3
  MBH = 2E6 #See Whewell+2016
elif AGN == str('MRK3'):
  z = 0.013509
  y = 4
  MBH = 4.47E8 #https://iopscience.iop.org/article/10.1086/342878/pdf
elif AGN == str('NGC4507'):
  z = 0.011801
  y = 3
  MBH = 2E7 #https://iopscience.iop.org/article/10.1088/0004-637X/692/1/856/pdf
elif AGN == str('NGC7582'):
  z = 0.005254
  y = 3
  MBH = 5.5E7 #https://arxiv.org/pdf/0807.2549.pdf
elif AGN == str('NGC5506'):
  z = 0.00589
  y = 5
  MBH = 1E7 #https://arxiv.org/pdf/1412.4541.pdf
elif AGN == str('NGC424'):
  z = 0.011840
  y = 5
  MBH = 6E7 #https://iopscience.iop.org/article/10.1088/0004-637X/794/2/111/pdf
elif AGN == str('NGC5643'):
  z = 0.003999
  y = 3
  MBH = 2.75E6 #https://www.aanda.org/articles/aa/pdf/2021/01/aa38256-20.pdf
elif AGN == str('CIRCINUS'):
  z = 0.001448
  y = 5
  MBH = 1.1E6 #https://arxiv.org/pdf/0807.2549.pdf
elif AGN == str('NGC4151'):
  z = 0.003262
  y = 38
  MBH = 3.59E7 #https://www.aanda.org/articles/aa/pdf/2021/01/aa38256-20.pdf

Z = 1+z
#From the table, choose the columns we want to use
X = Spec.Wave/Z  #Wavelength column
Y = Spec.Flux #Flux column
X_err = Spec.Wave_E #Wavelength errors column
Y_err = Spec.Flux_E #Flux errors column

#Plotting the Spectrum (with out errors)
plt.plot(X, Y) #Plots X axis against Y axis (wavelenght angainst flux)
plt.xlabel(r'Wavelength ($\AA$)', fontsize = 20) #Sets the x axis label (including units)
plt.ylabel(r'Flux (Counts/s/$m^2$/$\AA$)', fontsize = 20)#Sets the y axis label (incluing units)
plt.xlim(7, 37) #Sets the limits of the x axis between 7 and 28 A
plt.ylim(-1, y) #Sets the limits of the y axis between -1 and 80 Counts/s/m^2/A
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show() #Shows the plot

plt.figure()
plt.subplot(311)
plt.plot(X, Y)
plt.xlim(7,15)
plt.ylim(-0.5,y)
plt.subplot(312)
plt.plot(X, Y)
plt.xlim(15,28)
plt.ylim(-0.5,y)
plt.ylabel(r'Flux (Counts/s/$m^2$/$\AA$)', fontsize = 20)
plt.subplot(313)
plt.plot(X, Y)
plt.xlim(28,37)
plt.ylim(-0.5,y)
plt.xlabel(r'Wavelength ($\AA$)', fontsize = 20)
plt.show()

#########

#This section defines the wavelength range the emission line you want to measure is in.

X = Spec.Wave/Z
Y = Spec.Flux

#Set the x limits:
x_low = float(input('Lower x-limit '))
x_up = float(input('Upper x-limit '))
#For the full spectrum, set x_low = 7 and x_up = 38

xdat = []
ydat = []
T = list(zip(X, Y))

for i in range(len(T)):
	if T[i][0] > x_low and T[i][0] <= x_up:
		xdat.append(T[i][0])
		ydat.append(T[i][1])
X = xdat
Y = ydat


plt.plot(X, Y, '-')
plt.xlabel(r'Wavelength ($\AA$)', fontsize=18) #Sets the x axis label (including units)
plt.ylabel(r'Flux (Counts/s/$m^2$/$\AA$)', fontsize = 18) #Sets the y axis label (incluing units)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.xlim(x_low, x_up) #Sets the limits of the x axis between 7 and 28 A
plt.ylim(-1, y) #Sets the limits of the y axis between -1 and 40 Counts/s/m^2/A
plt.show()

#Here you input intial parameter values for the model.

CEN = float(input('What is the wavelength of the line? (%.2f < cen < %.2f):' % (x_low, x_up)))
AMP = float(input('What is the amplitude of the line? (0 < amp < 10):' ))
WID = float(input('What is the width of the line? (0.001 < wid < 0.5):' ))

#Print your selected parameter values
print(AMP, CEN, WID)

#Take your Gaussian (defined above) and set it to a model
gmodel = Model(gaussian)
#The Gaussian model fits the data using the intitial parameter values chosen
result1 = gmodel.fit(Y, x=X, amp=AMP, cen=CEN, wid=WID)

#Plot the model to the data from your initial values
#Was the initial parameter estimate good enough?
#If the initial parameters are not very good, then this may bias the fitting.
#Therefore, it is always good to re-input better parameter values to make sure the fit is correct

plt.figure()
plt.plot(X, Y,  lw=3.5, color='black', label='Data')
plt.plot(X, result1.init_fit, lw=3, color='red', label="Intial parameters")
plt.plot(X, result1.best_fit, lw=3, color='blue', label="Fitted parameters")
plt.xlabel(r'Wavelength ($\AA$)', fontsize=20) #Sets the x axis label (including units)
plt.ylabel(r'Flux Counts s$^{-1}$ 3m$^{-2}$ $\AA^{-1}$', fontsize = 25) #Sets the y axis label (incluing units)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(loc='best', fontsize=18)
plt.xlim(x_low, x_up) #Sets the limits of the x axis between 7 and 28 A
plt.ylim(-1, y) #Sets the limits of the y axis between -1 and 5 Counts/s/m^2/A
plt.show()


#This will print out the model parameter values after fitting the Gaussian to the data.
print(result1.fit_report())
#The main information here that we want are the "[Variables]": amp, cen and wid values along with their errors
print()
print('-------------------------------')
print('Parameter    Value       Stderr')
for name, param in result1.params.items():
    print('{:7s} {:11.5f} ± {:11.5f}'.format(name, param.value, param.stderr))
#Here we have printed the three parameters and their errors (±) in a clearer way.


#This part of the code saves the parameter values and errors for the velocity and distance calculations below.
cen_val = result1.params['cen'].value
amp_val = result1.params['amp'].value
wid_val = result1.params['wid'].value

cen_err = result1.params['cen'].stderr
amp_err = result1.params['amp'].stderr
wid_err = result1.params['wid'].stderr


######


#Measuring the Velocity

def Speed(wave_obs, wave_rest, c):
    v = ((wave_obs/wave_rest) - 1)*c
    return(v)

c = 3E8 #Speed of light

Wave_Rest = float(input('What is the rest wavelength of the fitted line? '))

v_out = Speed(cen_val, Wave_Rest, c)
#print('vout =', v_out, 'm/s') #This prints out the velocity of the emission line, relative to the rest frame

v = Speed(cen_val + cen_err, Wave_Rest, c)

v_out_err = np.sqrt((np.sqrt(v_out**2) - np.sqrt(v**2))**2)

#The error is the difference between the observed velocity and the velocity uncertainty value
print(' ')

#Print out the final line: Velocity ± Error
print('-----------------')
print('v_out =', v_out, '±', v_out_err/2 , 'm/s')


#Estimating the Distance
def Dist(v, G, M):
    R = (2 * G * M) / (v**2)
    return(R)
G = 6.67E-11 #Gravitational constant
M_sol = 1.9891E30 #Mass of sun in kg
M = 6E7 * M_sol #black hole mass 4E7
v_out = v_out #outflow velocity

R = Dist(v_out, G, M)
print(' ')

############
### Error on the distance
vel = (np.sqrt(v_out**2) + np.sqrt(v_out_err**2))

r = Dist(vel, G, M) #Calculate the distance using the velocity + error in velocity (distance uncertainty)

R_err = R - r #The error in the distance is equal to the difference between the distance and the distance uncertainty
print(vel)
print(R)
print(r)

#Print out the final line: Distance + Error
print('------------')
print('R =', R, '±', R_err, 'm')
