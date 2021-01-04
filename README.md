# Models of the cardiac L-type calcium current: a quantitative comparison
This repository contains all protocols, models, codes, figure generating files and animation for the CaV Review.

## Supporting materials
- Protocols
	- Web Lab
		- [Kinetic Protocols](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Kinetic_Protcols)
		- Action Potential and Calcium Transient
			- [Action Potential Clamp](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Action_Potential_Clamps/AP%20Clamp)
			- [Action Potential and Calcium Transient Clamp (bulk cytosol localization)](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Action_Potential_Clamps/AP%20CaT%20Clamp%20(bulk%20cytosol_localization))
			- [Action Potential and Calcium Transient Clamp (inherent localization)](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Action_Potential_Clamps/AP%20CaT%20Clamp%20(inherent%20localization))
		- [Calcium-dependent Inactivation](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Calcium-dependent%20inactivation)
		- [Driving Term Range](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Web%20Lab/Driving_Term_Range)
	- Python
		- [IC50](https://github.com/CardiacModelling/ical-review/tree/master/Protocols/Python)
- [Models](https://github.com/CardiacModelling/ical-review/tree/master/Models)
- Figures, and figure generating files
	- [Kinetic Protocols](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols)
	- Calcium Sensitivity
		- [Comparison of inactivation levels at different concentrations](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_sensitivity/CDI)
		- [Comparison of calcium concentration to bring about 50% drop in inactivation peak](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_sensitivity/ic50)
	- [Action Potential and Calcium Transient Clamps](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/AP_CaT_Clamp)
	- [Driving Term](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Driving_term)
	- [Calcium Transient](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_transient)
	- [Python scripts to calculate RMSD and NRMSD](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/calcium_transient)
- Supplementary Information : [README file](https://github.com/CardiacModelling/ical-review/blob/master/Supplementary_Information/README.md) gives a guide to the supporting material for this paper.

## About Software
- Web Lab : Simulations were run using the Cardiac Electrophysiology Web Lab. See the resultant experiment matrix at [https://tinyurl.com/y5vdjb8h](https://tinyurl.com/y5vdjb8h). Find out more about Web Lab from [doi: 10.1016/j.bpj.2015.12.012](https://dx.doi.org/10.1016%2Fj.bpj.2015.12.012).
- Python : The code requires Python (either 2.7 or 3.3+) and two dependencies: PINTS and Myokit. Myokit can be installed using <pip install myokit> (or <pip3 install myokit> for some python 3 environments). PINTS can be installed using the instructions on [https://github.com/pints-team/pints](https://github.com/pints-team/pints). Numpy is also required to run this script. Data Analysis script requires pandas and warnings.
- CellML : All model files are available in the CellML format. You can find out more about CellML from [doi: 10.3389/fphys.2015.00026](https://www.frontiersin.org/articles/10.3389/fphys.2015.00026/full).
- Veusz: We have used this scientific plotting and graphing program to generate the figures for this work. This can be download from [https://veusz.github.io/](https://veusz.github.io/download/).

