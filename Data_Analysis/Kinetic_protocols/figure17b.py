#!/usr/bin/env python3
#
# ICaL review figure: Priebe vs Inada et al. (with AP clamp)
#
#
#Load libraries
import myokit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator)

# Load AP clamp signal
d = np.loadtxt('../../Protocols/Action_Potential_Clamps/AP Clamp/AP_clamp.csv',
               delimiter=',')
ap_t = d[:, 0]
ap_v = d[:, 1]
ap_offset = -ap_t[0]
print(ap_offset)
print(ap_t[:20])
ap_t += ap_offset
print(ap_t[:20])

tmax = ap_t[-1] #+ (ap_t[-1] - ap_t[-2])
print(tmax)
del(d)

# Load WL IV curve
d = myokit.DataLog.load_csv('data/iv-priebe-inada.csv')
iv_v = d['vm']
iv_p = d['priebe']
iv_i = d['inada']
del(d)

# Shared variable names (todo: use labels instead)
time = 'environment.time'
vm = 'membrane.V'
ical = 'L_type_Ca_current.i_CaL'
gcal = 'L_type_Ca_current.g_CaL'
fancy_names = { # todo: use display name or other model meta name
    'priebe-1998': 'Priebe & Beuckelmann 1998',
    'inada-2009': 'Inada et al. 2009',
}

# Load models, create simulations
simulations = {}
for name in fancy_names:
    m = myokit.load_model(name + '.mmt')
    v = m.get(vm)
    v.set_binding(None)
    v.set_binding('pace')
    s = myokit.Simulation(m)
    simulations[name] = s

    # Pre-pace for 10s at -90mV
    s.set_protocol(myokit.pacing.constant(-90))
    s.pre(10e3)

    #
    # Find scaling for ical so that IV curve peaks at -1.0
    #
    debug = False

    # Get V at which current peaks
    vmax = iv_v[np.argmin(iv_p)]
    print(f'{name} peaks at v={vmax}')

    # Simulate a voltage step to this V, and record the peak current
    s.set_protocol(myokit.pacing.constant(vmax))
    d = s.run(1000, log=[time, ical])
    imax = np.min(d[ical])
    if debug:
        plt.figure()
        plt.plot(d.time(), d[ical])

    # Scale the conductance so that the peak current is -1
    g = m.get(gcal).eval()
    s.set_constant(gcal, g / -imax)

    if debug:
        s.reset()
        d = s.run(1000, log=[time, ical])
        imax = np.min(d[ical])
        plt.plot(d.time(), d[ical])
        plt.show()

#
# Create figure
#

# Set font
matplotlib.rc('font', family='arial', size=8)

# Tick style
ticks = dict(which='both', direction='in', bottom=True, top=True, left=True,
             right=True)

fig = plt.figure(figsize = (6.8, 2.6))
fig.subplots_adjust(0.085, 0.14, 0.99, 0.99, wspace=0.45)
grid = fig.add_gridspec(1, 3)

#
# IV curves
#
ax1 = fig.add_subplot(grid[0, 0])
ax1.tick_params(**ticks)
ax1.minorticks_on()
ax1.set_xlabel('Membrane potential (mV)')
ax1.set_ylabel('Peak Current (normalised)')
ax1.set_xlim(-45, 60)
ax1.set_ylim(-1.05, 0.15)
ax1.plot(iv_v, iv_p, label='Priebe 1998')
ax1.plot(iv_v, iv_i, label='Inada 2009')
ax1.legend(frameon=False, loc= 'upper right')

#
# AP clamp protocol
#
ax2 = fig.add_subplot(grid[0, 1:])
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Current (normalised)')
ax2.tick_params(**ticks)
ax2.minorticks_on()

# Simulate
for name, fancy in fancy_names.items():
    s = simulations[name]
    s.reset()
    s.set_fixed_form_protocol(ap_t, ap_v)
    d = s.run(tmax, log=[time, ical, vm])
    ax2.plot(d.time() - ap_offset, d[ical], label=fancy)


#
# Save
#
print('Saving...')
plt.savefig('figure17b.png')
#plt.savefig('figure17b.eps')
#plt.savefig('figure17b.pdf')
plt.close()
