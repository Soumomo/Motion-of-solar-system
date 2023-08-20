# Requirements:

Python 3+, Essential packages: (`Jupyter`, `numpy`, `matplotlib`, `astropy`, `scipy`, `scienceplots`)

# Setup:

1. Clone the repository from https://github.com/Soumomo/Motion-of-solar-system.
    Go to `Code` --> copy the https url --> terminal( `git clone <link here>`)
2. The file of interest is `main.ipynb` inside the `Code` sub-folder
# Procedure:

1.  Import datasets from the COBE-FIRAS database (https://lambda.gsfc.nasa.gov/product/cobe/firas_prod_table.html).
	We will be needing the following `FITS` files:
	* Destriped Sky Spectrum (Low Frequency, Low Spectral Resolution, 60-630 GHz)
	* Dust Spectrum Map (Low frequency, 60-630 GHz)
	For convenience, these files are stored in the `Datasets` sub-folder
2. These datasets contain the 'Spectrum' (Specific Intensity of the part of the sky), Galactic Co-ordinates of the part and pixel count. From the header, we find the range of frequencies.
3. Using `scipy.optimize.curvefit` , the specific intensities ($I_v$) from the `destriped_data` are fitted to the Planck Distribution function.
4. The temperature and uncertainty values obtained are averaged getting us an initial $T_{CMBR}$ 
5. Plot the temperatures using an `aitoff` equal area projection. 
6. The high contamination through Cosmic dust needs to be removed. Subtract the `SPECTRUM` of cosmic dust dataset from the original destriped data.
7. Find the average temperature again and plot the data to see the difference. 
8. Another source of contamination is the galactic emissions from our Milky Way, the spectrum from $b \le |20^{\circ}|$ (galactic latitude) is cut from the analysis.
9. A good practice in data analysis is removing every point more than $5\sigma$ (standard deviation) from the average temperature value.
10. Calculate $\cos \theta$ using galactic coordinates provided the vector equations in the manual.
11. Using $\chi^2$ method, fit the $\sigma$ corrected data and the $\cos \theta$ components onto the Doppler effect equation to find velocity.
12. Plot a contour showing the minimising of $\chi^2$. This reveals our final $T_{CMBR}$ and speed (v) vslue.
13. Repeat the method but this time varying $\cos \theta$ as function of the coordinates, this gets us the best-fit direction of velocity. 