# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 19:44:06 2020

@author: Aditi

Returns: 
conc: The IC50 value. This is represented by the calcium concentration that reduces inactivation peak by 50%.
The initial peak is measured at 10^-9 mM.
Variables: 'L_type_Ca_current.i_CaL' and 'membrane.V' are essential requirements. 
            Carefully tag the calcium concentration that is required to evaluate calcium sensitivity.
Others: This file assumes assumes time units to be in milliseconds, voltage in millivolts and all concentrations in millimolars.
        This file uses standard notations for the model variables which may differ from modle to model.
        
"""
#Load libraries
import myokit
import numpy as np

#Load model (can change the model directory as desired)
m = myokit.load_model('../pandit_2001.mmt')

#Clamp the voltage
clamp_voltage = m.get('membrane.V')
if clamp_voltage.binding() == None:
    clamp_voltage.set_rhs(0)
    if clamp_voltage.is_state() == True:
        clamp_voltage.demote()
else:
    clamp_voltage.set_binding(None)

#Clamp all ioninc concentrions
try:
    clamp_sodium_ext = m.get('sodium_dynamics.Na_o')
    if clamp_sodium_ext.is_state():
        clamp_sodium_ext.demote()
    clamp_sodium_ext.set_rhs(140)
except:
    print("External Sodium concentration not present in the model")

try:
    clamp_potassium_ext = m.get('potassium_dynamics.K_o')
    if clamp_potassium_ext.is_state():
        clamp_potassium_ext.demote()
    clamp_potassium_ext.set_rhs(5)
except:
    print("External Potassium concentration not present in the model")

try:
    clamp_calcium_ext = m.get('calcium_dynamics.K_o')
    if clamp_calcium_ext.is_state():
        clamp_calcium_ext.demote()
    clamp_calcium_ext.set_rhs(2)
except:
    print("External Calcium concentration not present in the model")

try:
    clamp_sodium_i = m.get('sodium_dynamics.Na_i')
    if clamp_sodium_i.is_state():
        clamp_sodium_i.demote()
    clamp_sodium_i.set_rhs(10)
except:
    print("Cytosolic Sodium concentration not present in the model")
    
try:
    clamp_sodium_ss = m.get('sodium_dynamics.Na_ss')
    if clamp_sodium_ss.is_state():
        clamp_sodium_ss.demote()
    clamp_sodium_ss.set_rhs(10)
except:
    print("Submembrane space Sodium concentration not present in the model")
    
try:
    clamp_sodium_dyd = m.get('sodium_dynamics.Na_dyd')
    if clamp_sodium_dyd.is_state():
        clamp_sodium_dyd.demote()
    clamp_sodium_dyd.set_rhs(10)
except:
    print("Dyadic Sodium concentration not present in the model")

try:
    clamp_potassium_i = m.get('potassium_dynamics.K_i')
    if clamp_potassium_i.is_state():
        clamp_potassium_i.demote()
    clamp_potassium_i.set_rhs(140)
except:
    print("Cytosolic Potassium concentration not present in the model")

#Some models may have ICaL channel in multiple compartments (Ca_i/ Ca_dyd/ Ca_ss),
# In those cases clamp all compartment concentrations and 
# evaluate sensitivity on a case by case basis

try:
    clamp_calcium = m.get('calcium_dynamics.Ca_ss')
    if clamp_calcium.is_state():
        clamp_calcium.demote()
    clamp_calcium.set_rhs(0.000000001)
except ValueError:
    print("Oops! Your model does not have any submembrane calcium concentration. Tag a different variable if you would like to evaluate that sensitivity")

#Simulate at holding potential  
s = myokit.Simulation(m)
s.set_constant('membrane.V', -90.01)
s.pre(10000)
#P1   
s.set_constant('membrane.V', -90.01)
d_p1 = s.run(500, log=['environment.time', 'L_type_Ca_current.i_CaL'])
#P2    
s.set_constant('membrane.V', -0.01)
d_p2 = s.run(120, d_p1)

# Find peak current
current = d_p2['L_type_Ca_current.i_CaL']
index = np.argmax(np.abs(current))
peak_initial = current[index]

#Concentration range to expore the IC50 value 
conc_range = np.logspace(-9, 0, num=100)

for conc in conc_range:
    clamp_calcium.set_rhs(conc)
    p = myokit.Simulation(m)
    p.set_constant('membrane.V', -90.01)
    p.run(10000, log =[])
    #P1   
    p.set_constant('membrane.V', -60.01)
    d_p1 = p.run(400, log=['environment.time', 'L_type_Ca_current.i_CaL'])
    #P2    
    p.set_constant('membrane.V', -0.01)
    d_p2 = p.run(120, d_p1)
    p.reset()
    
    current = d_p2['L_type_Ca_current.i_CaL']
    index = np.argmax(np.abs(current))
    peak_final = current[index]
    
    if abs(peak_final) < 0.5*abs(peak_initial):
        print ("IC50 calcium concentration is " + str(conc))
        break
    if conc == conc_range[-1]:
        print("Out of range")
    
    
    