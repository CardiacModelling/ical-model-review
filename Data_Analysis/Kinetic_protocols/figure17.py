#
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


models = ['priebe-1998.mmt', 'inada-2009.mmt']

# Set font
matplotlib.rc('font', family='arial', size = 8)

fig = plt.figure(figsize = (6.8, 2.6))
fig.subplots_adjust(0.085, 0.14, 0.99, 0.99, wspace=0.3)
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

axes = [ax2, ax3]
pro_step1 = [10.01, 60.01]

for ax, step in zip(axes, pro_step1):
    for model in models:

        print(model)
        m = myokit.load_model(model)

        v = m.get('membrane.V')
        v.set_binding(None)
        s = myokit.Simulation(m)

        # Stabilise the model a steady state by running for 10 seconds
        s.set_constant('membrane.V', - 90.01)
        s.run(10000, log = [])
        s.set_time(0)

        # Step to 60 mV
        s.set_constant('membrane.V', step)
        d = s.run(150, log=['L_type_Ca_current.i_CaL', 'environment.time'])

        tlast = d['environment.time'][-1]
        ical = d['L_type_Ca_current.i_CaL']
        ical_min = np.min(d['L_type_Ca_current.i_CaL'])

        # Step to 5 mV
        s.set_constant('membrane.V', 5.01)
        d = s.run(150, d).npview()

        ical = d['L_type_Ca_current.i_CaL']

        if model[0] == 'p':
            lab = 'Priebe & Beuckelmann 1998'
        else:
            lab = 'Inada et al. 2009'

        ax.plot(d['environment.time'], ical / -ical_min, label=lab)

        print('-----------')

ax3.plot(
    [0.16, 0.26, 0.26, 0.36, 0.36, 0.46],
    [0.1, 0.1, 0.4, 0.4, 0.21, 0.21],
    'k', transform=ax3.transAxes)

ax3.text(0, 0.12, '$-90$ mV', transform = ax3.transAxes)
ax3.text(0.17, 0.42, '$+60$ mV', transform = ax3.transAxes)
ax3.text(0.36, 0.23, '$+5$ mV', transform = ax3.transAxes)

ax2.plot(
    [0.55, 0.65, 0.65, 0.75, 0.75, 0.85],
    [0.1, 0.1, 0.3, 0.3, 0.21, 0.21],
    'k', transform=ax2.transAxes)

ax2.text(0.38, 0.12, '$-90$ mV', transform = ax2.transAxes)
ax2.text(0.56, 0.32, '$+10$ mV', transform = ax2.transAxes)
ax2.text(0.75, 0.23, '$+5$ mV', transform = ax2.transAxes)


# Step transition
ax2.axvline(tlast, ls = '--', color = 'grey')
ax3.axvline(tlast, ls = '--', color = 'grey')

ax2.set_xlabel('Time (ms)')

ax2.set_ylabel('Current (normalised)')

ax3.set_xlabel('Time (ms)')

ax3.set_ylabel('Current (normalised)')

ax1.tick_params(which = 'both', direction = 'in', bottom = True, top = True, \
    left = True, right = True)
ax1.minorticks_on()

ax2.tick_params(which = 'both', direction = 'in', bottom = True, top = True, \
    left = True, right = True)
ax2.minorticks_on()

ax3.tick_params(which = 'both', direction = 'in', bottom = True, top = True, \
    left = True, right = True)
ax3.minorticks_on()

# Plot IV curves from web lab
ax1.set_xlabel('Membrane potential (mV)')
ax1.set_ylabel('Peak Current (normalised)')
ax1.set_xlim(-45, 60)
ax1.set_ylim(-1.05, 0.15)
d = myokit.DataLog.load_csv('data/iv-priebe-inada.csv')
ax1.plot(d['vm'], d['priebe'], label='Priebe 1998')
ax1.plot(d['vm'], d['inada'], label='Inada 2009')
ax1.legend(frameon=False, loc= 'upper right')




# plt.tight_layout()
plt.savefig('figure17.eps')
plt.savefig('figure17.pdf')
plt.close()
