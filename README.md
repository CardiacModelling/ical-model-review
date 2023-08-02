# Models of the cardiac L-type calcium current: a quantitative comparison
This repository contains all protocols, models, codes, figure generating files, and animation for the comparison of ICaL models.

An interactive view of our main results can be viewed on the [Cardiac Electrophysiology Web Lab](https://scrambler.cs.ox.ac.uk/stories/8).

- [Example Models](https://github.com/CardiacModelling/ical-review/blob/master/Example_Models.ipynb) gives the equations for a Hodgkin-Huxley model and a Markov model. 
- [Models](https://github.com/CardiacModelling/ical-review/tree/master/Models) contains the CellML implementations for all models used (quantitatively) in this study, with links to the original sources and an overview of major [data sources](https://github.com/CardiacModelling/ical-model-comparison/blob/master/Models/data.md) used in their construction.
- [Figure 1](https://github.com/CardiacModelling/ical-model-comparison/blob/master/Data_Analysis/AP_CaT_Clamp/AP_Clamp_protocol/figure1.pdf)
	- Figure generating file is [here](https://github.com/CardiacModelling/ical-model-comparison/tree/master/Data_Analysis/AP_CaT_Clamp/AP_Clamp_protocol).
- [Figure 6](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Driving_term/figure6.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Driving_Term_Range).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Driving_term).
- [Figure 7](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/figure7.pdf), [Figure 8](https://github.com/CardiacModelling/ical-model-comparison/blob/master/Data_Analysis/Kinetic_protocols/figure8.pdf), [Figure 9](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/figure9.pdf), and [Figure 10](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/figure10.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Kinetic_Protcols).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols).
- [Figure 11](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/CDI/figure11.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Calcium-dependent%20inactivation).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_sensitivity/CDI).
- [Figure 12](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/figure12.pdf)
	- Protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/ic50).
	- Figure generating files and graphical tests of the regression line are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_sensitivity/ic50).
- [Figure 13](https://github.com/CardiacModelling/ical-model-comparison/blob/master/Data_Analysis/AP_CaT_Clamp/AP_Clamp_protocol/figure13.pdf)
	- Figure generating file is [here](https://github.com/CardiacModelling/ical-model-comparison/tree/master/Data_Analysis/AP_CaT_Clamp/AP_Clamp_protocol).  
- [Figure 14](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/ICal_All/figure14.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Action_Potential_Clamps).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/AP_CaT_Clamp/ICal_All).
- [Figure 15](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/figure15.pdf) and [Figure 16](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/figure16.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Action_Potential_Clamps/AP%20CaT%20Clamp%20(inherent%20localization)).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp).
- [Figure 17](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/figure17.pdf) generated using the python script [here](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/figure17.py).

## Software
- **Web Lab** Simulations were run using the Cardiac Electrophysiology Web Lab.
  An interactive overview of our results is [available here](https://scrambler.cs.ox.ac.uk/stories/8).
  Find out more about Web Lab from [doi: 10.1016/j.bpj.2015.12.012](https://dx.doi.org/10.1016%2Fj.bpj.2015.12.012).
- **Python** The code requires Python (either 2.7 or 3.3+) and the Python dependencies Myokit, and `pandas`.
  The other dependencies can be installed with `pip`, e.g. `pip install myokit` (or `pip3 install myokit` for some python 3 environments).
- **CellML** All model files are available in the CellML format.
  You can find out more about CellML from [cellml.org](https://www.cellml.org/).
- **Veusz** We have used this scientific plotting and graphing program to generate the figures for this work.
  This can be download from [https://veusz.github.io/](https://veusz.github.io/download/).

## Citing this repository

Please refer to the information in the [CITATION file](./CITATION).
