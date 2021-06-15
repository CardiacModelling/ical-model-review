# Example Equations
The equations for a Hodgkin-Huxley model and a Markov model can be found in [Example Model](https://github.com/CardiacModelling/ical-review/blob/master/Supplementary_Information/Example_Models.ipynb). 

# Calcium-dependent Inactivation

A frame by frame comparison of calcium dependent inactivation of all models as calcium concentration is increased can be found [here](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/calcium_sensitivity/CDI/calcium_sensitivity_animation.mp4).

# Outliers

## Kinetic Protocols

The [Kinetic_Protocols_outliers(ICaL)](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols/Kinetic_Protocols_outliers(ICaL).pdf) figure shows that the simulated response of all 54 models to the activation and inactivation protocols is varied across different models. </br>
<em>Left</em>: The normalised current from the activation protocol </br>
<em>Right</em>: The normalised current from the inactivation protocol </br>
Highlighted models have characteristics that are different from the standard behaviour of the models and are discussed in the text. **URL to WL Experiment here** </br>
</br>

The [Kinetic_Protocols_outliers(open_prob)](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols/Kinetic_Protocols_outliers(open_prob).pdf) figure shows that the simulated response of all 54 models to the activation and inactivation protocols is varied across different models. </br>
<em>Left</em>: The normalised open probability from the activation protocol </br>
<em>Right</em>: The normalised open probability from the inactivation protocol </br>
The normalisation was performed to accommodate for those models that do not fully open or those that have an open probability greater than one.
This normalisation was performed by dividing the peak open probability with the maximum peak.
</br>
Highlighted models have characteristics that are different from the standard behaviour of the models and are discussed in the text. **URL to WL Experiment here** </br>
</br>

The outlier behaviour of the models is explained below: </br>
- [McAllister et al. 1975](https://models.physiomeproject.org/exposure/60e23c3228a3e455699846704006a8fe) attains its maximum peak current of activation at a lower voltage as compared to other models. 
This may be because the currents in these models are the "secondary inward current" which includes all calcium currents including the T-type calcium current rather than pure ICaL. 
The open probability of this model has two slopes.
The first slope is higher than all other probabilities as shown in the figure [Kinetic_Protocols_outliers(open_prob)](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols/Kinetic_Protocols_outliers(open_prob).pdf).
This might be the reason for the peak current at a low voltage in simulated ICaL. </br>

- [Beeler & Reuter 1977](https://chaste.cs.ox.ac.uk/WebLab/entities/models/1/versions/4680f3e8395da43250412aa3a16013090da62570),
[Dokos et al. 1996](https://models.physiomeproject.org/exposure/462ab10275dfc099166c8a0e4f9e1be3),
[Corrias et al. 2011](https://github.com/Chaste/cellml/blob/master/cellml/corrias_purkinje_2011.cellml) and Pohl et al. 2016 
do not inactivate at higher voltages of the activation protocol.
The open probabilities of the models in Figure [Kinetic_Protocols_outliers(open_prob)](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols/Kinetic_Protocols_outliers(open_prob).pdf) are consistent with other models.
However, the driving force of all these models do not reverse or approach reversal potential within the physiological range of voltage. 
This might be the reason for the prolonged high activation peaks ICaL in Figure [Kinetic_Protocols_outliers(ICaL)](https://github.com/CardiacModelling/ical-review/tree/master/Data_Analysis/Kinetic_protocols/Kinetic_Protocols_outliers(ICaL).pdf). </br>

- [Liu et al. 1993](https://scrambler.cs.ox.ac.uk/entities/models/565/versions/640e7d71267fb9c2e7bd842f8a3ff14d801c847a) this model has an exponentially increasing driving term because of which the the I-V curve for the acyivation protocol attains very high positive values. This can be seen in [this figure](https://scrambler.cs.ox.ac.uk/experiments/29364/versions/29910/outputs_Ohmic_Driving_Term_gnuplot_data.csv/displayPlotFlot).

- [Priebe & Beuckelmann](https://scrambler.cs.ox.ac.uk/entities/models/38/versions/2a634280b8ddfa3d9b16b396af548b07858af34d) also has similar driving forces like the models discussed before. 
However, the maximum open probability of this model is different from other models and approaches zero at higher test voltages of the activation protocol.
Thus, the inconsistent driving force and open probability seem to compensate for each other to give a consistent ICaL. </br>

## Action Potential Clamp Protocol

Some of the simulated currents under the three AP-CaT-clamp experiments are positive.
Figure [AP_CaT_Clamp_driving_term_outlier](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Driving_term_outlier/I_CaL_AP_CaT_Clamp_driving_Term_outlier.pdf) shows the simulated driving force of the dual AP-CaT-clamp with inherent localisation experiment which reverses its sign for a small duration of the AP clamp.
[Demir et al. 1994](https://models.physiomeproject.org/exposure/15dc665c02ca9955b8e79fbace81a9e5), 
[Zhang et al. 2000](https://models.physiomeproject.org/exposure/01f6a47881da1925315d1d89d3a8d901) and 
[Kurata et al. 2002](https://models.physiomeproject.org/exposure/47b969553fcfe6f875d4e38d1fd33986) 
have an Ohmic driving force and the reversal potential of these models is less than the highest voltage of the AP clamp that we use in this review.
Similarly, Liu 1993 also has a positive driving force for some of the voltage potentials used in the AP Clamp becuase of its exponentially increasing driving force discussed above. 
[Kurata et al. 2002 (ICaL)](https://models.physiomeproject.org/exposure/47b969553fcfe6f875d4e38d1fd33986) and 
Wilders et al. 1991 have a GHK driving force and these models have a very high contribution of the ICaL carried by potassium ions, which makes the total current positive for high voltages during the AP clamp.

### Grouping by various factors
We have grouped the open probability from the dual AP-CaT-clamp under the inherent localisation experiment according to various factors including species, cell type, gating and localisation of channel.
We first attempted to find similarities among the models according to their species and cell type, however failed to see a strong agreement within the models grouped on the basis of these categories (Figure [species_panel](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/species_panel.pdf) and [cell_panel](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/cell_panel.pdf)).
Nevertheless, Canine models seemed to have the most agreement within themselves compared to other species and Purkinje models are most similar as compared to models of other cell types.

This lack of agreement of the simulated models led to the search for better ways to classify these models.
We observe a more convergent pattern of the simulated models as the complexity of gating increases as shown in Figure [gating_panel](https://github.com/CardiacModelling/ical-review/blob/master/Data_Analysis/AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/gating_panel.pdf).
