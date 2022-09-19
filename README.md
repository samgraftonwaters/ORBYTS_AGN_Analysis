# ORBYTS_AGN_Analysis
Python scripts to analyse X-ray spectra of nine different active galactic nuclei (AGN) during the ORBYTS outreach with schools project. The aim is to determine the outflow velocities and distances of the outflowing wind plasma regions, in addition to estimating the number of plasma regions. 

This code can be used to study the soft X-rays spectra of any AGN, provided the correct data is obtained. The data used in this work was reflection grating spectrometer data collected by XMM-Newton. 

**To cite these codes, use DOI: 10.5281/zenodo.5116838 @ https://zenodo.org/record/5116838**

A description of each script is detailed below, under the name of the file.

**AGN_Analysis(Main).py**

This is the main script that contains the code to read the data and fit the emission lines with a Gaussian model in the RGS spectra of each AGN, where the amplitude, line centre and width are measured. From here, the line shift can be calculated, allowing for the velocity and distance of each line to be calculated. This means the number of plasma clouds in the outflowing wind can be determined. See **S. Grafton-Waters et al 2021 Res. Notes AAS 5 172** (https://doi.org/10.3847/2515-5172/ac1689) for further details of how this model was used to study NGC 4151. This is the code you need to model your AGN spectrum.

**Spectrum_Plots.py**; **Velocity Plots.py**; **Distance Plots.py**

These Python scripts can be used to read data from an Excel spread sheet to plot the spectra and fitted Gaussian models to the data (**Spectrum_Plots**), and the velocities or distances as a function of wavelength (**Velocity Plots** and **Distance Plots**, respectively).

**Vel_Dist_All_Plots.py**

This script plots the velocities and distances, as a function of wavelength, of all the AGN in the analysis, in order to compare the results all together.

**Velocity_Distributions.py**

This script plots the velocity distribution for all AGN together, and for each AGN separately (but on the same figure). Using a modified version of the Gaussian from **AGN_Analysis(Main).py**, this script means you can measure the mean and standard deviation of the velocity distributions for the AGN.

**Monte_Carlo_Vel_Sim.py**

This script uses fake data to create velocity distributions based on random velocities, during 1000 iterations. The number of data points is the same as the total number of emission lines fitted to all AGN (in this case 167), where each data point is a random velocity chosen within a certain velocity range: (i) the full velocity range from the real data $v_{range} = -1547$ to $3421$ km s$^{-1}$; or (ii) the velocity range after removing the highest velocity value, $v_{range} = -1547$ to $2471$ km s$^{-1}$; or (iii) the velocity range between $± 3 \sigma$, $v_{range} = -1724$ to $1842$ km s^${-1}$. Also plotted is the velocity distribution for the observed data (from all AGN; e.g. from **Velocity_Distributions.py**).

This script also creates histograms for the average velocities of each velocity distribution (three, one for each velocity range), and compares the results to the average velocity from the observed data (of all AGN). 

**Analysis_Table.xls**

Table template to place your results. This table is then read by all scripts (except for **AGN_Analysis(Main).py**) to plot data. Change name accordingly - for each AGN, and the spreadsheet tabs should be labelled as the **YEAR** of the observation. Also shown in this file are the rest wavelengths and ions of the 16 strongest emission lines in the spectrum of NGC 4151 that can be modelled in the spectra of each AGN. The columns (in Python notation) are:

[1] Observed wavelength value; [2] Observed wavelength error;
[3] Line amplitude value; [4] Line amplitude error;
[5] Line width value (wavelength units); [6] Line width error (wavelength units);
[7] Rest wavelength (from SPEX line list: ); [8] Ion name;
[9] Line velocity value; [10] Line velocity error;
[11] Distance value; [12] Distance error.
