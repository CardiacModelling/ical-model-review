# Outliers

## Action Potential Clamp Protocol

Some of the simulated currents under the three AP-CaT-clamp experiments are positive.
Figure [AP_CaT_Clamp_driving_term_outlier](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Driving_term_outlier/I_CaL_AP_CaT_Clamp_driving_Term_outlier.pdf) shows the simulated driving force of the dual AP-CaT-clamp with inherent localisation experiment which reverses its sign for a small duration of the AP clamp.
[Demir et al. 1994](https://models.physiomeproject.org/exposure/15dc665c02ca9955b8e79fbace81a9e5), 
[Zhang et al. 2000](https://models.physiomeproject.org/exposure/01f6a47881da1925315d1d89d3a8d901), and 
[Kurata et al. 2002](https://models.physiomeproject.org/exposure/47b969553fcfe6f875d4e38d1fd33986) 
have an Ohmic driving force and the reversal potential of these models is less than the highest voltage of the AP clamp that we use in this review.
Similarly, Liu 1993 also has a positive driving force for some of the voltage potentials used in the AP Clamp becuase of its exponentially increasing driving force discussed above. 
[Kurata et al. 2002 (ICaL)](https://models.physiomeproject.org/exposure/47b969553fcfe6f875d4e38d1fd33986) and 
Wilders et al. 1991 have a GHK driving force and these models have a very high contribution of the ICaL carried by potassium ions, which makes the total current positive for high voltages during the AP clamp.
[Iyer et al. 2004](https://models.physiomeproject.org/exposure/e0922113f8ca0258441cc9f3d53dcc08/iyer_mazhari_winslow_2004.cellml), and [Michaelilova et al. 2005](https://scrambler.cs.ox.ac.uk/entities/models/557/versions/e4cc9339c5b76465ace8cd0870de08d4a5265edc) also have a GHK driving term and the direction of the flux reverses for very high potentials.
The experiments can be compared on Web Lab at [https://tinyurl.com/t9ta8c2a](https://tinyurl.com/t9ta8c2a).
### Grouping by various factors
We have grouped the open probability from the dual AP-CaT-clamp under the inherent localisation experiment according to various factors including species, cell type, gating and localisation of channel.
We first attempted to find similarities among the models according to their species and cell type, however failed to see a strong agreement within the models grouped on the basis of these categories (Figure [species_group](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/species_group.pdf) and [cell_group](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/cell_group.pdf)).
Nevertheless, canine models seemed to have the most agreement within themselves compared to other species and Purkinje models are most similar as compared to models of other cell types.

This lack of agreement of the simulated models led to the search for better ways to classify these models.
We observe a more convergent pattern of the simulated models as the complexity of gating increases as shown in Figure [gating_group](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/gating_group.pdf).
