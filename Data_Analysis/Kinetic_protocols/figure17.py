#!/usr/bin/env python3
#
# ICaL review figure: Priebe vs Inada et al.
#
#
#Load libraries
import myokit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator)

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
    s = myokit.Simulation(m)
    simulations[name] = s

    # Pre-pace for 10s at -90mV
    s.set_constant(vm, -90)
    s.pre(10e3)

    #
    # Find scaling for ical so that IV curve peaks at -1.0
    #
    debug = False

    # Get V at which current peaks
    vmax = iv_v[np.argmin(iv_p)]
    print(f'{name} peaks at v={vmax}')

    # Simulate a voltage step to this V, and record the peak current
    s.set_constant(vm, vmax)
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

#
# IV curves
#
ax1 = fig.add_subplot(1, 3, 1)
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
# First step protocol: -90, 10, 5
#
ax2 = fig.add_subplot(1, 3, 2)
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Current (normalised)')
ax2.tick_params(**ticks)
ax2.minorticks_on()
ax2.axvline(150, ls='--', color='#bbbbbb')

# Simulate
for name, fancy in fancy_names.items():
    s = simulations[name]
    s.reset()
    s.set_constant(vm, 10.01)
    d = s.run(150, log=[time, ical])
    s.set_constant('membrane.V', 5.01)
    d = s.run(150, d).npview()
    ax2.plot(d.time(), d[ical], label=fancy)

# Voltage protocol
ax2.plot(
    0.52 + np.array([0, 0.1, 0.1, 0.2, 0.2, 0.3]),
    0.1 + np.array([0, 0, 0.2, 0.2, 0.11, 0.11]),
    'k', transform=ax2.transAxes)
ax2.text(0.31, 0.12, '$-90$ mV', transform=ax2.transAxes)
ax2.text(0.56, 0.32, '10 mV', transform=ax2.transAxes)
ax2.text(0.75, 0.23, '5 mV', transform=ax2.transAxes)

#
# First step protocol: -90, 60, 5
#
ax3 = fig.add_subplot(1, 3, 3)
ax3.set_xlabel('Time (ms)')
ax3.set_ylabel('Current (normalised)')
ax3.tick_params(**ticks)
ax3.minorticks_on()
ax3.axvline(150, ls='--', color='#bbbbbb')

# Simulate
for name, fancy in fancy_names.items():
    s = simulations[name]
    s.reset()
    s.set_constant(vm, 60.01)
    d = s.run(150, log=[time, ical])
    s.set_constant('membrane.V', 5.01)
    d = s.run(150, d).npview()
    ax3.plot(d.time(), d[ical], label=fancy)

# Voltage protocol
ax3.plot(
    0.06 + np.array([0, 0.1, 0.1, 0.2, 0.2, 0.3]),
    0.12 + np.array([0, 0, 0.3, 0.3, 0.11, 0.11]),
    'k', transform=ax3.transAxes)
ax3.text(0.03, 0.06, '$-90$ mV', transform=ax3.transAxes)
ax3.text(0.11, 0.44, '60 mV', transform=ax3.transAxes)
ax3.text(0.29, 0.25, '5 mV', transform=ax3.transAxes)

#
# Save
#
print('Saving...')
plt.savefig('figure17.png')
plt.savefig('figure17.eps')
plt.savefig('figure17.pdf')
plt.close()
