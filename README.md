# Models of the cardiac L-type calcium current: a quantitative comparison
This repository contains all protocols, models, codes, figure generating files and animation for the CaV Review.

- [Example Models](https://github.com/CardiacModelling/ical-review/blob/master/Example_Models.ipynb) gives the equations for a Hodgkin-Huxley model and a Markov model. 
- [Models](https://github.com/CardiacModelling/ical-review/tree/master/Models)
- [Figure 6](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Driving_term/Driving_Term_Voltage_dependence.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Driving_Term_Range).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Driving_term).
- [Figure 7](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/activation_panel.pdf), [Figure 8](https://github.com/CardiacModelling/ical-model-comparison/blob/master/Data_Analysis/Kinetic_protocols/activation_outlier.pdf), [Figure 9](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/inactivation_panel.pdf), and [Figure 10](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/Kinetic_protocols/recovery_panel.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Kinetic_Protcols).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols).
- [Figure 11](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/CDI/calcium_sensitivity.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Calcium-dependent%20inactivation).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_sensitivity/CDI).
- [Figure 12](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/ic50/ic50_histogram.pdf)
	- Protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Python).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_sensitivity/ic50).
- [Figure 14](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/ICal_All/I_CaL_AP_CaT_Clamp_normalize.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Action_Potential_Clamps).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/AP_CaT_Clamp/ICal_All).
- [Figure 15](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/chronology_panel.pdf) and [Figure 16](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/calcium_localization.pdf)
	- WebLab protocol can be viewed [here](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Action_Potential_Clamps/AP%20CaT%20Clamp%20(inherent%20localization)).
	- Figure generating files are [here](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp).

## Software
- **Web Lab** Simulations were run using the Cardiac Electrophysiology Web Lab.
  See the resultant experiment matrix at [https://tinyurl.com/y5vdjb8h](https://tinyurl.com/y5vdjb8h).
  Find out more about Web Lab from [doi: 10.1016/j.bpj.2015.12.012](https://dx.doi.org/10.1016%2Fj.bpj.2015.12.012).
- **Python** The code requires Python (either 2.7 or 3.3+) and the Python dependencies PINTS, Myokit, `pandas`, and `warnings`.
  PINTS can be installed using the instructions on [https://github.com/pints-team/pints](https://github.com/pints-team/pints).
  The other dependencies can be installed with `pip`, e.g. `pip install myokit` (or `pip3 install myokit` for some python 3 environments).
- **CellML** All model files are available in the CellML format.
  You can find out more about CellML from [cellml.org](https://www.cellml.org/).
- **Veusz** We have used this scientific plotting and graphing program to generate the figures for this work.
  This can be download from [https://veusz.github.io/](https://veusz.github.io/download/).

