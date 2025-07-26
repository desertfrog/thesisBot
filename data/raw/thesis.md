## **Measuring Fission Chain Dynamics Through Inter-event** **Timing of Correlated Particles**

by


Mateusz Monterial


A dissertation submitted in partial fulfillment
of the requirements for the degree of
Doctor of Philosophy
(Nuclear Science)
in the University of Michigan
2017


Doctoral Committee:


Professor Sara A. Pozzi, Chair

Professor Christine A. Aidala

Dr. Shaun Clarke

Dr. Peter Marleau, Sandia National Laboratories

Professor David K. Wehe


Mateusz Monterial


mateuszm@umich.edu


ORCID iD: 0000-0002-0739-305X


© Mateusz Monterial 2017


_Ku pami˛eci mojej zmarłej babci, która zawsze wiedziała, ˙ze b˛ed˛e_
_miał tytuł doktora._


ii


**ACKNOWLEDGMENTS**


First and foremost, I am thankful to my adviser Professor Sara Pozzi for giving me a

chance to attend the fine nuclear program at the University of Michigan, and subse
quently providing me with the running room to explore my research interests. My Sandia

mentor Peter Marleau has been indispensable for the work presented in this thesis, and

I thank him for putting up with me over all these years. The discussions I had with my

colleagues at Sandia and the University of Michigan have made me a better researcher

and contributed to this work in innumerable ways. Special mention goes out to Marc

Paff and Tony Shin, who had to review this thesis on short notice because of my procras
tination. My mother always believed that I could do this, and she started me on this path

long ago. Lastly, my lovely wife Alisha has been a constant pillar of support throughout

all my schooling, and I am forever grateful for her patience and generosity.

Below is the mandatory shout-out to the taxpayers.

This material is based upon work supported by the U.S. Department of Homeland Se
curity under Grant Award Number, 2012-DN-130-NF0001. The views and conclusions

contained in this document are those of the authors and should not be interpreted as rep
resenting the official policies, either expressed or implied, of the U.S. Department of

Homeland Security.

Sandia National Laboratories is a multimission laboratory managed and operated by Na
tional Technology and Engineering Solutions of Sandia, LLC., a wholly owned sub
sidiary of Honeywell International, Inc., for the U.S. Department of Energy’s National

Nuclear Security Administration under contract DE-NA-0003525. SAND Number:

SAND2017-10258 T.

This work was funded in-part by the Consortium for Verification Technology under

Department of Energy National Nuclear Security Administration award number DE
NA0002534.


iii


### **TABLE OF CONTENTS**

**Dedication** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **ii**


**Acknowledgments** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **iii**


**List of Figures** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **vii**


**List of Tables** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **xii**


**List of Appendices** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **xiii**


**List of Abbreviations** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **xiv**


**Abstract** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **xvi**


**Chapter**


**1 Introduction** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **1**


1.1 Brief History of the Fission Chain . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

1.3 Thesis Contribution and Overview . . . . . . . . . . . . . . . . . . . . . . . . . 4


**2 Fissile Material Properties and Detection Techniques** . . . . . . . . . . . . . . . . . . **7**


2.1 Definitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.1 Source of Neutrons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2.1.2 Special Nuclear Material . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.1.3 Multiplication Factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.1.4 Subcritical Neutron Multiplication . . . . . . . . . . . . . . . . . . . . . 14
2.2 Fissile Material Analysis Techniques . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.1 Rossi-alpha . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.2.2 Feynman-Y . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.2.3 Multiplicity Counting . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.2.4 Correlating Particles with Fast Organic Scintillators. . . . . . . . . . . . 25
2.2.5 Time Correlated Pulse Height . . . . . . . . . . . . . . . . . . . . . . . 26


**3 Digital Pulse Processing** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **29**


3.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29

3.2 Timing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3.3 Energy Calibration and Resolution . . . . . . . . . . . . . . . . . . . . . . . . . 34
3.4 Neutron Light Output . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


iv


3.5 Pulse Shape Discrimination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.5.1 Pulse Shape Quantification . . . . . . . . . . . . . . . . . . . . . . . . . 38
3.5.2 Bayesian Classification Methodology . . . . . . . . . . . . . . . . . . . 40


**4 Time Correlated Pulse Height Distributions** . . . . . . . . . . . . . . . . . . . . . . . **45**


4.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45

4.2 Analytical Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
4.3 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
4.4 Measurement Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

4.5 Simulation Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55

4.6 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56


**5 Time of Flight Fixed by Energy Estimation** . . . . . . . . . . . . . . . . . . . . . . . . **57**


5.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

5.2 TOFFEE Definition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
5.3 Template Approach for Treaty Verification . . . . . . . . . . . . . . . . . . . . . 61
5.4 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
5.5 Methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65
5.6 Dismantlement Confirmation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
5.7 Item Confirmation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.8 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70


**6 Solving For Subcritical Assembly Physical Parameters** . . . . . . . . . . . . . . . . . **73**


6.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73

6.2 Two-Region Point Kinetics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
6.3 Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
6.4 Simulation Validations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

6.4.1 Cf-252 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79

6.4.2 BeRP Ball . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81

6.5 Bare Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
6.6 Reflected Configurations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
6.6.1 Multiplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
6.6.2 Shell Thickness and Material Type . . . . . . . . . . . . . . . . . . . . . 89
6.7 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91


**7 3D Imaging** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **93**


7.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93

7.2 Background of 2D and 3D Radiation Imaging . . . . . . . . . . . . . . . . . . . 95
7.3 Neutron Double Scatter 2D Imaging . . . . . . . . . . . . . . . . . . . . . . . . 96
7.4 Gamma-Neutron-Neutron 3D Imaging . . . . . . . . . . . . . . . . . . . . . . . 97
7.5 Image Reconstruction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
7.6 Stochastic Origin Ensemble . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
7.7 Measurements and Simulations . . . . . . . . . . . . . . . . . . . . . . . . . . . 104


7.7.1 Detection System and Setup . . . . . . . . . . . . . . . . . . . . . . . . 105
7.7.2 Point-source Image Results . . . . . . . . . . . . . . . . . . . . . . . . 106
7.7.3 Radial Distance and Angular Resolutions . . . . . . . . . . . . . . . . . 106


v


7.7.4 Thunderbird Simulations . . . . . . . . . . . . . . . . . . . . . . . . . . 109

7.8 System Resolution and Uncertainty Analysis . . . . . . . . . . . . . . . . . . . . 112
7.9 Augmented Reality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
7.10 Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115


**8 Summary, Conclusions and Future Work** . . . . . . . . . . . . . . . . . . . . . . . . . **117**


8.1 Summary and Conclusions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
8.2 Future Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119


**Appendices** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **121**


**Bibliography** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **146**


vi


### **LIST OF FIGURES**

2.1 Neutron probability distribution for induced fission of Pu-239, with 2 MeV neutron
incident neutron energy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2 Gamma probability distribution for induced fission of Pu-239 . . . . . . . . . . . . . . 9
2.3 Diagram of a fission chain evolution inside hypothetical sphere of special nuclear material. Each of the black lines represent neutrons, the red nodes represent a fission
events and the blue termination points represent neutron absorption. The total multiplication is equivalent to the total number of of neutrons or the number of black lines
( _M_ _T_ = 8). However, the leakage multiplication is only three ( _M_ _L_ = 3), equivalent to
the number of neutrons that escaped the sphere. . . . . . . . . . . . . . . . . . . . . . 15
2.4 Example of time binning in a Rossi-alpha experiment of a neutron event train depicted
by black bars. The blue arrows show binned times within each of the fixed time
windows of length _T_ _W_ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.5 Kinematics of neutron scatter on hydrogen nucleus (proton) which is the primary
mode of neutron detection in organic scintillators. . . . . . . . . . . . . . . . . . . . . 27
2.6 TCPH distributions for (a) non-multiplying and (b) multiplying sources with the theoretical line of arrival shown in red. . . . . . . . . . . . . . . . . . . . . . . . . . . . 28


3.1 Example of a pulse and its derivative as calculated using the DZC method. The zero
crossing time, marked by the red dot, is interpolated starting the the maximum of the
derivative. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

3.2 Example of a pulse and its cumulative integrals as calculated from the CIF method.
The fraction of the cumulative integral (10%) used for time-pick-off is marked by the
red dot. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

3.3 Gamma-gamma TOF spectra with optimized parameters for each of the three timing
methods. The optimized fractions for the DCZ and CFD methods were both 50%
and only 5% for the CIF method. The FWHMs, standard deviations and means are
expressed in units of nanoseconds . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
3.4 Gamma-neutron TOF spectra as calculated using the three timing methods. The data
was taken from a measurement of a Cf-252 source at 30 cm distance from the pair of
detectors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33

3.5 Comparison of simulation and measurement data of a gamma-neutron TOF spectra
from a Cf-252 source at 30 cm from the detectors. The data was processed using two
timing methods, DZC and CFD, with fractions set to 50%. . . . . . . . . . . . . . . . 34
3.6 Measured and simulated spectra of Na-22 source matched with optimum resolution
and calibration parameters. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36


vii


3.7 A 2" _×_ 2" stilbene crystal neutron light output data fit to Birks’ and Katz’s formulations. The Katz coefficients are _a_ = 0 _._ 505, _b_ = 1 _._ 072, _c_ = 0 _._ 446, and _d_ = 1, and the
Birks coefficients are _S_ = 1 _._ 63 and _k_ = 27 _._ 83. . . . . . . . . . . . . . . . . . . . . . 38
3.8 Example of tail and total integration windows used in the charge integration method. . 39
3.9 The mean (solid lines) and three standard deviation (dashed lines) fits as applied to
the Am-Be data set. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.10 The distribution of neutron posterior probabilities for 1:1 mixture of [60] Co and time
tagged neutron data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43


4.1 Simulated EJ-309 neutron response matrix and the resulting TCPH distribution with
assumed [239] Pu Watt neutron energy spectrum and source-to-detector distance of 50
cm. Each distribution is normalized to unity and displayed on a logarithmic scale. . . . 47
4.2 Distribution of time differences for various n _[th]_ -nearest-neighbor fission events is represented by each colored line, with the black line showing the distribution between all
fission events in a chain. The distributions were obtained from an MCNPX-PoliMi
simulation of bare BeRP ball (stairs) and then normalized to unity and fit by Gamma
functions (solid lines). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
4.3 Diagram of the experimental setup of the BeRP ball surrounded by four EJ-309 detectors. The detectors were spaced approximately 8.5 _[◦]_ apart. . . . . . . . . . . . . . . 51
4.4 Measured TCPH distributions (left) and corresponding models with parameters from
the minimization algorithm (right) for various BeRP ball configurations. . . . . . . . 54
4.5 Optimized shape and rate parameters for both simulation (blue) and measurement
(red) cases. The shielding configurations varied in thickness from 1.27-7.62 cm with
1.27 cm intervals. The increase in symbol size corresponded to an increase in multiplication, which is proportional to the area of each marker. Note that the bare configurations are furthest to the left for both measurements and simulations. . . . . . . . . 55


5.1 Space-time diagrams of gamma ray (green) and neutron (red) particle paths from birth
to detection (dashed blue line). The (a) non-multiplying diagram depicts the simultaneous birth of particles, and the (b) and (c) multiplying diagrams depict a fission
chain where each fission is separated by generation time ∆ _T_ _g_ . The measured timeof-flight difference, _t_ _n,γ_, is equivalent to the true time-of-flight difference _T_ _n,γ_ in the
non-multiplying case, but it includes the generation time in the multiplying case. The
dashed red lines depict possible estimates of the neutron’s velocity from proton recoil.
The end-points of those dashed lines on the time-axis at the assumed source distance
make up the TOFFEE distribution. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
5.2 TOFFEE distributions of simulation of the Beryllium Reflected Plutonium (BeRP)
ball constructed from gammas and neutrons originating from the same generation and
different generations of fissions. There are more correlations from different generations due to neutron multiplication of the BeRP ball ( _M_ = 4 _._ 389 _±_ 0 _._ 005). . . . . . . 61
5.3 A diagram of the principle operations of template-based verification measurements. . . 62
5.4 Photograph of the measurement of one of the BeRP ball configurations with the Stilbene Array. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65


viii


5.5 Count normalized (left) and time normalized (right) TOF corrected neutron-gamma
time distributions for the bare BeRP ball (black) and the BeRP ball in a 2.54 cm
HDPE shell (blue). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
5.6 The log-likelihood distribution (left) and corresponding Receiver Operator Characteristic (ROC) curve (right) for 10,000 — 8 second trails of the comparison of the bare
(dismantled) and moderated BeRP ball. . . . . . . . . . . . . . . . . . . . . . . . . . 67
5.7 The pairs of trusted and tested objects used for dismantlement verification. The moderators, HDPE and Lucite, were used as high explosive (HE) surrogates. The inner
and outer dimensions of the TACS shells are given in centimeters. . . . . . . . . . . . 68
5.8 False Positive rate as a function of dwell time assuming 99% True Positive operational
threshold with count normalized analysis of dismantled objects. . . . . . . . . . . . . 69
5.9 The pairs of trusted and tested objects used for dismantlement verification. The moderators, HDPE and Lucite, were used as high explosive (HE) surrogates. The inner
and outer dimensions of the TACS shells are given in centimeters. . . . . . . . . . . . 70
5.10 False Positive rate as a function of dwell time assuming 99% True Positive operational threshold with count normalized analysis for item confirmation comparing
TACS shells (HEU) and the BeRP ball against the non-multiplying Cf-252 and lowmultiplying Hemi shells. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71


6.1 The front of purpose-built stilbene array used for all measurements. . . . . . . . . . . 79
6.2 Measurement and simulation comparison of the Cf-252 source (a) pulse height distribution of gamma-ray correlated neutrons and (b) corresponding relative error of the
simulation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80

6.3 Measurement and simulation comparison of the Cf-252 source (a) TOFFEE distribution and (b) corresponding relative error of the simulation. . . . . . . . . . . . . . . . 81
6.4 Measurement and simulation comparison of the bare BeRP ball (a) TOFFEE distribution and (b) corresponding relative error of the simulation. . . . . . . . . . . . . . . . 82
6.5 Measurement and simulation comparison of the BeRP ball with 1 inch iron shielding
(a) TOFFEE distribution and (b) corresponding relative error of the simulation. . . . . 83
6.6 Comparison of the measured and simulated bare BeRP ball TOFFEE distributions and
exponential fits from Eq. 2.13. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
6.7 The estimated ( _α_ _F_ ) and calculated, from MCNP6, ( _α_ _M_ ) alpha parameters for BeRP
balls with mass ranging from 1 to 8 kg. A linear regression was performed with the
resulting relationship shown in the legend and a correlation coefficient of 0.9890. . . . 85
6.8 Derived neutron multiplications from TOFFEE fits of the bare BeRP balls with different masses with the corresponding (a) total and (b) leakage multiplications obtained
through MCNP6 simulations. The dashed line corresponds to perfect agreement between derived and actual multiplication, with the points above and below corresponding to overestimation and underestimation, respectively. . . . . . . . . . . . . . . . . 85
6.9 TOFFEE distributions of the measured iron configurations with corresponding double
exponential fits from Eq. 6.7. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
6.10 Comparison of the estimated multiplication of the measured and simulated TOFFEE
distribution for the shielded configuration of the BeRP ball. The dashed line represent
perfect agreement between the fit and the expectation from MCNP simulation. . . . . 88


ix


6.11 Estimated multiplication for simulated TOFFEE distributions of several configurations of shielded BeRP ball with different material types. . . . . . . . . . . . . . . . 88
6.12 Integral of a double exponential fit as a function of shell thickness. . . . . . . . . . . . 89
6.13 The integral of the fit of Eq. 6.7 to TOFFEE distributions of the reflected configurations of the BeRP ball and the effective areal density of each of the shells. . . . . . . . 90
6.14 The (a) scaling ratio and (b) neutron lifetime in the reflector from the fit of Eq. 6.7 to
TOFFEE distributions of the BeRP ball with various reflector shell thicknesses. . . . . 91


7.1 TOFFEE distributions of a measured Cf-252 source at a distance of 50 cm with neu
tron energy estimations using the proton recoil energy ( _E_ _p_ ) and the incident neutron
energy ( _E_ _n_ ) from double scatter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
7.2 Illustration of the kinematics of a double neutron scatter in a scatter camera, resulting
in a cone of possible source locations. . . . . . . . . . . . . . . . . . . . . . . . . . . 98
7.3 The cone of possible source locations from neutron double scatter and a corresponding correlated gamma ray. The second neutron scatter is not shown. The distances
between the source (yellow 4-pointed star) and first neutron scatter ( _R_ _n_ ) and gamma
ray ( _R_ _γ_ ) are shown for one of the possible locations along the surface of the cone. All
other possible source locations lay somewhere along the azimuthal ( _φ_ ) angle of the
cone. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99

7.4 Possible source locations for a single measured correlated events shown as colored
spheres. The first (red) and second (blue) neutron scatter define the central axis of
the cone and the opening angle, and the correlated gamma ray (green) constrains the
radial distance to form the resulting “donut" shape. The superposition of many donuts
will reveal the source location in the overlapping region. For illustrative purposes we
show the same object from two different angles. . . . . . . . . . . . . . . . . . . . . . 100
7.5 The number of displaced source locations per iteration during a SOE reconstruction
of an image. This particular reconstruction was ran 10 times in parallel, as indicated
by the legend. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
7.6 A photo of MINER in open configuration. . . . . . . . . . . . . . . . . . . . . . . . . 105
7.7 Measurement configuration showing the position of the two Cf-252 sources with respect to MINER. The dimensions of the detector and source-to-detector distances are
drawn in correct proportions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
7.8 The measurement ( _left_ ) and simulated ( _right_ ) images with each reconstructed source
point weighted by _r_ [4] . Each source is marked by a blue (60 cm source) and red (50 cm
source) square. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.9 The polar projection (top-down view) of the image reconstruction for both the ( _top_ )
measurement and ( _bottom_ ) simulation. . . . . . . . . . . . . . . . . . . . . . . . . . . 107
7.10 The radial distance ( _left_ ) and azimuthal angle ( _right_ ) distributions for both measurement ( _solid_ ) and simulation ( _dashed_ ). The radial distance distribution describes the
distance from detector center. The source points were taken from the within the
squares of the images in Figure 7.8, with matching color combinations. . . . . . . . . 108
7.11 The top-view ( _left_ ) and angled side view ( _right_ ) of the MCNP model of MINER detector cells and thunderbird shaped Cf-252 source. . . . . . . . . . . . . . . . . . . . 110


x


7.12 Image reconstructions of a thunderbird shaped Cf-252 source performed using (a)
back-projection and SOE with (b) 2 cm and (c) 4 cm bandwidth parameters. The
images are top-down view, with all source points between _−_ 5 _< z <_ 5 projected onto
an _x −_ _y_ plane. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
7.13 Visualization of the spread source-to-detector distance and the opening angle as a
function (red) _n −_ _n_ and (green) _γ −_ _n_ timing, and (blue) neutron pulse amplitude
uncertainty. Each source of uncertainty is treated separately, and the results are displayed in different colors, the combined result is shown in black. A timing resolution
of 2 ns and energy resolution of 10% was assumed . . . . . . . . . . . . . . . . . . . 112
7.14 Microsoft’s HoloLens. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114

7.15 Thunderbird source displayed as a hologram as seen through a HoloLens. The corner
of a virtual MINER detection system is on the left, and a bemused dog on the right. . . 115


xi


### **LIST OF TABLES**

2.1 Significant Quantities of SNM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11


4.1 Optimized Gamma function parameters for the five measured configurations of the
BeRP sphere with standard errors of 1 standard deviation shown . . . . . . . . . . . . 52
4.2 Optimized distances for the five measured configurations of the BeRP sphere with
standard errors of 1 standard deviation. The measured distance was measured from

the center of the BeRP ball to the face of the detectors. . . . . . . . . . . . . . . . . . 53


5.1 Total data collection times for objects at the DAF and LLNL measurement campaigns. 64
5.2 Summary of the time to confirm dismantlement with 99% TP and 1% FP rate. . . . . . 68
5.3 Summary of the time to item confirmation with 99% TP and 1% FP rate. . . . . . . . 70


6.1 Measurement details of the various configurations of the BeRP ball with iron and
nickel reflectors. The neutron multiplication was calculated from MCNP5 k-code
simulation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78

6.2 Linear leas-squared regression for the correlation between integral of the fit to TOFFEE distribution and effective areal density of the reflector material. . . . . . . . . . . 90


7.1 Radial distribution (units in cm) parameters for each source in both measurement and
simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109

7.2 Azimuthal angular distribution parameters for each source in both measurement and
simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109


xii


### **LIST OF APPENDICES**

**A Source Code** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **121**


**B Math** . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **143**


xiii


### **LIST OF ABBREVIATIONS**

**AR** Augmented Reality


**BeRP** Beryllium Reflected Plutonium


**CFD** Constant Fraction Discrimination


**DAF** Device Assembly Facility


**DU** Depleted Uranium


**DZC** Derivative Zero Crossing


**CIF** Cumulative Integral Fraction


**FWHM** Full Width Half Maximum


**FP** False Positive


**HEU** Highly Enriched Uranium


**IAEA** International Atomic Energy Agency


**MCMC** Markov chain Monte Carlo


**MeVee** MeV electron equivalent


**MINER** Mobile Imager of Neutrons for Emergency Response


**MLEM** Maximum Log-likelihood Expectation Maximization


**NDA** Non-Destructive Assay


**NPT** Non-Proliferation Treaty


**NNSS** Nevada National Security Site


**KDE** Kernel Density Estimator


**PET** Positron Emission Tomography


**PGF** Probability Generating Function


**PMT** Photomultiplier Tube


xiv


**PSD** Pulse Shape Discrimination


**ROC** Receiver Operator Characteristic


**TACS** Training Assembly for Criticality Safety


**TP** True Positive


**TCPH** Time Correlated Pulse Height


**TOF** Time of Flight


**TOFFEE** Time of Flight Fixed By Energy Estimation


**SOE** Stochastic Origin Ensemble


**SPECT** Single Photon Emission Computed Tomography


**SQ** Significant Quantities


**SNM** Special Nuclear Material


**WGPu** Weapons-Grade Plutonium


xv


### **ABSTRACT**

Neutrons born from fission may go on to induce subsequent fissions in self-propagating series of


reactions resulting in a fission chain. Fissile materials comprise all isotopes capable of sustain

ing nuclear fission chain reactions, and are therefore a necessary prerequisite for the construction


of a nuclear weapon. As a result the accountancy and characterization of fissile material is of


great importance for national security and the international community. The rate at which neutrons


“multiply" in a fissile material is a function of the composition, total mass, density, and shape of


the object. These are key characteristics sought out in areas of nuclear non-proliferation, safe

guards, treaty verification and emergency response. This thesis demonstrates a novel technique of


measuring the underlying fission chain dynamics in fissile material through temporal correlation


of neutrons and gamma rays emitted from fission.


Fissile material exhibits key detectable signatures through the emission of correlated neutrons


and gamma rays from fission. The Non-Destructive Assay (NDA) community has developed ma

ture techniques of assaying fissile material that detect these signatures, such as neutron counting


by thermal capture based detectors, and gamma-ray spectroscopy. An alternative use of fast or

ganic scintillators provides three additional capabilities: (1) discrimination between neutrons and


gamma-ray pulses (2) sub-nanosecond scale timing between correlated events (3) measurement of


deposited neutron energy in the detector. This thesis leverages these capabilities into to measure


a new signature, which is demonstrated to be sensitive to both fissile neutron multiplication and


presence of neutronically coupled reflectors. In addition, a new 3D imaging method of sources of


correlated gamma rays and neutrons is presented, which can improve estimation of total source


volume and localization.


xvi


## **CHAPTER 1**

# **Introduction**

## **1.1 Brief History of the Fission Chain**

The 20 _[th]_ century began with a rudimentary understanding of the atom, which was suitable for


chemistry and molecular studies. The only known subatomic particle was the electron. From the


start of the century, each breakthrough discovery of the subatomic structure of the atom came about


every decade. In 1911 Ernest Rutherford discovered the nucleus, and at the end of that decade, in


1919, the proton. In the 1920s Neils Bohr, Erwin Schrödinger, and Werner Heisenberg, among


other theorists, developed quantum mechanics, which contradicted the theory of nuclear electrons


that would keep protons from being repelled apart. This theoretical work greatly bolstered the case


for the existence of a neutron, which was eventually discovered in 1932 by James Chadwick at the


Cavendish laboratory headed by Rutherford himself.


The discovery of the neutron proved pivotal in the history of the fission chain, from that point


on the world was just thirteen years away from its first nuclear weapons test. Only a year out


from the necessary discovery of the neutron, Leo Szilard would conceive of the concept of self

sustaining neutron-induced chain reactions. Even more impressive was his immediate grasp of


the explosive implications of such theory, which would profoundly change the world [1]. In that


same year, Szilard and Enrico Fermi would patent the idea of a nuclear reactor. Nuclear fission


was discovered in 1938 by Otto Hahn, and explained theoretically a year later by Lise Meitner


and Otto Frisch through the use of Bohr’s liquid drop-model. That same year, Nazi Germany and


1


Soviet Union would join forces and invade Poland, officially starting World War II in the European


theater.


Szilard’s dream of a sustained fission chain was realized in 1942 when the Chicago Pile-1


reactor achieved criticality. The work of Szilard and his fellow European refugees under the Man

hattan project would eventually give birth to an atomic weapon which was first tested under the


code name “Trinity" in a New Mexico desert on July 16 _[th]_ 1945. The scientific lead of weapon


design, J. Robert Oppenheimer, described the moment that the bomb went off in an interview for a


1965 television program _The Decision to Drop The Bomb_ :


“We knew the world would not be the same. A few people laughed, a few people


cried. Most people were silent. I remembered the line from the Hindu scripture, the


Bhagavad Gita. Vishnu is trying to persuade the Prince that he should do his duty, and,


to impress him, takes on his multi-armed form and says, ’Now I am become Death,


the destroyer of worlds.’ I suppose we all thought that, one way or another."


The quote out of the Hindu scripture has now ubiquitous association with that fateful day. One


wonders if Oppenheimer thought of it before a fellow physicist Kenneth Bainbridge turned to him


immediately after the test and proclaimed:


“Now we are all sons of bitches."


The end of the war simultaneously begun the next chapter in geopolitical world order. The


proverbial Genie was out of the bottle and around the world atomic weaponry would be acquired,


by hook or by crook, by an exponentially weaker and poorer list of state actors stretching from


Joseph Stalin to Kim Jong-il. In the early 1950s United States and the Soviet Union developed


hydrogen bombs, while at same time Eisenhower launched an effort to demilitarize nuclear tech

nology beginning with the “Atoms for Peace" speech at the UN General Assembly. As of today


there are eight declared nuclear armed states and 31 countries with operational nuclear reactors.


2


## **1.2 Motivation**

The global spread in nuclear technology, coupled with a rapid buildup of nuclear weapon stockpile


during the Cold War, has left a legacy of abundant global supply of fissile material necessary for


making an atomic bomb. Anticipating this problem, the international community has put together a


regime of safeguards and non-proliferation, administered through the International Atomic Energy


Agency (IAEA), with the specific goal of accounting for and preventing the illicit spread of fissile


material and nuclear weapon technology. The centerpiece of global nuclear cooperation is the


Non-Proliferation Treaty (NPT), which stipulates a basic bargain: all countries may engage in


peaceful use of nuclear technology provided that it’s not used for nuclear weapons, and countries


with nuclear weapons will work toward complete disarmament. These frameworks function as


a deterrent for states that may seek nuclear weaponry, by providing an international inspection


regime of nuclear facilities inside member states.


Upholding the disarmament pillar of the NPT bargain has been largely carried out through bi

lateral treaties between the United States and Russia, which account for over 90% of total nuclear


warhead stockpile. These bilateral agreements started in the Cold War with the Strategic Arms


Limitation Talks (SALT), which lead to the Strategic Arms Reduction Treaties (START); the latest


generation of which is the New START ratified in 2011. These treaties are verified by each oth

ers’ inspection teams that are invited to visit host nuclear facility of the other country and certify


compliance.


The other threat of loose fissile material concerns the use of weapons of mass destruction by


non-state actors. Nuclear terrorism includes a range of potential attacks from deploying a dirty


bomb to poisoning the water supply, but by far the most consequential is acquisition of a nuclear


weapon [2]. Although the probability of terrorist acquiring and detonating a nuclear weapon is


low, the threat is quite real. In his 2009 speech in Prague on nuclear weapons, President Obama


singled out nuclear terrorism as primary concern:


“So, finally, we must ensure that terrorists never acquire a nuclear weapon. This is the


3


most immediate and extreme threat to global security. One terrorist with one nuclear


weapon could unleash massive destruction. Al Qaeda has said it seeks a bomb and that


it would have no problem with using it. And we know that there is unsecured nuclear


material across the globe."


Preventing fissile material from falling into the wrong hands involves monitoring of illicit traf

ficking at border crossings and through other ports of entry. The most important task is detection,


but once an item of concern is seized, its immediate characterization is a critical task for the emer

gency response teams. At a later time the item may be sent to a laboratory in order to determine


the place of origin through nuclear forensic methods.


The protocols concerning the nuclear threats outlined above fall into four general categories,


which have some overlaps:


1. Non-proliferation: preventing the spread of nuclear weapons.


2. Safeguards: securing and account of fissile material.


3. Treaty Verification: confirmation of disarmament.


4. Emergency Response: on-site characterization of seized material.


5. Nuclear forensics: laboratory investigation material age, source origin etc.


All of these require the measurement and characterization of fissile material, which by definition


produces nuclear chain reactions. As I will demonstrate, the measurement of fission chain dynam

ics is relevant because it provides information about the fissile material itself: mass, geometrical


configuration, and presence of any neutronically coupled materials, such as high explosives.

## **1.3 Thesis Contribution and Overview**


Fissions produce two primary detectable signatures: gamma rays and neutrons. The prevalence of


thermal capture neutron detectors, such as He-3 proportional counters, have limited the develop

4


ment of neutron counting based Non-Destructive Assay (NDA). An alternative use of Pulse Shape


Discrimination (PSD) capable fast organic scintillators provides three additional key capabilities:


1. Distinguishing between gamma ray and neutron pulses, and incorporating both into the anal

ysis.


2. Sub-nanosecond scale timing between correlated detected events.


3. Measurement of deposited neutron energy through scintillation due to proton recoil.


In addition, the use of fast electronics provides a way to store individual detected pulses and apply


advanced digital processing techniques in post-measurement analysis. This thesis leverages these


capabilities and provides an alternative technique for characterizing fissile material through fast


gamma-neutron correlations. The sensitivity of this new signature to fissile material neutron mul

tiplication and presence of neutron reflectors is explored. Furthermore, a correlated gamma ray


coupled with traditional double neutron scatter imaging is shown to produce a new 3D imaging


technique, which can further improve estimation of total source volume and localization.


The following is a brief summary of each chapter:


Chapter 2: The definitions of fissile material properties and other neutrons sources are laid


out. The basics of the three major NDA techniques, Rossi-alpha, Feynman-Y and Multiplic

ity Counting, are presented in chronological order, along with the history of the development


of each method. Finally, the rationale and advantages of using the new gamma-neutron cor

related signature concludes the chapter.


Chapter 3: The best practices and pitfalls of digital processing of organic scintillator pulses


from timing to pulse shape discrimination. The details of common processing tasks (e.g.


energy calibration) that are applied to data throughout this thesis are collected here for suc

cinctness. A Bayesian approach for classifying the pulses and estimating the gamma-ray or


neutron probability is put forward as the PSD method of choice for this work.


Chapter 4: An overview of the prior work with Time Correlated Pulse Height (TCPH) distri

bution is given, along with a new method of analyzing the distribution and fitting empirical


5


parameters. Results from fits to measured and simulated TCPH distributions of the BeRP


ball with polyethylene and tungsten reflectors are shown.


Chapter 5: A reformulation of TCPH signature into a one-dimensional Time of Flight Fixed


By Energy Estimation (TOFFEE) distribution is presented. A template matching approach


is used in the context of treaty verification for dismantlement and item confirmation of both


plutonium and uranium objects.


Chapter 6: A physical interpretation of the time-dependent neutron population in fissile


material surrounded by a reflector is derived from two-region point kinetics. The model is


then used to fit physical parameters to bare and reflected configurations of the BeRP ball.


Chapter 7: A new 3D imaging method of sources of coincident gamma rays and neutrons


is presented. Preliminary measurements and simulations are shown as a proof-of-concept of


the imaging technique.


6


## **CHAPTER 2**

# **Fissile Material Properties and Detection Techniques**

## **2.1 Definitions**

### **2.1.1 Source of Neutrons**

A broad overview and details about neutron sources and expected yields of most common sources


are given in [3]. The focus of the following overview is the correlated emission of neutrons and


gamma rays from those sources. The source of fission neutrons comes in two categories: spon

taneous and induced. Spontaneous fission is the result of heavy actinides spontaneously decaying


into two or more lighter isotopes. In this respect it’s simply another mode of decay of an isotope.


By contrast, induced fission necessitates neutron absorption by a fissionable isotope from outside


the nucleus. The emitted products are neutrons and gamma rays, with slight variations in the


energy and number (or multiplicity) of neutrons and gamma rays produced. In addition, there is


incident neutron energy dependence on the number and energy of the emitted neutrons. The fission


process typically results in the near simultaneous emission of 0 to 6 neutrons and 0 to 20 gamma


rays. The distribution of the number of emitted particles is called the “multiplicity" distribution,


and examples are shown in Figure 2.1 and 2.2.


The mean neutron multiplicity, ¯ _ν_, depends on the isotope, and varies from as little as 2.16 for


Pu-240 to as much as 3.757 for Cf-252. Establishing the value of ¯ _ν_ has been of utmost importance


because of its role in determining the length of a fission chain, and thus when an assembly becomes


critical. In a critical assembly the rate of neutron production, which depends among other factors


7


on ¯ _ν_, is equal to the rate of neutron loss. As a result, neutron multiplicity and ¯ _ν_ have been studied


with numerous experiments to a greater precision than gamma-ray multiplicity [4].





Figure 2.1: Neutron probability distribution for induced fission of Pu-239, with 2 MeV neutron
incident neutron energy [4].


The energy of the resulting gamma rays and neutrons also varies between fission events. The


mean energy of the fission neutrons is around 2 MeV, and distribution of the neutron energies can


be approximated by a Watt spectrum defines as



_f_ ( _E_ ) = _C_ exp( _−E/a_ ) sinh( _√_



_bE_ ) (2.1)



where _C_ is a normalization factor and _a_ and _b_ are constants that vary between fissioning isotopes


[7].


For isotopes with large cross-sections for fission over the Watt spectrum, the neutrons produced


from fission can subsequently induce other fissions, and thus causing a fission chain. Neutrons and


gamma rays from the same fission chain are also correlated, though some of them are not born


simultaneously. Because these correlated gamma rays and neutrons come from different fissions,


there will exist a characteristic time between their emission that set them apart from other sources


8


Figure 2.2: Gamma probability distribution for induced fission of Pu-239 [5, 6].


of correlated neutrons and gamma rays. It is this difference that is exploited and explored in this


dissertation.


The last category of ubiquitous sources of correlated gamma rays and neutrons are the so-called


alpha-neutron, or alpha-n, sources. Their name derives from the ( _α, n_ ) reactions that occur when


a heavy alpha emitter (e.g. Pu-238, Am-241) is brought together with suitable light target isotope


(e.g. Be-9, F-19, Li-7, O-17). After capturing the alpha particle and emitting a neutron, the product


isotope is left in an excited state which leads to emission of correlated gamma rays. Unlike fission


gamma rays, these have specific characteristic energies caused by discrete energy level differences


among the excited states and the ground state. The energy spectra of emitted neutrons are also quite


different from their fission counterparts, and vary widely between different of alpha-n sources. For


example, the mean neutron energy of an AmBe source is 4.5 MeV, but only 300 keV for an AmLi


source. This range of energies makes alpha-n sources versatile laboratory tools, but ( _α, n_ ) reactions


also provide a source of neutrons in reactor fuel and stored fissile material.


Uranium and plutonium oxides are the most common form of nuclear fuel used in commer

cial power plants, and uranium hexafluoride (UF 6 ) is used for enrichment and storage. Oxygen


and fluorine have a relatively large ( _α, n_ ) cross-sections, therefore these mixtures emit correlated


9


gamma rays and neutrons of both types: fission and ( _α, n_ ). The result is a mixed source of neu

trons, which have to be accounted for in the coincidence counting techniques described in Section


2.2. The neutrons born out of ( _α, n_ ) reaction have a multiplicity of one, and by themselves only


contribute to the uncorrelated background. However, just like spontaneous fission neutrons, ( _α, n_ )


neutrons may induce fissions and start fission chains, which contribute to the coincidence response.


The relative strength of ( _α, n_ ) neutrons depends in large part to the source strength of alpha emit

ters and the amount of low-Z isotopes mixed in the material, and not directly on the amount of


spontaneously fissioning isotopes [8]. Since fissile material assay is determined from measuring


the amount these spontaneously fissioning isotopes, any unaccounted contributions from ( _α, n_ )


neutrons may adversely affect the final mass estimations.

### **2.1.2 Special Nuclear Material**


Special Nuclear Material (SNM) is actually defined by law under Title I, Chapter 2, Section 11 of


the Atomic Energy Act of 1954 as “plutonium, uranium enriched in isotope 233 or in the isotope


235 [9]." The definition is quite unsatisfactory and leaves open the question of what is so “special"


about Special Nuclear Material (SNM). The answer comes later at the end of Section 53 “special


nuclear material shall be distributed only on terms... that no user will be permitted to construct


an atomic weapon." It’s clear, therefore, that SNM is important because it is the prerequisite for


making atomic weapons. For this reason SNM is often used interchangeably with the term “fissile"


material, however, the latter has a more precise technical definition.


Fissile material is capable of undergoing induced fission by the neutrons that they emit, and


therefore can sustain nuclear chain reactions. The binding energy supplied from capturing a neu

tron is greater than the critical energy necessary to split the atom. Therefore, no additional energy


is required from the neutron to induce a fission which gives birth to subsequent neutrons. In gen

eral, heavy actinides with odd number of neutrons meet the physical requirements to be considered


fissile. However, the most important fissile isotopes are U-235 and Pu-239, because both can be


readily weaponized for a fission-bomb [10]. The other fissile isotopes suffer from either high


10


spontaneous fission rate or high _α_ -emission rate, which can cause pre-detonation by supplying


initiating neutrons. The exception is U-233, which is theoretically weaponizable, but inevitably


contaminated by short lived U-232 which makes it practically prohibitive as a nuclear weapon


material [10].


Fissile material is a subset of a larger group of fissionable material. As the name suggests, fis

sionable material is capable of undergoing induced fission by a neutron above a threshold energy.


For example, U-235 is both fissionable and fissile. However, other fissionable but not fissile iso

topes require extra energy from the neutron to overcome the critical energy necessary to undergo


a fission. The distinction stems from the difference in the stability of heavy actinides with odd


number of neutrons and/or protons compared with those with an even number of both. The even


numbered isotopes are more stable, therefore an odd numbered isotope has greater binding energy


after it captures a neutron. Notable examples of fissionable isotopes are Th-232 and U-238, which


can be used in nuclear reactor fuel.


The IAEA has determined Significant Quantities (SQ) of different fissile isotopes that are “the


approximate amount of nuclear material for which the possibility of manufacturing a nuclear ex

plosive device can not be excluded... and should not be confused with critical masses. [11]" In


practice SQs are a useful standard in the safeguards community for discussing the smallest quantity


of fissile material worth accounting for, and are summarized in Table 2.1. Purity is also important,


uranium enriched in excess of 20% of U-235 is deemed Highly Enriched Uranium (HEU) and


plutonium with 93% or more Pu-239 is called Weapons-Grade Plutonium (WGPu).


Table 2.1: Significant Quantities of SNM [11].


Material SQ
Pu ~~_[a]_~~ 8 kg Pu
U-233 8 kg U-233
HEU (U-235 _≥_ 20%) 25 kg U-235


_a_ For Pu containing less than 80% Pu-238.


11


### **2.1.3 Multiplication Factor**

Fissile material is defined by its ability to “multiply" neutrons by generating fission chains. The


multiplication factor _k_ is the ratio of the number of neutrons born in one generation to those in the


previous generation:


number of neutrons in one generation
_k_ = (2.2)
number of neutrons in a previous generation _[.]_


This term provides a useful shorthand for the state of neutrons in a multiplying system, such as


a reactor. If _k_ = 1 then the neutron population is stable and the system is referred to as being


“critical". If _k >_ 1 then the neutron population will, on average, increase at a geometric rate and


the system is said to be “supercritical." Finally, if _k <_ 1 then neutron population will, on average,


decrease exponentially in subsequent generations and the system is said to be “subcritical."


In reactor theory, four and six-factor formulas are used to relate the factor _k_ to physical prop

erties of a system. The exact definitions of these formulas are not particularly relevant for this


thesis work, but the difference between them is useful in highlighting the meaning of k-effective or


_k_ _eff_, which often appears in literature without context. The four factor formula assumes an infinite


medium, but the six factor assumes a finite medium by including the probabilities of neutron non

leakage which results in _k_ _eff_ [12]. Neutron leakage is a term that describes the escape of neutrons


from the system.


The factor _k_ also makes an appearance as an eigenvalue for so-called criticality “search" prob

lems, where the goal is to determine the size and composition of a reactor which achieves criticality.


An example of its use can be seen in the operator notation of one-speed (energy) group neutron


diffusion model


**M** _φ_ = [1] (2.3)

_k_ **[F]** _[φ]_


where **M** is the destruction operator (leakage and absorption), **F** the production operator (fission),


12


and _φ_ the neutron flux [13]. In this form the factor _k_ plays a role of a modifier of the production


term, **F** _φ_, in order to make it equal to leakage and absorption of neutrons **M** _φ_ . The procedure is


to pick a reactor size and composition (which modifies **M** and **F** ), and solve for the factor _k_ . If


_k ̸_ = 1 then new reactor parameters are chosen and the calculation is repeated. However, if _k_ = 1


then the critical reactor configuration was found and the search is over.


Point reactor kinetics, which start from diffusion theory and omit spacial dependence, offer a


time based representation of _k_ . The spacial simplification allows for analytical solutions to time

dependent problems in nuclear reactor dynamics. This definition of _k_ takes the form of a quotient


of two terms:


_k_ = _[l]_ (2.4)

Λ


where _l_ is the neutron lifetime which is the mean time for one neutron to be removed by either


absorption or leakage, and neutron reproduction or generation time, Λ, is the mean time for one


neutron to be replaced by another via fission [14]. The implication here is that a reactor or assembly


is critical when _l_ = Λ.


Neutron generation time is a common term used in reactor point kinetics, but in the nonde

structive assay formulations, the mean fission time, _l_ _f_, is far more prevalent. The two factors are


related by ¯ _ν_ :


1
Λ = ¯ (2.5)
_ν_ Σ _f_ _v_

_l_ _f_ = [1] (2.6)

Σ _f_ _v_


where Σ _f_ is the macroscopic fission cross-section and _v_ is neutron velocity, the product of which


( _v_ Σ _f_ ) is the production rate of neutrons. Swapping out Λ with _l_ _f_ in Eq. 2.4 leads to another


13


interpretation of the multiplication factor:



_k_ = _[l][ν]_ [¯] = _p_ _f_ ¯ _ν_ (2.7)

_l_
_f_



where the ratio of mean neutron lifetime and mean time to fission is shown to be _p_ _f_, the probability


that a neutron undergoes fission.

### **2.1.4 Subcritical Neutron Multiplication**


The focus of this work is on subcritical systems, and specifically new techniques in measuring


their state and configuration. An important parameter derived from the multiplication constant _k_


is the subcritical neutron multiplication. If starting with a single source neutron, plugging in 1


to the denominator of Eq. 2.2, the factor _k_ becomes the average number of neutrons born in the


first generation. These first generation neutrons will go on to produce _k_ [2] neutrons in the second


generation and so on until the total number of neutrons produced from a single starting neutron is


1 + _k_ + _k_ [2] + _k_ [3] + _k_ [4] _..._ (2.8)


For subcritical systems ( _k <_ 1) this geometric series converges and the total neutron multiplication


is


1
_M_ _T_ = (2.9)
1 _−_ _k_


Eq. 2.9 is sometimes referred to as the prompt neutron multiplication, because the contribution


of delayed neutrons is ignored in this formulation. Prompt neutrons appear almost instantaneously


(femtoseconds) with the fission events. Delayed neutrons are the result of the decay of fission


products and contribute only a small fraction to the total neutrons resulting from fission. The delay


in the time that these neutrons are born is quite significant, as much as several seconds after the


14


initial fission event. The contribution of delayed neutrons are crucial for reactor dynamics and


they make reactor criticality control feasible [15]. However, for the purposes of this dissertation


the contribution of delayed neutrons can be ignored because the time-scales that govern their birth


(tens _µ_ s to tens of seconds) are outside of the coincident time windows that are used in the analysis


throughout this work (hundreds of ns).


A more important distinction in the definition of neutron multiplication is between total and


leakage multiplication. Leakage multiplication, sometimes referred to as "net" multiplication, de

scribes the number of neutrons that escape from the subcritical assembly [16]. This is an important


distinction because the neutrons that escape are the only ones that are available for measurement.


If the probability of leakage is _p_ _l_ then leakage multiplication is just


_p_ _l_
_M_ _L_ = _p_ _l_ _M_ _T_ = (2.10)
1 _−_ _k_ _[.]_


An illustration of the difference between total and leakage multiplication is shown in Figure 2.3.


Note that an individual fission chain is used as an example of subcritical multiplication, but in


actuality this concepts describes the average behavior of fission chains in a subcritical assembly.


Figure 2.3: Diagram of a fission chain evolution inside hypothetical sphere of special nuclear
material. Each of the black lines represent neutrons, the red nodes represent a fission events and
the blue termination points represent neutron absorption. The total multiplication is equivalent to
the total number of of neutrons or the number of black lines ( _M_ _T_ = 8). However, the leakage
multiplication is only three ( _M_ _L_ = 3), equivalent to the number of neutrons that escaped the
sphere.


15


## **2.2 Fissile Material Analysis Techniques**

The established techniques discussed below — Rossi-alpha, Feynman-Y and Multiplicity Count

ing — all fall under the theoretical purview of neutron noise analysis [17]. The first two techniques


trace their origins to the Manhattan project, and the works of Feynman, de Hoffmann and Serber


among many others [18]. Measurement of fundamental system parameters, for example the prompt


neutron period, and physical quantities, like ¯ _ν_, was of great interest to the brilliant scientists work

ing out these problems atop a New Mexican mesa. Their test subjects were either near-critical


or briefly supercritical fast assemblies, or purpose built reactors. A few decades later the NDA


community that inherited these techniques had to adapt to the new challenge of fissile material


accountancy. The challenge for these applications was to accurately measure the mass of fissile


material, and in particular plutonium, in test samples of unknown heterogeneous composition.


The application of the theory has been molded by technology available for neutron coincidence


counting at the time, namely thermal capture neutron detectors (He-3) and analog circuitry [8].


More recent work has focused on updating some techniques, such as multiplicity counting, by


adopting the analysis to include new factors that come with the use of fast organic scintillators


[19]. Some traditional techniques, like Feynman-Y, have been updated to include the contribution


for gamma rays measured by PSD capable organic scintillators [20]. This thesis work aims to


move beyond traditional analysis and make use of additional signatures available to fast organic


scintillators, which will be explored later in this chapter.

### **2.2.1 Rossi-alpha**


Rossi-alpha is one of the most well known and earliest neutron noise analysis methods. The


method’s namesake, Bruno Rossi, observed larger-than-expected fluctuations in neutron count


rates of a boiling water reactor at Los Alamos and reckoned that they were caused by correlated


neutrons from fission chains [21]. His key insight was that a single neutron could kick off a long


fission chain which would evolve on a characteristically shorter time scale than the random birth of


16


other source neutrons. The pioneers of neutron noise experiments were interested in measuring the


prompt neutron period, _α_, which is inversely related to the efficiency of explosive reactions [21].


The prompt neutron period can be measured directly by introducing and then removing a strong


neutron source (source jerk), or briefly forming a supercritical configuration [22]. Rossi’s exper

iment was an alternative approach to determine _α_ that relied on measuring the fluctuations from


many individual fission chains in a near critical assembly which is self-modulated (i.e. the mean


time between emission of source neutrons is of the order of or longer than prompt neutron pe

riod) [23].


The Rossi-alpha experiment itself is technically simple. First, an initial neutron detection opens


up a predetermined time window, or gate, and the times to all subsequent events in that window are


binned. The window then shifts to the second event and the binning process proceeds as before.


This process is shown in Figure 2.4, and in essence depicts the operations of a shift register. In the


days of analog circuitry these time windows would have to be fixed [8], but modern list-mode data


acquisitions allows for any time window to be applied in post-measurement analysis [24].


Figure 2.4: Example of time binning in a Rossi-alpha experiment of a neutron event train depicted
by black bars. The blue arrows show binned times within each of the fixed time windows of length
_T_ _W_ .


Feynman is credited for developing the theory for interpreting the Rossi experiments [25]. His


17


formulations had no spacial dimension (single region), and one-speed neutrons (single group),


which are prerequisites for modern point reactor kinetics. One-speed assumption meant a single


neutron energy, and thus a single average probability for induced fission. Under those assump

tions the rate of change of the number neutrons in a multiplying system is the difference between


production through fission and loss by absorption or leakage:



_dN_



_−_ _[N]_
_l_ _l_
_f_



_dN_ _[νN]_ [¯]

_dt_ [=] _l_



(2.11)
_l_



The terms in Eq. 2.11 have been previously defined in Section 2.1.3. Given the definition of


multiplication constant in Eq. 2.7, the balance Eq. 2.11 can be re-written as



_dN_



_dt_ [=] _[ k][ −]_ _l_ [1]



_N._ (2.12)
_l_



Taking _N_ (0) = _N_ 0 as the initial condition, the solution to this first order linear differential equation


is


_k−_ 1 _t_ _αt_
_N_ ( _t_ ) = _N_ 0 _e_ _l_ = _N_ 0 _e_ (2.13)


where _α_ is the prompt neutron period and is negative for subcritical assemblies [26]. The constant


_α_ is also referred to as the neutron rate of decay when the term in the exponent is negative [18]. It


is assumed that delayed neutrons are born on much longer time scales and therefore do not affect


the measurement of _α_ .


It follows that if the neutron population decays exponentially then the probability of detecting


a correlated neutron is governed by exponential decay. This probability of counting a correlated


neutron at time _t_ in interval _dt_ after an initial neutron at _t_ = 0 is


_D_ _v_ _k_ [2]
_p_ ( _t_ ) _dt_ = _Fϵ dt_ + _ϵ_ (2.14)

2(1 _−_ _k_ ) _l_ _[e]_ _[αt]_ _[dt]_


18


where _F_ is the average fission rate and _ϵ_ is the detection efficiency per fission [24]. Diven’s


parameter, _D_ _v_, is a measure of the relative width of the neutron multiplicity distribution


_D_ _v_ = _[ν]_ [(] _[ν]_ ¯ _[ −]_ [1][)] _._ (2.15)

_ν_ [2]


In practice the expression of the shape of the Rossi-alpha distribution is simplified to


_s_ ( _t_ ) = _A_ + _Re_ _[αt]_ (2.16)


where _A_ is the accidental rate of detecting uncorrelated neutrons in the time window and _R_ is the


correlated (or “real") coincidence rate [8]. With analog shift registers it is possible to measure


both _R_ and _A_ by opening two gates: a coincidence gate following the source trigger, and an


accidental gate after a some delay. List-mode digital acquisition allows for construction of Ross

alpha histograms made up of the time differences between detected neutrons. These measured


Rossi-alpha distributions are then fit to Eq. 2.16 in order to determine the prompt neutron decay


constant _α_ .

### **2.2.2 Feynman-Y**


The Feynman-Y, or the variance-over-mean technique, was developed by Richard Feynman along

side his theoretical work on the Rossi-alpha experiments [18] [27]. The fluctuations in counts


per unit time, _c_, from a purely random source should, by definition, follow a Poisson distribution.


However, the presence of correlated counts from fission chains add an excess variance beyond that


predicted from Poisson statistics. Feynman quantified this phenomena by taking the ratio of count


variance and mean:


¯
_c_ [2] _−_ ( _c_ ) [2]

¯ = 1 + _Y_ (2.17)
_c_


19


where ¯ _c_ is the average counts per unit time, _c_ [2] is the average of the square of the counts per unit


time, and _Y_ accounts for a deviation from Poisson statistics. For a gate width _t_, the parameter _Y_


can be approximated by



(2.18)
�




_[−]_ _[ν]_ [¯][)]
_Y_ = _[ϵ]_ [(] _[ν]_ [2]

( _−αl_ _f_ ) [2]



1 + [1] _[ −]_ _[e]_ _[αt]_

_αt_

�



where _l_ _f_ is the mean time between fissions, defined previously in Eq. 2.6. Note that this is follow

ing Orndoff’s [26] rather than Feynman’s [18] notation for _α_ in order to stay consistent with the


presentation in Section 2.2.1.


The expression in Eq. 2.18 can be further simplified to just the first term if the gate width is


long enough to capture the prompt period but small compared to the delay period and the delayed


neutrons do not significantly contribute to the overall neutron multiplication [28]. It is possible


to determine if the gate width is long enough by taking multiple measurements with increasing


gate widths. The Feynman-Y test statistic will asymptotically approach a maximum value, and


the minimum required gate width can be determined by plotting the two values against each other.


Feynman also made approximations and variations on _Y_ to make it useful for interpreting exper

imental data. In particular, Feynman used the technique for measuring and validating the second


moment of the neutron multiplicity distribution [28].


Operationally the measurement of Feynman-Y differs in two important ways from the Rossi

alpha. First, the number of counts is recorded, as opposed to the time between counts in a gate.


Second, the gate is opened through a series of clock triggers, not by events registered in the detec

tor. Feynman-Y histograms, or distributions, can be constructed from the number of counts in each


gate, and provide a visual representation of the deviation from an expected Poisson distribution.


The first and second moments of the Feynman-Y distributions were used by Dowdy et al. to


develop a formalism that includes the contributions of spontaneous fission, neutron multiplication


and ( _α_,n) contaminants [29]. A variation on the Feynman-Y was used by Dowdy et al. to relate


20


measured fluctuations with these physical parameters:


_Q_ _m_ = _c_ ( _c −_ 1)¯ _c_ [2] (2.19)


where _c_ is still counts per unit time. However, it was only possible to solve for two of the three


parameters under two special cases: negligible ( _α_,n) contribution or a non-multiplying sample


( _M_ = 1). Using a more advanced technique, Multiplicity Counting, it is possible to solve for all


three unknowns. This technique is the subject of the following section.

### **2.2.3 Multiplicity Counting**


Multiplicity counting arose out of the need for accountability of fissile material in the nuclear fuel


cycle. The problem is that the fissile material recovered from spent fuel has a complex source term


driven by


1. _F_ _s_ : spontaneous fission rate


2. _S_ _α_ : ( _α, n_ ) neutron emission rate


3. _M_ _L_ : neutron leakage multiplication


The goal is to ultimately measure _F_ _s_, which in passive counting can be related back to plutonium


effective mass through empirically determined factors [8]. This still requires the knowledge of


plutonium isotopics, which can be measured with gamma ray spectroscopy. HEU mass can be


measured through active multiplicity counting, with a variation of the equations discussed in this


section [30]. _S_ _α_ and _M_ _L_ are complicating parameters whose contribution depends on isotopic


composition and total fissile mass and geometry.


Before multiplicity counting theory was developed in the early 1980s, it was possible to mea

sure _F_ _s_ through neutron coincidence counting by assuming that either _S_ _α_ or _M_ _L_ was negligi

ble [31] [32]. Multiplicity counting theory set out to relate the probability distribution, _r_ _m_ ( _τ_ ),


of counting _m_ number of neutron multiplets in time window _τ_ with the three source properties


21


enumerated above. The following four general assumptions underline the multiplicity counting


theory [33, 34]:


1. The test sample is taken to have no spacial extent (point geometry), and therefore parameters


such as the detector efficiency and the probability of fission are assumed to be spatially


uniform.


2. Neutron detection efficiency, probability of fission, and neutron multiplicity are assumed to


be energy independent. All physically associated quantities are in effect collapsed into a


single energy group. The neutron energy spectrum from ( _α, n_ ) reactions and spontaneous


fission are assumed to be the same.


3. The time response of the detector, or the neutron die-away time in the detector moderator,


follows a single exponential function with a characteristic decay constant _λ_ .


4. All induced fission neutrons are emitted simultaneously with the initiating ( _α, n_ ) or sponta

neous fission neutrons. This is often referred to as the “superfission" concept, and is valid if


the time response of the detector is much slower compared to the lifetime of a fission chain.


5. Neutron capture without fission is negligible, which means the probability of leakage is just


the complement of the fission probability ( _p_ _L_ = 1 _−_ _p_ _f_ ).


Early efforts led to rather complex expressions for the source parameters and required exten

sive numerical efforts. In particular, the probability distribution _P_ _ν_ ( _p_ _f_ ) of emitting _ν_ neutrons


from a fission cascade was computed using Monte Carlo [35]. This distribution depends on the


multiplicity distribution of neutrons _P_ _ν_ and the probability of a neutron inducing fission _p_ _f_, and is


the consequence of the superfission assumption and the need to account for neutron multiplication.


By taking the moments of _r_ _m_ ( _τ_ ) it is possible to use analytical approximations for the moments of


_P_ _ν_ ( _p_ _f_ ) which are accurate for a limited number of fissions in a cascade [36]. The approximation is


the result of summing the products of probabilities of neutron emission across multiple generations


until any additional contributions to _P_ _ν_ ( _p_ _f_ ) become negligible.


22


The real breakthrough came by using the mathematical tool of the Probability Generating Func

tion (PGF) and forming the _factorial_ moments of _r_ _m_ ( _τ_ ) into which the _P_ _ν_ ( _p_ _f_ ) distribution also


enters in the form of its factorial moments [37, 38]. Factorial moments of _r_ _m_ ( _τ_ ) are far less com

plicated and require less numerical effort to solve for requisite source term properties compared to


the moment formulations [39]. The _µ_ [th] factorial moment of the _P_ _ν_ ( _p_ _f_ ) distribution is



_ν_ ( _µ_ ) ( _p_ _f_ ) =



_∞_
�


_ν_ = _µ_



_ν_

_P_ _ν_ ( _p_ _f_ ) (2.20)

� _µ_ �



which can be expressed analytically as a function of the factorial moments of the neutron multi

plicity distribution for either induced, ¯ _ν_ _I_ ( _µ_ ), or spontaneous, _ν_ ¯ _s_ ( _µ_ ), fissions [34]. These are defined


as



_ν_ ¯ _j_ ( _µ_ ) = �


_µ_ = _ν_



_ν_

_P_ _jν_ (2.21)

� _µ_ �



where _j_ = _s_ or _j_ = _I_ for either spontaneous or induced fissions. Note that the first moment and


factorial moment of neutron multiplicity are equivalent ( _ν_ ¯ = ¯ _ν_ _j_ (1) ).


The single, _R_ 1, double, _R_ 2, and triple _R_ 3 count rates can be expressed in terms of the afore

mentioned factorial moments, detector efficiency ( _ϵ_ ) and desired sample source terms:


_R_ 1 = _ϵM_ _L_ ( _F_ _s_ _ν_ ¯ _s_ (1) + _S_ _α_ ) (2.22)



_ν_ ¯ _s_ (1) _ν_ ¯ _I_ (2)
� _ν_ ¯ _s_ (2) (¯ _ν_ _I_ (1) _−_ 1)



(2.23)
�



_R_ 2 = _ϵ_ [2] _F_ _s_ _M_ _L_ [2] _[ν]_ [¯] _[s]_ [(2)]


_R_ 3 = _ϵ_ [3] _F_ _s_ _M_ [3] _ν_ ¯ _s_ (3)



1 + ( _M_ _L_ _−_ 1) 1 + ¯ _S_ _α_
� � _ν_ _s_ (1) _F_ _s_



_ν_ ¯ _s_ (2) _ν_ ¯ _I_ (2)
1 + 2( _M_ _L_ _−_ 1) ¯ (2.24)
� _ν_ _s_ (3) (¯ _ν_ _I_ (1) _−_ 1)



_ν_ ¯ [2]
_I_ (2)
1 + 2( _M_ _L_ _−_ 1) ¯

� _ν_ _I_ (3) (¯ _ν_ _I_ (1) _−_ 1)



���



+( _M_ _L_ _−_ 1) 1 + ¯ _S_ _α_
� _ν_ _s_ (1) _F_ _s_



_ν_ ¯ _s_ (1) _ν_ ¯ _I_ (2)
� [�] _ν_ ¯ _s_ (3) (¯ _ν_ _I_ (1) _−_ 1)



These are idealized rates because they do not account for detector response time and method of


triggering, either on signal or randomly on gate of length _τ_ . The number of counts in those gates are


used to build signal _n_ _m_ ( _τ_ ) and random or background _b_ _m_ ( _τ_ ) distributions whose factorial moments


23


( _m_ _n_ ( _µ_ ) and _m_ _b_ ( _µ_ ) ) are then related back to the rates of correlated signal multiplets, _R_ _µ_, defined in


Eqs. 2.22, 2.23, and 2.24. It’s possible to formulate _R_ _µ_ only in term of _m_ _b_ ( _µ_ ), which under certain


conditions are equivalent to the factorial moments of the Feynman-Y distribution [40].


Cifarelli and Hage gave a comprehensive overview of possible solutions of source and detector


parameters in [34]. For the purposes of this background, it will suffice to give the case for the


absolute determination of _F_ _s_, _S_ _α_ and _M_ _L_ . First, _M_ _L_ is obtained from the smallest possible solution


( _M_ _L_ _>_ 1) of the following third order polynomial:


_a_ + _bM_ _L_ + _cM_ _L_ [2] [+] _[ dM]_ [ 3] _L_ [= 0] (2.25)


where


_a_ = _[R]_ [3] (2.26)

_ϵ_ [3]



(2.27)
�



_b_ = _[R]_ [2]

_ϵ_ [2]



� _νν_ ¯¯ _ss_ ((2)3) _−_ 2 _ν_ ¯ _I_ (1) _ν_ ¯ _I_ ( _−_ 2) 1



2 _R_ 2 _ν_ ¯ _I_ (2)
+ (2.28)
� _ϵ_ [2] (¯ _ν_ _I_ (1) _−_ 1)



_R_ 1
_c_ =
_ϵ_ (¯ _ν_ _I_ (1) _−_ 1)



_ν_ ¯ _I_ ( ¯ 2) _ν_ ¯ _s_ (3) _−_ _ν_ ¯ _I_ (3)
� _ν_ _s_ (2)



2 _R_ 2 _ν_ ¯ _I_ (2)
_d_ = (2.29)
_ϵ_ [2] (¯ _ν_ _I_ (1) _−_ 1) _[−]_ _[c]_


The spontaneous fission rate and ( _α, n_ ) neutron rate can then be solved in terms of _M_ _L_ :


_F_ _s_ = _R_ 2 _−_ _R_ 1 _ν_ ¯¯ _I_ (2) ( _M_ _L_ _−_ 1) (2.30)
_ϵ_ [2] _M_ _L_ [2] _[ν]_ [¯] _[s]_ [(2)] _ϵM_ _L_ _ν_ _s_ (2) (¯ _ν_ _I_ (1) _−_ 1)



_−_ _R_ 2 _ν_ ¯ _s_ (1)
(2.31)
_ϵ_ [2] _M_ [2]
� _L_ _[ν]_ [¯] _[s]_ [(2)]



_S_ _α_ = _ϵM_ _[R]_ [1] _L_



�1 + _[ν]_ [¯] _[s]_ _ν_ ¯ [(][1] _s_ [)] (2) _[ν]_ [¯] _[I]_ (¯ [(] _ν_ [2][)] _I_ [(] (1) _[M]_ _−_ _[L]_ _[ −]_ 1) [1][)]



Multiplicity counting is a mature and robust technique that is useful for assaying a wide array


of test samples with unknown contribution of ( _α, n_ ) neutrons. The typical assay bias is minimal


if the test sample is well represented by a point model [33]. However, the biggest drawback is the


need for both accurate knowledge of and large absolute detector efficiency. The former is needed


to keep uncertainties to a minimum and the latter is required for reasonable measurement times.


24


Both are a consequence of the _ϵ_ [3] term that is manifest in Eq. 2.24, which can become quite small.


As a consequence, multiplicity counters are typically large and are designed to surround the entire


test sample. If the value _S_ _α_ is known or negligible then other correlation counting methods can


yield more accurate results in a shorter measurement time [8, 33].

### **2.2.4 Correlating Particles with Fast Organic Scintillators.**


A single fission event releases multiple correlated neutrons and gamma rays, both of which can


both be measured with PSD capable organic scintillators. Unlike capture based systems, which


require fast neutrons to be slowed or “moderated" to lower energies where capture cross-sections


are high, organic scintillators can detect fast neutrons and gamma rays on a sub-nanosecond time


scale. This timing allows for resolution of the generation time between fissions in a chain. The PSD


capability enables the measurement of cross-correlation distributions of neutron-neutron, gamma

neutron, neutron-gamma, or gamma-gamma pairs from fission events in the same fission chain. In


addition, the mode of detection of fast neutrons in organics scintillators makes it possible to pre

serve some information about the incident neutron energy. This additional information allows for


an extension of gamma-neutron and neutron-gamma correlations into TCPH distributions which


are useful for characterizing fissile material [41–43]. The TCPH distribution is a bivariate his

togram of an estimated incident neutron energy and the time to a correlated gamma ray. TCPH


analysis is introduced in Section 2.2.5, but before proceeding it is important to explain the choice


of mixed particle correlation and the issues with neutron-neutron and gamma-gamma pairs.


Gamma-gamma and neutron-neutron pairs suffer from significantly more detector cross-talk:


when the same particle scatters between separate detector cells. These cross-talk events are char

acteristic of the detector system geometry, not the measured source itself. Additionally, in different


but correlated neutron-neutron pairs, both particles have a time-of-flight that depends on their re

spective energies, and thus the time between two correlated neutrons is spread, even for pairs


originating from the same fission.


By contrast, correlated gamma rays from the same fission should arrive at the detector simul

25


taneously. Therefore, any time spread between two detected gamma rays above that of timing


resolution can be attributed to fission chain smearing. However, correlated gamma-gamma pairs


have many terrestrial (e.g. K-40, Tl-208, Ra-226, Ac-228) and cosmic sources of uncorrelated


background that degrade the signal-to-noise of this signature. In addition to correlated fission


gamma rays, fissile material typically produces many more uncorrelated decay gamma rays from


fission products. Depending on the amount of material present, these uncorrelated gamma rays can


create an overwhelming rate of accidental coincidences.


Gamma rays are also highly attenuated by the emitting fissile material itself, because of the high


density and mass number. As a result of this self-shielding, detectors will be primarily sensitive


to gamma rays emitted from the outer layer of an assembly. It is therefore desirable to include at


least one neutron in the correlated pair to gain sensitivity to a larger fraction of the total volume of


material.


It can be reasonably concluded that correlated gamma-neutron and neutron-gamma pairs offer


the good sensitivity and signal-to-noise ratio. The gamma ray provides a clean indication of the


time of a fission, while the neutron is both more penetrating and a clear indication of fission. Cross


talk is also reduced by correlating particles of different type, rather than the same type.

### **2.2.5 Time Correlated Pulse Height**


The TCPH distribution is a bivariate histogram of the time difference between correlated neutrons


and gamma rays, and deposited neutron energy measured by the light output in the scintillator [44].


In a non-multiplying source, such as Cf-252, most correlated neutrons and gamma rays that are


detected within a short time window (10s of nanoseconds) by a fast system are generated from the


same fission event. Therefore, the arrival time of a neutron, which depends on neutron incident


energy, sets an upper limit on the light output achievable for that event.


The theoretical time between arrival of a gamma ray and a neutron from the same fission can


26


be determined from its energy:



_d_
_t_ =
~~�~~ 2 _E_



_d_

_−_ _[d]_
2 _E_ _n_ _/M_ _n_ _c_



(2.32)
_c_



where _d_, _E_ _n_, and _M_ _n_ are the source-to-detector distance, energy of the neutron, and its mass,


respectively. The _d/c_ term is used to compensate for the arrival time of the gamma ray. However,


in organic scintillators the kinematics of neutrons scatter on protons (hydrogen atoms), shown in


Figure 2.5, limit the proton recoil energy to at most the incident energy of the neutron ( _E_ _p_ _≤_ _E_ _n_ ).


Therefore, for a non-multiplying source, counts on the TCPH distribution will fall below this


theoretical time of arrival line described by Eq. 2.32, as shown in Figure 2.6(a).


But multiplying sources make it possible to correlate neutrons to gamma rays from earlier


fissions in a fission chain, which would make the time from the correlated gamma greater than


the time predicted by Eq. 2.32. Even with the lesser energy deposition from the proton recoil,


some counts would inevitably fall above this theoretical line of arrival. An example of the TCPH


distribution of a multiplying source, along with the theoretical line of arrival line from Eq. 2.32 is


shown in Figure 2.6(b).


Figure 2.5: Kinematics of neutron scatter on hydrogen nucleus (proton) which is the primary mode
of neutron detection in organic scintillators.


The utility of the TCPH distribution has been extensively studied with non-multiplying [252] Cf


[41], low-multiplying mixed oxide powder and plutonium-gallium disks [42], and highly enriched


uranium [45] measurements and simulations [43]. Simulations of the BeRP ball and the result

ing TCPH distributions demonstrated a correlation between multiplication and spreading in the


27


(b) Multiplying



(a) Non-multiplying







Figure 2.6: TCPH distributions for (a) non-multiplying and (b) multiplying sources with the theoretical line of arrival shown in red.


TCPH distribution [46]. In Chapter 4, the measured results are shown, along with a method for


quantifying the spread in the TCPH distribution.


Earlier efforts to characterize multiplication relied on counting the correlated events that fell


above the theoretical line of arrival, or estimating the gradient of counts above this line. But as


will be shown in Chapter 4, the TCPH distribution is actually spread in both time directions due to


presence of fissile material. The intermediate goal of this dissertation work was to determine other


additional physical quantities of interest that could be extracted by examining the full TCPH distri

bution. The analysis will progress in Chapter 5 to collapse the TCPH distribution into the TOFFEE


distribution, a simpler one-dimensional form which gives greater insight into the underlying fission


chain dynamics measured from gamma-neutron correlations.


28


## **CHAPTER 3**

# **Digital Pulse Processing**

## **3.1 Motivation**

The advent of fast Analog-to-Digital Converters (ADCs) has enabled the capture, storage and


offline processing of scintillator waveforms after they are acquired [47]. This has allowed us to


move beyond analog pulse-shaping techniques achieved through clever rearrangements of resistors


and capacitors. Many digital processing techniques have their analog equivalents (e.g. filtering)


[48], but digital processing also allows for any operation that a computer can do to a list of numbers.


Therefore, it is important to explain the choice of appropriate digital processing techniques used to


get the desired signature for time correlated analysis.


Three pieces of information are required about an interaction that gives rise to a pulse: time


of the interaction, energy deposited by interacting particle and the type of particle by pulse shape


discrimination (PSD). The challenge is to accurately extract that information when both the gamma


ray and neutron interaction are necessary for analysis. The following serves as an overview of some


of the available digital processing techniques applicable for pulses recorded from fast organic


scintillators coupled to PMTs. The goal is to provide a detection system agnostic reference to


processing methods required to replicate the results presented throughout this work.


29


## **3.2 Timing**

Three candidate methods were investigated for their ability to reliably provide gamma and neutron


interaction times: Derivative Zero Crossing (DZC), Constant Fraction Discrimination (CFD) and


Cumulative Integral Fraction (CIF). The DZC method is often referred as the constant fraction


discrimination method because it is how analog circuitry was used to find a constant fraction of a


pulse [49]. The original pulse is operated on by the following:



DZCPulse[ _k_ ] =
�



_L_
� _F ∗_ Pulse[ _k −_ _i_ ] _−_ Pulse[ _k −_ _i −_ _D_ ] (3.1)


_i_ =1



where a fraction _F_ of the original pulse is subtracted by a pulse delayed by _D_ . The time is then


found by looking for the zero crossing past the maximum as shown in Figure 3.1.







Figure 3.1: Example of a pulse and its derivative as calculated using the DZC method. The zero
crossing time, marked by the red dot, is interpolated starting the the maximum of the derivative.


When _D_ and _F_ are both unity, DZC method amounts to taking the derivative of the original


pulse, hence the naming convention adopted in this work. On the other hand the second method,


CFD, relies on an intuitive implementation of the name “constant fraction". The time is found by


interpolating the rising edge of the pulse up to some fraction of the pulse maximum. Finally, the


third method, CIF, finds the time at some fraction of the cumulative integral of the pulse, as shown


30


in Figure 3.2. Trapezoidal integration method was used to better approximate the true pulse’s


integral.







Figure 3.2: Example of a pulse and its cumulative integrals as calculated from the CIF method.
The fraction of the cumulative integral (10%) used for time-pick-off is marked by the red dot.


Testing timing performance can be accomplished with pair of equivalent detectors and a source


that emits coincident gamma rays. This setup allows for the measurement of the gamma-gamma


Time of Flight (TOF) distribution, the width of which is indicative of timing performance. The


spacial arrangement of the source and detectors is only important if it’s necessary to measure the


relative transit time of the PMTs coupled to each detector cell. In that case it’s necessary to have


the source be equal-distant to each detector. Each timing method has a fraction parameter, which


was optimized to give the lowest achievable standard deviation and Full Width Half Maximum


(FWHM) of the gamma-gamma TOF distribution. The delay was set to one ( _D_ = 1) for the DZC


method.


The optimized TOF spectra for all three methods are shown in Figure 3.3. The FWHM was


calculated via interpolation, and the standard deviation was taken from the entire set of ∆ _T_ s be

tween -10 ns and 10 ns. In this case the standard deviation can not be taken as an absolute measure


of detector system performance, since its value will change with the length of the time window.


Note that the TOF spectra are not Gaussian in shape and the FWHM is not directly proportional


31


to the standard deviation. Nevertheless, these two metrics were used to optimize the fractions for


each of the three methods. The optimized fractions for the DCZ and CFD methods were both at


50% and only 5% for the CIF method.











Figure 3.3: Gamma-gamma TOF spectra with optimized parameters for each of the three timing methods. The optimized fractions for the DCZ and CFD methods were both 50% and only
5% for the CIF method. The FWHMs, standard deviations and means are expressed in units of
nanoseconds


In general, lowering the fraction decreased both the standard deviation and FWHM. The lower


bound on the optimized fractions was dictated by the appearance symmetrical “resonance" peaks at


the sampling rate of the digitizer. Since a 500 MS/s CAEN DT5730 digitizer was used for testing,


those resonances peaks appeared at +2 ns and -2 ns intervals. Quantitatively the resonances would


increase the standard deviation while the FWHM would continue to decrease.


At this point it may seem reasonable to conclude that each method is equally suitable for timing


experiments. However, this dissertation primarily concerns mixed gamma-neutron correlations and


when each method is compared against measured gamma-neutron TOF spectra, as shown in Figure


3.4, the flaw with the CIF method is revealed. Because the CIF method is pulse shape dependent,


it will systematically over-estimate the arrival time of a neutron pulse as compared with a gamma


ray pulse.


The gamma-neutron TOF spectra also revealed a problem with the DZC method, which was


32


Figure 3.4: Gamma-neutron TOF spectra as calculated using the three timing methods. The data
was taken from a measurement of a Cf-252 source at 30 cm distance from the pair of detectors.


not apparent int the gamma-gamma TOF spectra in Figure 3.3. Given a sufficiently high fraction,


from Eq. 3.1, the resonances disappeared from the gamma-gamma TOF spectra, but persisted in the


gamma-neutron spectra. The remaining resonances were diminished significantly by increasing the


delay parameter _D_ from one to two. The results comparing both DZC and CFD against simulation


of the same Cf-252 source at 30 cm is shown in Figure 3.5. The chi-squared test statistics between


the expected simulation and the observed measured results were 99.42 for DZC and 98.79 for


CFD, and therefore neither method had the edge in matching simulation. Judging from this result,


and the similarity in features shown in Figure 3.3, these two methods are almost indistinguishable.


Furthermore, with an increased delay parameter, the spread of the gamma-gamma TOF standard


deviation of the DZC came into agreement with the TOF spectra of the CFD method.


In conclusion, the three timing methods tested have similar performance, but CIF is not suitable


for picking off timing from particles that result in different pulse shapes. The remaining two


methods, DZC and CFD, are indistinguishable once their respective parameters are optimized.


The CFD timing method was used for TCPH work in Chapter 4, and for DZC method was used


for all other work presented in this thesis.


33


Figure 3.5: Comparison of simulation and measurement data of a gamma-neutron TOF spectra
from a Cf-252 source at 30 cm from the detectors. The data was processed using two timing
methods, DZC and CFD, with fractions set to 50%.

## **3.3 Energy Calibration and Resolution**


For gamma ray spectroscopy the procedure for determining energy calibration and resolution typ

ically involves fitting known full energy photo-peaks to Gaussian functions. The means and stan

dard deviations of the fits are then used to determine the calibration and resolution of the system,


respectively. Unfortunately, physics disallows such full energy photo-peaks in spectra gathered


with organic scintillators due to the dominance of Compton scattering in low-Z materials, such as


organic scintillator. The only recognizable features are therefore Compton edges corresponding to


the maximum possible scattering angle:



�



_E_ _CE_ = _E_



1
1 _−_ 1 + 2 _E_

� _m_ _e_ _c_ [2]



(3.2)



where _E_ is the incident gamma-ray energy and _m_ _e_ is the resting mass of the electron. It is difficult


to determine this edge accurately, because it’s not clearly delineated on a pulse height spectrum


due to a finite energy resolution and the effects of multiple scattering interactions.


One approach for estimating the location of the Compton edge is to fix its location at some


34


fraction of the Compton edge peak. A more robust approach is to fit the measurement results


to a Monte Carlo simulation, with energy smearing term to account for energy resolution of the


detector [50]. The measured pulse heights (PH) are shifted by linear calibration formula


_L_ = _a ∗_ PH + _b_ (3.3)


where _L_ is the calibrated light output (in MeV) and _a_ and _b_ are calibration parameters. At the


same time the simulated results are broadened by the approximate energy resolution of the system


parameterized by



(3.4)
_L_ [2]



∆ _L_

_L_ [=]



~~�~~



_α_ [2] + _[β]_ [2]




[2]

_[γ]_ [2]
_L_ [+] _L_ [2]



where _α_, _β_ and _γ_ parameters include contributions from light transmission within detector cell,


statistical fluctuations of light production, and electronic noise, respectively [51].


The Levenberg-Marquardt algorithm was employed to find the optimum calibration and reso

lution parameters and an example of the results are shown in Figure 3.6. It is important to give


extra weight to the regions of the spectra around the Compton edges, and to ignore the back-scatter


peak, which is absent from the simulation due to lack of surrounding materials.


This spectrum matching technique is arguably more robust than using a fraction of the Compton


edge peak, because it incorporates the detector resolution parameters, any improvement over this


simpler method is probably marginal at best. In any case, the limiting factor is the relatively


poor energy resolution of organic scintillators. In addition, the spectrum matching approach is


complicated by the covariance between the energy calibration parameters in Eq. 3.3 and resolution


parameters in Eq. 3.4. An improvement on this approach would require an independent method


for measuring the resolution of the detector, such as the Compton coincidence technique [52].


35


Figure 3.6: Measured and simulated spectra of Na-22 source matched with optimum resolution
and calibration parameters.

## **3.4 Neutron Light Output**


The amount of light emitted from an interaction in a scintillator depends on the energy deposited


and the type of recoiling charged particle. For gamma rays these charged particles are electrons


and for neutrons they are predominantly protons (hydrogen nuclei). In many organic scintillators,


electrons provide a near-linear response at energies greater than 125 keV [53], which justifies


linear energy calibration used in Eq. 3.3. However, since the light output response from protons is


different than electrons, it is useful to refer to this electron light output in terms of MeV electron


equivalent (MeVee). This unit, introduced in Figure 3.6, provides an absolute measure of the light


output that is useful for characterizing light output caused by proton recoil in terms of its electron


equivalent energy.


There are two problems with neutron light output response that make it challenging. First, un

like the electron response the proton response is non-linear, which necessitates multiple calibration


points. Second, with exception of deuterium-deuterium ( 2.5 MeV) and deuterium-tritium ( 14.1


MeV) fusion neutron generators there is a lack of portable mono-energetic sources of neutrons. A


popular approach to characterize the neutron light output response is through time-tagged exper

iments; where the incident neutron energy can be segregated through time-of-flight [54–56]. For


36


organic scintillators, it’s common to fit the neutron response to an empirical exponential formula


first developed by Katz [57]:


_L_ ( _E_ _p_ ) = _aE_ _p_ _−_ _b_ [1 _−_ exp( _−cE_ _p_ _[d]_ [)]] _[.]_ (3.5)


The coefficients _a_, _b_, and _c_ are often reported in terms of units of MeVee/MeV, and _d_ is typically


assumed to be unity and is a dimensionless constant [54, 55, 58, 59], and provided that the calibra

tion methodology is the same, can be used universally for detectors of the same geometry and size.


The formulation in Eq. 3.5, and its inverse, will be used for analysis in Chapter 4.


A more physical insight into light output yield can be gained by relating the _dL/dx_, fluorescent


energy emitted per unit path length, and _dE/dx_, energy loss per unit path length for a specific


particle [60]. This relationship is commonly referred to as the Birks’ formula



_E_ _p_
_L_ ( _E_ _p_ ) = _S_
� 0



_p_

_dE_ 1 + _k_ _[dE]_
0 � _dx_



_dx_



_−_ 1

(3.6)
�



where _S_ is the normal scintillation efficiency and _k_ reflect the effect of quenching. The requisite


_dE/dx_ for electrons and protons in stilbene were calculated using SRIM software [61, 62], and


provided by personal correspondence by Mark Norsworthy [63]. Scintillation efficiency refers


to the fraction of incident particle energy that is converted to visible light, and is degraded by


quenching which is an umbrella term for all the de-excitation pathways that do not lead to emission


of light. Birks’ formula has been found to work better at lower thresholds ( _<_ 100 keV) than the


empirical function in Eq. 3.5 [63, 64], but it requires the knowledge of the stopping power of


charged particles for the material of interest. A comparison of the fit to the two formulations


for data obtained from solution grown 2" _×_ 2" stilbene [65] is shown in Figure 3.7. The neutron


light output yield for 2" stilbene crystals was measured by Bourne et al. in a separate set of


experiments [65]. Birks’ formula fit was used in this thesis for all the data acquired with and


simulations of 2" _×_ 2" stilbene.


37


Figure 3.7: A 2" _×_ 2" stilbene crystal neutron light output data fit to Birks’ and Katz’s formulations.
The Katz coefficients are _a_ = 0 _._ 505, _b_ = 1 _._ 072, _c_ = 0 _._ 446, and _d_ = 1, and the Birks coefficients
are _S_ = 1 _._ 63 and _k_ = 27 _._ 83.

## **3.5 Pulse Shape Discrimination**


In organic scintillators the fraction of light emitted during delayed fluorescence depends on the


exciting particle’s _dE/dx_, therefore it is possible to differentiate between neutron and gamma-ray


interactions through PSD. Segregating gamma ray and neutron pulses is a two step process. First,


the pulse shape is quantified into some singular quantity called the PSD parameter. Then the PSD


parameter is used to quantitatively separate neutron and gamma ray pulses, typically on an energy


dependent basis. It is the novel application of Bayes’ theorem to this second classification step that


was extensively used throughout this dissertation work to maximize the return on gamma rays and


neutrons. The details of the comparative performance of this method can be found in [66].

### **3.5.1 Pulse Shape Quantification**


The charge integration PSD method, in both analog and digital applications, relies on the ratio


of pulse tail to total integrals [67] as shown in Figure 3.8. This PSD parameter is widely used


in comparing PSD performance in organic scintillators [68–70]. An alternative approach used


38


in this work relies on taking the difference in time between fractions of the pulse integral. This


amounts to using the CIF method, shown in Figure 3.2, twice for two different fractions and taking


the difference of the results. This approach has the advantage of requiring only two parameters,


one less necessary for specifying the tail and total integration windows for the charge integration


method.













Figure 3.8: Example of tail and total integration windows used in the charge integration method.


There are other methods for quantifying PSD parameters [71], all of which provide a way


of clustering neutrons and gamma rays in a particular two dimensional space. Typically, one


dimension of this space is the PSD parameter, and the other is some metric of energy deposition


such as pulse height or pulse integral. The two clusters of gamma rays and neutrons can be cleaved


with a decision boundary, which provides a binary classification of each pulse. The following


section demonstrates an alternative Bayesian approach, which gives confidence probabilities on an


event-by-event basis. This allows for re-adjustment of the PSD “cut" by adjusting the minimum


allowed probabilities in post-processing.


39


### **3.5.2 Bayesian Classification Methodology**

Applying Bayes’ theorem requires a conditional probability, or likelihood, and a prior probability.


In this method, the former is defined as the value of an energy dependent Gaussian fit for a given


tail-to-total ratio and the latter as the energy dependent gamma-to-neutron ratio. The discussion on


estimating both parameters proceeds in the following two sections. Initially, the prior probability


is not known and thus it must be inferred from the data by an iterative procedure. Therefore, the


Bayesian probability is adaptive to a particular collection of data.


The Bayesian method and an experimental study of its performance relative to a decision


boundary technique have been previously published in [66]. The following overview demonstrates


the method only, which was used throughout the work in this thesis to classify neutron and gamma

ray pulses. Appendix A.2 includes the source code that employs the Bayesian method for PSD.


**3.5.2.1** **Fitting detector specific parameters**


The first step is to determine the detector specific parameters, the means and standard deviations,


from a double Gaussian fit to the PSD parameters. This step should preferably be accomplished


on a data-set with nearly equal gamma ray and neutron populations. These parameters are energy


dependent, therefore the data has to be binned into specific light output groups. The groups have


to be narrow enough to capture the changing means and standard deviations, but wide enough to


include statistically significant number of counts to perform an accurate fit. The number of counts


decreases with increasing light output, but fortunately the variations in the means and standard


deviations also decrease with increasing light output, as is shown in Figure 3.9, and therefore can


accommodate larger light output bin widths. These parameters are only system dependent, and


like gain calibration procedures, only need to be performed once for a particular experiment.


Each binned group of PSD parameters was fit in descending order of light output, with the


previously calculated coefficients used as the next initial guess. This ensured continuity of the


coefficients across all groups, and facilitated the precarious fitting at lower light outputs where dis

tributions overlap the most. The Gaussian distributions were normalized and took on the familiar


40


form:


where _s_ is the PSD parameter.



_−_ [(] _[s][ −]_ _[µ]_ [)] [2]
2 _π_ [exp] � 2 _σ_ [2]



(3.7)
�



1
_f_ ( _s_ ) =
_σ_ ~~_√_~~



2 _σ_ [2]



In order to calculate the Bayesian probability for each pulse individually, the Gaussian coeffi

cients were fit across the light output range of interest. Smoothing splines were used to approximate


the mean and standard deviation coefficients as a function of light output. The resulting R-squared


values were greater than 0.99 for all fitted parameters. The result of the fitting procedure is shown


in Figure 3.9, as applied to a subset of data collected with an Am-Be source. The details of the ex

perimental setup are given in [66]. Conditional probabilities for the Bayesian formula were taken


from these fits.


Figure 3.9: The mean (solid lines) and three standard deviation (dashed lines) fits as applied to the
Am-Be data set.


By fixing the mean and standard deviation parameters from a calibration data set, the assump

tion is that they only depend on the detector system, and therefore do not need to be refitted for


other measurements.


41


**3.5.2.2** **Inferring the gamma-to-neutron ratio**


The Gaussian fits provide the conditional probabilities, but a prior is required in order to calcu

late a gamma-ray or neutron posterior probability. In this case the prior is the energy dependent


ratio of gammas-to-neutrons, which will change depending on the incident radiation (i.e. the type


of radiation source measured). Therefore, an iterative procedure is introduced that updates the


gamma-to-neutron ratio by recalculating posterior probabilities until a convergence criteria in the


gamma-ray and neutron populations is met.


The following formulation of the Bayes’ theorem was used for calculating posterior probabili

ties for either gamma rays


_f_ _γ_ ( _s_ ) _R_ _γ/n_
_P_ ( _γ|s_ ) = (3.8)
_f_ _γ_ ( _s_ ) _R_ _γ/n_ + _f_ _n_ ( _s_ )


or neutrons


_f_ _n_ ( _s_ )
_P_ ( _n|s_ ) = (3.9)
_f_ _γ_ ( _s_ ) _R_ _γ/n_ + _f_ _n_ ( _s_ )


where _f_ ( _s_ ) are the Gaussian fits from Eq. 3.7, the _γ_ or _n_ index indicates the gamma-ray and


neutron distribution and _s_ is the PSD parameter. _R_ _γ/n_ is the ratio of the estimated number of


counts in the gamma-ray and neutron distributions within a light output group. The number of


instances of gamma rays and neutrons is estimated by summing the posterior probabilities of each


class


_N_ _γ_ = � _P_ ( _γ|s_ ) (3.10)

_s∈E_ _i_



for a particular light output group _E_ _i_ .



_N_ _n_ = � _P_ ( _n|s_ ) (3.11)

_s∈E_ _i_


42


For the first iteration _R_ _γ/n_ is assumed to be unity, then the results from Eqs. 3.8 and 3.9 are


used to estimate its value for the subsequent iteration:


_R_ _γ/n_ = _[N]_ _[γ]_ _._ (3.12)

_N_ _n_


The iterative approach used is an example of an expectation-maximization algorithm for Gaus

sian mixtures [72] with fixed means and standard deviations. Iterations terminate when the conver

gence criteria is satisfied. Convergence criteria was defined as 1% difference in total _R_ _γ/n_ between


two consecutive iterations. This iterative scheme is robust, and converges to the same solution


given a wide range of initial _R_ _γ/n_ . The final result are posterior probabilities, as shown in Figure


3.10, which can be used to adaptively classify pulses.


Figure 3.10: The distribution of neutron posterior probabilities for 1:1 mixture of [60] Co and time
tagged neutron data.


**3.5.2.3** **Variance estimation**


Since the sum of probabilities, not counts, is used to estimate the size of gamma-ray and neutron


populations, a different formulation from counting statistics is required to account for the uncer

tainty of the posterior probability itself. In this work the variance on the total number of estimated


43


instances _N_ was calculated by


_V ar_ ( _N_ ) = � _P_ _i_ + � _P_ _i_ (1 _−_ _P_ _i_ ) (3.13)


where _P_ _i_ are either gamma ray or neutron posterior probabilities for each pulse. _N_ represents the


number of gamma ray or neutron instances as calculated by Eqs. 3.10 and 3.11. The first term


in Eq. 3.13 sums to _N_ and represents the variance on the total number of counts. The second


term is the variance on each individual probability, which follows a binomial distribution because


there are only two classes, gamma rays and neutrons. In the limit that all the _P_ _i_ are large, the


variance estimation reduces to _N_ . On the other hand, if _P_ _i_ are small, then the variance estimation


is effectively doubled to 2 _N_ .


44


## **CHAPTER 4**

# **Time Correlated Pulse Height Distributions**

## **4.1 Motivation**

The details of the TCPH distribution and its relation to characterizing fissile material were intro

duced in Section 2.2.5. The analysis pioneered by Miller et al. focused on the counts that lay above


the theoretical line of arrival. This stemmed from the observation that in the presence of fission


chain neutrons from later generation events could be correlated with earlier gamma rays, hence


increasing the time between the two correlated events [42]. This misses the corollary observation,


which is that neutrons from earlier fission events can be correlated with later generated gamma


rays. Therefore, the time of arrival is either shorter or longer depending on the order of the gener

ation along the fission chain of the correlated gamma-neutron pair. In a multiplying assembly of


fissile material this effect manifests itself as a spreading or smearing of the TCPH distribution, not


just increased counts above the theoretical line of arrival.


To characterize this behavior, a new method had to be developed to quantify the smearing of the


whole TCPH distribution. The method and experimental results were first published in [73], and


this Chapter summarizes that approach and results. The underlying assumption of the method is


that the smearing is caused by the time distribution of fission events within a chain. The approach in


this Chapter uses the Gamma function as an empirical approximation for this smearing distribution.


The goal is to fit empirical parameters of the Gamma function that correlate with the underlying


fission chain timing distribution. These empirically fit parameters were found to correlate with


45


multiplication, shielding material types and source-to-detector distance. They provided another


handle on the characterization of fissile material that would be useful in warhead dismantlement


confirmation, where knowledge of the presence of the coupled material might be useful to confirm


that surrounding moderating material has been removed. The application of a variation of the


TCPH distribution for treaty verification is explored in Chapter 5.

## **4.2 Analytical Model**


In order to access the fission chain timing distribution, a model was constructed of TCPH dis

tributions for multiplying sources. The model consists of a linear combination of the expected


distribution for gamma-neutron pairs that are correlated by the same-fission and those correlated


by different fissions within the same chain.


The “same-fission" distribution is determined by a combination of the detector response to fis

sion spectrum neutrons (Watt) and the time delay expected for the source-to-detector distance. The


detector response matrix was simulated using MCNPX-Polimi [74]. Pu-239 fission Watt spectrum


was assumed for energies of incident neutrons and Katz’s formula, from 3.5, was used for the light


output function [55]. The simulated neutron response matrix and the resulting same-fission TCPH


distribution are shown in Figure 4.1


The different-fission distribution includes additional time smearing due to the time difference


between any two fissions within a chain. A physical model of the fission chain process is outside


the scope of this Chapter, it will be introduced in Chapter 6. Therefore, the Gamma function was


used as an empirical substitute for the physical model of the time distribution of fission events in a


chain.


The probability density function of a Gamma distributed random variable is


1
_f_ ( _x_ ) = (4.1)
Γ( _α_ ) _θ_ _[α]_ _[x]_ _[α][−]_ [1] _[e]_ _[−][x/θ]_


46


(b) TCPH Distribution
(a) Response Matrix


Figure 4.1: Simulated EJ-309 neutron response matrix and the resulting TCPH distribution with
assumed [239] Pu Watt neutron energy spectrum and source-to-detector distance of 50 cm. Each
distribution is normalized to unity and displayed on a logarithmic scale.


where _α_ is the shape parameter and _θ_ is the rate parameter. Two properties of the Gamma func

tion make it a plausible representation for the distribution of times between fission events. First,


the Gamma function describes the waiting times until the _α_ _[th]_ Poisson distributed event. Second,


the sum of independent Gamma distributed events follow a Gamma function. The independence


condition is not true for events in a fission chain; however, it can be empirically demonstrated


that the time distribution between fission events roughly follows a Gamma function by compar

ing MCNPX-PoliMi simulations. The simulated distribution of time differences between fission


events in a bare BeRP sphere and corresponding Gamma function fits are shown in Figure 4.2.


Although the time distribution between a set number of fission events follow a Gamma function,


with coefficient of determination (R [2] ) between 0.930 and 0.949, the fit for all possible fission com

binations has R [2] of 0.997. The Gamma function fits systematically undershoot the peaks of the


time difference distributions from simulation, because those distributions are generally narrower.


The smaller variance in those time differences from simulation is due in part to the fact that fission


events in a chain are correlated. The other phenomena not captured by the Gamma function is


branching of a fission chain, which makes it possible for fission events in different generations to


47


be closer in time than expected from a straight linear succession of fissions in a chain.


Figure 4.2: Distribution of time differences for various n _[th]_ -nearest-neighbor fission events is represented by each colored line, with the black line showing the distribution between all fission events
in a chain. The distributions were obtained from an MCNPX-PoliMi simulation of bare BeRP ball

(stairs) and then normalized to unity and fit by Gamma functions (solid lines).


Finally, the TCPH distribution for a multiplying source is constructed using a linear combina

tion of the non-multiplying TCPH distribution, as shown in Figure 4.1(b), and a TCPH distribution


smeared by the Gamma function. The smearing is accomplished by setting each bin on the TCPH


distribution equal to the sum of neighboring bins along the time axis, with a weight given by the


Gamma function for the time delay between bins. Included in the sum is the contribution of the


original same fission bin weighted by factor _n_ .


The factor _n_ represents the fraction of correlated pairs from like fissions over all fission and in


theory should be proportional to the length of fission chain _L_ :


_n ∝_ _[L]_ _L_ _._ (4.2)
~~�~~ 2 ~~�~~


By definition the average length of the fission chain is related to the sub-critical multiplication


from Eq. 2.9 such that _M_ = ( _L_ [¯] _−_ 1).


48


A conditional statement is added to the Gamma function to account for _n_ :



_F_ ( _x|α, θ, n_ ) =














_f_ ( _x|α, θ_ ) if x _>_ 0



(4.3)

_n_ otherwise.



where _f_ ( _x_ ) is defined in Eq. 4.1. The smeared TCPH distribution is calculated by


_**M**_ = _**N**_ _× F_ ( _**A**_ ) (4.4)


where _**N**_ is a pulse height by time matrix of the same-fission TCPH distribution. The matrix _**A**_


is a symmetric Toeplitz matrix with the first row defined as the cumulative difference between the


times in the TCPH distribution _**N**_ . In this case, the function _F_ performs a point-wise operation on


values in matrix _**A**_ .


The resulting TCPH distribution _**M**_ depends on _α_, _θ_ and _n_ which define how the distribution


is smeared, and the distance from the detector which shifts the non-multiplying TCPH distribution


_**N**_ . If the distance is known it can be fixed, otherwise it can be included as a free parameter with the


other three parameters. To solve for the parameters, the loss function is defined as the root-mean

square error (RMSE) between the modeled TCPH distribution _**M**_ and a measured distribution.


This function is then minimized by employing an unconstrained non-linear optimization method


based upon the Nelder-Mead simplex algorithm [75, 76].


The parameters of interest are solved in three steps. In the first and the final third step all four


parameters are optimized, and in the intermediate second step the source-to-detector distance is


fixed. In between the steps the initial guesses are changed to the previous solutions. The Nelder

Mead simplex algorithm works best with fewer parameters, therefore by reducing their number in


the middle step the Gamma function parameters could be further optimized. The distance parame

ter was fixed because it proved to be the most well constrained with the smallest relative covariance


with respect to the other parameters.


49


## **4.3 Experimental Setup**

A series of measurements of the BeRP [77] ball were conducted at the Nevada National Security


Site (NNSS) to acquire data to assess TCPH distribution analysis for highly multiplying assemblies


of fissile material. The BeRP ball is a 4.5 kg sphere of _α_ -phase WGPu metal, original manufactured


in October 1980 by Los Alamos National Laboratory [77]. To explore a range of multiplications


with different levels of moderation and reflection, five configurations were measured: bare, 1.27


cm and 2.54 cm thick close fitting shells of tungsten, and 2.54 cm and 7.62 cm thick close fitting


shells of high density polyethylene (HDPE). The measurement times for each configuration were


5515, 3600, 8999, 3600, and 2509 seconds, respectively.


Data were collected using four 7.62 _×_ 7.62 cm cylindrical EJ-309 liquid scintillation detectors.


The source-to-detector distances were measured from the center of the BeRP ball. Most configu

rations were measured at 50 cm distances with the exception of 2.54 cm tungsten and polyethylene


measured at 48 and 60 cm, respectively. A diagram of the experimental setup, taken from an


MCNPX-PoliMi model, is shown in Figure 4.3. Anode outputs from 7.62 cm Electron Tubes


photomultiplier tubes (PMTs) coupled to each cell were digitized using CAEN DT5720 digitizer,


capable of 12-bit (nominal) resolution and 250 MHz sampling rate. All data processing was per

formed off-line after the measurements, and a 0.2 MeVee (MeV electron-equivalent), equivalent to


neutron energy of 1.2 MeV, threshold was applied in post-processing.

## **4.4 Measurement Results**


A subset of the measured TCPH distributions and corresponding optimized models built from


best-fit parameters are shown in Figure 4.4. The same-fission TCPH distribution, shown in Figure


4.1(b), is smeared to produce TCPH distributions shown in subfigures (b), (d) and (f) of Figure 4.4.


The smearing parameters are optimized in order to match the measured TCPH distribution shown


in subfigures (a), (c) and (e) of Figure 4.4.


The optimized Gamma function parameters and factors of _n_ are shown in Table 4.1. It is


50


Figure 4.3: Diagram of the experimental setup of the BeRP ball surrounded by four EJ-309 detectors. The detectors were spaced approximately 8.5 _[◦]_ apart.


expected that the parameter _n_ would decrease with increasing sub-critical multiplication given


its relationship to fission chain length in Eq. 4.2. This trend is apparent within each shielding


material configuration, but is not present between them. Furthermore, the relative uncertainty in


this parameter is over five times greater than the others, which limits its predictive capability.


The shape parameter, _α_, clearly demarcates the differences between the polyethylene modera

tor and tungsten reflector. Although _α_ has no obvious physical interpretation when its a non-integer


less than 1, it is valuable that it can distinguish between intervening material type independently


of multiplication.


It is also expected that the rate parameter, _θ_, would increase with multiplication because it


is proportional to the degree of smearing of the TCPH distribution. The corollary to this is the


measure of the gradient of the TCPH distribution found in [42]. This positive correlation is only


apparent for the tungsten case, and is actually negative for the polyethylene. The negative correla

51


tion in polyethylene was unexpected, but the difference in source-to-detector distances between the


two polyethylene measurements could be a factor. The greater distance increases the time between


correlated gamma rays and neutrons, and therefore somewhat smears out the TCPH distribution.


However, this effect is incorporated into the analytical TCPH model that is used for fitting. The


other factor to consider is that the two polyethylene measurements were performed on different


experimental campaigns. The source-to-detector distance is the only noted difference between the


two measurements, but that does not exclude any other systematic differences that could arise from


setting up measurements on different days. In Section 4.5 it is shown that for simulated polyethy

lene cases the rate parameter is positively correlated with multiplication, as expected.


Table 4.1: Optimized Gamma function parameters for the five measured configurations of the
BeRP sphere with standard errors of 1 standard deviation shown [73].

|case|α θ n Multiplication|
|---|---|
|bare<br>1.27 cm W<br>2.54 cm W<br>2.54 cm HDPE<br>7.62 cm HDPE|0.57_ ±_ 0.04<br>12.41_ ±_ 0.62<br>0.08_ ±_ 0.03<br>4.429_ ±_ 0.002<br>0.87_ ±_ 0.04<br>14.91_ ±_ 0.63<br>0.11_ ±_ 0.03<br>6.447_ ±_ 0.004<br>0.90_ ±_ 0.02<br>19.67_ ±_ 0.53<br>0.06_ ±_ 0.01<br>8.752_ ±_ 0.006<br>0.48_ ±_ 0.03<br>26.74_ ±_ 1.38<br>0.08_ ±_ 0.03<br>7.743_ ±_ 0.005<br>0.53_ ±_ 0.03<br>22.54_ ±_ 0.91<br>0.07_ ±_ 0.02<br>20.3_ ±_ 0.2|



The optimized source-to detector distances are shown in Table 4.2. Multiplication values were


calculated from MCNP5 simulations of each configuration [7]. In all cases the optimized distance


was smaller than the measured distance, with the greatest discrepancy present in the thicker tung

sten case. This suggests that this effect may be due to self-shielding; correlated particles from


fission events closer to the surface of the BeRP ball on the side of the detectors are more likely to


be detected. Therefore, any additional high-Z material would preferentially favor gamma rays born


at the surface of the BeRP ball, which would decrease the optimized source-to-detector distance.


This effect is seen in simulation, where the source-to-detector distance decreases significantly for


increasing tungsten reflector thickness but remains only slightly altered for low-Z polyethylene


moderator.


52


Table 4.2: Optimized distances for the five measured configurations of the BeRP sphere with
standard errors of 1 standard deviation. The measured distance was measured from the center of

the BeRP ball to the face of the detectors.

|case|optimized distance (cm) measured distance (cm)|
|---|---|
|bare<br>1.27 cm W<br>2.54 cm W<br>2.54 cm HDPE<br>7.62 cm HDPE|49.02_ ±_ 0.06<br>50_ ±_ 0.5<br>49.04_ ±_ 0.12<br>50_ ±_ 0.5<br>44.75_ ±_ 0.11<br>48_ ±_ 0.5<br>59.72_ ±_ 0.09<br>60_ ±_ 0.5<br>49.25_ ±_ 0.09<br>50_ ±_ 0.5|



53


(a) Bare measured (b) Bare model


(c) 2.54 cm W measured (d) 2.54 cm W model


(e) 7.62 cm HDPE measured (f) 7.62 cm HDPE model


Figure 4.4: Measured TCPH distributions (left) and corresponding models with parameters from
the minimization algorithm (right) for various BeRP ball configurations.


54


## **4.5 Simulation Results**

MCNPX-PoliMi simulations with shielding configurations of 1.27-7.62 cm for polyethylene and


1.27-7.62 cm for tungsten in 1.27 cm intervals were simulated to better illustrate the trends in the


TCPH distribution. The optimization results of the shape and rate parameter for both simulations


and measurement are shown in Figure 4.5, with multiplication proportional to the area of each


marker.


The standard errors were taken from a covariance matrix of the best-fit parameters derived


from a numerical estimation of the Jacobian. There are considerable absolute differences between


measurement and simulation, but the general trends remain the same with the notable exception of


the aforementioned measured polyethylene cases. The simulations reveal that it would be possible


to measure the relative change in multiplication, independently of the change of surrounding mod

erator for a reflector or vice versa. The main driver in the size of the relative standard errors was


the number of total correlated gamma-neutron pairs. This is most apparent for the thick tungsten


cases which effectively shield the vast majority of fission gamma rays.


1.0


0.9



0.8


0.7


0.6


0.5


0.4





0.3

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
||||||||||||||
||||||||||||||
|||||||||Bare<br>~~Tung~~|Bare<br>~~Tung~~|~~sten~~|||
|||||||||Polye<br>|Polye<br>|thylen<br>|e<br>||
|||||||||~~Meas~~<br>Simul|~~Meas~~<br>Simul|~~urem~~<br>ations|~~nts~~<br>||
||||||||||||||
||||||||||||||
||||||||||||||


0 10 20 30 40 50 60 70 80 90
θ ~~-~~ rate parameter



Figure 4.5: Optimized shape and rate parameters for both simulation (blue) and measurement (red)
cases. The shielding configurations varied in thickness from 1.27-7.62 cm with 1.27 cm intervals.
The increase in symbol size corresponded to an increase in multiplication, which is proportional
to the area of each marker. Note that the bare configurations are furthest to the left for both
measurements and simulations.


55


## **4.6 Conclusions**

This Chapter introduced a new approach for the characterization of SNM based on a signature


of temporally correlated gamma rays and neutrons. The approach was to fit the empirical ap

proximation of the timing distribution between fissions in a fission chain to the measured TCPH


distribution. It was shown that for the BeRP ball these empirical parameters correlate with both


multiplication and the type of material (e.g. low-Z moderator or high-Z reflector) coupled to the


fissile assembly. This property makes this method a candidate for treaty verification applications,


where confidence in warhead dismantlement is the objective. In this case warhead dismantlement


would involve the removal of high explosives, which is a form of moderating material, from the


fissile material of a warhead. The reliance on a signature that is unique to SNM makes it more dif

ficult to spoof dismantlement of fissile material. Furthermore, the signature used can be captured


with a portable set of fast organic scintillators which could be carried by an inspector.


Though the Gamma function was shown to reproduce the measured TCPH distributions in bare


fissile assemblies, as increasing amounts of reflector were added, it became a less relevant proxy for


the complete effect of the fission chain dynamics. Despite this, the rate parameter of the optimized


Gamma function correlated positively with multiplication. Simulation results revealed this trend,


but it was not shown to be the case for the measured polyethylene cases. This multiplication-rate


parameter relationship followed a different trend-line for moderated and reflected systems; which


were easily identified by the shape parameter.


For this work, an empirical model was utilized to identify general trends in the fissile assem

blies. However, if this were replaced by a physical model of the timing distribution of fissions


within fission chains, then it may be possible to further improve the available information present


in this signature. Furthermore, the TCPH distribution is a representation of the raw signatures:


time between correlated neutrons and gamma rays, and the energy deposited by the incident neu

tron. The underlying signature that captures the fission chain dynamics is missed in this form. In


the subsequent Chapters these raw signatures will be transformed into more physically meaningful


and easier to work with 1D TOFFEE distribution.


56


## **CHAPTER 5**

# **Time of Flight Fixed by Energy Estimation**

## **5.1 Motivation**

In Chapter 4 it was shown that the TCPH distribution is sensitive to the change in multiplication that


arises from the presence of reflector/moderator around fissile material. This signature is unique to


fissile material as it relies on underlying fission chain dynamics. Furthermore, it can be measured


with a relatively small detection system that can be made to be portable. These attributes make this


signature and analysis a useful choice for applications such as treaty verification, where the claim


of warhead dismantlement and initial warhead count has to be certified.


However, the TCPH distribution is essentially the raw representation of gathered recorded times


between correlated gammas and neutrons, and the corresponding light output from the neutron in

teraction. Comparing changes in this 2D distribution is made difficult by the lower statistics per


bin, as compared to a 1D distribution with the same number of total counts. Therefore, it would


be advantageous for both comparative and quantitative analysis to reduce the dimensionality of the


measured distribution while still using the information gained from the light output of the neutron


interaction. This goal was accomplished by using a new Time-Of-Flight Fixed by Energy Estima

tion (TOFFEE) distribution. The derivation of this new TOFFEE distribution, and its application


as a template analysis for potential application to treaty verification is discussed in this Chapter.


The application of TOFFEE for treaty verification was first presented at the 57 _[th]_ annual Institute


of Nuclear Materials Management conference [78].


57


## **5.2 TOFFEE Definition**

TOFFEE is the measured time between correlated gamma rays and neutrons adjusted by the ex

pected TOF of the neutron and gamma ray from the point of emission to the detector. The incident


neutron energy, _E_ _n_, is estimated by the energy deposited in the detector as determined by the elas

tic scatter on a proton, _E_ _p_ . Because the neutron typically deposits only a fraction of its energy in


this interaction, this estimated energy will be systematically low and thus the estimated neutron


TOF will be systematically too large. With a known source-to-detector distance _d_, it is possible to


estimate the travel time difference between a neutron and gamma ray emitted simultaneously:



_t_ _p_ = _d_ 2 ~~_m_~~ _E_ _n_
� ~~�~~



~~_m_~~ _n_

_−_ [1]
2 _E_ _c_
_p_



_c_



(5.1)
�



where _c_ is the speed of light and _m_ _n_ is neutron’s mass. The calculated quantity _t_ _p_ is therefore


the estimated difference in neutron and gamma-ray time of flight difference from the proton recoil


energy. Since _E_ _p_ is systematically smaller than the true incident neutron energy, _t_ _p_ will overes

timate the true time of flight difference between the neutron and gamma ray. Finally, the "fixed"


in TOFFEE refers to subtracting this quantity from the measured time between a gamma ray and


neutron pair, _t_ _n,γ_ .


For non-multiplying sources (e.g. spontaneous fission or ( _α_, n)), the actual travel time differ

ence between a gamma ray and a neutron, _T_ _n,γ_, will equal the measured _t_ _n,γ_, as shown in Figure


5.1(a). Therefore, TOFFEE for non-multiplying sources will be less than or equal to zero


_t_ _n,γ_ _−_ _t_ _p_ _≤_ 0 _._ (5.2)


In contrast, for multiplying sources the measured time difference between correlated gamma rays


and neutrons will include the difference in generation time, ∆ _T_ _g_, as shown in Figures 5.1 (b) and


(c). As a result, TOFFEE for sources with fission chains will be less than or equal to the times


58


between fission events that emitted each particle


_t_ _n,γ_ _−_ _t_ _p_ _≤_ ∆ _T_ _g_ _._ (5.3)


There are three important implications from Eqs. 5.2 and 5.3 on the relationship between


TOFFEE and the type of source measured. First, there is a sharp distinction between non-multiplying


and multiplying sources because the former should have a steep drop in counts on the positive side


of the TOFFEE distribution. The TOFFEE distribution of a multiplying source will, in contrast,


be “smeared" in both negative and positive time directions by ∆ _T_ _g_ . The bi-directional smearing is


exemplified in Figures 5.1 (b) and (c), and is the consequence of correlating gamma-neutron pairs


where either the gamma ray or the neutron were born first.


Second, the TOFFEE distribution is sensitive to the level of neutron multiplication, _M_, in fis

sile material, given in Eq. 2.9. Neutron multiplication is defined as the average number of neutrons


produced per starting neutron or the average length of a fission chain [16]. The probability of de

tecting particles from the same fission grows linearly with _M_, which will be distributed according


to Eq. 5.2. Whereas, the probability of detecting particles from different fissions in a chain in

creases factorially with _M_ and will be distributed according to Eq. 5.3. The contributions of the


particles correlated in the same generation and different generation from a simulation of the bare


BeRP ball is shown in Figure 5.2. In this example, generations are used to distinguish correlated


events, because MCNPX-PoliMi output provides the generation number of a fission that originated


a detected particle, but not a unique identifier of the fission event itself. Multiple fissions can be

long to the same generation, because of branching in a fission chain, therefore this example is an


approximation to TOFFEE distributions from same and different fissions. As a consequence, the


same generation TOFFEE distribution, shown in Figure 5.2, will sometimes include the time be

tween fissions of the same generation and will therefore also include a ∆ _T_ _g_ smearing term. The


different generation TOFFEE distribution is not only smeared out due to the addition ∆ _T_ _g_, but also


has noticeably more counts due to the greater probability of detecting particles that are correlated


59


(a) Non-multiplying


(b) Multiplying, gamma ray born first (c) Multiplying, neutron born first


Figure 5.1: Space-time diagrams of gamma ray (green) and neutron (red) particle paths from birth
to detection (dashed blue line). The (a) non-multiplying diagram depicts the simultaneous birth
of particles, and the (b) and (c) multiplying diagrams depict a fission chain where each fission is
separated by generation time ∆ _T_ _g_ . The measured time-of-flight difference, _t_ _n,γ_, is equivalent to the
true time-of-flight difference _T_ _n,γ_ in the non-multiplying case, but it includes the generation time
in the multiplying case. The dashed red lines depict possible estimates of the neutron’s velocity
from proton recoil. The end-points of those dashed lines on the time-axis at the assumed source
distance make up the TOFFEE distribution.


from separate fission events.


Finally, the influence of ∆ _T_ _g_, as shown in Eq. 5.3, means that the TOFFEE distribution is


simultaneously a measure of the length of a fission chain and the timing distribution of fissions


60


|Same Generation<br>Different Generation|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|20<br>10<br>0<br>10<br>20<br><br>TOFFEE (ns)|3|0||||40||5|



Figure 5.2: TOFFEE distributions of simulation of the BeRP ball constructed from gammas and
neutrons originating from the same generation and different generations of fissions. There are
more correlations from different generations due to neutron multiplication of the BeRP ball ( _M_ =
4 _._ 389 _±_ 0 _._ 005).


within that chain. The characteristic time between fission events in a chain is indicative of the


probability of fission, and the average neutron energy between fissions. In addition, for assemblies


that are coupled to a reflector, the time between fission events also depends on the probability and


delay time for a neutron to return to the fissile material.

## **5.3 Template Approach for Treaty Verification**


Treaty verification is a process under which States party to a particular treaty validate each other’s


compliance through mutual monitoring. The objective of treaty verification is to establish trust and


confidence that treaty obligations are not being violated. Any effective monitoring system should


be sensitive enough to reliably verify compliance. However, for nuclear dismantlement and arms


control treaties there is also the desire that sensitive information is not divulged through collected


data [79]. Therefore, proper information barriers (IB) should be incorporated into measurement


systems while maintaining the system’s reliability. Templating is often presented as a methodology


that offers a natural sequestration of sensitive information; all sensitive information used to confirm


61


an object is contained in a template which is protected by an information barrier [80].


Generally, a template based approach involves measuring a unique signature of a trusted object


to build an identifying template. This measurement is then repeated on a tested object and the


measured signature is compared against the previously acquired template in order to verify the


object’s identity [81]. A diagram of the procedure is shown in Figure 5.3. Because this technique


relies on any deviation in measured signature, and not the absolute value of thereof, determination


on object’s authenticity can be made relatively quickly and with high confidence. Additionally,


any potential sensitive information is carried with the template itself which naturally lends itself


to application of information barriers; examples include zero-knowledge protocols [82, 83] and


public-key cryptography [84].


Figure 5.3: A diagram of the principle operations of template-based verification measurements.


The ability of the template based approach to impart confidence in the declaration rests in the


uniqueness of the measured signature and trust in the authenticity of the measurement. This work


does not deal with that latter requirement. The TOFFEE distribution measures the direct effects


of the underlying fission chain timing distribution of a multiplying object, which is sensitive to


any changes in fissile material mass, geometry and presence of surrounding neutronically coupled


material. The sensitivity of the presence of a fission chain, and any perturbations in its timing


distribution due to changes in its configuration makes TOFFEE distributions a useful signature for


62


item (warhead) confirmation and dismantlement confirmation. In general, these activities aim to


answer the following questions:


  - Dismantlement confirmation: Has the high explosive been separated from the fissile mate

rial?


  - Item (warhead) confirmation: Is the fissile assembly including reflecting material in the


tested object consistent with a nuclear warhead?


In the following sections the two propositions will be tested on surrogate fissile materials.

## **5.4 Experimental Setup**


Dismantlement confirmation was tested by comparing bare and moderated configurations of WGPu


BeRP ball [77] and of HEU Training Assembly for Criticality Safety (TACS) shells [85]. The


moderated configurations used a surrogate material to simulate the presence of high explosive.


The moderated BeRP ball configuration was surrounded with 2.54 cm thick shells of HDPE. In


contrast, the TACS shells configuration is more complex with nested layers of Lucite, HEU and


depleted uranium (DU) moving from the inside to outside. The inner radius of the Lucite was


4.6 cm, and the outside radius 7.92 cm at the edge of the DU. The inner most Lucite was left


there from previous experiments in which the Am-Li source was placed at the center of the as

sembly. The moderated TACS configuration included an additional outer shell of 1.12 cm thick


Lucite. Collectively the HEU shells weighed 16.53 kg compared to just 6.4 kg for the Depleted


Uranium (DU). The presence of DU made confirmation measurement more difficult by attenuating


all potential gammas emanating from U-235 fissions. In addition, HEU’s lack of a strong source of


spontaneous fissions necessitated actively interrogating the configuration with an Am-Li source.


The interrogating source was placed on the opposite side of the TACS HEU shells with respect to


the detectors.


Item confirmation was tested with a series of sources with increasing level of neutron mul

tiplication: non-multiplying Cf-252, relatively low-multiplication 190 grams of WGPu Oxide


63


hemispheres (Hemis), and the relatively highly-multiplying BeRP ball. These were compared with


the moderated BeRP ball and TACS shells. Except for the Hemis, which were measured at B262


at Lawrence Livermore National Laboratory (LLNL), all the other measurements were performed


at the NNSS Device Assembly Facility (DAF). A summary of all the measured objects is provided


in Table 5.1.


Table 5.1: Total data collection times for objects at the DAF and LLNL measurement campaigns.

|configuration|distance (cm) measurement rate of gamma ray<br>campaign<br>time (min) neutron pairs (Bq)|
|---|---|
|BeRP<br>BeRP + 1 in HDPE<br>TACS (HEU)<br>TACS (HEU) + 0.6 in Lucite<br>Cf-252<br>Hemi|34<br>59<br>55.6<br>DAF<br>34<br>589<br>77.8<br>DAF<br>34<br>55<br>0.068<br>DAF<br>34<br>80<br>0.077<br>DAF<br>36<br>31<br>10<br>DAF<br>46<br>499<br>0.096<br>LLNL|



The measurement system consists of eight, 2â A [˘] [˙] I in diameter and 2â A [˘] [˙] I thick (2â A [˘] [˙] I _×_ 2") stilbene


crystals arranged in a cylindrical pattern, as shown in Figure 5.4. Each stilbene crystal was coupled


to H1949-50 Hamamatsu Photomultiplier Tube (PMT) with a custom low voltage to high voltage


bias converter. Quarter inch thick pucks of lead were attached to the front of the detectors in


order to minimize count rate from uncorrelated and low energy decay gamma rays emitted by the


plutonium and americium in the BeRP ball. The PMT outputs were digitized by an 8 channel,


14-bit, 500 MS/s CAEN DT5730 desktop digitizer operated in asynchronous acquisition mode.


Asynchronous acquisition allows each channel to record pulses above threshold independently,


allowing for correlation analysis to be performed off-line with different coincidence windows.


In synchronous or coincident acquisition, multiple channels have to trigger inside a certain time


window for the events to be recorded. This second mode conveniently saves on the amount of


acquired data, but the coincident window remains fixed to the acquisition settings used to collect


the data. In this experiment, all pulses above the minimum threshold were recorded in list-mode


and the gamma/neutron PSD and timing analysis was performed off-line. The PSD was performed


using Bayesian procedure outlined in Section 3.5.


64


Figure 5.4: Photograph of the measurement of one of the BeRP ball configurations with the Stilbene Array.

## **5.5 Methodology**


A log-likelihood was used as a metric to compare the template to other test object measurements.


The counts in each bin of the TOFFEE distribution are assumed to follow Poisson statistics, and


the template is used to get the expected mean for each bin. The metric value is then the sum of


log-likelihoods for every bin:



_L_ =



_n_
� _−_ log( _P_ ( _x_ _i_ _|µ_ _i_ )) (5.4)


_i_ =0



where _n_ is the total number of bins and _P_ ( _x_ _i_ _|µ_ _i_ ) is the Poisson probability of measuring bin value


x given the scaled template bin value _µ_ in the i [th] bin. The bin range of -5 to 60 nanoseconds was


used to compare different measured distributions.


All correlated measurements will exhibit a â AIJflatâ [˘] A [˘] [˙] I background of uncorrelated random


accidentals, the level of which is linearly dependent on the overall interaction rate. This rate will


vary between different sources and configurations, ranging from 0.07 _s_ _[−]_ [1] from TACS to 78 _s_ _[−]_ [1]


for the BeRP ball. The background rate was estimated by taking the average of the neutron pulse

height dependent rate of correlated counts in the -1500 ns to -500 ns window ahead of each gamma


65


ray. This average rate was then subtracted from the rest of the distribution for each measurement.


The rate of correlated neutrons and gamma rays varies between different sources and configu

rations. For example, the addition of a moderator provides some shielding while simultaneously


increasing multiplication with the net effect of greater rate of measured correlated neutrons and


gammas. The rate of correlated neutrons is sufficient to distinguish between almost all of our


source configurations, as shown in Table 5.1, but this alone is not sensitive to the length of fission


chain nor their temporal development. In contrast, the TOFFEE distribution, is uniquely sensitive


to multiplication of the object itself. In order to separate the effects of correlated count rate and


TOFFEE distribution shape, each test was conducted with both count normalized and time nor

malized TOFFEE distributions. In the time normalized analysis, the primary discriminator is the


difference in rate. In count normalized analysis we remove these differences by using the same


number of events from each distribution. This ensures that only differences in the shape of the


timing distribution will enter the comparison metric. An example of both count normalized and


time normalized TOFFEE distributions of the bare and moderated BeRP ball are shown in Figure


5.5.


(a) Count Normalized (b) Time Normalized


Figure 5.5: Count normalized (left) and time normalized (right) TOF corrected neutron-gamma
time distributions for the bare BeRP ball (black) and the BeRP ball in a 2.54 cm HDPE shell
(blue).


66


Verification performance was judged on the basis of minimum dwell times required to confirm


dismantlement or a warhead. TOFFEE distributions of the tested object were constructed for spe

cific dwell times by using a randomly sampled subset of measured data. A total of 10,000 trails


of such randomly sampled subsets of data were used to estimate log-likelihood distributions for


each dwell time, as is shown in Figure 5.6. An arbitrary operation point of 99% True Positive


(TP) rate was chosen, and dwell times were incrementally increased until the False Positive (FP)


fell just below 1%. The dwell times that met both these operational thresholds were recorded for


comparison among different sets of trusted and tested objects.


Figure 5.6: The log-likelihood distribution (left) and corresponding Receiver Operator Characteristic (ROC) curve (right) for 10,000 — 8 second trails of the comparison of the bare (dismantled)
and moderated BeRP ball.

## **5.6 Dismantlement Confirmation**


Dismantlement confirmation performance was tested by comparing bare and moderated configu

rations of the BeRP ball and TACS HEU shells. The bare configurations were used as templates


and the moderated configurations were the test objects. A depiction of each trusted and test object


pairs are shown in Figure 5.7.


The BeRP ball took only a few seconds to confirm, which was over an order of magnitude


67


Figure 5.7: The pairs of trusted and tested objects used for dismantlement verification. The moderators, HDPE and Lucite, were used as high explosive (HE) surrogates. The inner and outer
dimensions of the TACS shells are given in centimeters.


less time than the TACS shells. This difference is predictable due to the much higher spontaneous


fission rate of Pu-240 in the BeRP ball which allows for much higher rate of fission chain initiation.


Figure 5.8 illustrates the dependence of the False Positive rate for the two objects, assuming 99%


True Positive rate operational threshold, on dwell time. In theory, it would be possible to reduce


the dwell time required to confirm HEU by using a stronger interrogating source. The presence of


DU shielding also effectively cuts down on the rate of measured correlated neutron and gamma-ray


pairs.


Table 5.2: Summary of the time to confirm dismantlement with 99% TP and 1% FP rate.


trusted tested count time

object object normalized (s) normalized (s)
BeRP ball BeRP ball + HDPE 12 3.7

TACS shells TACS shells + Lucite 380 590


68


Figure 5.8: False Positive rate as a function of dwell time assuming 99% True Positive operational
threshold with count normalized analysis of dismantled objects.

## **5.7 Item Confirmation**


Item confirmation was performed by using the moderated configurations of the BeRP ball and


TACS shells as trusted objects. A depiction of each trusted and test object pairs are shown in


Figure 5.9. The choice of a test objects for item confirmation is much more difficult than in the


case of dismantlement confirmation because of the open ended options for potential spoofs that


an adversary could use. Two test objects were used: Cf-252 and plutonium oxide hemispheres


(Hemis). The former is a readily available laboratory source of Watt spectrum fission neutrons,


and the latter is fissile material with far smaller mass and Oxide chemical form.


As with the dismantlement confirmation, the requisite dwell times for confirmation against


the BeRP ball are significantly shorter. The limited number of counts in the HEU measurement


requires coarser binning in time and ultimately results in a much noisier template. The results


are summarized in Table 5.3. The assumptions about Poisson statistics for calculating the log

likelihood also break down for any comparison that is statistically starved. Comparisons of False


Positive rates as a function of dwell time for all cases are shown in Figure 5.10.


69


Figure 5.9: The pairs of trusted and tested objects used for dismantlement verification. The moderators, HDPE and Lucite, were used as high explosive (HE) surrogates. The inner and outer
dimensions of the TACS shells are given in centimeters.


Table 5.3: Summary of the time to item confirmation with 99% TP and 1% FP rate.


trusted tested count time

object object normalized (s) normalized (s)
BeRP ball + HDPE Cf-252 12 6

BeRP ball + HDPE Hemi shells 2 6

TACS shells Cf-252 1100 80

TACS shells Hemi shells 540 960

## **5.8 Conclusions**


The previously studied TCPH distribution, a bi-variate histogram of neutron deposition energy and


time to correlated gamma ray, was collapsed into one dimensional TOFFEE distribution. As a


result, the direct effect of the inter-generational time within a fission chain, ∆ _T_ _g_, on the measured


signature became apparent. Furthermore, TOFFEE was more desirable for direct comparison of


measurements, because of the greater counts per bin, which improve statistical performance over


the TCPH analysis. This capability was tested in the context of two treaty verification problems:


dismantlement and item confirmation. The goal was to determine the minimum dwell time required


70


Figure 5.10: False Positive rate as a function of dwell time assuming 99% True Positive operational
threshold with count normalized analysis for item confirmation comparing TACS shells (HEU) and
the BeRP ball against the non-multiplying Cf-252 and low-multiplying Hemi shells.


to confirm that the test object did not match the trusted object, and to demonstrate that TOFFEE is


a useful signature for these applications.


A TOFFEE distribution template of a trusted object was compared against test object’s TOFFEE


distribution with the log-likelihood as a metric of comparison. Distributions of the log-likelihoods


were built by sampling 10,000 times from the measurements of the trusted and test objects for spe

cific dwell times. These were then used to build Receiver Operator Characteristic (ROC) curves


from which operational performance was determined. The desired performance threshold was set


at 99% TP rate with a corresponding 1% or less FP rate, and the minimum dwell times required to


achieve those performance thresholds were reported.


For both dismantlement and item confirmation, the BeRP ball required only several seconds (2

12 s) to determine that the test object was inauthentic. By contrast, TACS shells required hundreds


of seconds of dwell time for confirmation at the same operational thresholds. The difference was


mainly due to the relatively strong source of spontaneous fission neutrons from Pu-240 inside


the BeRP ball, which drove the initiation of fission chains and corresponding correlated particles.


The TACS shells, whose fissile component was HEU, had to be stimulated by an external Am-Li


71


interrogation source. In addition, the outer DU shell around the HEU further suppressed the signal


from correlated neutrons and especially gammas.


Finally, the analysis was performed over both count normalized and time normalized TOFFEE


distributions. It was expected that the additional difference in gamma-neutron correlation pair


detection rates between trusted and tested objects would allow for faster confirmation and thus


lower dwell times. However, the time normalized results were not consistently lower than the count


normalized counterparts. In particular, the dismantlement confirmation with TACS shells and the


item confirmation with the Hemi’s produced the opposite of expected results. The measurement


of those objects suffered from relatively lower gross counts due to equally low rates of detected


gamma-neutron pairs. As a result, the reported dwell time may carry significant uncertainty, which


was not reported in this work. However, this uncertainty is reflected by the difference in the count


and time normalized dwell times which run counter to the expected results.


72


## **CHAPTER 6**

# **Solving For Subcritical Assembly Physical** **Parameters**

## **6.1 Motivation**

In Chapter 5, the measured TOFFEE distribution was used to distinguish between different sources


of correlated gamma rays and neutrons in the context of treaty verification. The reduction in the


number of dimensions from the TCPH distribution made it more suitable for direct comparison


of two measurements. In addition, the role of inter-fission timing in the shape of the TOFFEE


distribution became clear. Inter-fission timing is influenced by both the amount of fissile material


and presence of any reflectors. The sensitivity of the TOFFEE distribution to those factors was


tested in Chapter 5. The work presented in this chapter will explore the extraction of physical


parameters driving fission chain dynamics from the measurement of a TOFFEE distribution.


In a way this is a return to the analysis shown in Chapter 4, where empirical parameters of


a Gamma function were shown to correlate with neutron multiplication and type of reflector ma

terial. However, the construction of an analytical TCPH distribution was rather convoluted and


the empirical parameters of the Gamma function lacked immediate physical interpretation. This


is avoided here by fitting the positive side of the simpler one dimensional TOFFEE distribution


to a physically meaningful model that describes time dependent neutron population behavior in a


critical assembly coupled to a neutron reflector. The physical model is developed from two-region


point kinetics theory, which is an extension of the one-region point kinetics used in Rossi-alpha


73


method described in Section 2.2.1.


The goal is to determine three inter-dependent parameters:


1. Neutron multiplication


2. Amount of coupled neutron reflector material


3. The type of neutron reflector material


These are intrinsically difficult to decouple because greater amounts of neutron reflector increase


neutron multiplication. The determination of the amount and composition of reflector material


could be useful in the area of emergency response, or safeguards. Therefore, the analysis developed


here could complement other traditional methods (e.g. multiplicity counting, Rossi-alpha analysis


and gamma spectroscopy) that are complicated by the presence of neutronically coupled reflector


material.

## **6.2 Two-Region Point Kinetics**


As described in Section 5.2, the spread in the TOFFEE distribution of a multiplying source is driven


by the generation time, ∆ _T_ _g_, between the detected gamma-rays and neutrons. The probability of


detecting these particles is governed by the time dependent population of fissions, or the corre

sponding neutrons that propagate fission chains. Point kinetics equations are a well established


method for studying the time-dependent neutron populations in a nuclear reactor. However, mod

eling neutron behavior inside reflected assemblies required a two-region kinetic model [86, 87].


First, traditional reactor point kinetics is simplified by ignoring delayed neutron precursors that


result from the cascade of decays of fission product isotopes. These fission product isotopes are


typically organized into six groups with half-lives ranging from hundreds of milliseconds to tens


of seconds [88]. These delayed neutrons can be ignored because the TOFFEE correlation window


of interest is only on the order of a hundred nanoseconds. Ignoring delayed precursors, the time

dependent neutron population of prompt neutrons in a reflected assembly can be approximated


74


by:


where:



_c_

_dt_ [=] _[ k]_ _[c]_ _[ −]_ _l_ [1]



(6.1)
_l_ _r_



_dN_ _c_




_[ −]_ [1] _N_ _c_ + _f_ _rc_ _N_ _r_

_l_ _c_ _l_ _r_



_dN_ _r_



_c_

_−_ _[N]_ _[r]_
_l_ _c_ _l_ _r_



_r_ _N_ _c_

_dt_ [=] _[ f]_ _[cr]_ _l_



(6.2)
_l_ _r_



_N_ _c_ is the number of neutrons in the fissile core region


_N_ _r_ is the number of neutrons in the reflector


_k_ _c_ is the multiplication factor in the fissile core region


_l_ _c_ is the neutron lifetime in the fissile core region


_l_ _r_ is the neutron lifetime in the reflector region


_f_ _cr_ is the fraction of neutrons that leak from the fissile core region into the reflector


_f_ _rc_ is the fraction of neutrons that leak from the reflector back into the core


Note that the _k_ _c_ is different from the multiplication factor _k_, but the two are related as shown in


Eq. 6.17. The former is the property of only the core, while the latter is the property of the whole


_system_ (i.e. the core and reflector assembly).


The system of equations in Eqs. 6.1 and 6.2 can be solved by converting them to a second order


differential equation:



_l_ _r_ _l_ _c_ _d_ [2] _N_ _c_



(6.3)
_dt_ _[−]_ [(] _[f]_ [ +] _[ k]_ _[c]_ _[ −]_ [1)] _[N]_ _[c]_ [ = 0]



_N_ _c_ [+ (] _[l]_ _[c]_ _[ −]_ _[l]_ _[r]_ [(] _[k]_ _[c]_ _[ −]_ [1))] _[dN]_ _[c]_

_dt_ [2] _dt_



The new variable _f_ is the fraction of neutrons that leak out of the core and are reflected back, which


is just the product of two previously defined terms


_f_ = _f_ _rc_ _f_ _cr_ (6.4)


75


The complete solution requires two initial conditions:


_N_ _c_ (0) = _N_ _o_ (6.5)


_N_ _r_ (0) = 0 (6.6)


at _t_ = 0 the neutron population in the core is _N_ _o_ and no neutrons are present in the reflector. The


solution to Eq. 6.3, given these initial conditions is a familiar double exponential:


_N_ _c_ ( _t_ ) = _N_ _o_ �(1 _−_ _R_ ) _e_ _[tr]_ [1] + _Re_ _[tr]_ [2] [�] (6.7)


where the roots to the characteristic polynomial are



~~�~~
_r_ 1 = _[−]_



(6.8)
2 _l_ _c_ _l_ _r_



4 _l_ _c_ _l_ _r_ ( _f_ + _k_ _c_ _−_ 1) + ( _l_ _c_ _−_ _l_ _r_ ( _k_ _c_ _−_ 1)) [2] _−_ _l_ _c_ + _l_ _r_ ( _k_ _c_ _−_ 1)



(6.9)
2 _l_ _c_ _l_ _r_



4 _l_ _c_ _l_ _r_ ( _f_ + _k_ _c_ _−_ 1) + ( _l_ _c_ _−_ _l_ _r_ ( _k_ _c_ _−_ 1)) [2] _−_ _l_ _c_ + _l_ _r_ ( _k_ _c_ _−_ 1)



_r_ 2 =


and scaling ratio _R_ is


where



~~�~~



_R_ = _[r]_ [1] _[ −]_ _[α]_ (6.10)

_r_ 1 _−_ _r_ 2



_α_ = _[k]_ _[c]_ _[ −]_ [1] (6.11)

_l_ _c_



_f_ and _k_ _c_ are constrained to be less than 1. The factor _R_ falls within the range 0 to 1 for all plausible


combinations of these variables.


The solution to Eq. 6.7 collapses to a single exponential shown in Eq. 2.13, which is a starting


point for Rossi-alpha analysis, in three special cases:


1. The reflector does not return any neutrons, in effect the fissile material is bare.


76


2. Neutron lifetime in the reflector is large, and as a result neutrons crossing into the reflector


just stay there.


3. Neutron lifetime in the reflector is exceedingly small, and as a result reflected neutrons are


immediately returned to the fissile core.


In the first case none of the leaked neutrons are reflected back, that is _f_ _rc_ = 0 and therefore


_f_ = 0. As a result, Eq. 6.1 simplifies to Eq. 2.12 and the solution is a single exponential.


The second and third case involve the extremes of the _l_ _r_ parameter. If _l_ _r_ is large, then the


neutrons spend a long time in the reflector and do not return to the fissile core. Under that condition,


and assuming a subcritical fissile core ( _k_ _c_ _<_ 1), the roots of the characteristic polynomial are


lim (6.12)
_l_ _r_ _→∞_ _[r]_ [1] [ =] _[ α]_


lim (6.13)
_l_ _r_ _→∞_ _[r]_ [2] [ = 0]


which implies that _R_ = 0 and the solution in Eq. 6.7 again collapses to a single exponential


characteristic of a bare assembly with the rate parameter _α_ .


On the other hand if _l_ _r_ is really small ( _l_ _r_ _<_ 0 _._ 01 _ns_ ) then the roots are


_l_ lim _r_ _→_ 0 _[r]_ [1] [ =] _[ −∞]_ (6.14)

_l_ lim _r_ _→_ 0 _[r]_ [2] [ =] _[f]_ [ +] _[ k]_ _l_ _c_ _[c]_ _[ −]_ [1] (6.15)


which in implies that _R_ = 1 and again the solution collapses into a single exponential. The


neutrons that enter the reflector either immediately disappear or are instantaneously return the


fissile core. In this case the fraction _f_ effectively adds to the probability that a neutron fissions in


the core.


77


## **6.3 Experiments**

The measurements were conducted at the NNSS, with five distinct reflector configurations shown


in Table 6.1, at a source-to-detector distance of 30 cm. The reflectors were made from close fitting


sets hemispherical shells made of iron and nickel, with a single 4.509 cm diameter hole used to


support the fissile material at the center of the shells.


Table 6.1: Measurement details of the various configurations of the BeRP ball with iron and nickel
reflectors. The neutron multiplication was calculated from MCNP5 k-code simulation.

|case|measurement rate of gamma-ray multiplication<br>time (sec) neutron pairs (Bq)|
|---|---|
|bare<br>0.5 in Fe<br>1 in Fe<br>1.5 in Fe<br>1.0 in Ni|1968<br>136<br>4.433_ ±_ 0.001<br>897<br>211<br>5.584_ ±_ 0.008<br>2095<br>280<br>6.648_ ±_ 0.012<br>1497<br>239<br>7.182_ ±_ 0.015<br>1497<br>243<br>7.472_ ±_ 0.016|



In addition to a multiplying source, a 21 _µ_ Ci Cf-252 source was measured at a source to de

tector distance of 35 cm. This measurement was performed independently at Sandia National


Laboratories. This measurement served as a starting point for validation of the MCNPX-PoliMi


simulations that were used to extend the available measured configurations of the BeRP ball.


All measurements were performed with the same purpose-built portable array of eight 2" by 2"


cylindrical stilbene crystals and acquisition system described in Section 5.4 and shown in Figure


6.1. The acquisition threshold was approximately 20 keVee (keV electron-equivalent), and the


post-processing threshold was set to be 100 keVee.


The Birks’ formula, from Eq. 3.6, was used for the neutron light output calculations with fitted


parameters of _S_ = 1 _._ 63 (MeVee/MeV) and _k_ = 27 _._ 83 (mg/(cm [2] MeV)). The integrand in Eq. 3.6


was evaluated for deposited energies ranging from 1 keV to 250 MeV, and the results were saved


in a lookup table. Linear interpolation of the values in the table was used to calculate light output


from simulations and approximate proton recoil energy from light output in measurement.


78


Figure 6.1: The front of purpose-built stilbene array used for all measurements.

## **6.4 Simulation Validations**


The measured configurations of the BeRP ball, shown in Table 6.1, include three sets of shell


thickness and two types of reflector material. Simulations were used to expand the range shell


thicknesses, explore other reflector materials, and vary the mass of the BeRP ball by changing the


diameter of the sphere. In order to have confidence in these results, it was necessary to validate the


simulations by comparing them with measurements as will be done in the following sections.

### **6.4.1 Cf-252**


The goal of starting with a Cf-252 source was to isolate contributions to the TOFFEE distribution


caused by factors other than the development of a fission chain. One factor is the detector response,


which depends on the energy calibration and validity of the light output function shown in Eq. 3.6.


Another factor is particles scattering from other objects in the experimental setup, contributing to


the so-called room return.


The ubiquitous Cf-252 isotope is a very well characterized source of correlated gamma rays and


neutrons, and is readily available as built-in source option for MCNPX-Polimi [74]. In addition,


the commercially available Cf-252 source capsule used for the measurement is small enough to


79


be approximated as point source in the simulation. The effects of room return were simulated by


the addition of a 30 cm thick concrete floor 1 meter below the source. The floor is expected to


dominate the scattering effects because of its proximity to the source, therefore the walls (2+ _m_


away) and other smaller scattering materials were not included in the simulations.


The neutron Pulse Height Distributions (PHDs) were compared to test the energy calibration


and neutron light output function. The neutrons were limited to those that were correlated with


gamma rays inside a 2 _µ_ s window. The measured and simulated PHDs shown in Figure 6.2 overlap


with the entire range of measured energies, without any noticeable systematic bias and within


the statistical error. The statistical fluctuations are reflected in the relative error, which oscillates


around zero.









(a)



(b)



Figure 6.2: Measurement and simulation comparison of the Cf-252 source (a) pulse height distribution of gamma-ray correlated neutrons and (b) corresponding relative error of the simulation.


In contrast to the PHDs, which is relatively featureless, the TOFFEE distributions shown in


Figure 6.3 have several features whose shape depend on the detector response. The most significant


feature is the bell-like curve between -10 and 5 ns which includes the vast majority of correlated


counts. The width of these curves line up with each other, indicating that the energy calibration


and corresponding thresholds are well matched, and that time resolution is properly applied. In


addition, the width is affected by the source-to-detector distance, which in both the simulation and


measurement was 35 cm.


80


The higher counts in the measurement in the region between -20 and -10 ns is partly due to PSD


misclassification, where gamma-gamma correlations are mistakenly classified as gamma-neutron.


There is also good agreement in the region beyond 60 ns, where the effects of scattering from


the floor is evident. There are not many counts in that region, which contributes to the erratic


relative error, but the simulation and measurement match within the statistical error. The region of


the largest notable error lies roughly between 5 and 25 ns, right around the steep drop in counts


expected from a non-multiplying source.


Finally, there is the rate of “accidental" correlations that depend on the source strength and


appear as a flat background in the TOFFEE distribution. The contribution from accidentals is esti

mated by averaging counts in each bin of a region offset by 1000 to 1500 ns from each coincidence


trigger. This is then subtracted from the TOFFEE distribution.





(a)







(b)



Figure 6.3: Measurement and simulation comparison of the Cf-252 source (a) TOFFEE distribution
and (b) corresponding relative error of the simulation.

### **6.4.2 BeRP Ball**


The BeRP ball is a much more complicated source compared to Cf-252. It’s a distributed spherical


source having a diameter of 7.59 cm and a multiplication of 4.4, and therefore cannot be treated


as a non-multiplying point source. In the simulation, the source term was evenly distributed spon

taneous fissions of Pu-240. In reality the BeRP ball includes a more complicated mix of isotopes


81


that become ingrown over time, but these were omitted from the simulation because they primarily


contribute to the flat uncorrelated accidental background which was subtracted out.


The bare configuration comparison, shown in Figure 6.4, shows that the measured TOFFEE


distribution is just slightly wider. The larger source of discrepancy is in the region between 40 and


100 ns, which is dominated by reflection from the floor. There are many time bins that are within


statistical agreement in that region, but also a handful that have no counts at all. The problem is


that the accidental background rate is much lower in the simulation (1 per ns) compared to the


measurement (62 per ns) because of the lack of ingrown isotope sources in the former. In the


measurement the higher accidental background competes with the effect of room return and is


statistically significant when the two are subtracted, which is apparent from the large uncertainties.





(a)







(b)



Figure 6.4: Measurement and simulation comparison of the bare BeRP ball (a) TOFFEE distribution and (b) corresponding relative error of the simulation.


The overall agreement between simulated and measured TOFFEE distributions improves as


reflector material is added. The BeRP ball with 1 inch iron is shown in Figure 6.5 as a representa

tive example of the improvement. It appears that the time smearing associated with longer fission


chains dominates over the discrepancies caused by room return, and accidental background.


82


(a)







(b)



Figure 6.5: Measurement and simulation comparison of the BeRP ball with 1 inch iron shielding
(a) TOFFEE distribution and (b) corresponding relative error of the simulation.

## **6.5 Bare Configurations**


Neutron multiplication and reflector thickness are correlated, since neutron reflection increases


the neutron population and average length of fission chains. In order to study the effect of mul

tiplication independently from the effects of reflector bare BeRP balls with various masses were


simulated, ranging from 1 to 8 kg. The change in mass was accomplished by changing the diame

ter of the BeRP ball. A section of TOFFEE distribution, from 0 to 100 ns, were fitted to Eq. 2.13,


which is a single exponential that doesn’t account for a reflector.


A comparison of the measured and simulated BeRP ball is shown in Figure 6.6. As explained in


Section 6.4.2, there is some disagreement at later times due to competing effects of floor reflection


and accidental correlations. However, the fits and resulting _α_ parameters for measurement (0 _._ 144 _±_


0 _._ 003) and simulation (0 _._ 153 _±_ 0 _._ 004) are within two standard deviations of each other.


The multiplication factors and neutron lifetimes for the bare cases were tallied in MCNP6


simulations, and Eq. 6.11 was used to calculate corresponding _α_ parameters. Figure 6.7 shows


the comparison of these MCNP derived alpha values with the alpha values estimated from the


exponential fits. The relationship between estimated and MCNP alphas is linear, and a regression


analysis revealed a correlation coefficient greater than 0.98, and a slope of 1.0974.


83


Figure 6.6: Comparison of the measured and simulated bare BeRP ball TOFFEE distributions and
exponential fits from Eq. 2.13.


As shown in Figure 6.7, there is a slight deviation from the linear trend for the actual BeRP


ball simulation and measurement. For all other masses the thin stainless steal shell surrounding the


BeRP ball was removed and truly bare Pu spheres were simulated.


Neutron multiplication can be derived from the neutron decay constant and core lifetime by


rearranging Eq. 6.11:



_M_ = _−_ [1] _._ (6.16)

_αl_ _c_



Neutron multiplications were derived from fitted alpha parameters by using previously tallied core


neutron lifetimes from MCNP6. As expected, there is a positive linear correlation between the


derived and actual neutron multiplication, as shown in Figure 6.8(a). However, the derived values


underestimate the actual values, and the deviation grows with increasing BeRP ball mass. This


increasing underestimation could be due in part to self-shielding, which would mean that detected


particles are preferentially drawn from near the surface of the sphere. This is consequential because


on average fission chains near the surface are shorter than the ones near the center.


Leakage multiplication, defined in Section 2.1.4, should compensate for the effect of self

shielding by taking into the account the probability of neutron leakage. The relationship between


84


Figure 6.7: The estimated ( _α_ _F_ ) and calculated, from MCNP6, ( _α_ _M_ ) alpha parameters for BeRP
balls with mass ranging from 1 to 8 kg. A linear regression was performed with the resulting
relationship shown in the legend and a correlation coefficient of 0.9890.


derived multiplication and leakage multiplication is shown in Figure 6.8(b). There is still underesti

mation of the leakage multiplication with increasing BeRP ball mass, although it’s less pronounced


with average deviation of -10.69%.











(a)



(b)



Figure 6.8: Derived neutron multiplications from TOFFEE fits of the bare BeRP balls with different
masses with the corresponding (a) total and (b) leakage multiplications obtained through MCNP6
simulations. The dashed line corresponds to perfect agreement between derived and actual multiplication, with the points above and below corresponding to overestimation and underestimation,
respectively.


85


## **6.6 Reflected Configurations**

Next we fit Eq. 6.7, derived from two-region point kinetics model in Section 6.2, to the reflected


BeRP ball configurations. In Eq. 6.7 there is total of four physical parameters, but two of the


parameters were constrained to make a meaningful fit.


At first three parameters were considered in the fitting routine: _l_ _c_, _l_ _r_ and _f_ . Either _k_ _c_ or _l_ _c_


have to be constrained because the correlation coefficient between the two is 1. However, the


remaining two parameters, _l_ _r_ and _f_, had no discernible trend between reflector material and across


different shell thicknesses. Furthermore, the coefficient of correlation between the parameters was


large, and corresponding uncertainties on the fitted parameters were large. A strategy had to be


developed to systematically fit only two parameters.


Most meaningful results were obtained by fixing both _k_ _c_ and _l_ _c_ and letting _l_ _r_ and _f_ float. The


core multiplication constant was taken from MCNP6 kcode calculation. The neutron lifetime in


the core was then solved for separately for both simulations and measurements using Eq. 6.11


with the fitted _α_ from the bare BeRP ball. The Eq. 6.7 fits of the measured iron cases are shown


in Figure 6.9. In the first 60 ns time window the fit tracks quite well with the data, but undershoots


the data at later times in the 80-100 ns window. Some of this behavior is due to the lower statistics


in that region which make it less important for the fit. There is also some effect of floor reflection


that is not accounted for in the two-region point kinetics model and therefore missing from Eq.


6.7.

### **6.6.1 Multiplication**


The parameter _f_ is related to the total system _k_ by


_k_ _c_
_k_ = (6.17)
(1 _−_ _f_ ) _[.]_


Neutron multiplication is then be calculated from Eq. 2.9. The comparison of this “Estimated Mul

tiplication" with the MCNP6 equivalent for the measured and simulated cases is shown in Figure


86


Figure 6.9: TOFFEE distributions of the measured iron configurations with corresponding double
exponential fits from Eq. 6.7.


6.10. As expected, there is convergence between the simulated and measured cases with increas

ing shell thickness. The average relative difference between estimated and expected multiplication


was 10%.


The simulation results that include aluminum and tungsten shells of up to 6 in thick are shown


in Figure 6.11. The estimated multiplications for all shielding materials have positive correlations


with the MCNP multiplication, although the relationship is different between materials. The trend


is superlinear for aluminum and sublinear for tungsten. Iron and nickel have a more linear trend.


The average relative difference also varied from one material type to the next, with as little at 14%


for aluminum and as much at 22% for iron. Unlike with the bare case correlation with leakage mul

tiplication produced even worse agreement and the trends among the different materials remained


the same.


87


Figure 6.10: Comparison of the estimated multiplication of the measured and simulated TOFFEE
distribution for the shielded configuration of the BeRP ball. The dashed line represent perfect
agreement between the fit and the expectation from MCNP simulation.











Figure 6.11: Estimated multiplication for simulated TOFFEE distributions of several configurations of shielded BeRP ball with different material types.


88


### **6.6.2 Shell Thickness and Material Type**

Apart from the fitted parameters, _f_ and _l_ _r_, there were a couple of derived quantities that proved


to be correlated with physical quantities. The integral of Eq. 6.7 used in fitting the reflected


configurations is



� 0 _∞_



_∞_

_N_ _c_ ( _t_ ) _dt_ = _[R][ −]_ [1]
0 _r_ 1




_[ −]_ [1]

_−_ _[R]_

_r_ 1 _r_ 2



(6.18)
_r_ 2



Plotting this integral against shell thickness, as shown in Figure 6.12, reveals unique linear cor

relations for each material type. As mentioned before, shell thickness and multiplication are in


themselves correlated, but the integral has much more linear and consistent correlations with shell


thickness. Furthermore, the slope of each line increases with atomic number and density. This


demonstrates that it may be possible to determine material type if shell thickness is known, or vice


versa.









Figure 6.12: Integral of a double exponential fit as a function of shell thickness.


Given the relationships demonstrated in Figure 6.12, it was worth investigating the correlation


with the integral of the fit could be decoupled from any particular element and related back to


the total amount of reflector. The total amount of reflector surrounding the core was quantified


by the effective areal density, which takes into account shell thickness and density. The integral


89


correlation with effective areal density for all four reflector materials is shown in Figure 6.13. The


results of linear least-squares regression for each material and all of them combined is shown in


Table 6.2. Each material has a unique linear correlation, but the combined regression shows a


strong correlation coefficient of 0.9717. The deviation between materials is likely due to inelastic


and other capture neutron interactions within each reflector, which is not correcting for.









Figure 6.13: The integral of the fit of Eq. 6.7 to TOFFEE distributions of the reflected configurations of the BeRP ball and the effective areal density of each of the shells.


Table 6.2: Linear leas-squared regression for the correlation between integral of the fit to TOFFEE
distribution and effective areal density of the reflector material.

|reflector|correlatio<br>slope intercept<br>coefficien|
|---|---|
|Aluminum<br>Iron<br>Nickel<br>Tungsten<br>All|0.064<br>7.06<br>0.9748<br>0.175<br>8.46<br>0.9889<br>0.274<br>9.10<br>0.9895<br>0.237<br>8.91<br>0.9815<br>0.251<br>6.55<br>0.9717|



The second derived quantity of interest is the scaling ratio, _R_, which asymptotically approaches


unity with increasing shell thickness, as shown in Figure 6.14(a). As the amount of reflector


material goes up, so does its effect on the TOFFEE distribution. Eventually this dominant reflector


term collapses the double exponential fit into a single exponential. This suggests that it may be


90


difficult to separate the effects fissile material mass and presence coupled reflector at sufficiently


high areal densities of said reflector.


The asymptotic behavior of the scaling ratio approaching unity is driven by the fitted _l_ _r_ that for


the heavier materials approached zero, as shown in Figure 6.14(b). The results from fitted _l_ _r_ mir

ror those of the scaling ratio shown in Figure 6.14(a), but unfortunately lack meaningful physical


interpretation. Neutron lifetime in the reflector is expected to be largest for the denser materials,


and increase with shell thickness. Instead, the exact opposite is shown to be the case. This may be


a consequence of the negative covariance between _f_ and _l_ _r_ . As was shown in the multiplication


analysis in Section 6.6.1, the parameter _f_ appropriately increased with greater neutron multipli

cation. But this may have inadvertently driven the fitted value of _l_ _r_ down because of its negative


correlation.











(a)





(b)





Figure 6.14: The (a) scaling ratio and (b) neutron lifetime in the reflector from the fit of Eq. 6.7 to
TOFFEE distributions of the BeRP ball with various reflector shell thicknesses.

## **6.7 Conclusions**


The positive side of the TOFFEE distribution was fitted, from 0 to 100 ns, to time dependent


neutron population derived from point kinetics theory. A bare subcritical assembly is sufficiently


described by a single exponential in Eq. 2.13 and introduction of a reflector yields a double expo

91


nential shown in Eq. 6.7.


For the bare cases the estimated alpha parameters and the expected alpha values are linearly


correlated. A derived multiplication was calculated from the estimated alpha parameters by assum

ing a known _l_ _c_ from MCNP6 simulations. This derived multiplication positively correlated with


the leakage multiplication with an average relative error of 10.6%.


The TOFFEE distributions from the reflected BeRP ball assemblies were fitted to the double


exponential model from Eq. 6.7. The derived multiplication from _f_ had a positive correlation with


the expected multiplication for MCNP6, although the relationship varied between material types.


Furthermore, we determined that the effective areal density of the reflectors was positively and


linearly correlated with the integral of those same double exponential fits. It is conceivable that


with knowledge of either shell thickness or material composition it would be possible to determine


the other property.


92


## **CHAPTER 7**

# **3D Imaging**

## **7.1 Motivation**

Nominally this thesis is about measuring fission chain dynamics through gamma-neutron correla

tions. TOFFEE distributions provide an indirect means of measuring of the temporal evolution of a


fission chain. The central approximation at the core of TOFFEE stems from the overestimation of


the neutron travel time from proton recoil shown in Eq. 5.1. This is due to the fact that the proton


recoil energy ( _E_ _p_ ) underestimates the incident neutron energy ( _E_ _n_ ):


_E_ _p_ _≤_ _E_ _n_ (7.1)


which results in the inequalities in Eqs. 5.2 and 5.3.


If the incident neutron energy was known, then the measurement of the TOFFEE distribution


would directly measure the generation time difference between correlated particles:


_t_ _n,γ_ _−_ _t_ _p_ = ∆ _T_ _g_ (7.2)


As a consequence, the TOFFEE distributions from non-multiplying sources would resemble a delta


function centered around zero, having a width due to timing and energy resolution of the detec

tor system. This would potentially improve discrimination sensitivity between non-multiplying


and multiplying sources, and improve characterization of the latter since ∆ _T_ _g_ would be measured


93


directly.


Neutron incident energy can be estimated with a double scatter neutron spectrometer, which,


through detection of correlated gamma-neutron-neutron ( _γ −_ _n −_ _n_ ) events, could yield this bet

ter resolved TOFFEE distribution. Fortunately, double scatter neutron imagers also function as


neutron spectrometers, and those that can detect gamma rays have been in development for over a


decade at both Sandia National Laboratories and University of Michigan [89]. A preliminary mea

surement of Cf-252 source with Mobile Imager of Neutrons for Emergency Response (MINER)


[90], shown in Figure 7.1, revealed that estimated incident neutron energy rather than the proton


recoil energy shifted the TOFFEE distribution around the origin, but did not appreciably narrow


it. This is caused by the relatively poor energy and timing resolution of MINER, and therefore


dominating the width of the TOFFEE distribution.









Figure 7.1: TOFFEE distributions of a measured Cf-252 source at a distance of 50 cm with neutron
energy estimations using the proton recoil energy ( _E_ _p_ ) and the incident neutron energy ( _E_ _n_ ) from
double scatter.


With this preliminary result, it is unclear if incident neutron energy information is worth the


substantial diminished efficiency in detecting a triple coincidence of _γ −_ _n −_ _n_ . Intuitively, the


timing between gamma-neutron correlations carry with them information regarding the source-to

detector distance, a fact that was known from previous studies of the TCPH distributions discussed


94


in Chapter 4. In this Chapter, I rigorously prove the _γ_ _−n−n_ coincidence provides the information


required to reconstruct a correlated source in three dimensions. Some preliminary measurements


and the proof of the method were first published in [91]. With this technique it is possible to


perform 3D reconstructions of correlated gamma-neutron sources from a view from a single side,


which is unique because traditional 3D imaging techniques require some movement of the detector


around the source of interest or multiple detectors positioned around the object to be imaged.


This new imaging technique utilizes an inherent property of the majority of neutron sources


important in nuclear threat-search, safeguards and non-proliferation: the coincident emission of


neutrons and gamma rays. These sources include those undergoing spontaneous and induced fis

sion [92], a property of SNM, and common ( _α_,n) sources that leave the remaining nucleus in an


excited state leading to prompt gamma ray emission [93].

## **7.2 Background of 2D and 3D Radiation Imaging**


Radiation imaging is well established in fields as diverse as medicine [94, 95], astronomy [96, 97],


and nuclear safeguards and non-proliferation [98, 99]. Because fission energy gamma rays and


neutrons cannot be lensed as in optical imaging, they function by either:


1. modulating (blocking) the incident radiation


2. tracking multiple scatters of the incident particle in the detector medium, and estimating


their incident direction by kinematic reconstruction of their paths.


The first gamma-ray camera was developed by Hal Anger who used multichannel collimators to


modulate incident radiation [100]. The same principle can be applied with more complex coded


aperture masks, which are analogous to superimposed pinhole cameras, to image both thermal and


fast neutrons [101, 102].


The technique introduced in this chapter is an extension of the second category of radiation


cameras which track multiple scatters to reconstruct source direction. In gamma-ray imaging,


95


these are called Compton cameras [98], and are a mature technology with commercially available


portable cameras [103]. The functioning of a neutron scatter camera is analogous to the Compton


camera, but with the use of the time-of-flight (TOF) between the first two scatters to determine


the incident neutron energy rather than relying on full energy deposition in the second interaction


[104].


The discussion so far has been limited to 2D imaging systems, but in principle any radiation


camera can produce a 3D reconstruction of a source. The most common approach is to take


multiple 2D images from different views, and combine them to form 3D rendering of the source.


This technique is used in Single Photon Emission Computed Tomography (SPECT) and Positron


Emission Tomography (PET) to image radioisotopes inside a patient [94]. Recently, researchers


at Lawrence Berkeley National Laboratory have used a variation of this technique, combined with


a 3D rendering of physical space, to reconstruct source locations in real time [105]. All of these


techniques require multiple views of the source and some freedom of movement with respect to


the object being imaged.


Single-sided 3D imaging has been demonstrated in Compton cameras by taking advantage of


the parallax effect [106]. However, parallax techniques require a large solid angle coverage to


function as a modality at all, whereas the _γ −_ _n −_ _n_ correlation method that I will describe only


necessitates solid angle coverage to increase efficiency. Furthermore, the _γ_ _−n−n_ technique could


function at any distance with a portable system, even if it requires long measurement times.

## **7.3 Neutron Double Scatter 2D Imaging**


Measurement of a double-scatter neutron provides a conical surface of possible source locations


with the vertex at the first neutron scatter ( _n_ 0 ) and axis defined by the location of two scatters. In


a traditional segmented scatter camera, each scatter is measured as a separate interaction within


any two detector cells of the measurement system. Crucially, the incident neutron energy and by


extension velocity of the incident neutron ( _v_ _n_ ) is also calculated from this measurement [104].


96


The outgoing energy following the first neutron scatter is calculated by the time-of-flight


(∆ _t_ _n_ 0 _,n_ 1 ) to the second scatter:



2

(7.3)
�



_E_ _n_ 1 = _[m]_ 2 _[n]_



_d_ _n_
� ∆ _t_ _n_ 0 _,n_ 1



where _d_ _n_ is the distance between the two scatters. The outgoing energy is then summed with the


energy lost due to proton recoil ( _E_ _p_ ) in the first scatter which gives the initial incident energy of


the neutron:


_E_ _n_ 0 = _E_ _p_ + _E_ _n_ 1 _._ (7.4)


The opening angle of the cone of possible source locations is


cos [2] ( _θ_ _n_ 1 ) = _[E]_ _[n]_ [1] _._ (7.5)

_E_ _n_ 0


The resulting cone of possible source locations is illustrated in Figure 7.2. Typically, a projection


distance has to be chosen in order to display the image formed from the overlapping regions of the


projected cones. The following section will show that by measuring a coincident gamma ray with


a double scattered neutron it is possible to calculate the distance from the first neutron scatter to


the possible source locations along the surface of the cone.

## **7.4 Gamma-Neutron-Neutron 3D Imaging**


An illustration of the first neutron scatter ( _n_ 0 ) and the correlated gamma ray is shown in Figure


7.3. _R_ _n_ and _R_ _γ_ are the distances from a possible source location to the neutron and gamma ray


interactions, respectively. Note that the second neutron scatter is omitted from this illustration,


but it’s shown in Figure 7.2. The goal is to solve for _R_ _n_ in order to constrain the possible source


location to the third dimension along the surface of the cone.


97


Figure 7.2: Illustration of the kinematics of a double neutron scatter in a scatter camera, resulting
in a cone of possible source locations.


The two unknown distances _R_ _n_ and _R_ _γ_, and the known distance _d_ triangulate the location of


the source along the azimuthal angle, _φ_, around the cone. These variables are related by the law of


cosines in a parametric equation


_R_ _γ_ [2] [=] _[ R]_ _n_ [2] [+] _[ d]_ [2] _[ −]_ [2] _[R]_ _[n]_ _[µd]_ (7.6)


where _µ_ is the cosine of the angle between the cone surface and the vector _[−→]_ _nγ_


_−→_
_nγ_
_µ_ = _R_ _n_ ( _φ_ ) _._ (7.7)

_d_ _[·]_ [ ˆ]


ˆ
_R_ _n_ is a unit vector pointing from the vertex of the cone to any possible source location along cone


surface. The locations of _γ_ and _n_ 0 interactions, and therefore the distance ( _d_ ) between them, are


known implicitly from the detectors that participated in each interaction.


The measured time difference between _γ_ and _n_ 0 ( _t_ _γ,n_ ) relates _R_ _n_ and _R_ _γ_ through



_t_ _γ,n_ = _[R]_ _[n]_




_[R]_ _[n]_ _−_ _[R]_ _[γ]_

_v_ _n_ _c_



(7.8)
_c_ _[.]_



98


Figure 7.3: The cone of possible source locations from neutron double scatter and a corresponding
correlated gamma ray. The second neutron scatter is not shown. The distances between the source
(yellow 4-pointed star) and first neutron scatter ( _R_ _n_ ) and gamma ray ( _R_ _γ_ ) are shown for one of the
possible locations along the surface of the cone. All other possible source locations lay somewhere
along the azimuthal ( _φ_ ) angle of the cone.


By substituting _R_ _γ_ from Eq. 7.8 into Eq. 7.6, the resulting quadratic equation can be solved in


terms of the distance from the first neutron interaction:



_c_ [2] _t_ _γ,n_ _v_ _n_ _−_ _dv_ _n_ [2] _[µ][ ±]_
~~�~~
_R_ _n_ ( _φ_ ) =



(7.9)
_c_ [2] _−_ _v_ _n_ [2]



_v_ _n_ [2] ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)] ~~�~~



Using these two solutions for image reconstruction is problematic, especially if the value of the


discriminant is significant and dominates the resolution of the detection system. Fortunately, only


one solution is physically possible, because the neutron cannot have a velocity exceeding _c_ . The


full proof of this is included in Appendix B. The valid solution is the one with the positive discrim

inant:



_c_ [2] _t_ _γ,n_ _v_ _n_ _−_ _dv_ _n_ [2] _[µ]_ [ +]
�
_R_ _n_ ( _φ_ ) =



_v_ _n_ [2] ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)] ~~�~~

(7.10)
_c_ [2] _−_ _v_ _n_ [2]



The parametric solution to Eq. 7.10 effectively cuts a slice of possible source locations from


the double neutron scatter cone from Figure 7.3. As a consequence, the distribution of possible


source locations resembles “donut" in 3D space, as shown in Figure 7.4. This torus-like shape is


99


analogous to PET’s line-of-response for a measured pair coincident gamma rays. Multiple such


events further constrain the distribution of possible source locations by superposition of the torus

like shapes in 3D space. The region of overlap among those shapes reveals the true source location.


Figure 7.4: Possible source locations for a single measured correlated events shown as colored
spheres. The first (red) and second (blue) neutron scatter define the central axis of the cone and
the opening angle, and the correlated gamma ray (green) constrains the radial distance to form the
resulting “donut" shape. The superposition of many donuts will reveal the source location in the
overlapping region. For illustrative purposes we show the same object from two different angles.

## **7.5 Image Reconstruction**


The solutions in Eqs. 7.5 and 7.10 provide the opening angle ( _θ_ ) of the cone and distance from


its vertex to possible source location ( _R_ _n_ ), but additional steps are necessary to provide possible


source locations. There are two ways to proceed with image reconstruction: the so-called list-mode


or bin-mode [107]. In list-mode each possible source location is stored in an array, for example


Cartesian ( _x, y, z_ ) coordinates. In bin-mode the space of possible source locations is divided up


into predefined bins of certain size and calculated source locations fill those bins. This distinction


is only significant for the purpose of choosing an advanced reconstruction method like Maximum


Log-likelihood Expectation Maximization (MLEM) or Stochastic Origin Ensemble (SOE). For


this work, SOE was used to improve image quality, and it was intuitive to store all possible source


locations in list-mode. The implementation of SOE is discussed in greater detail in Section 7.6.


100


In addition to calculating _R_ _n_ and _θ_, it’s also necessary to compute the unit vector between the


first and second neutron scatter:


_−−→_
ˆ _n_ 1 _n_ 0
_n_ = (7.11)

_d_ _n_


where _d_ _n_ is the distance between two interactions. This vector will have to be declined by the


opening angle of the cone, in any arbitrary direction. First, an axis has to be defined which points


90 _[◦]_ away from ˆ _n_ by taking the cross product between ˆ _n_ and any arbitrary vector ˆ _u_ and normalizing


the result


ˆ
_′_
_n_ = _[u]_ [ˆ] _[ ×]_ [ ˆ] _[n]_ (7.12)

_|n_ [ˆ] _[′]_ _|_


With this result, the original vector from the two neutron scatter points can be declined by the


opening angle of the cone:


_s_ ˆ = ˆ _n_ cos( _θ_ ) + sin( _θ_ )( _n_ [ˆ] _[′]_ _×_ ˆ _n_ ) (7.13)


This source vector, ˆ _s_, points to _one_ of the possible source locations, but it’s necessary to rotate


it around the azimuthal angle of the cone, _φ_ from Figure 7.3, in order to represent all possible


source locations. The vector ˆ _s_ can be rotated around axis ˆ _n_ by angle _φ_ through Rodrigues’ rotation


formula:


_s_ ˆ _rot_ = ˆ _s_ cos( _φ_ ) + (ˆ _n ×_ ˆ _s_ ) sin( _φ_ ) + ˆ _n_ (ˆ _n ·_ ˆ _s_ )(1 _−_ cos( _φ_ )) (7.14)


Once this vector is calculated, the source location can be determined by multiplying by the distance


_R_ _n_ .


101


The range of the azimuthal angle of the cone is constrained by


0 _[◦]_ _< φ <_ 360 _[◦]_ (7.15)


but in reality there has to be a finite number of possible source points stored per set of correlated


detected events. For this application, 100 points was sufficient for reconstructing a desired image.


Any greater number of source points increased computational time without any tangible improve

ments in image quality. Each correlated set of events produced 100 points Cartesian coordinates


of possible source locations, and the full list provided flexibility in how the final images were dis

played. I went a step further, and applied SOE to improve image quality, as explained in the next


section.

## **7.6 Stochastic Origin Ensemble**


SOE is an application of the Metropolis-Hastings algorithm that is used to improve the reconstruc

tion quality over standard back-projection. The new 3D imaging technique works just fine with


back-projection, but advanced reconstruction techniques aid with the lack of adequate correlated


counts. This is a particular problem for a technique that requires _γ −_ _n −_ _n_ particle coincidence.


SOE was chosen because it is relatively straight forward to implement and it has been shown to


improve the signal-to-noise and image quality in neutron imaging systems [108].


The basic idea behind SOE is to sample the measured quantities (time, interaction location, en

ergy resolution) with appropriate uncertainties and estimate the source distribution as a probability


density function (PDF). This is repeated for many iterations, as shown in Figure 7.5. The recon

structed source locations are displaced between iterations if certain criteria regarding new source


location density is met. This displacement rate decreases rapidly over during the first set of itera

tions, referred to as the “burn-in" period. Once the rate of displaced locations has stabilized and


adequate number of iterations is completed, the desired PDF is estimated as the density of source


locations averaged over all iterations with uncertainties given by the variance of all interactions,


102


excluding the initial burn-in period. Details of the SOE algorithm as applied to Compton imagers


is given in [109], and the principles are the same for neutron scatter cameras.


SOE can be computationally intensive, especially if the required number of iterations is large.


Individual iterations may also require substantial computational time if there are many source


locations, and if non-standard source density estimation is employed. Fortunately, SOE is in a


class of Markov chain Monte Carlo (MCMC) methods which means that multiple iterations can be


launched in parallel, and the final PDF can be determined from the average over all iterations. The


source displacement over parallel iteration sessions is shown in Figure 7.5.


Figure 7.5: The number of displaced source locations per iteration during a SOE reconstruction of
an image. This particular reconstruction was ran 10 times in parallel, as indicated by the legend.


The SOE method requires an accurate assessment of the source density between iterations. This


task is made difficult with small number of correlated counts (a few thousand) in three-dimensional


space. The simplest method of estimating density is by computing a multidimensional histogram.


However, subdividing just 1 m [3] of space into 1 cc parts requires a million voxels, and given only


a few thousand reconstructed source locations leaves the vast majority of the voxels empty or


with only one count. Obviously, this makes for a dismal estimation of the source density at each


location.


103


As a solution, a Kernel Density Estimator (KDE) was used to calculate the density at each


source location. This method provides for an estimate of source density at every single point,


regardless of how sparse the points are in space. A multidimensional KDE is defined as



ˆ
_f_ ( _**s**_ ) = [1]

_n_



_n_
� _K_ ( _**s**_ _−_ _**s**_ _**i**_ ) (7.16)


_i_ =1



where source locations are _s_ _i_ = ( _x_ _i_ _, y_ _i_ _, z_ _i_ ) _[T]_ for a total of _n_ . _K_ is the kernel function, for this


application the Epanechinkov kernel provided optimal results at reasonable CPU times. Besides


the choice of an appropriate kernel, it’s also necessary to select a bandwidth parameter, which


acts as a sort of smoothing factor. The bandwidth parameter is analogous to the size of voxels or


bins in the histogramming approach. If the bandwidth parameter is too large then the final image


will appear blurry and smeared out. Otherwise, if its too small then the source density may be


overestimated in certain areas leading to a distorted image. For this application, the bandwidth


parameter closest to the resolution of the system (2-6 cm) appeared to work the best. The Scikit

learn machine learning package for Python was used to compute the requisite density estimations


and multidimensional KDE computation [110].

## **7.7 Measurements and Simulations**


As a proof of concept, a neutron scatter camera called MINER was used to conduct preliminary


measurements [90]. MINER was adequate at proving the technique works, but it was primar

ily designed as a compact emergency response tool, rather than a high resolution system which


would show the technique’s full potential. Simulations of the MINER system with better, but cur

rently achievable, timing and interaction location resolutions were conducted and the comparison


between image resolutions are discussed in the following in this section.


104


### **7.7.1 Detection System and Setup**

MINER is an array of sixteen 7.62 _×_ 7.62 cm EJ-309 cylindrical detectors packaged in a larger


cylindrical form-factor for portability and symmetry which allows for omnidirectional (4 _π_ ) imag

ing. A photo of the opened system is shown in Figure 7.6. The portability comes at the expense of


imaging resolution because adjacent cells centers are only 11.9 cm apart.


Figure 7.6: A photo of MINER in open configuration.


Two equal strength, 26.7 _µ_ Ci, Cf-252 sources were measured 50 and 60 cm away from the


center of MINER. The two sources were placed 45 _[◦]_ apart as shown in Figure 7.7. The centers


of each detector cell were taken as the position of the incident particle interaction. MINER has a


timing resolution of approximately 2 ns and interaction location resolution of 2.2 cm.


The corresponding simulations assumed timing resolution of 200 ps and interaction location


resolution of 5 mm. The former is possible with fast photomultiplier tubes (PMTs) or silicon


photomultipliers (SiPMs) [111]. The latter can be achieved by using smaller detector cells, or


using multiple readouts to better localize the interaction withing the detector. MCNPX-PoliMi


was used to perform the requisite simulations [112].


105


Figure 7.7: Measurement configuration showing the position of the two Cf-252 sources with respect to MINER. The dimensions of the detector and source-to-detector distances are drawn in
correct proportions.

### **7.7.2 Point-source Image Results**


Traditional 2D images of the measured and simulated Cf-252 sources are shown in Figure 7.8.


Each source is marked by red (50 cm source) and blue (60 cm source) squares. The source points


from those marked regions were used to estimate the radial distance and azimuthal angle resolu

tions. These resolution results are discussed in Section 7.7.3.


Figure 7.9 essentially displays a top-down view of the sources by looking at source particle


densities projected on a polar plane. In all images and distributions shown each source point was


weighted by _r_ [4] in order to account for the efficiency of detecting two correlated particles.


In both measurement and simulation the two sources are clearly resolved in both radial distance


and angular space. The 2D image from the measurement shows some reconstruction artifacts,


likely caused by the application of SOE. These are largely due to the choice of a narrow bandwidth


parameter, which improves resolution at the cost of having these artifacts in the final reconstruction.


Nevertheless, the final image reconstruction of these point sources was not very sensitive to the


selection of a bandwidth parameter from 2 to 10 cm.

### **7.7.3 Radial Distance and Angular Resolutions**


It’s clear from Figures 7.8 and 7.9 that the images improve with better detector system resolution


parameters, but the images alone are not enough to quantify the improvement. For that purpose,


106


Figure 7.8: The measurement ( _left_ ) and simulated ( _right_ ) images with each reconstructed source
point weighted by _r_ [4] . Each source is marked by a blue (60 cm source) and red (50 cm source)

square.


Figure 7.9: The polar projection (top-down view) of the image reconstruction for both the ( _top_ )
measurement and ( _bottom_ ) simulation.


the reconstructed source locations were projected along radial distance and azimuthal angle, and


the results are shown in Figure 7.10. Peak locations and FWHM of the resulting 1D distributions


were used to estimate accuracy and resolution, respectively. Both parameters were estimated by


interpolating through the points in the distributions. The radial distribution and angular distribution


parameters are shown in Tables 7.1 and 7.2.


The relative resolution of the radial distance is the ratio of FWHM and peak location, and it


averaged at 26% for the measurement and 11% for the simulation. The angular resolution for the


measurement improved from FWHM of 23 _[◦]_ to 15 _[◦]_ with source-to-detector distance. The simu

107


|0.14 0.16 y r4|Col2|60 cm Measured 50 cm Measured 60 cm Simulated|
|---|---|---|
|0.04<br>0.06<br>0.08<br>0.10<br>0.12<br>ormalized counts weighted b||50 cm Simulated|
|20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br><br>0.00<br>0.02<br>N|20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br><br>0.00<br>0.02<br>N|20<br>30<br>40<br>50<br>60<br>70<br>80<br>90<br><br>0.00<br>0.02<br>N|


|7 8 9|Col2|Col3|60 cm Measured 50 cm Measured 60 cm Simulated|
|---|---|---|---|
|2<br>3<br>4<br>5<br>6<br>|||50 cm Simulated|
|0<br>50<br><br>0<br>|0<br>50<br><br>0<br>|0<br>50<br><br>0<br>|100<br>150<br>200<br>250<br>300<br>3|



Figure 7.10: The radial distance ( _left_ ) and azimuthal angle ( _right_ ) distributions for both measurement ( _solid_ ) and simulation ( _dashed_ ). The radial distance distribution describes the distance from
detector center. The source points were taken from the within the squares of the images in Figure
7.8, with matching color combinations.


lation results have an improved azimuthal FWHM of 11 _[◦]_ for both sources. There is an apparent


skewness of the radial distance distribution of the 60 cm source in the direction of the 50 cm source,


which may contribute to the increase in absolute FWHM. This is due to some 50 cm source points


present in the same angular region of the 60 cm source, which is due to the nearly double relative


efficiency of detecting correlated signature from a source that is 20% closer.


The peak location for the measurement is off by 5.8 cm for the 50 cm source. If the source


locations are not weighted by radial distance this discrepancy drops to 2.1 cm. By contrast the


60 cm source peak location is off by only 1.5 cm. This shift in peak location is not exhibited in


the simulated system with better timing and interaction location resolution. This effect is caused


by both the weighting of source locations and the presence of the 60 cm source. However, the


weighting skewed the radial distribution of the 50 cm source toward the 60 cm source due to


the significant overlap in the both radial distribution. By contrast the radial distributions of the


simulated sources were well separated, as seen in Fig. 7.10, and the peak locations matched the


true locations of the sources.


108


Table 7.1: Radial distribution (units in cm) parameters for each source in both measurement and
simulation

|Col1|Source Distance Peak Location FWHM|
|---|---|
|Measurement|50<br>55.8<br>13.5<br>60<br>61.5<br>15.1|
|Simulation|50<br>50.6<br>5.7<br>60<br>60.3<br>6.8|



Table 7.2: Azimuthal angular distribution parameters for each source in both measurement and
simulation

|Col1|Angular Position Peak Location FWHM|
|---|---|
|Measurement|45_◦_<br>47_◦_<br>15_◦_<br>90_◦_<br>91_◦_<br>23_◦_|
|Simulation|45_◦_<br>45_◦_<br>11_◦_<br>90_◦_<br>90_◦_<br>11_◦_|


### **7.7.4 Thunderbird Simulations**


The results shown so far are of simulations and measurements of Cf-252 point sources. How

ever, an extended source, one with actual physical dimensions, can better illustrate the utility and


limitations of source reconstruction methods, such as SOE used in this work. For that purpose,


I constructed a Cf-252 source in the shape of Sandia’s thunderbird logo that was 27.5 cm wide,


25.5 cm long and 2 cm thick in MCNP. MINER was again used as a detection system, and with


the same improved timing resolution of 200 ps and interaction location resolution of 5 mm. The


MCNP model of both the source and detector system is shown in Figure 7.11.


The thunderbird source was laid flat from the point of view of the detector system. In a typical


2D image, this source would appear as essentially a line source, or a thin rectangle. But the advan

tage of the 3D imaging reconstruction, is that the depth of the source can be revealed. Furthermore,


a top-down view of the source can be provided, just as it was with the polar projections in Figure


7.9, which would show the true nature of the source.


The image reconstruction of the thunderbird was performed in three ways: standard back

109


Figure 7.11: The top-view ( _left_ ) and angled side view ( _right_ ) of the MCNP model of MINER
detector cells and thunderbird shaped Cf-252 source.


projection, SOE with 2 cm bandwidth parameter, and SOE with 4 cm bandwidth parameter. All


three results are shown in Figure 7.12. In the back-projected image the thunderbird is visible,


but through a cloud of non-source reconstructions. These are the result of throwing 100 source


locations per correlated event, 99 of which will not correspond to the true source locations. The


overlap of these points is more likely at the true source location, which is why the thunderbird


shines through the image. The goal of SOE is to reduce the number of non-source reconstruction,


and narrowing down on the correct _φ_ for each correlated event.


However, as previously discussed in Section 7.6, SOE technique requires the choice of a band

width parameter, which acts as a width of the kernel used for the density calculation. This was not


as consequential for point sources, but makes a noticeable difference in extended sources like the


thunderbird. Thunderbird image reconstructions using both 2 cm and 4 cm bandwidth parameters


are shown at the bottom of Figure 7.12. The 2 cm image is sharper, but has mis-reconstructed


source points floating around it and the body of the thunderbird itself is breaking apart. These


are the side effects of a bandwidth parameter that is getting to be too narrow. During the re

construction process, source points become isolated islands, or hot-spots, which can make them


110


over-represented in certain areas of the image. With the wider 4 cm bandwidth parameter, these


problems are largely mitigated, but at the cost of final image resolution. In fact, it would be diffi

cult to discern that the original source was a thunderbird. Nevertheless, SOE is still a valuable tool


in this case, since it increases the overall number of reconstructed source points at the true source


location, and therefore improving signal-to-noise ratio.


(a) back-projection


(b) SOE with 2 cm bandwidth (c) SOE with 4 cm bandwidth


Figure 7.12: Image reconstructions of a thunderbird shaped Cf-252 source performed using (a)
back-projection and SOE with (b) 2 cm and (c) 4 cm bandwidth parameters. The images are
top-down view, with all source points between _−_ 5 _< z <_ 5 projected onto an _x −_ _y_ plane.


111


## **7.8 System Resolution and Uncertainty Analysis**

System resolution is quantified here by the source-to-detector distance _R_ and the opening angle


of the projected cone _θ_ . Apart from the interaction location, the remaining measured sources of


uncertainties are _n −_ _n_ and _γ −_ _n_ timing and neutron pulse amplitude. The impact of all three can


be visualized by assuming timing resolution of 2 ns and energy resolution of 10%, and then solving


Eqs. 7.5 and 7.10. The result of this is shown in Figure 7.13. As expected, _γ_ _−n_ timing only effects


the radial distance, which makes sense because it’s introduced into the equations specifically to


solve for it. The remaining sources of uncertainty, neutron pulse amplitude, and _n −_ _n_ timing,


effect both quantities of interest although the sign of the correlation is different with each.


Figure 7.13: Visualization of the spread source-to-detector distance and the opening angle as a
function (red) _n −_ _n_ and (green) _γ −_ _n_ timing, and (blue) neutron pulse amplitude uncertainty.
Each source of uncertainty is treated separately, and the results are displayed in different colors,
the combined result is shown in black. A timing resolution of 2 ns and energy resolution of 10%
was assumed


Uncertainty quantification on _R_ was performed using linear error propagation theory [113]


which also included contribution from interaction location resolution. The overall timing resolu

tion had over twice the error contribution compared with the interaction location resolution. The


gamma ray timing was nearly six times more important than the neutron timing, which makes sense


112


given the relative speed of each particle. By contrast the neutron interaction location contributed


nearly an order of magnitude more compared with the gamma ray interaction location. The first


neutron interaction location had double the contribution of the second interaction.


In conclusion, the gamma ray timing resolution and neutron interaction location resolution are


the primary contributors to uncertainty in radial source-to-detector distance. This was true for the


measurement with timing resolution of 2 ns and interaction location resolution of 3 cm. At the


simulated resolutions of 200 ps and 5 mm, the uncertainty in the proton recoil energy from the


first neutron scatter ( _E_ _p_ ) was the limiting factor. This includes the effects of energy resolution


and calibration of the detector and measurement of light output response. The current practice


involves fitting light output response to an empirical formula [54, 114]. Improvements could be


made by better characterization of the detector response, but the estimation of the proton recoil


energy would ultimately be limited by the low energy resolution of organic scintillators.

## **7.9 Augmented Reality**


3D radiation imaging is a powerful tool, but it’s difficult to display the results on a monitor dis

play or a flat piece of paper. There are limits to what can be shown through the use of multiple


projections, or views of the source, as used in Figures 7.8 and 7.9. Ideally, one would display the


3D reconstructed image of a source as a hologram, and preferably in the context of the real world


surroundings of said source. Fortunately, this thesis is being written in 2017, the future is now, and


the technology exists to accomplish just that.


Augmented Reality (AR) is a live display which allows a used to "augment" the real world


elements through computer generated graphics, or other sensory inputs. This differs from virtual


reality, where the entire sensory space is computer generated, and the user is unaware of their actual


physical surroundings. Microsoft has developed AR capable headset called the HoloLens, which


is pictured in Figure 7.14. The HoloLens is a head-mounted portable computer with smartglasses


and variety of cameras, and other sensors. Smartglasses display either 3D holograms or 2D flat


113


projections that appear as part of the physical world. The cameras and sensors map out the physical


surroundings and track movement of the user, which allows the visualizations to stay in place and


interact with the real world. For example, a hologram of a coffee mug can be placed on top of a


real table, and the mug will maintain its position as the user moves around the room.


Figure 7.14: Microsoft’s HoloLens.


Fortunately for me, researchers at Sandia have already obtained a HoloLens for other unrelated


work and had experience getting it to display holograms. I collaborated with them, providing


them with the 3D reconstructed image data, with the goal of having the images displayed through


the HoloLens. A demonstration of the technology and 3D radiation method was given during the


2016 Consortium for Verification Technology Workshop. The results of these efforts are difficult


to show on paper in this dissertation, but an example of the aforementioned thunderbird source


as seen through a HoloLens is shown in Figure 7.15. The thunderbird source hologram floats in


space, and can be inspected from any angle that the user chooses to look at it.


The other useful feature of this technology is that it allows for display of holograms behind a


physical barrier. For example, it is possible to render pipes that are installed inside a wall. This


may be applicable to emergency response scenarios, where a source is hidden inside a figurative


black box, and 3D imaging can provide the physical dimensions of the source without the need to


open up the container. Another similar application in treaty verification may involve the imaging


of pits that are stored inside drums. AR would allow an inspector to walk around the drum and


visualize the object inside without the need to open anything.


114


Figure 7.15: Thunderbird source displayed as a hologram as seen through a HoloLens. The corner
of a virtual MINER detection system is on the left, and a bemused dog on the right.

## **7.10 Conclusions**


A new method for 3D reconstruction of sources that emit correlated gamma rays and neutrons


was demonstrated. The technique is distinguished from traditional 3D radiation imaging methods


by only requiring a single-sided measurement of the source. Parallax by comparison would be


restricted by system size and require close enough source-to-detector distances to function at all.


This makes the _γ_ _−n−n_ technique potentially valuable for nuclear inspection, emergency response


and treaty verification, where multiple views of the object of interest may be restricted, even though


the location of the source is known. The method proposed here is an extension of double neutron


scatter imaging, combined with a correlated gamma ray to constrain the source location to the third


dimension.


It is possible to resolve two sources of equal strength 10 cm apart using a portable scatter


camera with sub-optimal timing and angular resolution. Simulated results with improved detector


system resolution show a substantial improvement in radial resolution, and a modest improvement


in angular resolution. Such improvements should be attainable with current technology, such as


new photo-detectors like SiPMs. Furthermore, the detector cell geometry and size could be further


optimized to improve localization resolution while maintaining adequate efficiency.


The efficiency of detecting a correlated neutron-gamma pair decreases as _r_ _[−]_ [4], where _r_ is the


115


radial distance between source and detector system center. Therefore, it is not an ideal technique


for standoff detection, although efficiency could be scaled with number and size of detector cells.


However, this technique could prove valuable in application where access to the object of interest


is limited. For example, this could include inspection of nuclear facilities for safeguards or treaty


verification. Furthermore, neutron sources that emit correlated gamma rays (e.g. fission, ( _α_,n)) are


ubiquitous and include the vast majority of sources of concern in the aforementioned applications.


116


## **CHAPTER 8**

# **Summary, Conclusions and Future Work**

## **8.1 Summary and Conclusions**

This thesis explored a new method for probing fission chain dynamics through correlated mea

surements of gamma rays and neutrons. Fission chains are a defining and unique feature of fissile


material, whose detection and characterization is needed for diverse applications such as non

proliferation, safeguards, emergency response, and treaty verification. The context of those appli

cations was given in Chapter 1. Chapter 2 explains the basic definitions and properties of fissile


material, along with an overview of established measurement techniques. However, these tech

niques were historically developed around neutron counting with thermal capture detectors. The


alternative use of organic scintillators proposed in this work provides three new capabilities:


1. Fast (sub-nanosecond) timing resolution, which allows for distinction between fission events


in a chain.


2. Measurement of elastic proton recoil, which puts an upper bound estimate on the incident


neutron energy.


3. Gamma ray detection, which provides a clean start time of a fission event that gave birth to


the detected particle.


The best practices and methodology for extracting that relevant information from digitized


pulses is laid out in Chapter 3. In prior work, these signatures were combined into TCPH distri

117


butions, which were shown to be sensitive to fissile material and neutron multiplication [41, 42].


In Chapter 4 TCPH analysis was advanced by building an empirical model, and fitting it to mea

sured distributions. The results showed that TCPH distributions were not only sensitive to the level


of neutron multiplication, but also the type of reflector material. However, the methodology was


somewhat convoluted, partly due to the two-dimensional aspect of TCPH.


The TOFFEE distribution was introduced in Chapter 5, which combined the same signature


of TCPH, but into a one-dimensional distribution. A template-based approach was used to test


TOFFEE in two treaty verification scenarios: dismantlement and item confirmation. In the former


case, WGPu and HEU with and without reflector were compared, and the latter involved a test


to determine the authenticity of the same fissile materials surrounded by a reflector. Under an


arbitrary performance threshold of 99% True Positive (TP) and 1% False Positive (FP) the WGPu


objects were verified within several seconds. By contrast, HEU confirmation required several


minutes, because of the limited number of induced fissions created even under active interrogation.


These tests revealed that TOFFEE was sensitive to the amount and configuration of fissile material,


but did not provide a characterization of the object.


In depth characterization required a physical model, which was developed in Chapter 6 from


two-region point kinetics theory. The resulting equations provided the time-dependent neutron


populations in fissile material surrounded by a reflector, which were fitted to the positive side of


the TOFFEE distribution. Positive linear relationships were established between the estimated


and actual prompt neutron periods of the bare cases. And same trends were evident between esti

mated and actual neutron multiplication of the reflected cases. The estimated physical parameters


also provided a way to discriminate between different reflector material types, from lightweight


aluminum to heavy tungsten.


Chapter 7 introduced a new 3D technique enabled by detection of a correlated gamma ray


with a double scatter neutron. Preliminary proof-of-concept measurements of Cf-252 showed that


it is possible to resolve sources that are 10 cm apart, even with a neutron scatter camera with


optimized for efficiency rather than resolution. Possibilities with better performing and possible


118


future systems was explored through simulations. Uncertainty quantification was provided as a


guide for improvement of future detection systems. Finally, AR was proposed as the best way of


visualizing the reconstructed 3D images.

## **8.2 Future Work**


An alternative approach could be explored which combines the elements of analysis presented in


Chapters 4 and 5. The empirical model of the TCPH distribution started with a like-fission distri

bution, and then smeared it to incorporate the perturbation from fission chain dynamics. TOFFEE


distributions showed that the difference between non-multiplying and multiplying measurements


is the addition in generation time, _T_ _g_, between detected correlated particles in the latter. Therefore,


the distribution of generation time differences of fissions in a chain, convolved with the TOFFEE


distribution built from only like-fission events, should produce the TOFFEE distribution expected


from a multiplying fissile material. A Cf-252 measurement could be a surrogate for like-fission


TOFFEE distribution. And the distribution of fission generation time differences could be built


with either Monte Carlo, or a variation on the two-region point kinetics model shown in Chapter


5. Regardless of the means of creating that distribution, the underlying physical parameters would


provide relevant information about measured fissile material.


The 3D imaging technique was proven to work with Cf-252, but the implicit assumption is that


the detected gamma ray and neutron are born at the same space and time. This assumption does


not hold in the presence of fission chains, therefore additional work is required to image fissile


material. To solve this problem, it’s necessary to develop a method which could determine and


compensate for the time and space difference between birth of correlated particles. A solution


would provide a way to simultaneously image fissile material, and measure the underlying fission


chain dynamics. This is actually a difficult problem, and may require assumptions about the aver

age distance separating fission events in a chain. But a successful effort would provide a way for


a passive imaging system to reconstruct both the average fission chain length (multiplication) and


119


the volumetric distribution of fissile material from a single measurement.


120


## **APPENDIX A**

# **Source Code**

## **A.1 Pulse Parsing**

' ' ' Raw wavedata p r o c e s s i n g module


This module i s designed to clean waveform and time tag data and a l s o
r e t u r n amplitude and PSD parameters
' ' '


import numpy as np
from scipy import i n t e g r a t e
import m a t p l o t l i b . pyplot as p l t
import o p e r a t o r


def time_order ( time_stamps, f r e q =250, t s _ b i t s =31) :
""" Orders time stamps s e q u e n t i a l l y


Time stamps which o s c i l l a t e due to number of b i t s are re _−_ ordered
s e q u e n t i a l l y . This f u n c t i o n may be u s e f u l f o r cases where f u l l waveforms
are not saved but time stamps are s t i l l n e c e s s a r y f o r a n a l y s i s .


Parameters

_−−−−−−−−−−_


time_stamps : array, shape (N, ), o p t i o n a l
Timestamps of the d i g i t i z e r, must be the same l e n g t h as number
of waves .
f r e q : int, o p t i o n a l
Frequency of the time clock in MHz
d e f a u l t i s 250
t s _ b i t s : int, o p t i o n a l
Number of b i t s of the s t o r e d time stamp value, which determines
the maximum timestamp value (2** t s _ b i t s ) .
d e f a u l t i s 31


Returns

_−−−−−−−_


time_ns : a r r a y
Event times in ns

"""


121


negindx = np . f l a t n o n z e r o ( np . d i f f ( time_stamps * 1 . ) <0)
time_ns = time_stamps *1.
f o r i in negindx :
time_ns [ i +1:]+=2.** t s _ b i t s
time_ns = time_ns * 1 . / ( f r e q *1. e6 ) *1. e9

i f ( np . d i f f ( time_ns ) <0) . any ( ) :
r a i s e Exception ( " Time stamps are not s e q u e n t i a l, check clock i n p u t s ! " )
r e t u r n time_ns


c l a s s Eventdata ( o b j e c t ) :
' ' '
Object t h a t p r o c e s s e s waveforms and timestamps, to produce amplitude,
pulse shape d i s c r i m i n a t i o n parameters and time of events . Mu l ti pl e
methods are a v a i l a b l e f o r psd and time pick _−_ o f f .


Parameters

_−−−−−−−−−−_


waves : ndarray, shape (N, wave_length ) :
Raw waves from the d i g i t i z e r


Examples

_−−−−−−−−_


Take raw n e g a t i v e p o l a r i t y pulses, i n v e r t, b a s e l i n e s u b t r a c t, apply
t h r e s h o l d
and e x t r a c t amplitude, pulse shape parameters and timing .


>>> import snappy . waveparser as wp
>>> import numpy as np
>>> from scipy . s t a t s import lognorm
>>> num_waves = 10000
>>> x = np . arange (100)
>>> waves = 2.**14 _−_ 100 _−_ np . random . normal ( lognorm . pdf ( np . t i l e ( x, ( num_waves

, 1 ) ),10,20) *1000)
>>> ev = wp . Eventdata ( waves )
>>> ev . i n v e r t ( dynamic_range =14)
>>> ev . b a s e l i n e ( b l i n e =5)
>>> ev . t h r e s h o l d ( t h r e s h o l d =200, c e i l i n g =500, mode= 'sum ' )
>>> amp = ev . get_amp ( mode= 'sum ' )
>>> psd = ev . psd_cdf ( f r a c =0.2, 0 . 9 )
>>> time_stamps = np . f l o o r ( np . l i n s p a c e (0,2**31, num_waves ) )
>>> time_ns = ev . t i m e _ d e r i v a t i v e ( f r a c t i o n =0.5, delay =1, time_stamps=
time_stamps, f r e q =500)
' ' '


def _ _ i n i t _ _ ( s e l f, waves ) :
s e l f . waves = waves


waves = p r o p e r t y ( o p e r a t o r . a t t r g e t t e r ( ' _waves ' ) )
@waves . s e t t e r

def waves ( s e l f, w) :
i f w. ndim != 2: r a i s e Exception ( "Waves must be a 2D a r r a y " )
s e l f . _waves = w
s e l f . r e s e t ( )


def r e s e t ( s e l f ) :
' ' ' Resets a l l a t t r i b u t e s to i n i t i a l i n s t a n c e c r e a t i o n


Function may be u s e f u l when s e t t i n g d i f f e r e n t t h r e s h o l d s l e v e l s form


122


the command l i n e .

' ' '
s e l f . i n d _ c l e a n = np . arange ( s e l f . waves . shape [ 0 ] ) # indexes of cleaned

a r r a y s
s e l f . p u l s e s = s e l f . waves . copy ( )


def i n v e r t ( s e l f, dynamic_range ) :
' ' ' I n v e r t s waveforms i f they are n e g a t i v e p o l a r i t y


Parameters

_−−−−−−−−−−_


dynamic_range : i n t
The number of b i t s in the dynamic range of the d i g i t i z e r, which
determines the maximum value in waves (2** d r _ b i t s ) .
' ' '


s e l f . p u l s e s = 2** dynamic_range _−_ s e l f . p u l s e s


def b a s e l i n e ( s e l f, b l i n e =5) :
' ' ' Applies b a s e l i n e c o r r e c t i o n


Parameters

_−−−−−−−−−−_


b l i n e : i n t
Number of p o i n t s used f o r b a s e l i n e s u b t r a c t i o n a t the begining
of the pulse t r a i n
d e f a u l t i s 5

' ' '
s e l f . p u l s e s = s e l f . pulses _−_ np . mean ( s e l f . p u l s e s [ :, 0 : b l i n e ], a x i s =1, keepdims=
True, dtype= ' i4 ' )


def t h r e s h o l d ( s e l f, t h r e s h o l d, c e i l i n g =np . inf, mode= ' t r a p z ' ) :
' ' ' Applied a t h r e s h o l d c u t t i n g out some p u l s e s


Parameters

_−−−−−−−−−−_


t h r e s h o l d : f l o a t
Threthold in d i g i t i z e r u n i t s below which to cut out the p u l s e s .
c e i l i n g : f l o a t
Upper t h r e s h o l d above which p u l s e s are cut, d e f a u l t i s i n f .
' ' '
amp = s e l f . get_amp ( mode )
remove_ind = np . where ( np . l o g i c a l _ o r (amp< t h r e s h o l d, amp> c e i l i n g ) ) [ 0 ]

s e l f . i n d _ c l e a n = np . d e l e t e ( s e l f . ind_clean, remove_ind )
keep_ind = np . where ( np . l o g i c a l _ a n d (amp>= t h r e s h o l d, amp<= c e i l i n g ) ) [ 0 ]

s e l f . p u l s e s = s e l f . p u l s e s [ keep_ind ]


def p l o t _ p u l s e s ( s e l f, pnum ) :
' ' ' P l o t some number of random p u l s e s


Parameters

_−−−−−−−−−−_


pnum : i n t
Number of waves to p l o t
' ' '


ind = np . random . r a n d i n t (0, s e l f . p u l s e s . shape [ 0 ], pnum )
p l t . p l o t ( s e l f . p u l s e s [ ind ] . T)


123


p l t . show ( )


def get_amp ( s e l f, mode= ' t r a p z ' ) :
""" C a l c u l a t e wave amplitude of the waveform


Parameters

_−−−−−−−−−−_


mode : { ' t r a p z ', ' peak ', ' sum ' } :
The type of camplitude c a l c u l a t i o n to perform


Returns

_−−−−−−−_


amp : a r r a y
E s t i m a t i o n of the amplitude of the

"""


i f ( mode== ' t r a p z ' ) :
s e l f . amp = np . t r a p z ( s e l f . p u l s e s )
e l i f ( mode== ' peak ' ) :
s e l f . amp = s e l f . p u l s e s . max ( 1 )
e l i f ( mode== ' sum ' ) :
s e l f . amp = s e l f . p u l s e s . sum ( 1 )
e l s e :

r a i s e ValueError ( " I n v a l i d i n p u t f o r mode" )
r e t u r n s e l f . amp


def p s d _ r a t i o ( s e l f, sgate, l g a t e, p r i o r =5) :
' ' ' C a l c u l a t e d the psd parameter using charge i n t e g r a t i o n t e c h n i q u e .


Parameters

_−−−−−−−−−−_


s g a t e : i n t
Length of the s h o r t gate, in d i g i t i z e r u n i t s .
l g a t e : i n t
Length of the long gate, in d i g i t i z e r u n i t s
p r i o r ( i n t ) : Number of p o i n t s before pulse .


Returns

_−−−−−−−_


psd : ndarray, shape (N, )
1 _−_ D a r r a y of PSD parameters corresponding to each wavelendth
' ' '


numW, lenW = s e l f . p u l s e s . shape
lamp = np . zeros (numW)
samp = np . zeros (numW)
ind_max = s e l f . p u l s e s . argmax ( a x i s =1)
l s t a r t = ind_max _−_ p r i o r
lend = l s t a r t + l g a t e
send = lend

s s t a r t = send _−_ s g a t e
f o r i in range (numW) :
# check i f the pulse i s v a l i d
i f ( l s t a r t [ i ] >0 or s s t a r t [ i ] >0 or lend [ i ] <lenW or send [ i ] <lenW ) :
lamp [ i ] = s e l f . p u l s e s [ i, l s t a r t [ i ] : lend [ i ] ] . sum ( )
samp [ i ] = s e l f . p u l s e s [ i, s s t a r t [ i ] : send [ i ] ] . sum ( )
psd = np . nan_to_num ( samp * 1 . / lamp )

r e t u r n psd


124


def psd_cdf ( s e l f, f r a c 1 =0.1, f r a c 2 =0.9) :
' ' ' Cal cate the time between f r a c t i o n a l i n t e g r a l s of the pulse


Uses the t r a p i z o i d a l r u l e to c a l c u l a t e the time a t a f r a c t i o n of the
t o t a l pulse i n t e g r a l, and uses the d i f f e r e n c e to c a l c u l a t e the PSD
parameter .


Parameters

_−−−−−−−−−−_


f r a c 1 : f l o a t
F i r s t i n t e g r a l f r a c t i o n, the d e f a u l t i s 0 . 1 .
f r a c 2 : f l o a t
Second i n t e g r a l f r a c t i o n .


Returns

_−−−−−−−_


psd : array, shape (N, )
PSD parameters c o r r e s p i n d i n g to each pulse in the t r a i n .
' ' '


prob = i n t e g r a t e . cumtrapz ( s e l f . p u l s e s ) / i n t e g r a t e . t r a p z ( s e l f . p u l s e s ) [ :,
None ]
nrow, ncol = prob . shape
rows = np . arange ( nrow )
time = np . zeros ( shape =(2, nrow ) )
f o r i, f in enumerate ( [ frac1, f r a c 2 ] ) :
y0 = np . argmax ( prob >f, a x i s =1) _−_ 1
x0 = prob [ rows, y0 ]
x1 = prob [ rows, y0 +1]


_−_ _−_
time [ i ] = y0 + np . d i v i d e ( ( f x0 ), ( x1 x0 ) )
time = np . nan_to_num ( time )
psd = time [1] _−_ time [ 0 ]

r e t u r n psd


def time_cdf ( s e l f, t f r a c, time_stamps, f r e q =250, t s _ b i t s =31) :
' ' ' Returns event time using f r a c t i o n a l i n t e g r a l of the pulse


The cdf of each pulse i s c a l c u l a t e d and the time a t some c o n s t a n t
f r a c t i o n of i t i s used . This method should not be used f o r data with
p u l s e s of varying shapes, as with mixed neutron and gamma data s e t s .


Parameters

_−−−−−−−−−−_


t f r a c : f l o a t
F r a c t i o n of cummulative i n t e g r a l f o r time p i c k o f f
time_stamps : array, shape (N, )
Timestamps of the d i g i t i z e r, must be the same l e n g t h as number
of waves .
f r e q : int, o p t i o n a l
Frequency of the time clock in MHz
d e f a u l t i s 250
t s _ b i t s : int, o p t i o n a l
Number of b i t s of the s t o r e d time stamp value, which determines
the maximum timestamp value (2** t s _ b i t s ) .
d e f a u l t i s 31


Returns


125


_−−−−−−−_


time_ns : array, shape (N, )
Array of event times in nanoseconds a s s o c i a t e d with each pulse .


Notes

_−−−−−_


. . f i g u r e : : . . / . . / . . / images / time_cdf . png
: a l i g n : c e n t e r
: width : 10cm


A pulse and the corresponding cdf from which the time i s picked
based on some c o n s t a n t f r a c t i o n .

' ' '


i f ( time_stamps . s i z e != s e l f . waves . shape [ 0 ] ) :
r a i s e ValueError ( "Number of time stamps must match number of waves ! " )
time_stamp_ns = time_order ( time_stamps, freq, t s _ b i t s )
time_stamp_ns = time_stamp_ns [ s e l f . i n d _ c l e a n ]
prob = i n t e g r a t e . cumtrapz ( s e l f . p u l s e s ) / i n t e g r a t e . t r a p z ( s e l f . p u l s e s ) [ :,
None ]
nrow, ncol = prob . shape
rows = np . arange ( nrow )
time = np . zeros ( shape =(1, nrow ) )
f o r i, f in enumerate ( [ t f r a c ] ) :
y0 = np . argmax ( prob >f, a x i s =1) _−_ 1
x0 = prob [ rows, y0 ]
x1 = prob [ rows, y0 +1]


_−_ _−_
time [ i ] = y0 + np . d i v i d e ( ( f x0 ), ( x1 x0 ) )
time = np . nan_to_num ( time )
time [ 0 ] [ time [0] <0] = 0
time_ns = time_stamp_ns + time [ 0 ] / ( f r e q *1. e6 ) *1. e9
r e t u r n time_ns


def t i m e _ d e r i v a t i v e ( s e l f, f r a c t i o n, delay, time_stamps, f r e q =250, t s _ b i t s
=31) :
' ' ' Returns event time using d e r i v a t i v e method .


This method t a k e s each wave and with delay s u b t r a c t s some f r a c t i o n
of i t s e l f . When ` f r a c t i o n ` and ` delay ` are both one t h i s method i s
e q u i v a l e n t
to t a k i n g the d e r i v a t i v e of the pulse and looking f o r the zero c r o s s i n g
time .


The optimal ` f r a c t i o n ` w i l l depend on pulse shape, a l a r g e r delay has
the a f f e c t of smoothing the pulse . T y p i c a l l y a ` delay =1 ` i s
s u f f i c i e n t .


Parameters

_−−−−−−−−−−_


f r a c t i o n : f l o a t
F r a c t i o n of the i n i t i a l pulse to s u b t r a c t
delay : i n t
The delay of the pulse t h a t w i l l be s u b t r a c t e d
time_stamps : array, shape (N, )
Timestamps of the d i g i t i z e r, must be the same l e n g t h as number
of waves .
f r e q : int, o p t i o n a l


126


Frequency of the time clock in MHz
d e f a u l t i s 250
t s _ b i t s : int, o p t i o n a l
Number of b i t s of the s t o r e d time stamp value, which determines
the maximum timestamp value (2** t s _ b i t s ) .
d e f a u l t i s 31


Returns

_−−−−−−−_


time_ns : array, shape (N, )
Array of event times in nanoseconds a s s o c i a t e d with each pulse .


Notes

_−−−−−_


This method i s e q u i v a l e n t to the d i g i t a l implementation of analog
c o n s t a n t f r a c t i o n d i s r i m i n a t i o n, see [ 1 ] _ .


. . f i g u r e : : . . / . . / . . / images / t i m e _ d e r i v a t i v e . png
: a l i g n : c e n t e r
: width : 10cm


A pulse and the corresponding d e r i v a t i v e, the zero c r o s s i n g time
i s used f o r time e s t i m a t i o n .


References

_−−−−−−−−−−_


. . [ 1 ] A. Fallu _−_ Labruyere, H. Tan, W. Henning, W.K. Warburton, " Time
r e s o l u t i o n s t u d i e s using d i g i t a l c o n s t a n t f r a c t i o n d i s c r i m i n a t i o n ",
Nucl . I n s t . Meth . Section A, vol . 579, 1, pp . 247 _−_ 251, 2007.


' ' '


i f ( time_stamps . s i z e != s e l f . waves . shape [ 0 ] ) :
r a i s e ValueError ( "Number of time stamps must match number of waves ! " )
time_stamp_ns = time_order ( time_stamps, freq, t s _ b i t s )
time_stamp_ns = time_stamp_ns [ s e l f . i n d _ c l e a n ]

d i f f = s e l f . p u l s e s [ :, 1 * delay : ] * f r a c t i o n _−_ s e l f . p u l s e s [:,: _−_ 1* delay ]
x_max = d i f f . argmax ( 1 )
# s h i f t d i f f by x_max, each row i s independent
rows, column_indices = np . ogrid [ : d i f f . shape [ 0 ], : d i f f . shape [ 1 ] ]
r o l l = d i f f . shape [ 1 ] _−_ x_max
r o l l [ r o l l < 0] += d i f f . shape [ 1 ]
column_indices = column_indices _−_ r o l l [ :, np . newaxis ]

d i f f _ s h i f t = d i f f [ rows, column_indices ]
# f i n d index a f t e r zero c r o s s i n g
x2 = np . argmax ( d i f f _ s h i f t <0,1) + x_max
x2 [ x2>= d i f f . shape [ 1 ] ] = d i f f . shape [1] _−_ 1
x1 = x2 _−_ 1
y1 = d i f f [ range ( d i f f . shape [ 0 ] ), x1 ] * 1 .
y2 = d i f f [ range ( d i f f . shape [ 0 ] ), x2 ] * 1 .

_−_
time = x1 *1. + y1 * 1 . / ( y1 y2 )
time = np . nan_to_num ( time )
time_ns = time_stamp_ns + time / ( f r e q *1. e6 ) *1. e9
r e t u r n time_ns


127


## **A.2 Pulse Shape Discrimination**

' ' ' PSD data p r o c e s s i n g module


Module f o r t u r n i n g PSD parameters i n t o p r o b a b i t i e s f o r a number of d e s i r e d
c l a s s e s .


' ' '


import numpy as np
import m a t p l o t l i b . pyplot as p l t
from m a t p l o t l i b . c o l o r s import LogNorm
from scipy . optimize import c u r v e _ f i t
from scipy . c l u s t e r . vq import kmeans2, whiten
import p i c k l e
from scipy import i n t e r p o l a t e


def skew2 ( x, E, S1, S2 ) :
' ' ' Skew normal d i s t r i b u t i o n


Args :

x ( a r r a y [T ] ) : An a r r a y of data p o i n t s f o r each s l i c e .
E ( a r r a y [K] ) : Means f o r each c l a s s .
S1 ( a r r a y [K] ) : P o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
S2 ( a r r a y [K] ) : Negative s t a n d a r d d e v i a t i o n f o r each c l a s s .
Returns : E

y ( a r r a y [K, T ] ) : Normalized skewed g au s si a n values
' ' '


# check i f i n p u t i t the proper format
i f not np . i s s c a l a r (E) and E . size >1: E = np . reshape (E, ( _−_ 1,1) )
i f not np . i s s c a l a r ( S1 ) and S1 . size >1: S1 = np . reshape ( S1, ( _−_ 1,1) )
i f not np . i s s c a l a r ( S2 ) and S2 . size >1: S2 = np . reshape ( S2, ( _−_ 1,1) )


r e t u r n 2 . / ( S1+S2 ) * ( normpdf ( x, E, S1 ) *( x>=E) + normpdf ( x, E, S2 ) *( x<E) )


def normpdf ( x, mu, sigma ) :
' ' ' C a l c u l a t e the normalized Gaussian values .


Args :

x ( a r r a y [T ] ) : Array of values .
mu ( a r r a y [K] ) : Array of means f o r each c l a s s .
sigma ( a r r a y [K] ) : Array of means f o r each c l a s s .
Returns :

y ( a r r a y [K, T ] ) : Array of g au s si a n values .
' ' '
mu = np . a r r a y (mu)

sigma = np . a r r a y ( sigma )

i f mu. size >1 : mu = mu. reshape (( _−_ 1,1) )
i f sigma . size >1 : sigma = sigma . reshape (( _−_ 1,1) )
u = ( x _−_ mu) / np . abs ( sigma )

_−_
y = ( 1 . / ( np . s q r t ( 2 . * np . pi ) ) ) *np . exp( u*u / 2 . )
r e t u r n y


def gauss_2 ( x, alpha, E_0, E_1, S1_0, S1_1 ) :
' ' ' Returns b e s t double g au s si a n f i t
This i s a workaround so the f u n c t i o n can be c a l l e d by curve f i t t i n g t o o l
' ' '


128


r e t u r n ( alpha *normpdf ( x, E_0, S1_0 ) / S1_0 + (1. _−_ alpha ) *normpdf ( x, E_1, S1_1 ) /
S1_1 )


def gauss_1 ( x, E_0, S1_0 ) :
' ' ' Returns b e s t s i n g l e g au s si a n f i t


This i s a workaround so the f u n c t i o n can be c a l l e d by curve f i t t i n g t o o l
' ' '
r e t u r n normpdf ( x, E_0, S1_0 ) / S1_0


def calcProb ( x, w, E, S1, S2 ) :
' ' ' C a l c u l a t e s the p o s t e r i o r _−_ p r o b a b i l i t y ( P (K| x,D) ) f o r each p o i n t x and
c l a s s K


Args :

x : ( a r r a y [T ] ) : Array of PSD parameters .
w ( a r r a y [K] ) : Weight f o r each c l a s s .
E ( a r r a y [K] ) : Means f o r each c l a s s .
S1 ( a r r a y [K] ) : P o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
S2 ( a r r a y [K] ) : Negative s t a n d a r d d e v i a t i o n f o r each c l a s s .
Returns :

probs ( a r r a y [K, T ] ) : P r o b a b i l i t i e s f o r each c l a s s f o r each event .
' ' '


# Check number of weights passed
i f not np . i s s c a l a r (w) and w. size >1:
w = np . reshape (w, ( len (w),1) )

# quick and d i r t y s o l u t i o n
p_probs = w*skew2 ( x, E, S1, S2 )
' ' '

i f w. s i z e ==2:

p_probs [ 0 ] = p_probs [ 0 ] * ( x<E [ 1 ] )
p_probs [ 1 ] = p_probs [ 1 ] * ( x>E [ 0 ] )
' ' '
probs = np . d i v i d e ( p_probs, np . sum ( p_probs +1e _−_ 6, a x i s =0) )
e l s e :

probs=np . ones ( len ( x ) )
probs [ np . isnan ( probs ) ] = 1e _−_ 16


r e t u r n probs


def calcE ( x, prob, E, S1, S2 ) :
' ' ' C a l c u l a t e the new e p s i l o n ( r e l a t e d to mean
Args :

x ( a r r a y [T ] ) : Array of PSD parameters .
prob ( a r r a y [K, T ] ) : Array of p o s t e r i o r p r o b a b i l i t i e s f o r each p o i n t .
E ( a r r a y [K] ) : Means f o r each c l a s s .
S1 ( a r r a y [K] ) : P o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
S2 ( a r r a y [K] ) : Negative s t a n d a r d d e v i a t i o n f o r each c l a s s .
Returns :

E ( a r r a y [K] ) : New means f o r each c l a s s .
' ' '
i f not np . i s s c a l a r (E) and E . size >1:
E = np . reshape (E, ( len (E),1) )
ax=1

e l s e :


ax=0
r e t u r n ( S2 **2.* np . sum ( x* prob *( x>=E), a x i s =ax ) + S1 **2.* np . sum ( x* prob *( x<E),


129


a x i s =ax ) ) / \
( S2 **2.* np . sum ( prob *( x>=E), a x i s =ax ) + S1 **2.* np . sum ( prob *( x<E), a x i s
=ax ) )


def calcS ( x, E, prob ) :
' ' ' C a l c u l a t e the new s t a n d a r d d e v i a t i o n s


Args :

x ( a r r a y [T ] ) : Array of PSD parameters .
E ( a r r a y [K] ) : Array of means f o r each c l a s s .
prob ( a r r a y [T,K] ) : Array of p o s t e r i o r p r o b a b i l i t i e s f o r each p o i n t .
Returns :

S1 ( a r r a y [K] ) : Array of p o s i s i t v e s t a n d a r d d e v i a t i o n s f o r each c l a s s .
S2 ( a r r a y [K] ) : Array of n e g a t i v e s t a n d a r d d e v i a t i o n s foe each c l a s s .
' ' '


E = np . a r r a y (E)

i f E . size >1:

E = E . reshape (( _−_ 1,1) )

ax = 1

e l s e :


ax = 0


C = np . sum ( prob, a x i s =ax )
C1 = np . sum ( ( x _−_ E) **2.* prob *( x<E), a x i s =ax )
C2 = np . sum ( ( x _−_ E) **2.* prob *( x>=E), a x i s =ax )
S2 = (C1 /C* ( 1 . + ( C2 / C1) * * ( 1 . / 3 ) ) ) * * ( 1 . / 2 )
S1 = (C2 /C* ( 1 . + ( C1 / C2) * * ( 1 . / 3 ) ) ) * * ( 1 . / 2 )

r e t u r n S1, S2


# change t h i s to accept p r o b a b i l i t i e s and then c a l c u l a t e skew2 by i t s e l f
def calcLogLike ( x, probs, w, E, S1, S2 ) :
' ' ' C a l c u l a t e the log l i k e l e h o o d given p r o b a b i l i t y, weight and parameters .


Args :

x ( a r r a y [T ] ) : An a r r a y of data p o i n t s f o r each s l i c e .
probs ( a r r a y [K, T ] ) : Array of p o s t e r i o r p r o b a b i l i t i e s f o r each p o i n t .
E ( a r r a y [K] ) : Means f o r each c l a s s .
S1 ( a r r a y [K] ) : P o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
S2 ( a r r a y [K] ) : Negative s t a n d a r d d e v i a t i o n f o r each c l a s s .
Returns :

Q ( f l o a t ) : Log _−_ l i k e l i h o o d .
' ' '
w = ( np . a r r a y (w) ) . reshape (( _−_ 1,1) )
Q = np . sum ( np . log (w) * probs ) + np . sum ( np . log ( skew2 ( x, E, S1, S2 ) +1e _−_ 16)* probs )
r e t u r n Q


def calcskewEM ( x, maxiter, eps, w, E, S1, S2, update =None ) :
' ' ' C a l c u l a t e skew parameters using E x e p c t a t i o n Maximization Algorithm


Args :

x ( a r r a y [T ] ) : An a r r a y of data p o i n t s f o r each s l i c e .
maxiter ( i n t ) : Maximum number of i t e r a t i o n s .
eps ( f l o a t ) : The log _−_ l i k e l i h o o d d i f f e r e n c e to t e r m i n a t e i t e r a t i o n
w ( a r r a y [K] ) : I n i t i a l guess weight f o r each c l a s s .
E ( a r r a y [K] ) : I n i t i a l guess means f o r each c l a s s .
S1 ( a r r a y [K] ) : I n i t i a l guess p o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
S2 ( a r r a y [K] ) : I n i t i a l guess n e g a t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .


130


update ( a r r a y [K] ) : Which c l a s s e s should have v a r i a b l e s updated .
Returns :

probs ( a r r a y [K, T ] ) : P o s t e r i o r p r o b a b i l i t i e s f o r each c l a s s .
w ( a r r a y [K] ) : New weights f o r each c l a s s .
E ( a r r a y [K] ) : New means f o r each c l a s s .
S1 ( a r r a y [K] ) : New p o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
S2 ( a r r a y [K] ) : New n e g a t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
' ' '


# Convert imput i n t o numy a r r a y and check f o r equal s i z e .
w = np . a s a r r a y (w, dtype= f l o a t )

E = np . a s a r r a y (E, dtype= f l o a t )

S1 = np . a s a r r a y ( S1, dtype= f l o a t )
S2 = np . a s a r r a y ( S2, dtype= f l o a t )

i f not (w. s i z e ==E . s i z e ==S1 . s i z e ==S2 . s i z e ) :
r a i s e ValueError ( " All of the i n i t i a l guesses must be equal s i z e " )
i f update ==None : update = np . ones (w. size, dtype= bool )
T = len ( x )

i t e r s = 0
while ( maxiter > i t e r s ) :
# s t e p 1: C a l c u l a t e i n i t i a l p o s t e r i o r p r o b a b i l i t i e s
i f i t e r s ==0: probs = calcProb ( x, w, E, S1, S2 )
# s t e p 2: C a l c u l a t e new weights f o r each c l a s s .
w = np . a s a r r a y ( np . sum ( probs . T, a x i s =0) / T)

# c a l c u l a t e the o t h e r parameters only i f r e q u e s t e d
i f ( np . sum ( update ) >0) :
# s t e p 3: C a l c u l a t e new means given new weights .
probs = calcProb ( x, w, E, S1, S2 )
Enew = calcE ( x, probs, E, S1, S2 )
# check i f v a r i a b l e s need to be updated
i f ( Enew . size >1) :
f o r i in range ( Enew . s i z e ) :
i f update [ i ] : E[ i ] = Enew [ i ]
e l s e :

i f update : E = Enew
# s t e p 4: C a l c u l a t e new s t d given new means and weights
probs = calcProb ( x, w, E, S1, S2 )
S1new, S2new = calcS ( x, E, probs )
i f ( S1new . size >1) :
f o r i in range ( S1new . s i z e ) :
i f update [ i ] :
S1 [ i ] = S1new [ i ]
S2 [ i ] = S2new [ i ]
e l s e :

i f update :
S1 = S1new

S2 = S2new
# s t e p 5: C a l c u l a t e new p r o b a b i l i t y and check log _−_ l i k e l i h o o d
probs = calcProb ( x, w, E, S1, S2 )
i f i t e r s >0:
loglike_new = calcLogLike ( x, probs, w, E, S1, S2 )
i f ( eps >np . abs (1 _−_ l o g l i k e _ o l d / loglike_new ) ) :
break
l o g l i k e _ o l d = loglike_new
e l s e :

l o g l i k e _ o l d = calcLogLike ( x, probs, w, E, S1, S2 )
i t e r s +=1

i f maxiter == i t e r s :


131


p r i n t " Warning ! Maximum number of i t e r a t i o n s exceeded \ n"
r e t u r n probs, w, E, S1, S2


def calcGaussEM ( x, maxiter, eps, w, E, S1, update =None ) :
' ' ' C a l c u l a t e Gaussian parameters using E x e p c t a t i o n Maximization Algorithm


Args :

x ( a r r a y [N] ) : An a r r a y of data p o i n t s f o r each s l i c e .
maxiter ( i n t ) : Maximum number of i t e r a t i o n s .
eps ( f l o a t ) : The log _−_ l i k e l i h o o d d i f f e r e n c e to t e r m i n a t e i t e r a t i o n
w ( a r r a y [K] ) : I n i t i a l guess weight f o r each c l a s s .
E ( a r r a y [K] ) : I n i t i a l guess means f o r each c l a s s .
S1 ( a r r a y [K] ) : I n i t i a l guess p o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
update ( a r r a y [K] ) : Which c l a s s e s should have v a r i a b l e s updated .
Returns :

probs ( a r r a y [K,N] ) : P o s t e r i o r p r o b a b i l i t i e s f o r each c l a s s .
w ( a r r a y [K] ) : New weights f o r each c l a s s .
E ( a r r a y [K] ) : New means f o r each c l a s s .
S1 ( a r r a y [K] ) : New p o s i t i v e s t a n d a r d d e v i a t i o n f o r each c l a s s .
' ' '


# Convert imput i n t o numy a r r a y and check f o r equal s i z e .
w = ( np . a s a r r a y (w, dtype= f l o a t ) )

E = np . a s a r r a y (E, dtype= f l o a t )

S1 = np . a s a r r a y ( S1, dtype= f l o a t )

i f not (w. s i z e ==E . s i z e ==S1 . s i z e ) :
r a i s e ValueError ( " All of the i n i t i a l guesses must be equal s i z e " )
i f update ==None : update = np . ones (w. size, dtype= bool )
N = len ( x )

i t e r s = 0
while ( maxiter > i t e r s ) :
# s t e p 1: C a l c u l a t e i n i t i a l p o s t e r i o r p r o b a b i l i t i e s
i f i t e r s ==0:
probs = calcProb ( x, w, E, S1, S1 )
# s t e p 2: C a l c u l a t e new weights f o r each c l a s s .
Nk = np . sum ( probs . T, a x i s =0)
w = ( np . a s a r r a y (Nk /N) )

# c a l c u l a t e the o t h e r parameters only i f r e q u e s t e d
i f ( np . sum ( update ) >0) :
# s t e p 3: C a l c u l a t e new means given new weights .
probs = calcProb ( x, w, E, S1, S1 )
ax=0


i f w. size >1: ax=1
Enew = ( 1 . / Nk) *np . sum ( probs *x, a x i s =ax )
# check i f v a r i a b l e s need to be updated
i f ( Enew . size >1) :
f o r i in range ( Enew . s i z e ) :
i f update [ i ] : E[ i ] = Enew [ i ]
e l s e :

i f update : E = Enew
# s t e p 4: C a l c u l a t e new s t d given new means and weights
probs = calcProb ( x, w, E, S1, S1 )
i f w. size >1:

S1new = ( 1 . / Nk) * np . sum ( probs *( x _−_ E . reshape (( _−_ 1,1) ) ) **2., a x i s =1)
e l s e :

S1new = ( 1 . / Nk) * np . sum ( probs *( x _−_ E) **2., a x i s =0)
S1new = np . s q r t ( S1new )

i f ( S1new . size >1) :


132


f o r i in range ( S1new . s i z e ) :
i f update [ i ] : S1 [ i ] = S1new [ i ]
e l s e :

i f update : S1 = S1new
# s t e p 5: C a l c u l a t e new p r o b a b i l i t y and check log _−_ l i k e l i h o o d
probs = calcProb ( x, w, E, S1, S1 )
i f i t e r s >0:
loglike_new = calcLogLike ( x, probs, w, E, S1, S1 )
i f ( eps >np . abs (1 _−_ l o g l i k e _ o l d / loglike_new ) ) :
break
l o g l i k e _ o l d = loglike_new
e l s e :

l o g l i k e _ o l d = calcLogLike ( x, probs, w, E, S1, S1 )
i t e r s +=1

i f maxiter == i t e r s :
p r i n t " Warning ! Maximum number of i t e r a t i o n s exceeded \ n"
S2 = S1

r e t u r n probs, w, E, S1, S2


def calcCurve ( x, w, E, S1, S2 ) :
' ' ' Curve f i t s a s i n g l e skewed Gaussian or normal double Gaussian


I n s t e a d of using EM a l g o r i t h m t h i s f u n c t i o n performs curve f i t t i n g, t h i s
i s i d e a l f o r d i s t r i b t u i o n s with only a s i n g g l e c l a s s (gamma measurements )
where EM could s t r u g g l e with o u t l i e r s .
' ' '

i f w. size >2:

r a i s e ValueError ( " Curve f i t t i n g works on maximum of 2 c l a s s e s " )
ydata, xdata = np . histogram ( x, bins =100, normed=True )
xdata = xdata [: _−_ 1] + 0.5 * ( xdata [ 1 : ] _−_ xdata [: _−_ 1])

p i n i t = (E, S1 )
i f w. s i z e ==1:

E, S1 = c u r v e _ f i t ( gauss_1, xdata, ydata, p0= p i n i t ) [ 0 ]
w = np . a s a r r a y ( 1 . )
# performs a double g au s si a n f i t
e l s e :

r e t = c u r v e _ f i t ( gauss_2, xdata, ydata, p0= np . append (w[ 0 ], p i n i t ) ) [ 0 ]
w = np . a r r a y ( [ r e t [0],1. _−_ r e t [ 0 ] ] )

E = r e t [ 1 : 3 ]
S1 = r e t [ 3 : 5 ]
S2 = S1

probs = calcProb ( x, w, E, S1, S2 )
r e t u r n probs, w, E, S1, S2


def b i n d a t a ( psd, amp, isa, mincounts =5000, maxbinwidth = 20000) :
""" C r e ates bins along amplitude with an equal number of counts in each .


Args :

psd ( a r r a y [T ] ) : PSD data to be divided along amplitude bins .
amp ( a r r a y [T ] ) : Amplitude data .
i s a ( a r r a y [T ] ) : Values by which amplitude i s s o r t e d by .
mincounts ( i n t ) : Minimum number of counts in each bin .
maxbinwidth ( i n t ) : Maximum a l l o w a b l e bin width
Returns :

x_bin ( a r r a y [T,K] ) : Matrix of psd value with each row corresponding to
s e p e r a t e bin .
xedges ( a r r a y [K+1]) : Amplitude value of the edges of each bin .
x c e n t e r s ( a r r a y [K] ) : Amplitude value of the c e n t e r s of each bin .


133


"""

amp = amp [ i s a ]

psd = psd [ i s a ]
ampbins = np . f l o o r ( amp . s i z e / mincounts )
a_bin = np . a r r a y _ s p l i t (amp, ampbins )
i _ b i n = np . a r r a y _ s p l i t ( isa, ampbins )
xedges = [ a [ 0 ] f o r a in a_bin ]
xedges . append ( amp . max ( ) ) # add the r i g h t most edge
xedges = np . a s a r r a y ( xedges )
x c e n t e r s = xedges [: _−_ 1] + 0.5 * ( xedges [ 1 : ] _−_ xedges [: _−_ 1])
x_bin = np . a r r a y _ s p l i t ( psd, ampbins )
# add bins i f the maximum bin i s exceeded
l a s t b i n w i d t h = xedges [ _−_ 1] _−_ xedges [ _−_ 2]
i f ( l a s t b i n w i d t h >maxbinwidth ) :
amphigh = np . hstack ( a_bin [ _−_ 1])
psdhigh = np . hstack ( x_bin [ _−_ 1])
i s a h i g h = np . arange ( len ( amphigh ) )
x_bin2, xedges2, x c e n t e r s 2 = b i n d a t a w i d t h ( psdhigh, amphigh, isahigh, np .
f l o o r ( l a s t b i n w i d t h / maxbinwidth ) )
# clean up old and add the new
xedges = np . append ( xedges [: _−_ 2], xedges2 )
x c e n t e r s = np . append ( x c e n t e r s [: _−_ 1], x c e n t e r s 2 )
x_bin . pop ( )
x_bin = x_bin + x_bin2
r e t u r n x_bin, xedges, x c e n t e r s


def b i n d a t a w i d t h ( psd, amp, i s a =None, ampbins =5) :
""" C r e ates bins along amplitude with an equal width in each .


Args :

psd : a r r a y [T]
PSD data to be divide d along amplitude bins .
amp : a r r a y [T]
Amplitude data .
i s a : a r r a y [T ] )
Values by which amplitude i s s o r t e d by .
ampbins : i n t
Number of bins in each

Returns :

x_bin ( a r r a y [T,K] ) : Matrix of psd value with each row corresponding to
s e p e r a t e bin .
xedges ( a r r a y [K+1]) : Amplitude value of the edges of each bin .
x c e n t e r s ( a r r a y [K] ) : Amplitude value of the c e n t e r s of each bin .

"""


i f i s a ==None :
i s a = np . a r g s o r t ( amp )
amp = amp [ i s a ]

psd = psd [ i s a ]
# d e c r e a s e bin width u n t i l t h e r e i s counts in a bin
while ( True ) :
h = np . histogram (amp, ampbins ) [ 0 ]
# d e c re a s e the number of bins i f l e s s than 100 p l o t s remain in a bin
i f sum ( h <100) >0:
ampbins _−_ =1
e l s e :

xedges = np . histogram (amp, ampbins ) [ 1 ]
break
x c e n t e r s = xedges [: _−_ 1] + 0.5 * ( xedges [ 1 : ] _−_ xedges [: _−_ 1])


134


s p l i t = np . where ( np . d i f f ( np . d i g i t i z e (amp, xedges [: _−_ 1]) ) >0) [ 0 ]
x_bin = np . s p l i t ( psd, s p l i t )

r e t u r n x_bin, xedges, x c e n t e r s


def r e j e c t _ o u t l i e r s ( data, m = 2 . ) :
d = np . abs ( data _−_ np . median ( data ) )
mdev = np . median ( d )

s = d / mdev i f mdev e l s e 0.
r e t u r n data [ s <m]


def c a l c p r o b s ( psd, amp, s h o w s l i c e s =1e9, mincounts =5000, maxbinwidth =20000,
maxiter =1000, eps =1e _−_ 6, w= [ 0 . 5, 0 . 5 ], E=[17,35], S1 =[1,1],
S2 = [ . 1, . 1 ], E f i t =None, S 1 f i t =None, S 2 f i t =None, verbose =True,
f i t t y p e = 'EMskew ', curve_cut =1e9 ) :
' ' ' Finds the p o s t e r i o r p r o b a b i l i t i e s of a l l the data p o i n t s in the c l a s s .


Data i s divided i n t o K c l a s s e s each modeled by a skewed _−_ Gaussian . The
number of c l a s s e s i s dependent on the number of i n i t i a l parameters
provided . The a l g o r i t h m f i t s each s l i c e s t a r t i n g with the h i g h e s t
amplitude to the lowest and uses i n i t i a l guesses from the p r ev i ou s
r e s u l t as next i n i t i a l guesses .


I f the f i t i n t e r p o l a t e o b j e c t f o r parameters i s provided then those
parameters
f o r each c l a s s are not r e c a l c u l a t e d, only the weight i s r e c a l c u l a t e d .
The parameters f o r c l a s s e s in which f i t was not provided are r e c a l c u l a t e d .


I f the number of minimum counts i s not met in a p a r t i c u l a i r bin then
a k _−_ means a l g o r i t h m i s used to compute the mean and s t a n d a r d d e v i a t i o n .
A g a u s s i an shape i s assumed f o r the computation of both parameters .


Args :

psd ( a r r a y [T ] ) : PSD data p o i n t s .
amp ( a r r a y [T ] ) : Corresponding amplitude data .
s h o w s l i c e s : Number of s l i c e s to skip between p l o t t i n g f i t r e s u l t s .
mincounts ( int, o p t i o n a l ) : Minimum counts in each amplitude bin .
maxiter ( int, o p t i o n a l ) : Maximum number of i t e r a t i o n f o r the EM a l g o r i t h m .
eps ( f l o a t, o p t i o n a l ) : Exit c o n d i t i o n f o r EM a l g o r i t h m .
w ( a r r a y [K], o p t i o n a l ) : I n i t i a l weights f o r each c l a s s .
E ( a r r a y [K], o p t i o n a l ) : I n i t i a l means f o r each c l a s s .
S1 ( a r r a y [K], o p t i o n a l ) : I n i t i a l p o s i t i o v e s t a n d a r d d e v i a t i o n .
S2 ( a r r a y [K], o p t i o n a l ) : I n i t i a l n e g a t i v e s t a n d a r d d e v i a t i o n .
E f i t ( a r r a y [K] ) : Array of i n t e r p o l a t e o b j e c t s .
S 1 f i t ( a r r a y [K] ) : Array of i n t e r p o l a t e o b j e c t s .
S 2 f i t ( a r r a y [K] ) : Array of i n t e r p o l a t e o b j e c t s .
verbose : Output t h a t p r i n t s to screen s i z e .
f i t t y p e : 'EM ' or ' curve ' option f o r type of f i t t i n g
curve_cut : Above t h i s value always perform curve f i t t i n g


Returns :

probs ( a r r a y [K, T ] ) : P o s t e r i o r p r o b a b i l i t i e s f o r each c l a s s .
E_arr ( a r r a y [K, S ] ) : Means f o r each amplitude bin .
S1_arr ( a r r a y [K, S ] ) : P o s i t i v e s t d f o r each amplitude bin .
S2_arr ( a r r a y [K, S ] ) : Negative s t d f o r each amplitude bin .
ampcenters ( a r r a y [ S ] ) : Array of amplitude c e n t e r s .
' ' '


135


# Convert imput i n t o numy a r r a y and check f o r equal s i z e .
i f np . i s s c a l a r (w) : w = np . a r r a y ( [w] )
i f np . i s s c a l a r (E) : E = np . a r r a y ( [ E ] )
i f np . i s s c a l a r ( S1 ) : S1 = np . a r r a y ( [ S2 ] )
i f np . i s s c a l a r ( S2 ) : S2 = np . a r r a y ( [ S2 ] )


w = np . a s a r r a y (w)

E = np . a s a r r a y (E)

S1 = np . a s a r r a y ( S1 )
S2 = np . a s a r r a y ( S2 )

i f not (w. s i z e ==E . s i z e ==S1 . s i z e ==S2 . s i z e ) :
r a i s e ValueError ( " All of the i n i t i a l guesses must be euqal s i z e " )
# check the number of f i t s p r e s e n t
i f not ( E f i t ==None and S 1 f i t ==None and S 2 f i t ==None ) :
num_fits = len ( E f i t )
update = np . zeros ( num_fits, dtype= bool )
# The d i f f e r e n c e w i l l be updated
f o r i in range (w. size _−_ num_fits ) :
update = np . append ( update, True )
f i t s _ p a s s e d = True
e l s e :

f i t s _ p a s s e d = False
update = None


i s a = np . a r g s o r t ( amp )
psd_bin, ampedges, ampcenters = b i n d a t a ( psd, amp, isa, mincounts,
maxbinwidth )


# c o r r e c t f o r high e n e r g i e s


# f i t e v e r y t h i n g going backwards
p r o b _ a r r = [ ]
E_arr = [ ]
S1_arr = [ ]
S2_arr = [ ]
f o r i in range ( len ( ampcenters ) _−_ 1, _−_ 1, _−_ 1) :
# i f f i t s where passed use those to get the next value
i f f i t s _ p a s s e d :
amp = ampcenters [ i ]
E = np . append ( np . a s a r r a y ( [ x ( amp ) f o r x in E f i t ] ), E[ num_fits : ] )
S1 = np . append ( np . a s a r r a y ( [ x ( amp ) f o r x in S 1 f i t ] ), S1 [ num_fits : ] )
S2 = np . append ( np . a s a r r a y ( [ x ( amp ) f o r x in S 2 f i t ] ), S2 [ num_fits : ] )


i f len ( psd_bin [ i ] ) >1000 and f i t t y p e != ' kmeans ' :
# f o r f i t t i n g only one parameter, curve f i t t i n g i s b e t t e r
i f f i t t y p e == ' curve ' or ampcenters [ i ] > curve_cut :
probs, w, E, S1, S2 = calcCurve ( psd_bin [ i ], w, E, S1, S2 )
e l i f f i t t y p e == 'EMskew ' :
probs, w, E, S1, S2 = calcskewEM ( psd_bin [ i ], maxiter, eps, w, E, S1,
S2, update )
e l i f f i t t y p e == ' EMgauss ' :
probs, w, E, S1, S2 = calcGaussEM ( psd_bin [ i ], maxiter, eps, w, E, S1,
update )
e l s e :

i f ( verbose ) : p r i n t ' Using k _−_ means '
# c on vert t h i s i n t o i t s own c o l l a b l e f u n c t i o n
data = psd_bin [ i ]
E, l = kmeans2 ( data, k=E, minit = ' matrix ' )


136


# somehow t h i s has to s o r t
w = np . a r r a y ( [ ] )

S1 = np . a r r a y ( [ ] )

f o r k in range ( len (E+1) ) :
d = data [ l ==k ]
#d = r e j e c t _ o u t l i e r s ( d )
S1 = np . append ( S1, d . s t d ( ) )
w = np . append (w, ( l ==k ) . sum ( dtype= f l o a t ) )
w = w/w. sum ( )

S2 = S1

probs = calcProb ( psd_bin [ i ], w, E, S1, S2 ) ;
# check t h a t the output i s c o r r e c t
i f ( np . sum ( ( np . isnan (w), np . isnan (E), np . isnan ( S1 ), np . isnan ( S2 ) ) ) > 0) :
r a i s e RuntimeError ( "EM f a i l e d on s l i c e " + s t r ( i ) + " with amp " + s t r (
ampcenters [ i ] ) )
p r o b _ a rr . append ( probs . copy ( ) )
E_arr . append (E . copy ( ) )
S1_arr . append ( S1 . copy ( ) )
S2_arr . append ( S2 . copy ( ) )

i f ( verbose ) : p r i n t "Done with s l i c e : " + s t r ( i )
# p l o t some r e s u l t s i f r e q u e s t e d
i f ( np . mod( i +1, s h o w s l i c e s ) ==0) :
fx = np . l i n s p a c e ( psd_bin [ i ] . min ( ), psd_bin [ i ] . max ( ),1000)

p r i n t w, E, S1, S2
p l t . t i t l e ( ' S l i c e number : ' + s t r ( i ) + " Amp: " + s t r ( ampcenters [ i ] ) )
p l t . h i s t ( psd_bin [ i ],100, normed=True, h i s t t y p e = ' s t e p ' )
p l t . p l o t ( fx,w*skew2 ( fx, E, S1, S2 ) . T)
p l t . show ( )
# s o r t the p r o b a b i l i t i e s to the i n p u t amplitude order
probs = np . hstack ( l i s t ( r e v e r s e d ( p r o b _a r r ) ) )
E_arr = np . a r r a y ( l i s t ( r e v e r s e d ( E_arr ) ) ) . T
S1_arr = np . a r r a y ( l i s t ( r e v e r s e d ( S1_arr ) ) ) . T
S2_arr = np . a r r a y ( l i s t ( r e v e r s e d ( S2_arr ) ) ) . T

i f len ( probs . shape ) >1:
f o r k in range ( probs . shape [ 0 ] ) :
probs [ k ] = probs [ k ] [ np . a r g s o r t ( i s a ) ]
e l s e :

probs = np . a r r a y ( [ probs [ np . a r g s o r t ( i s a ) ] ] )
E_arr = np . a r r a y ( [ E_arr ] )
S1_arr = np . a r r a y ( [ S1_arr ] )
S2_arr = np . a r r a y ( [ S2_arr ] )
r e t u r n probs, E_arr, S1_arr, S2_arr, ampcenters


def p l o t p s d (amp, psd, probs=None, pcut = [ 0 . 9, 0 . 9 ] ) :
' ' ' P l o t s psd r e s u l t s f o r each c l a s s
' ' '
i f probs ==None : probs = np . ones ( len ( amp ) )
i f len ( probs . shape ) >1:
f, ( ax1, ax2 ) = p l t . s u b p l o t s (2, sharex =True, sharey =True )
ax1 . s e t _ t i t l e ( ' Separated photons and n eu t ro n s . ' )
ax1 . h i s t 2 d (amp, psd, bins =[200,100], norm=LogNorm ( ), weights =( probs [0] > pcut

[ 0 ] ) . astype ( i n t ), cmin =1)
ax2 . h i s t 2 d (amp, psd, bins =[200,100], norm=LogNorm ( ), weights =( probs [1] > pcut

[ 1 ] ) . astype ( i n t ), cmin =1)
p l t . show ( )
e l s e :

p l t . h i s t 2 d (amp, psd, bins =[200,100], norm=LogNorm ( ), weights =probs, cmin =1)
p l t . show ( )


137


def p l o t p s d f i t (amp, psd, p s d f i t, E, S1, S2, ampbins ) :
' ' ' P l o t s psd r e s u l t s f o r each c l a s s
' ' '
# reshape ampbins i f needed
# ampbins = np . a r r a y ( ampbins ) . reshape ( ( len (E), _−_ 1) )
x = np . l i n s p a c e ( np . min ( amp ), np . max ( amp ),1000)

p l t . h i s t 2 d (amp, psd, bins =[200,100], norm=LogNorm ( ), cmin =1)
f o r i in range ( len ( p s d f i t [ 'E ' ] ) ) :
# p l o t the f i t s
p l t . p l o t ( x, p s d f i t [ 'E ' ] [ i ] ( x ), ' g ', lw =3)
p l t . p l o t ( x, p s d f i t [ 'E ' ] [ i ] ( x ) + p s d f i t [ ' S1 ' ] [ i ] ( x ), ' k ', lw =3)
p l t . p l o t ( x, p s d f i t [ 'E ' ] [ i ] ( x ) _−_ p s d f i t [ ' S2 ' ] [ i ] ( x ), ' k ', lw =3)
# p l o t the i n d i v i d u a l p o i n t s
p l t . p l o t ( ampbins, E[ i ], ' go ' )
p l t . p l o t ( ampbins, E[ i ]+S1 [ i ], ' ro ' )
p l t . p l o t ( ampbins, E[ i ] _−_ S2 [ i ], ' ro ' )
p l t . show ( )


def getRecArr ( prob, psd, amp, time ) :
' ' ' C r e ates a r ecco rd a r r a y t h a t can be saved to a r o o t f i l e


This f u n c t i o n i s purpose b u i l t f o r photons and ne u tr o ns being present,
but i t a l s o l i v e s as an example f o r o t h e r p o t e n t i a l programs .
' ' '
wtype = np . dtype ( [ ( ' probG ', prob [ 0 ] . dtype ), ( ' probN ', prob [ 1 ] . dtype ),

( ' psd ', psd . dtype ), ( ' amp ',amp . dtype ), ( ' time ', time . dtype ) ] )
w = np . empty ( len ( prob [ 0 ] ), dtype=wtype )
w[ ' probG ' ] = prob [ 0 ]
w[ ' probN ' ] = prob [ 1 ]
w[ ' psd ' ] = psd
w[ ' amp ' ] = amp
w[ ' time ' ] = time


r e t u r n w


# t u r n t h i s i n t o a c l a s s
def f i t p s d p a r m s (E, S1, S2, ampbins, smooth, knot, fitnum =1) :
' ' ' F i t s psd paramers with s p l i n e s and r e t u r n s d i c t i o n a r y of f i t s


Spli ne f i t t i n g i s performed on PSD parameters and saved in a d i c t i o n a r y .
These f i t s can then be used to update the p r o b a b i l i t y maps f o r subsequent
measurements . The f i t t i n g i s performed f o r K number of c l a s s e s t h a t are
placed in the d i c t i o n a r y as s p l i n e s in the same order .


Args :

amp : Amplitude of p u l s e s ( f o r p l o t t i n g )
psd : PSD parameter of p u l s e s ( a l s o f o r p l o t i n g )
E, S1, S2 ( a r r a y [ n,K] ) : Means and s t a n d a r d d e v i a t i o n s of d i s t r i b u t i o n s .
ampbins a r r a y ( [ n,K] ) : Amplitude c e n t e r s of each s l i c e .
smooth ( a r r a y [3,K] ) : Array of smoothing parameters .
knot ( a r r a y [3,K] ) : Array of knots f o r the smoothing s p l i n e
fitnum : number of f i t s

Returns :

p s d f i t s : D i c t i o n a r y of smooth s p l i n e f i t s f o r each parameter
' ' '
# reshape ampbins i f needed
# ampbins = np . a r r a y ( ampbins ) . reshape ( ( fitnum, _−_ 1) )
# Add v alues to the d i c t i o n a r y to be p i c k l e d


138


p s d f i t s = {}
p s d f i t s [ 'E ' ] = [ ]
p s d f i t s [ ' S1 ' ] = [ ]
p s d f i t s [ ' S2 ' ] = [ ]


f o r i in range ( fitnum ) :
# means

E f i t = i n t e r p o l a t e . U n i v a r i a t e S p l i n e ( ampbins, E[ i ], k=knot [ i ] [ 0 ],

s=smooth [ i ] [ 0 ] )
# s t a n d a r d d e v i a t i o n s
S 1 f i t = i n t e r p o l a t e . U n i v a r i a t e S p l i n e ( ampbins, S1 [ i ], k=knot [ i ] [ 1 ],
s=smooth [ i ] [ 1 ] )


S 2 f i t = i n t e r p o l a t e . U n i v a r i a t e S p l i n e ( ampbins, S2 [ i ], k=knot [ i ] [ 2 ],
s=smooth [ i ] [ 2 ] )
# Append e v e r y t h i n g to the c o r r e c t d i c t i o n a r y value
p s d f i t s [ 'E ' ] . append ( E f i t )
p s d f i t s [ ' S1 ' ] . append ( S 1 f i t )
p s d f i t s [ ' S2 ' ] . append ( S 2 f i t )
r e t u r n p s d f i t s


def s a v e p s d f i t s ( p s d f i t s, o u t p u t _ f i t f i l e ) :
' ' ' Saves the d i c t i o n a r y of PSD f i t s to an output f i l e


The psd f i t f i l e should be saved once the f i t f o r every channel i s
complete .


Args :

p s d f i t s : D i c t i o n a r y of f i t f u n c t i o n s f o r parameters
o u t p u t _ f i t f i l e : The d e s t i n a t i o n f i l e f o r saving the f i t s .
' ' '
f o u t = open ( o u t p u t _ f i t f i l e, 'w ' )
p i c k l e . dump ( p s d f i t s, f o u t )
f o u t . c l o s e ( )

## **A.3 3D Imaging**


' ' '
S e r i e s of f u n c t i o n s f o r c o n v e r t i n g c o r r e l a t e d data p o i n t s i n t o source
l o c a t i o n s t h i s one i n c l u d e s u n c e r t a n t i e s

' ' '


import numpy as np


def s c a t t e r i n g _ e n e r g y ( d i s t, delT ) :
' ' '

C a l c u l a t i n g neuton energy a f t e r s c a t t e r from f i r s t d e t e c t o r
Parameters :


d i s t : Distance between i n t e r a c t i o n s
delT : Travel time between i n t e r a c t i o n s ( ns )


Return :

Energy between two s c a t t e r s
' ' '


139


m_n = 1.6749 e _−_ 27

delT = delT / 1 . e9
erg1 = (m_n / 2 . )  - ( ( d i s t /100) **2 / delT **2) * 6.242 e12
r e t u r n erg1


def c a l c _ i n c i d e n t ( d i s t, delT, erg_dep ) :
' ' '

C a l c u l a t e i n c i d e n t energy and opening angle of the cone
Args :

d i s t : Distance between i n t e r a c t i o n s

delT : The d i f f e r e n c e in time between two i n t e r a c t i o n s
erg_dep : energy d e p o s i t e d in f i r s t d e t e c t o r (MeV)
' ' '
# d e f i n e c o n s t a n t s append numbers to record a r r a y
erg1 = s c a t t e r i n g _ e n e r g y ( d i s t, delT )
erg0 = erg_dep + erg1
angle = np . arccos ( np . s q r t ( erg1 / erg0 ) )
r e t u r n angle, erg0


def r o d r i g u e s ( k, v, t h e t a, mode= ' uniform ' ) :
' ' ' Rotate v e c t o r v about a x i s of v e c t o r k by angle t h e t a using the
r i g h t hand r u l e


Parameters :


k : u n i t v e c t o r to t u r n on .
v : u n i t v e c t o r being turned :
t h e t a : angle of r o t a t i o n
mode : Default = ' uniform ', r o t a t e s a l l the vectors, ' s p e c i f i c ', each
v e c t o r i s r o t a t e s according to corresponding angle
Return :

vn ( d a t a _ p o i n t s, c o r d i n a t e s, t h e t a ) : Rotated v e c t o r n
' ' '

i f mode== ' uniform ' :
vn = v [ :, :, None ]* np . cos ( t h e t a ) + np . c r o s s ( k, v ) [ :, :, None ]* np . s i n ( t h e t a ) +( k

     - [( k]     - [v ) .][ sum][ ( 1 ) [ :, None ] ) [ :, :, None]]     - [(1] _[ −]_ [np . cos ( t h e t a ) )]

e l i f mode== ' s p e c i f i c ' :
vn = v*np . cos ( t h e t a ) [ :, None ] + np . c r o s s ( k, v ) *np . s i n ( t h e t a ) [ :, None ]+( k *( k*v

) . sum ( 1 ) [ :, None ] ) *(1 _−_ np . cos ( t h e t a ) ) [ :, None ]
vn = vn [ :, :, None ]

r e t u r n vn


def g e t _ v e c t o r ( p0, p1 ) :
' ' '
Gets the v e c t o r and i t s magniture from two p o i n t s
p0 _−−−−−−_  - p1

Parameters :

p0 : F i r s t p o i n t
p1 : Secont p o i n t
Returns :

vec : Vector def ined by two p o i n t s
d i s t : d i s t a n c e between two p o i n t s ( or magnitude of the v e c t o r )
' ' '


_−_
vec = p0 p1

d i s t = np . s q r t ( np . sum ( vec **2,1) )
r e t u r n vec, d i s t


def solve_R ( f, d, v, t ) :


140


' ' '
Solves f o r the two p o s s i b l e s o l u t i o n s of R
Args :

d : d i s t a n c e between neutron and gamma (cm)
v : speed of i n c i d e n t neutron (m/ s )
f : dot product of R u n i t v e c t o r and g _−_ n u n i t v e c t o r
t : time between gamma _−_ neutron events ( ns )
Returns :


R1, R2 : The two s o l u t i o n s f o r R
' ' '

c = 3 . e8

d = d / 1 0 0 .


t = t / 1 . e9

f = f . T
R = ( np . s q r t ( v **2*( c **2*d**2 _−_ 2*c **2*d* f * t *v + c **2* t **2*v**2 + d**2* f **2*

v**2 _−_ d**2*v**2 ) )
+ c **2* t *v _−_ d* f *v **2) / ( c **2 _−_ v **2)
R = R. T


r e t u r n R*100.


def im3_type ( ) :
' ' '
Returns the 3d imaging data type which i n c l u d e s :
n0loc ( 3, ) : Location (cm) of f i r s t neutron s c a t t e r
n1loc ( 3, ) : Location (cm) of second neutron s c a t t e r
gloc ( 3, ) : Location (cm) of the gamma i n t e r a c t i o n
nnt : Time ( ns ) between f i r s t and second s c a t t e r
gnt : Time ( ns ) between gamma and n e u tr o ns c a t t e r
n0erg : Deposited energy in f i r s t neutron i n t e r a c t i o n
' ' '
im_type = np . dtype ( [ ( ' n0loc ', ' f l o a t ',3), ( ' n1loc ', ' f l o a t ',3), ( ' gloc ', ' f l o a t '

,3),

( ' nnt ', ' f l o a t ' ), ( ' gnt ', ' f l o a t ' ), ( ' n0erg ', ' f l o a t ' ) ] )
r e t u r n im_type


def im2_type ( ) :
' ' '
Returns the 2d imaging data type which i n c l u d e s :
n0loc ( 3, ) : Location (cm) of f i r s t neutron s c a t t e r
n1loc ( 3, ) : Location (cm) of second neutron s c a t t e r
nnt : Time ( ns ) between f i r s t and second s c a t t e r
n0erg : Deposited energy in f i r s t neutron i n t e r a c t i o n
' ' '


im_type = np . dtype ( [ ( ' n0loc ', ' f l o a t ',3), ( ' n1loc ', ' f l o a t ',3),

( ' nnt ', ' f l o a t ' ), ( ' n0erg ', ' f l o a t ' ) ] )
r e t u r n im_type


def c a r t 2 s p h e r e ( xyz ) :
' ' ' Converts c a r t e s i a n to s p h e r i c a l c o o r d i n a t e s
' ' '
r = np . s q r t ( np . sum ( xyz **2,1) )
t h e t a = np . a r c t a n 2 ( xyz [ :, 1 ], xyz [ :, 0 ] )
phi = np . arccos ( xyz [ :, 2 ] / r )
r t p = np . a r r a y ( [ r, t h et a, phi ] ) . T
r e t u r n r t p


def s p h e r e 2 c a r t ( r t p ) :


141


' ' ' Converts s p h e r i c a l to c a r t i s i a n c o o r d i n a t e s
' ' '
x = r t p [ :, 0 ] * np . cos ( r t p [ :, 1 ] ) *np . s i n ( r t p [ :, 2 ] )
y = r t p [ :, 0 ] * np . s i n ( r t p [ :, 1 ] ) *np . s i n ( r t p [ :, 2 ] )
z = r t p [ :, 0 ] * np . cos ( r t p [ :, 2 ] )
xyz = np . a r r a y ( [ x, y, z ] ) . T

r e t u r n xyz


def g e t _ s o u r c e ( data, n _ t h e t a s = 100) :
' ' '
Returns source p o i n t s in c a r t e s i a n c o o r d i n a t e s based on the i n p u t data


Parameters :

data : Record a r r a y of l o c a t i o n s, times and energy in f i r s t neutron s c a t t e r
n _ t h e t a s : Number of source l o c a t i o n s to throw per cone, i f 1 then uses
random


o t h e r w i s e i t s a uniform d i s t r i b u t i o n

Return :

source ( n_evnets, 3 c o o r d i n a t e s, n _ t h e t a s ) : Array of the p o s s i b l e source
p o i n t s based on the i n p u t .
T

' ' '


# get the u n i t v e c t o r t h a t d e f i n e s the n _−_ n s c a t t e r a x i s
nn_vec, nn_d = g e t _ v e c t o r ( data [ ' n0loc ' ], data [ ' n1loc ' ] )
nn_hat = nn_vec / nn_d [ :, None ]
# get v e c t o r and magnitude t h a t d e f i n d s the n _−_ g a x i s
ng_vec, ng_d = g e t _ v e c t o r ( data [ ' gloc ' ], data [ ' n0loc ' ] )
ng_hat = ng_vec / ng_d [ :, None ]
# get energy and opening angle of the cone
theta1, erg0 = c a l c _ i n c i d e n t ( nn_d, data [ ' nnt ' ], data [ ' n0erg ' ] )
v_n = np . s q r t ( 2 . * erg0 / ( 9 3 9 . 5 / 3 . e8 **2) )
# d e c l i n e nn_hat by the opening angle of the cone
norm_nn = np . c r o s s ( [ 1, 1, 1 ], nn_hat )
norm_nn = norm_nn / np . s q r t ( np . sum ( norm_nn * * 2 ., 1 ) ) [ :, None ]

ns_hat = nn_hat *np . cos ( t h e t a 1 ) [ :, None]+ np . s i n ( t h e t a 1 ) [ :, None ]* np . c r o s s (

norm_nn, nn_hat )
# r o t a t e ns_hat around given azimuthal angle around the cone
i f n_thetas >1:
c o n e _ t h e t a s = np . l i n s p a c e (0, np . pi *2, n _ t h e t a s )
cone_hat = r o d r i g u e s ( nn_hat, ns_hat, cone_thetas, mode= ' uniform ' )
e l s e :

c o n e _ t h e t a s = np . random . rand ( ns_hat [ :, 0 ] . s i z e ) *2*np . pi
cone_hat = r o d r i g u e s ( nn_hat, ns_hat, cone_thetas, mode= ' s p e c i f i c ' )
# c a l c u l a t e d i s t a n c e r f o r each p o i n t and get the f i n a l source p o i n t
f = ( cone_hat * ng_hat [ :, :, None ] ) . sum ( 1 ) # cosine of angles between cone
s u r f a c e and n _−_ g v e c t o r
Rn = solve_R ( f, ng_d, v_n, data [ ' gnt ' ] )
source = cone_hat *Rn [ :, None ] + data [ ' n0loc ' ] [ :, :, None ]


r e t u r n source


142


## **APPENDIX B**

# **Math**

## **B.1 3D Imaging**

The solution to the quadratic equation, shown Section 7.4, that yields the distance from the fist


neutron interaction to the source along the length of the projected cone is



_c_ [2] _t_ _γ,n_ _v_ _n_ _−_ _dv_ _n_ [2] _[µ][ ±]_
~~�~~
_R_ _n_ =



(B.1)
_c_ [2] _−_ _v_ _n_ [2]



_v_ _n_ [2] ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)] ~~�~~



The proof will demonstrate that only one of those roots is a valid solution, because the speed of


the neutron has to be less than the speed of light _v_ _n_ _< c_ . First, Eq. 7.8 can be rearranged to solve


for source-gamma distance:



_R_ _n_
_R_ _γ_ = _c_ _−_ _t_ _γ,n_
� _v_ _n_



(B.2)
�



_R_ _γ_ has to be positive, therefore:



_t_ _γ,n_ _<_ _[R]_ _[n]_ (B.3)

_v_ _n_


143


This inequality can be substituted back into Eq. B.1:



_c_ [2] _t_ _γ,n_ _v_ _n_ _−_ _dv_ _n_ [2] _[µ][ ±]_
~~�~~
_t_ _γ,n_ _<_



_v_ _n_ ( _c_ [2] _−_ _v_ _n_ [2] [)]



_v_ _n_ [2] ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dvµt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)] ~~�~~



_c_ [2] _t_ _γ,n_ _−_ _t_ _γ,n_ _v_ _n_ [2] _[< c]_ [2] _[t]_ _[γ,n]_ _[−]_ _[dv]_ _[n]_ _[µ][ ±]_ ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dvµt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)]



_dv_ _n_ _µ −_ _t_ _γ,n_ _v_ _n_ [2] _[<][ ±]_ ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)] (B.4)



This is a key part in the proof, because at this point one has to decide which sign, positive or


negative, to choose for the term on the right-hand-side. The proof is in showing which sign satisfies


the inequality. Assuming the sign has to be _negative_, then by definition both sides of Eq. B.4 have


to be less than zero. Therefore, if both sides are squared then the inequality sign has to flip:


( _dv_ _n_ _µ_ ) [2] _−_ 2 _dv_ _n_ [3] _[µt]_ _[γ,n]_ [+] _[ t]_ [2] _γ,n_ _[v]_ _n_ [4] _[> c]_ [2] [(] _[t]_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dvµt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)]


_v_ _n_ [2] [(] _[t]_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ [ +] _[ d]_ [2] [)] _[ > c]_ [2] [(] _[t]_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] [)]


The validity of this expression hinges on whether the term in the parenthesis is positive or negative.


It is indeed always positive because


_t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] _[ ≥]_ [(] _[d][ −]_ _[t]_ _[γ,n]_ _[v]_ _[n]_ [)] [2] _[ >]_ [ 0]


_−_ 1 _≤_ _µ ≤_ 1 _._


and therefore the _negative_ solution is invalid. Assume the positive sign right-hand-side of Eq. B.4,


and the left-hand-side has to be positive because that is only valid result from taking a square root:



_|dv_ _n_ _µ −_ _t_ _γ,n_ _v_ _n_ [2] _[|][ <]_
~~�~~



_|dv_ _n_ _µ −_ _t_ _γ,n_ _v_ _n_ _[|][ <]_ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dvµt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)]

~~�~~ _v_ _n_ [2] [(] _[t]_ [2] _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] _[µ]_ [2] [)] _[ <]_ ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dvµt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)]



_v_ _n_ [2] [(] _[t]_ [2] _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] _[µ]_ [2] [)] _[ <]_
~~�~~



_c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dvµt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)]



144


Since both sides have to be positive, squaring them maintains the inequality. The terms can be


re-arranged as before and result in


_v_ _n_ [2] [(] _[t]_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ [ +] _[ d]_ [2] [)] _[ < c]_ [2] [(] _[t]_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] [)]


_v_ _n_ _< c._


which is demonstrably true. Therefore, the solution for the distance from the first neutron scatter


and possible source location along the surface of a cone is:



_c_ [2] _t_ _γ,n_ _v_ _n_ _−_ _dv_ _n_ [2] _[µ]_ [ +]
~~�~~
_R_ _n_ =



_c_ [2] _−_ _v_ _n_ [2]


145



_v_ _n_ [2] ~~�~~ _c_ [2] ( _t_ [2] _γ,n_ _[v]_ _n_ [2] _[−]_ [2] _[dv]_ _[n]_ _[µt]_ _[γ,n]_ [+] _[ d]_ [2] [) +] _[ v]_ _n_ [2] _[d]_ [2] [(] _[µ]_ [2] _[ −]_ [1)] ~~�~~



(B.5)


### **BIBLIOGRAPHY**


[1] R. Rhodes, _Making of the Atomic Bomb_ . New York: Simon and Schuster, 1986.


[2] M. Bunn, Y. Morozov, R. Mowatt-Larssen, S. Saradzhyan, W. Tobey, V. I. Yesin, and P. S.
Zolotarev, “The u.s.-russia join threat assessment of nuclear terrorism,” 2011.


[3] D. Reilly, N. Ensslin, H. J. Smith, and S. Kreiner, “The origin of neutron radiation,” in
_Passive nondestructive assay of nuclear materials_, pp. 337–356, Los Aalamos National
Laboratory, 1991.


[4] J. M. Verbeke, C. Hagmann, and D. Wright, “Simulation of neutron and gamma ray emission from fission and photofission,” Tech. Rep. UCRL-AR-228518, Lawrence Livermore
National Laboratory, 2014.


[5] T. E. Valentine, “Evaluation of prompt fission gamma rays for use in simulating nuclear
safeguard measuements,” Tech. Rep. ORNL/TM-1999/300, Oak Ridge National Laboratory,
1999.


[6] V. V. Verbinski, H. Weber, and R. E. Sund, “Prompt gamma rays from [235] U( _n, f_ ),
239 Pu( _n, f_ ), and spontaneous fission of 252 Cf,” _Phys. Rev. C_, vol. 7, pp. 1173–1185, Mar
1973.


[7] X-5 Monte Carlo Team, _MCNP - A General Monte Carlo N-Particle Transport Code, Ver-_
_sion 5, Volume I: Overview and Theory_ . Los Alamos National Laboratory, April 2003.
Appendix H - Fission Spectra Constants and Flux-To-Dose Factors Constant for Fission
Spectra.


[8] N. Ensslin, “Principle of neutron coincident counting,” in _Passive nondestructive assay of_
_nuclear materials_, pp. 457–492, Los Alamos National Laboratory, 1991.


[9] “Nuclear regulatory legislation,” Tech. Rep. NUREG-0980, U. S. Nuclear Regulatory
Comission, September 2013.


[10] B. C. Reed, “An examination of potential fission-bomb weaponizability of nuclides other
than U-235 and Pu-239,” _American Journal of Physics_, vol. 85, pp. 38–44, 2017.


[11] “Iaea safeguards glossary,” Tech. Rep. IAEA/NVS/3, International Atomic Energy Agency,
Vienna, 2002.


146


[12] J. J. Duderstadt and L. J. Hamilton, _Nuclear Reactor Analysis_, ch. 1 Introductory Concepts
of Nuclear Power Reactor Analysis, p. 84. John Wiley and Sons, 1976.


[13] J. J. Duderstadt and L. J. Hamilton, _Nuclear Reactor Analysis_, ch. 5 The One-Speed Diffusion Theory Model, pp. 150–225. John Wiley and Sons, 1976.


[14] J. D. Lewins, “Neutron lifetime, generation time and reproduction time,” _Nucl. Sci. Eng._,
vol. 78, p. 105, 1981.


[15] K. O. Ott and R. J. Neuhold, _Nuclear Reactor Dynamics_, ch. 2 Delayed Neutrons, pp. 5–19.
Illinois, USA: American Nuclear Society, 1985.


[16] R. Serber, “The definitions of neutron multiplication,” Tech. Rep. LA-335, Los Alamos
National Laboratory, 1945.


[17] I. Pazsit and L. Pal, _Neutron Fluctiations_, ch. 11 Theory of Multiplicity in Nuclear Safeguards, pp. 294 – 311. Amsterdam: Elsevier, 2008.


[18] F. de Hoffmann, “Intensity fluctuations of a neutron chain reactor,” Tech. Rep. LA-DC-256,
Los Alamos National Laboratory, 1944.


[19] M. M. Pickerell, K. Veal, and N. Ensslin, “Fast and epithermal neutron multiplicity counting,” in _Passive nondestructive assay of nuclear materials_, no. LA-UR-07-1602, pp. 1–19,
Los Alamos National Laboratory, 2007.


[20] D. Chernikova, K. Axell, S. Avdic, I. Pázsit, A. Nordlund, and S. Allard, “The neutrongamma feynman variance to mean approach: Gamma detection and total neutron-gamma
detection (theory and practice),” _Nuclear Instruments and Methods in Physics Research Sec-_
_tion A: Accelerators, Spectrometers, Detectors and Associated Equipment_, vol. 782, pp. 47
– 55, 2015.


[21] C. P. Baker, “Time scale measurement by the rossi method,” Tech. Rep. LA-617, Los
Alamos National Laboratory, 1947.


[22] R. E. Malenfant, “Controlled production of an explosive nuclear chain reaction,” Tech. Rep.
LA-397, Los Alamos Nationa Laboraory, 1945.


[23] J. D. Orndoff and C. W. Johnstone, “Time scale measurement by the rossi method,” Tech.
Rep. LA-744, Los Alamos National Laboratory, 1949.


[24] G. E. Mckenzie, “Modern rossi alpha measurements,” 2014.


[25] R. Feynman, “Statistical behavior of neutron chains,” Tech. Rep. LA-591, Los Alamos National Laboratory, 1946.


[26] J. D. Orndoff, “Prompt neutron periods of metal critical assemblies,” _Nuclear Science and_
_Engineering_, vol. 2, pp. 450 – 460, 1957.


[27] F. de Hoffman, “Statistical fluctuations in the water boiler and the dispersion of neutrons
exitted per fission,” Tech. Rep. LA-101, Los Alamos National Laboratory, 1944.


147


[28] R. P. Feynman, F. de Hoffmann, and R. Serber, “Dispersion of the neutron emission in u-235
fission,” _J. Nuclear Energy_, vol. 3, pp. 64– 69, February 1956.


[29] E. J. Dowdy, G. E. Hansen, A. A. Robba, and J. C. Pratt, “Effects of ( _α_, n) contaminants
and sample multiplication on statistical neutron correlation measurements,” Tech. Rep. LAUR-80-743, Los Alamos National Laboratory, 1980.


[30] N. Ensslin, W. H. Geist, M. S. Krick, and M. M. Pickrell, “Active neutron multiplicity
counting,” in _Passive nondestructive assay of nuclear materials_, no. LA-UR-07-1403, pp. 1–
23, Los Alamos National Laboratory, 2007.


[31] G. Birkhoff, L. Bondar, J. Ley, R. Berg, R. Swennen, and G. Busca, “On the determination
of pu-240 in solid waster containers by spontaneous fission neutron measurements, application to reprocessing plant waste,” Tech. Rep. EUR-5158e, Commission of the European
Communities, Joint Research Centre, Ispra, 1974.


[32] K. Böhnel, “Die plutoniumbestimmung in kernbrennstoffen mit der neutronen — koinzidensmethode,” Tech. Rep. KFK-2203, Kernforschungszentrum, Karlsruhe, 1975.


[33] N. Envsslin, M. S. Krick, D. G. Langner, M. M. Pickrell, T. D. Reilly, and J. E. Stewart,
“Passive neutron multiplicity counting,” in _Passive Nondestructive Assay of Nuclear Mate-_
_rials_, pp. 1–32, Los Alamos National Laboratory, 2007.


[34] D. M. Cifarelli and W. Hage, “Models for a three-parameter analysis of neutron signal correlation measurement for fissile material assay,” _Nuclear Instruments and Methods in Physics_
_Research Section A_, vol. 251, pp. 550 – 563, 1986.


[35] L. Bondar and B. G. R. Smith, “Interpretation of pu waste measurements by the euroatom
time correlation analyser,” in _Proc. Int. Symp. Managment α-Contaminated Waste_, (Vienna),
June 2-6 1980.


[36] R. Dierckx and W. Hage, “Neutron signal multiplet analysis for the mass determination of
spontaneous fission isotopes,” _Nuclear Science and Engineering_, vol. 85, no. 4, pp. 325–
338, 1983.


[37] W. Hage and D. M. Cifarelli, “On the factorial moments of the neutron multiplicity distribution of fission cascades,” _Nuclear Instruments and Methods in Physics Research Section_
_A_, vol. 236, pp. 165 – 177, 1985.


[38] K. Böhnel, “The effect of multiplication on the quantitative determination of spontaneously
fissioning isotopes by neutron correlation analysis,” _Nuclear Science and Engineering_,
vol. 90, pp. 75 – 82, 1985.


[39] W. Hage and D. M. Cifarelli, “Correlation analysis with neutron count distributions in randomly or signal triggered time intervals for assay of special fissile material,” _Nuclear Sci-_
_ence and Engineering_, vol. 89, pp. 159 – 176, 1985.


148


[40] S. Croft, A. Favalli, D. Hauck, D. Henzlova, and P. Santi, “Feynman variance-to-mean in
the context of passive neutron coincidence counting,” _Nuclear Instruments and Methods in_
_Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equip-_
_ment_, vol. 686, pp. 136 – 144, 2012.


[41] E. Miller, S. Clarke, A. Enqvist, S. A. Pozzi, P. Marleau, and J. K. Mattingly, “Characterization of special nuclear material using a time-correlated pulse-height analysis,” _Journal of_
_Nuclear Materials Managment_, vol. XLI, no. 1, pp. 32–37, 2012.


[42] E. Miller, J. Dolan, S. Clarke, S. Pozzi, A. Tomanin, P. Peerani, P. Marleau, and J. Mattingly, “Time-correlated pulse-height measurements of low-multiplying nuclear materials,”
_Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrome-_
_ters, Detectors and Associated Equipment_, vol. 729, pp. 108 – 116, 2013.


[43] M. G. Paff, M. Monterial, P. Marleau, S. Kiff, A. Nowack, S. D. Clarke, and S. A. Pozzi,
“Gamma/neutron time-correlation for special nuclear material detection â A¸S active stimu- [˘]
lation of highly enriched uranium,” _Annals of Nuclear Energy_, vol. 72, pp. 358 – 366, 2014.


[44] E. Miller, _Characterization of Fissionable Material using Time-Correlated Pule-Height_
_Technique for Liquid Scintillators_ . PhD thesis, University of Michigan, 2012.


[45] P. Marleau, A. Nowack, M. Paff, M. Monterial, S. Clarke, and S. Pozzi, “Gamma/neutron
time-correlation for special nuclear material detection â A¸S active stimulation of highly en- [˘]
riched uranium,” Tech. Rep. SAND2013-7442, Sandia National Laboratories, 2013.


[46] M. Monterial, M. Paff, S. Clarke, E. Miller, S. A. Pozzi, P. Marleau, A. N. S. Kiff, and J. K.
Mattingly, “Time-correlated-pulse-height technique measurements of fissile samples at the
device assembly facility.,” in _Proceesdings of the Institute of Nuclear Materials Manage-_
_ment 54_ _[th]_ _Annual Meeting_, (Palm Desert, California), July 17-22 2013.


[47] N. Kornilov, V. Khriatchkov, M. Dunaev, A. Kagalenko, N. Semenova, V. Demenkov, and
A. Plompen, “Neutron spectroscopy with fast waveform digitizer,” _Nuclear Instruments and_
_Methods in Physics Research Section A_, vol. 497, no. 23, pp. 467 – 478, 2003.


[48] mesytech GmbH, _4 channel particle discriminator module for liquid scintillators_, 2017. "V
2.12_01".


[49] A. Fallu-Labruyere, H. Tan, W. Hennig, and W. Warburton, “Time resolution studies using digital constant fraction discrimination,” _Nuclear Instruments and Methods in Physics_
_Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment_,
vol. 579, no. 1, pp. 247 – 251, 2007. Proceedings of the 11th Symposium on Radiation
Measurements and Applications.


[50] B. von Krosigk, L. Neumann, R. Nolte, S. Röttger, and K. Zuber, “Measurement of the proton light response of various lab based scintillators and its implication for supernova neutrino detection via neutrino–proton scattering,” _The European Physical Journal C_, vol. 73,
no. 4, p. 2390, 2013.


149


[51] H. Schölermann and H. Klein, “Optimizing the energy resolution of scintillation counters at
high energies,” _Nuclear Instruments and Methods_, vol. 169, no. 1, pp. 25 – 31, 1980.


[52] L. Swiderski, M. Moszy´nski, W. Czarnacki, J. Iwanowska, A. Syntfeld-Ka˙zuch, T. Szcz˛e´sniak, G. Pausch, C. Plettner, and K. Roemer, “Measurement of compton edge position in
low-z scintillators,” _Radiation Measurements_, vol. 45, no. 3, pp. 605 – 607, 2010. Proceedings of the 7th European Conference on Luminescent Detectors and Transformers of
Ionizing Radiation (LUMDETR 2009 ).


[53] G. F. Knoll, _Radiation Detection and Measurement_, ch. 10 Radiation Spectroscopy with
Scintillators, p. 229. John Wiley and Sons, fourth ed., 2010.


[54] A. Enqvist, C. C. Lawrence, B. M. Wieger, S. A. Pozzi, and T. N. Massey, “Neutron light
output response and resolution functions in EJ-309 liquid scintillation detectors,” _Nuclear_
_Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, De-_
_tectors and Associated Equipment_, vol. 715, pp. 79 – 86, 2013.


[55] C. C. Lawrence, M. Febbraro, T. N. Massey, M. Flaska, F. Becchetti, and S. A. Pozzi, “Neutron response characterization for an ej299-33 plastic scintillation detector,” _Nuclear Instru-_
_ments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors_
_and Associated Equipment_, vol. 759, no. 0, pp. 16 – 22, 2014.


[56] J. Iwanowska, L. Swiderski, T. Krakowski, M. Moszynski, T. Szczesniak, and G. Pausch,
“The time-of-flight method for characterizing the neutron response of liquid organic scintillators,” _Nuclear Instruments and Methods in Physics Research Section A: Accelerators,_
_Spectrometers, Detectors and Associated Equipment_, vol. 781, pp. 44 – 49, 2015.


[57] R. Katz, S. Sharma, and M. Homayoonfar, “Detection of energetic heavy ions,” _Nuclear_
_Instruments and Methods_, vol. 100, no. 1, pp. 13 – 32, 1972.


[58] L. Stevanato, D. Fabris, X. Hao, M. Lunardon, S. Moretto, G. Nebbia, S. Pesente, L. SajoBohus, and G. Viesti, “Light output of {EJ228} scintillation neutron detectors,” _Applied_
_Radiation and Isotopes_, vol. 69, no. 2, pp. 369 – 372, 2011.


[59] H. Wang, D. Carter, T. N. Massey, and A. Enqvist, “Neutron light output function and
resolution investigation of the deuterated organic liquid scintillator ej-315,” _Radiation Mea-_
_surements_, vol. 89, pp. 99 – 106, 2016.


[60] J. Birks, _The Theory and Practice of Scintillation Counting_ . New York, USA: Perrgamon,
1964.


[61] J. F. Ziegler, “SRIM-2013,” 2013.


[62] J. F. Ziegler, J. P. Biersack, and M. D. Ziegler, _SRIM: The Stopping and Range of Ions in_
_Matter_ . 15th ed. ed., 2015.


[63] M. A. Norsworthy, A. Poitrasson-Riviére, M. L. Ruch, S. D. Clarke, and S. A. Pozzi, “Evaluation of neutron light output response functions in ej-309 organic scintillators,” _Nuclear_
_Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, De-_
_tectors and Associated Equipment_, vol. 842, pp. 20 – 27, 2017.


150


[64] N. Kornilov, I. Fabry, S. Oberstedt, and F.-J. Hambsch, “Total characterization of neutron
detectors with a 252cf source and a new light output determination,” _Nuclear Instruments_
_and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and_
_Associated Equipment_, vol. 599, no. 2 -3, pp. 226 – 233, 2009.


[65] M. Bourne, S. Clarke, M. Paff, A. DiFulvio, M. Norsworthy, and S. Pozzi, “Digital pileup rejection for plutonium experiments with solution-grown stilbene,” _Nuclear Instruments_
_and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and_
_Associated Equipment_, vol. 842, pp. 1 – 6, 2017.


[66] M. Monterial, P. Marleau, S. Clarke, and S. Pozzi, “Application of bayes’ theorem for pulse
shape discrimination,” _Nuclear Instruments and Methods in Physics Research Section A:_
_Accelerators, Spectrometers, Detectors and Associated Equipment_, vol. 795, pp. 318 – 324,
2015.


[67] J. Adams and G. White, “A versatile pulse shape discriminator for charged particle separation and its application to fast neutron time-of-flight spectroscopy,” _Nuclear Instruments_
_and Methods_, vol. 156, no. 3, pp. 459 – 476, 1978.


[68] I. A. Pawełczak, S. A. Ouedraogo, A. M. Glenn, R. E. Wurtz, and L. F. Nakae, “Studies
of neutron _γ_ pulse shape discrimination in ej-309 liquid scintillator using charge integration
method,” _Nuclear Instruments and Methods in Physics Research Section A_, vol. 711, pp. 21
– 26, 2013.


[69] C. Liao and H. Yang, “n/ _γ_ pulse shape discrimination comparison of ej301 and ej339a liquid
scintillation detectors,” _Annals of Nuclear Energy_, vol. 69, pp. 57 – 61, 2014.


[70] S. A. Pozzi, M. M. Bourne, and S. D. Clarke, “Pulse shape discrimination in the plastic
scintillator ej-299-33,” _Nuclear Instruments and Methods in Physics Research Section A_,
vol. 723, pp. 19 – 23, 2013.


[71] K. A. A. Gamage, M. J. Joyce, and N. P. Hawkes, “A comparison of four different digital
algorithms for pulse-shape discrimination in fast scintillators,” _Nuclear Instruments and_
_Methods in Physics Research Section A_, vol. 642, no. 1, pp. 78 – 83, 2011.


[72] Y. Uchida, E. Takada, A. Fujisaki, M. Isobe, K. Ogawa, K. Shinohara, H. Tomita,
J. Kawarabayashi, and T. Iguchi, “A study on fast digital discrimination of neutron and
gamma-ray for improvement neutron emission profile measurement,” _The Review of Scien-_
_tific Instruments_, vol. 85, no. 11, p. 11E118, 2014.


[73] M. Monterial, P. Marleau, M. Paff, S. Clarke, and S. Pozzi, “Multiplication and presence of
shielding material from time-correlated pulse-height measurements of subcritical plutonium
assemblies,” _Nuclear Instruments and Methods in Physics Research Section A: Accelerators,_
_Spectrometers, Detectors and Associated Equipment_, vol. 851, pp. 50 – 56, 2017.


[74] S. A. Pozzi, E. Padovani, and M. Marseguerra, “MCNP-PoliMi: a Monte-Carlo code for correlation measurements,” _Nuclear Instruments and Methods in Physics Research Section A:_
_Accelerators, Spectrometers, Detectors and Associated Equipment_, vol. 513, no. 3, pp. 550
– 558, 2003.


151


[75] J. A. Nelder and R. Mead, “A simplex method for function minimization,” _The Computer_
_Journal_, vol. 7, pp. 308–313, jan 1965.


[76] J. C. Lagarias, J. A. Reeds, M. H. Wright, and P. E. Wright, “Convergence properties of the
Nelder-Mead simplex method in low dimensions,” _SIAM Journal of Optimization_, vol. 9,
pp. 112–147, 1998.


[77] J. Mattingly, “Polyethylene-reflected plutonium metal sphere: Subcritical neutron and
gamma measurements,” Tech. Rep. SAND2009-5804, Sandia National Laboratories, 2009.


[78] M. Monterial, P. Marleau, and S. A. Pozzi, “Demonstration of time-correlated pulse heigh
template-base confirmation measurements,” in _Proceesdings of the Institute of Nuclear Ma-_
_terials Management 57_ _[th]_ .


[79] D. W. MacArthur, D. K. Hauck, and M. K. Smith, “Confirmation of nuclear treaty limited items: Pre-dismantlement vs. post-dismantlement,” in _Proceedings of the 35th Annual_
_ESARDA Symposium_, (Bruges, Belgium), May 28-30 2013.


[80] A. G. Jie Yan, “Nuclear warhead verification: A review of attribute and template systems,”
_Science & Global Security_, vol. 23, no. 3, pp. 157–170, 2015.


[81] J. M. Benz. and J. E. Tanner, “Tempting as a chain of custody tool for arms control,” in
_Proceedings of the 35th Annual ESARDA Symposium_, (Bruges, Belgium), May 28-30 2013.


[82] A. Glaser, B. Barak, and R. Goldston, “A new approach to nuclear warhead verification
using a zero-knowledge protocol.,” in _Proceesdings of the Institute of Nuclear Materials_
_Management 53_ _[rd]_ _Annual Meeting_, (Orlando, Florida), July 15-19 2012.


[83] S. Philippe, R. J. Goldston, A. Glaser, and F. d’Errico, “A simplex method for function
minimization,” _Nature Communications_, vol. 7, Sep 2016.


[84] C. J. MacGahan, M. A. Kupinski, E. M. Brubaker, N. R. Hilton, and P. A. Marleau, “Development of nonsensitive template for arms-control-treaty-verification tasks.,” in _IEEE Sym-_
_posium on Radiation Measurements and Applications_, (Berkeley, California), May 22-26
2016.


[85] C. M. Percher and D. P. Heinrichs, “Criticality safety evaluation for tacs at daf,” Tech. Rep.
LLNL-TR-489234, Lawrence Livermore National Laboratory, June 21 2011.


[86] C. E. Cohn, “Reflected-reactor kinetics,” _Nuclear Science and Engineering_, vol. 13, no. 1,
pp. 12 – 17, 1962.


[87] G. D. Spriggs, R. D. Busch, and J. G. Williams, “Two-region kinetic model for reflected
reactors,” _Annals of Nuclear Energy_, vol. 24, no. 3, pp. 205 – 250, 1997.


[88] J. J. Duderstadt and L. J. Hamilton, _Nuclear Reactor Analysis_, ch. 1 Introductory Concepts
of Nuclear Power Reactor Analysis, pp. 62–63. John Wiley and Sons, 1976.


152


[89] A. Poitrasson-Riviére, M. C. Hamel, J. K. Polack, M. Flaska, S. D. Clarke, and S. A. Pozzi,
“Dual-particle imaging system based on simultaneous detection of photon and neutron collision events,” _Nuclear Instruments and Methods in Physics Research Section A: Accelera-_
_tors, Spectrometers, Detectors and Associated Equipment_, vol. 760, pp. 40 – 45, 2014.


[90] J. E. M. Goldsmith, M. D. Gerling, and J. S. Brennan, “MINER - a mobile imager of neutrons for emergency responders,” in _Symposium on Radiation Measurements and Applica-_
_tions_, (Ann Arbor, MI), June 9-12 2014.


[91] M. Monterial, P. Marleau, and S. A. Pozzi, “Single-view 3-d reconstruction of correlated
gamma-neutron sources,” _IEEE Transactions on Nuclear Science_, vol. 64, pp. 1840–1845,
July 2017.


[92] T. Gozani, “Fission signatures for nuclear material detection,” _IEEE Transactions on Nu-_
_clear Science_, vol. 56, pp. 736–741, June 2009.


[93] K. Geiger and L. V. D. Zwan, “Radioactive neutron source spectra from [9] Be( _α, n_ ) cross
section data,” _Nuclear Instruments and Methods_, vol. 131, no. 2, pp. 315 – 321, 1975.


[94] M. Wernick and J. Aarsvold, _Emission Tomography: The Fundamentals of PET and SPECT_ .
Elsevier Science, 2004.


[95] R. W. Todd, J. M. Nightingale, and D. B. Everett, “A proposed [gamma] camera,” _Nature_,
vol. 251, pp. 132–134, Sep 1974.


[96] V. Schönfelder, “Imaging principles and techniques in space-borne gamma-ray astronomy,”
_Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrom-_
_eters, Detectors and Associated Equipment_, vol. 525, no. 1-2, pp. 98 – 106, 2004. Proceedings of the International Conference on Imaging Techniques in Subatomic Physics,
Astrophysics, Medicine, Biology and Industry.


[97] D. Herzo, R. Koga, W. Millard, S. Moon, J. Ryan, R. Wilson, A. Zych, and R. White,
“A large double scatter telescope for gamma rays and neutrons,” _Nuclear Instruments and_
_Methods_, vol. 123, no. 3, pp. 583 – 597, 1975.


[98] G. W. Phillips, “Gamma-ray imaging with compton cameras,” _Nuclear Instruments and_
_Methods in Physics Research Section B: Beam Interactions with Materials and Atoms_,
vol. 99, no. 1, pp. 674 – 677, 1995.


[99] G. W. Phillips, “Applications of compton imaging in nuclear waste characterization and
treaty verification,” in _Nuclear Science Symposium, IEEE_, (Albuquerque, NM), Nov 9-15
1997.


[100] H. O. Anger, “Scintillation camera with multichannel collimators,” _J Nucl Med._, vol. 5,
pp. 583 – 531, July 1964.


[101] P. Vanier, “Improvements in coded aperture thermal neutron imaging,” in _SPIE Conference_
_Proceedings_, vol. 5199, p. 124, 2004.


153


[102] P. Marleau, J. Brennan, E. Brubaker, and J. Steele, “Results from the coded aperture neutron imaging system,” in _IEEE Nuclear Science Symposuim Medical Imaging Conference_,
pp. 1640–1646, Oct 2010.


[103] C. G. Wahl, W. R. Kaye, W. Wang, F. Zhang, J. M. Jaworski, A. King, Y. A. Boucher, and
Z. He, “The polaris-h imaging spectrometer,” _Nuclear Instruments and Methods in Physics_
_Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment_,
vol. 784, pp. 377 – 381, 2015. Symposium on Radiation Measurements and Applications
2014 (SORMA XV).


[104] G. Legge and P. V. der Merwe, “A double scatter neutron spectrometer,” _Nuclear Instruments_
_and Methods_, vol. 63, no. 2, pp. 157 – 165, 1968.


[105] R. Barnowski, A. Haefner, L. Mihailescu, and K. Vetter, “Scene data fusion: Real-time
standoff volumetric gamma-ray imaging,” _Nuclear Instruments and Methods in Physics_
_Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment_,
vol. 800, pp. 65 – 69, 2015.


[106] J. E. McKisson, P. S. Haskins, G. W. Phillips, S. E. King, R. A. August, R. B. Piercey, and
R. C. Mania, “Demonstration of three-dimensional imaging with a germanium compton
camera,” _IEEE Transactions on Nuclear Science_, vol. 41, pp. 1221–1224, Aug 1994.


[107] M. Hamel, J. Polack, A. Poitrasson-Riviére, S. Clarke, and S. Pozzi, “Localization and
spectral isolation of special nuclear material using stochastic image reconstruction,” _Nu-_
_clear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers,_
_Detectors and Associated Equipment_, vol. 841, pp. 24 – 33, 2017.


[108] M. Hamel, J. Polack, A. Poitrasson-Riviére, M. Flaska, S. Clarke, S. Pozzi, A. Tomanin,
and P. Peerani, “Stochastic image reconstruction for a dual-particle imaging system,” _Nu-_
_clear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers,_
_Detectors and Associated Equipment_, vol. 810, pp. 120 – 131, 2016.


[109] A. Andreyev, A. Sitek, and A. Celler, “Fast image reconstruction for compton camera using
stochastic origin ensemble approach,” _Medical Physics_, vol. 38, no. 1, 2011.


[110] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel,
P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher,
M. Perrot, and E. Duchesnay, “Scikit-learn: Machine learning in Python,” _Journal of Ma-_
_chine Learning Research_, vol. 12, pp. 2825–2830, 2011.


[111] P. Cattaneo, M. D. Gerone, F. Gatti, M. Nishimura, W. Ootani, M. Rossella, S. Shirabe,
and Y. Uchiyama, “Time resolution of time-of-flight detector based on multiple scintillation
counters readout by sipms,” _Nuclear Instruments and Methods in Physics Research Section_
_A: Accelerators, Spectrometers, Detectors and Associated Equipment_, vol. 828, pp. 191 –
200, 2016.


154


[112] S. Pozzi, S. Clarke, W. Walsh, E. Miller, J. Dolan, M. Flaska, B. Wieger, A. Enqvist,
E. Padovani, J. Mattingly, D. Chichester, and P. Peerani, “Mcnpx-polimi for nuclear nonproliferation applications,” _Nuclear Instruments and Methods in Physics Research Section_
_A: Accelerators, Spectrometers, Detectors and Associated Equipment_, vol. 694, pp. 119 –
125, 2012.


[113] E. O. Lebigot, “Uncertainties: a Python package for calculations with uncertainties.” Version 2.4.8.1.


[114] F. Pino, L. Stevanato, D. Cester, G. Nebbia, L. Sajo-Bohus, and G. Viesti, “The light output and the detection efficiency of the liquid scintillator ej-309,” _Applied Radiation and_
_Isotopes_, vol. 89, pp. 79 – 84, 2014.


155


