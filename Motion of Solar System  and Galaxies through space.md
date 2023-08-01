## 1.1 INTRODUCTION

#### What is CMB and how do we know it?

The CMB or the Cosmic Microwave Background is a collective entity constituting the very initial photons emitted with the onset of recombination era,The Recombination Epoch.Recombination epoch took place about 380,000 years after the Big-Bang . CMB constitutes the photon constituents which decombined from matter during the Recombination Epoch had started and flew apart in all directions. As the universe expanded, The energy of these emitted photons reduced, and they were shifted from the infrared spectrum being the dominant spectrum during the recombination epoch to the microwave spectrum. Overtime, tiny fluctuations on scales of micro kelvin, known as Anisotropies were revealed in the 'observed' CMB. The largest anisotropy found was a temperature change of around 0.008 K.

This is largely a result of the Earth/our solar system collectively moving with The Milky Way through space towards a series of galaxy clusters known as the Great Attractor. This creates a temperature gradient in the observed microwave background from one side to the other known as the Dipole Anisotropy. NASA's contribution to this was the Cosmic Background Explorer or the COBE satellite which had a precise magnifier to notice the differences in temperature in tiny pixels of the CMB. Data was collected by the COBE from 1989 up until 1996 where it mapped the large-scale anisotropies. 3 instruments were carried by COBE. DIRBE(diffused infrared experiment), DMR(Differential Microwave Radiometer), FIRAS(far-infrared absolute spectrophotometer), all these 3 constituted in the understanding of the CMB and THE LARGE DIPOLE ANOSOTROPY 

IN OUR WORK WE HAD CONSIDERED ONLY THE DATA OF THE FIRAS INSTRUMENT 

##### Temperature of the CMB -

The assumption on which our study stands is That the initiation of 'The Universe as we know it' happened with The Big Bang. This assumption suggests that the primeval fireball (The universe just before the recombination epoch) behaved like a black body which further becomes a postulate when we observe the intensity vs frequency graph of the pure CMB radiation. Hence we can use the *Planck distribution law* on the relic radiation which is spread all across the universe. when we do so we attain a best fit temperature of the CMB as 2.726 K +- 0.0016 k (presently accepted value).
This means that if a perfect black body in an isolated system emitted em waves similar in nature to the cmb radiation,it would have the temperature of 2.726 k. Though during the recombination era the temperature of CMB was ~3000 K which had decreased to the present value due to the universal expansion.

##### Finding velocity by studying anisotropies  - 

The spectrum data that we obtain from the sky is not purely CMB. We subdivide the spectrum data into 3 dominant components.

> COMPLETE SPECTRUM DATA = CMB SPECTRUM DATA + CMB DIPOLE SPECTRUM DATA + CONTAMINATION SPECTRUM DATA

1. **CMB Spectrum data** - spectrum of em-waves a stationary observes reads in an isolated system. stationary respect to the CMB frame.
2. **CMB dipole  spectrum data** - additional spectrum data a moving observer reads in an isolated system due to the doppler shift. moving with respect to the CMB frame.
3. **Contamination spectrum data** - additional spectrum data one observes in a non-isolated system in space due to presence of physical entities like cosmic dust.

* The 2nd and 3rd are the reasons for observed anisotropies.

* By a brief study of the 2nd spectrum, we can find out the velocity of the entity from which CMB is observed. for instance our Earth, which is the primary goal of this project.

-------------------------------------------------------------------

##### A CONCISE EXPLANATION OF THE PROCESS WE ADOPTED IN THE PROJECT - 

 -IN THIS PROJECT,WE HAVE OPERATED ON THE LOW FREQUENCY DATA OBTAINED VIA THE LEFT OUTPUT PORT OF COBE FIRAS IN THE SHORT SLOW SCAN MODE- 

1. We obtained the firas data from the [Lambda][https://lambda.gsfc.nasa.gov/] website. The primary data files required are -
   (i) FIRAS_DESTRIPED_SKY_SPECTRA_LOWF.FITS
   (ii) FIRAS_DUST_SPECTRUM_MAP_LOWF.FITS

2. The sky is divided into 6067 pixels, The data which we obtain in the above 2 files is the brightness/intensity observed of electromagnetic radiations of 43 different frequencies(frequency points) obtained about each pixel, the location of each pixel in terms of galactic latitudes and galactic longitudes.

3. The sky spectrum data constitutes all the 3 dominant components. To obtain a new dataset which only constitutes the Pure CMB component and a dipole component, we subtract the dust spectrum data from the sky spectrum data for each pixel. The operations described below are also applied on the (i) dataset to see the contrast between the dataset which contains dust spectrum(control setup) and the dataset from which dust is removed(experimental setup) 

4. Now to get rid of the large scale galactic anisotropy, we remove those datapoints from the dataset which provide us with the brightness/intensity of the galactic plane and locations surrounding the galactic plane. To get the most appropriate results we remove the region defined as $|b| \lt 20$ degrees where b stands for galactic latitude. 

5. On the dataset , we apply the planck distribution law and with the help of scipy libraries, obtain the best fit temperatures and best fit uncertainities in temperatures for each pixel.

6. We then take the root mean square value of all temperature points. The value obtained is a good approximation of the CMB temperature(root mean square temperature of the experimental setup)

7. We then produce the aitoff temperature map of the sky ,in terms of the pixels we are left with after galactic cutting. For the sake of interest, one can also obtain aitoff maps for other possible datasets by recalibrating the region which is removed.

8. We then subtract the good approximation CMB temperature so obtained from each temperature element of the best fit temperature data we had obtained, this dataset so obtained is the dipole dataset.The temperature map of this dataset is the map of the CMB dipole component 

9. We make a function to find the cosine of an arbitrary pixel with respect to the direction of the earth's motion.

10. We use the temperature-velocity relation as shown below to attain speed relative to temperature values of each pixel giving us a list of speeds.

11. We then take the mean of all these values which is an approximate value of speed. To attain the direction, we simply obtain the pixel components whose temperature value is the highest in the dipole spectrum dataset.

12. To obtain a better value of speed, we use the chi-square minimization method. plotting the chi-square values with respect to speeds.
















