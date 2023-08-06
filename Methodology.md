
The data used in the analysis is from the `COBE-FIRAS`(Cosmic Background Explorer - Far Infrared Absolute Spectrometer) instrument. This data is of the form:

* **Galactic Coordinates of the part of sky** : The sky here is divided into $6144$ pixels of which $6067$ (~$95$%) pixels are retrieved with sufficient measurements.

* **The Intensity of radiation received at that pixel** : There are $182$ values of Intensities measured in MJy/sr, across a set of frequencies. This analysis only considers data in the low-frequency band ($60-630$ GHz)

It is assumed that the Cosmic Microwave Background is a blackbody radiating EM waves from all directions, the relation of intensity of these radiations to its frequency was given by Max Planck. The data is fitted to the Planck Distribution spectrum:
$$I(v,T) = \frac{2hv^3}{c^2(e^{\frac{hv}{kT}}-1)}$$
There are 43 non-zero intensity points for each pixel. The detector's initial captured frequency is $68.020812$ GHz with measuring interval of 13.604162$ GHz, putting the whole spectrum in the microwave region.

Linear regression is used to fit the data, this leads to the acquiring of the Blackbody temperature($T_{obs}$) corresponding to that patch of the sky. 
$$\chi^2 = \sum^N_i \frac{(I_{obs}-I_{theo})^2}{\sigma_i^2}$$
Then, a temperature map is plotted to review our data and check for anisotropies. It is inferred that the Milky Way galaxy and the Cosmic Dust sorrounding it have caused abnormalities in the temperature values. This leads to our next step of removing the unnecessary Cosmic Dust spectra from our original data. 

The FIRAS website has a corresponding dataset of the Cosmic Dust measured in the low-frequency range. These values are directly subtracted from our previous intensity values to give us uncontaminated CMBR emissions. Upon running the regression again and finding the temperatures and plotting, we start seeing the dipole anisotropy of the CMB. To spot it clearly, it is important to remove the galactic emissions. This is done by cutting the data across the galactic equator ($|b|\le 20$)

Along with cutting the spectrum data, it is also apparent to cut the respective longitude/latitudes for correct plotting of data. We repeat the regression and plot the temperature map. This time, a clear and comprehensive temperature map is generated with the dipole visible. Taking the average of the temperatures: $T_{CMBR} =  2.727780 +- 0.000196$ K . Further down the analysis, we achieved an even better approximation.

# Calculating Velocity of our Solar System

We say that the solar system moves at some speed relative to the Cosmic Microwave Background. As per what is explained above , this motion of Earth causes us to read relatively more energetic EM waves of any source observed in the direction of our motion and relatively less energetic EM waves of any source observed in the direction opposite to our motion. This principle applies for the CMB radiation too. The apparent background temperature of an observer moving with a velocity v with respect to the background radiation is of the form{reference : 1968 paper}:
$$
\begin{aligned}

T_{obs}&= T_{cmbr}\frac{\sqrt{1-\frac{v^2}{c^2}}}{1-\frac{v}{c}cos\theta} \\
\\
&\approx T_{cmbr}(1+\frac{v}{c}cos\theta)

\end{aligned}
$$
First, we need to find the values $cos\theta$ from every pixel of the sky to the point of the highest temperature. 

## Finding the cosine of angles between the pixels:

For example, we have 2 points indicating 2 pixels in the sky:
Point A$(l_1,b_1)$ and B$(l_2,b_2)$

The normal vectors pointing outward from the celestial sphere from these 2 points are of the form:
$n_A=\cos b_1 . \cos l_1\hat{x} + \cos b_1  . \sin l_1\hat{y} + \sin b_1\hat{z}$
$n_B=\cos b_2 . \cos l_2\hat{x} + \cos b_2 . \sin l_2\hat{y} + \sin b_2 \hat{z}$

The cosine of the angle $\theta$ between these vectors can be easily calculated from the following vector definition of cosine

$$\begin{aligned}
\cos \theta & = \frac{n_A . n_B}{|n_A|.|n_B|} \\
\\
&= \frac{\cos b_1 . \cos l_1 . \cos b_2 \cos l_2  + \cos b_1  . \sin l_1 . \cos b_2 . \sin l_2 + \sin b_1 \sin b_2}{1}
\end{aligned}
$$
Thus, by using the hottest point of the dipole as initial point, cosines of each angle is determined.


## Chi-Squared($\chi^2$) analysis

To find the velocity and it's tolerance, we turn back to a well-known data analysis technique. This is used to calculate best-fit parameters(A and B) using linear regression

$$\chi^2 = \sum{\frac{(y_i-Ax_i-B)^2}{\sigma^2_i}}$$
Here, $y$ is the Temperatures obtained from the previous set of analysis, $x$ is the expression $T_{CMBR}. \cos \theta/c$, having the average temperature of the sky and the cosines we calculated in the former step. $A$ & $B$ are the velocity and $T_{CMBR}$ respectively.
Opening the summation into the terms of the equation, we get:

$$\chi^2 = \sum{\frac{y^2_i}{\sigma^2_i}} - 2A \sum{\frac{y_ix_i}{\sigma^2_i}} - 2B\sum{\frac{y_i}{\sigma^2_i}} - 2AB \sum{\frac{x_i}{\sigma^2_i}} + A^2 \sum{\frac{x^2_i}{\sigma^2_i}} + B^2 \sum{\frac{1}{\sigma^2_i}}$$

To save space, we redefine those sums and rewrite as,
$$\chi^2 = [S_{yy}] -2A[S_{xy}] -2B[Sy] -2AB[S_x] +A^2[S_{xx}] +B^2[S_0] $$
By completing the square and exchanging the six parameters(the S's) for six new parameters $A^*,\sigma_A,B^*,\sigma_B,\rho$ and $\chi^2_{min}$:

$$\chi^2 = \frac{(A-A^*)^2}{\sigma_A^2} + \frac{(B-B^*)^2}{\sigma_B^2} + 2\rho\frac{(A-A^*)(B-B^*)}{\sigma_A \sigma_A} + \chi^2_{min}$$
Of course, you recognize this as the equation of an elliptic paraboloid! This means that in place of a parabola along the A axis we now have a (bowl shaped) three-dimensional paraboloid hovering above the A-B plane. The best fit parameters $A^*$ and $B^*$ are located at the minimum point of the paraboloid, where $\chi^2=\chi^2_{min}$.
Solving both euqtions in terms of the new parameters, we get:
$$A^* = \frac{S_0 . S_{xy} - S_x . S_y}{S_0 . S_{xx} - S^2_x} $$
$$\sigma_A = \frac{1}{\sqrt{S_{xx}}} $$
$$B^* = \frac{S_y . S_{xx} - S_x . S_{xy}}{S_0 . S_{xx} - S^2_x} $$
$$\sigma_B = \frac{1}{\sqrt{S_{0}}} $$
$$\rho = \frac{S_x}{\sqrt{S_{xx} . S_0}} $$
$$\chi^2_{min} = \frac{S_0 . S^2_{xy} - 2S_x.S_y . S_xy + S^2_y . S_{xx}}{S^2_x - S_0 . S_xx} +S_{yy} $$
Creating a suitable interval, a contour map is plotted to reveal the true values of the required parameters($v, T_{CMBR}$). The 68% and 95% confidence levels are derived from the $\chi^2_min + 2.3$ and $\chi^2_min + 6.17$ respectively.

![[Pasted image 20230731171028.png]]

From the calculations done, the value of velocity is found out to be $386.8660 \pm 0.3574$ km/s and $T_{CMBR}$ to be $2.727756 \pm 0.000003$ K (95% CL)

It is equally important to state the direction of the motion, so we turn back to $\chi^2$ analysis this time for only 1 parameter.  