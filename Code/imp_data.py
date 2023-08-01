from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import h,c,k
from scipy.optimize import curve_fit

data = fits.open('FIRAS_DESTRIPED_SKY_SPECTRA_LOWF.FITS') 
destriped_data=data[1].data



dsig = fits.open('FIRAS_C_VECTOR_LOWF.FITS')  
x=dsig[1].data
sig=x['C_VECTOR']
sig=sig[0]


def Intensity(freq,T):
    
    e=np.exp(h*freq/(k*T))
    return (2*h*freq**3)/(c**2*(e-1))*1e20  # 1e20 used to convert the units
    
'''  h = planck constant
    k = boltzmann constant
    c = speed of light in vacuum
    T = temperature of blackbody
    wave_num = wave number of the radiation (1/wavelength)'''



def get_Temperature(frequency,input): # function to get best fit temperatures and uncertainties
    
    Pixel_data=dict()
    Pixel_data['Temperature']=np.zeros(4005)
    Pixel_data['Uncertainty']=np.zeros(4005)
    
    for i in range(len(input)):
    
        Intensity_observed=input[i]
        Intensity_observed=Intensity_observed[0:43:]
        sigma=sig[0:43:]
        T0=2
        popt,pcov=curve_fit(Intensity,frequency,Intensity_observed,sigma=sigma,p0=[T0])
        
        Temperature_fit=popt[0]
        Uncertainty_fit=np.sqrt(np.diag(pcov))
        Pixel_data['Temperature'][i] = Temperature_fit
        Pixel_data['Uncertainty'][i] = Uncertainty_fit
    
    return Pixel_data

# 1st frequency is 68.020812 Ghz
freq_0=68.020812*1e9
freq_interval=13.604162*1e9
#wave number is freq/c. there are 43 total values measured with this interval

wave_number=[]
for i in range(43):
    freq_flag=freq_0+i*freq_interval
    wave_number.append(freq_flag)
wave_number=np.array(wave_number)
frequency=wave_number

def root_mean_square(input): # function to find rms of the data
    
    input=np.array(input)
    squared_input=input**2
    mean=np.mean(squared_input)

    return np.sqrt(mean)

final_data_control = [i*0 for i in range(0,6067)]

for i in range(len(destriped_data['SPECTRUM'])):
    final_data_control[i] = destriped_data['SPECTRUM'][i][:43:] + final_data_control[i]

latitude = destriped_data['GAL_LAT']
longitude = destriped_data['GAL_LON']
Intensity_observed = final_data_control
Intensity_observed_control = destriped_data['SPECTRUM']

i=[]
accepted_spectrum=[]
accepted_spectrum_control =[]
accepted_latitude=[]
accepted_longitude=[]


for i in range(0,len(latitude)):
    
    if latitude[i] < 20:
    
        if latitude[i] > -20:
            continue
    
        else:
            accepted_spectrum.append(Intensity_observed[i])
            accepted_spectrum_control.append(Intensity_observed_control[i])
            accepted_latitude.append(latitude[i])
            accepted_longitude.append(longitude[i])
    
    if latitude[i]> 20:
        accepted_spectrum.append(Intensity_observed[i])
        accepted_spectrum_control.append(Intensity_observed_control[i])
        accepted_latitude.append(latitude[i])
        accepted_longitude.append(longitude[i])

spectrum_cut=np.array(accepted_spectrum)
spectrum_cut_control = np.array(accepted_spectrum_control)
spectrum_cut.shape
spectrum_cut_control.shape

'''just for reference. remove the hashtag to observe the respective arrays'''
#print(spectrum_cut)
#print(spectrum_cut_control)

Pixel_data = get_Temperature(frequency,spectrum_cut_control)


avg_temperature = np.mean(Pixel_data['Temperature'])
avg_uncertainty = np.mean(Pixel_data['Uncertainty'])  
one_sigma = np.std(Pixel_data['Uncertainty'])/np.sqrt(Pixel_data['Temperature'].size)
root_mean_square_temperature = root_mean_square(Pixel_data['Temperature'])
standard_deviation_temperature = np.std(Pixel_data['Temperature'])

print('T in terms of arithmetic means(Averages) = {:.6f} +- {:.6f} K'.format(avg_temperature , avg_uncertainty))
print('T in terms of arithmetic means(uncertainty as from book) = {:.6f} +- {:.6f} K'.format(avg_temperature , one_sigma))
print('T in terms of root mean square values = {:.6f} +- {:.6f} K'.format(root_mean_square_temperature , standard_deviation_temperature))