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
fig.subplots_adjust(0.085, 0.14, 0.99, 0.99, wspace=0.25)
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

axes = [ax2]
pro_step1 = [60.01]

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

'''
# Voltage protocol
ax1.axhline(-1, xmin = 0.35, xmax = 0.4, color = 'black', ls = '-')
ax1.axvline(10117, ymin = 0.045, ymax = 0.225, color = 'black', ls = '-')
ax1.axhline(-0.8, xmin = 0.4, xmax = 0.5, color = 'black', ls = '-')
ax1.axvline(10150, ymin = 0.180, ymax = 0.225, color = 'black', ls = '-')
ax1.axhline(-0.85, xmin = 0.5, xmax = 0.6, color = 'black', ls = '-')
ax1.axvline(10183, ymin = 0.180, ymax = 0.045, color = 'black', ls = '-')
ax1.axhline(-1, xmin = 0.6, xmax = 0.65, color = 'black', ls = '-')
ax1.text(0.38, 0.234, '10 mV', transform = ax1.transAxes)
ax1.text(0.51, 0.19, '5 mV', transform = ax1.transAxes)
ax1.text(0.61, 0.052, '- 90 mV', transform = ax1.transAxes)

ax2.axhline(-2.3, xmin=0.35, xmax=0.4, color = 'black', ls = '-')
ax2.axvline(117, ymin=0.045, ymax=0.250, color = 'black', ls = '-')
ax2.axhline(-1.78, xmin=0.4, xmax=0.5, color = 'black', ls = '-')
ax2.axvline(150, ymin=0.150, ymax=0.250, color = 'black', ls = '-')
ax2.axhline(-2.0, xmin=0.5, xmax=0.6, color = 'black', ls = '-')
ax2.axvline(183, ymin=0.162, ymax=0.045, color = 'black', ls = '-')
ax2.axhline(-2.3, xmin=0.6, xmax=0.65, color = 'black', ls = '-')

'''

ax2.plot(
    [0.1, 0.2, 0.2, 0.3, 0.3, 0.4],
    [0.1, 0.1, 0.4, 0.4, 0.21, 0.21],
    'k', transform=ax2.transAxes)

ax2.text(-7, -1.95, '$-90$ mV')
ax2.text(50, -1.25, '$+60$ mV')
ax2.text(90, -1.7, '$+5$ mV')


# Step transition
ax2.axvline(tlast, ls = '--', color = 'grey')

ax2.set_xlabel('Time (ms)')

ax2.set_ylabel('Current (normalised)')

#ax2.legend(frameon=False)

ax2.xaxis.set_minor_locator(MultipleLocator(10))
ax2.yaxis.set_minor_locator(MultipleLocator(0.1))

# Plot IV curves from web lab
ax1.set_xlabel('Membrane potential (mV)')
ax1.set_ylabel('Peak Current (normalised')
ax1.set_ylim(-1.05, 0.15)
d = myokit.DataLog.load_csv('data/iv-priebe-inada.csv')
ax1.plot(d['vm'], d['priebe'], label='Priebe & Beuckelmann 1998')
ax1.plot(d['vm'], d['inada'], label='Inada et al. 2009')
ax1.legend(frameon=False, loc=(0.25, 0.81))




#plt.tight_layout()
plt.savefig('figure17.eps')
plt.savefig('figure17.pdf')
plt.close()
