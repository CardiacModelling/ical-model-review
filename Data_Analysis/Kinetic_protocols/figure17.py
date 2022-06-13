#Load libraries
import myokit
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import (MultipleLocator)

def plot_ical_open():
    models = ['priebe-1998.mmt', 'nygren-1998.mmt']

    fig = plt.figure(figsize = (8, 6))
    ax1 = fig.add_subplot(221)
    ax2 = fig.add_subplot(222)
    ax3 = fig.add_subplot(223)
    ax4 = fig.add_subplot(224)

    ax_ical = [ax1, ax2]
    ax_op = [ax3, ax4]
    
    pro_step1 = [10.01, 55.01]
    for j in range(len(pro_step1)):
        for model in models:

            print(model)
            m = myokit.load_model(model)

            v = m.get('membrane.V')
            v.set_binding(None)
            s = myokit.Simulation(m)
            
            # Stabilise the model a steady state by running for 10 seconds
            s.set_constant('membrane.V', - 90.01)
            s.run(10000, log = [])

            # Step to 55 mV
            s.set_constant('membrane.V', pro_step1[j])
            d = s.run(150, log = ['L_type_Ca_current.i_CaL', 'environment.time', \
                'L_type_Ca_current.open'])

            tlast = d['environment.time'][-1]
            
            # Step to 5 mV
            s.set_constant('membrane.V', 5.01)
            d = s.run(150, d)

            ical = d['L_type_Ca_current.i_CaL']
            ical_min = min(d['L_type_Ca_current.i_CaL'])

            op = d['L_type_Ca_current.open']
            op_max = max(d['L_type_Ca_current.open'])

            ax_ical[j].plot(d['environment.time'], -1*np.divide(ical, ical_min), \
                label = f'{model[:-4]}')
            ax_op[j].plot(d['environment.time'], np.divide(op, op_max), \
                label = f'{model[:-4]}')

            print('-----------')

    ax1.axvline(tlast, ls = '--', color = 'grey')
    ax2.axvline(tlast, ls = '--', color = 'grey')
    ax3.axvline(tlast, ls = '--', color = 'grey')
    ax4.axvline(tlast, ls = '--', color = 'grey')

    ax3.set_xlabel('Time (ms)')
    ax4.set_xlabel('Time (ms)')

    ax1.set_ylabel('Current\n(normalised)')
    ax3.set_ylabel('Open probability\n(normalised)')

    ax1.set_title(f'{pro_step1[0]} mV to 5 mV')
    ax2.set_title(f'{pro_step1[1]} mV to 5 mV')
        
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()

    plt.tight_layout()
    plt.show()
    
def plot_ical():
    models = ['priebe-1998.mmt', 'aslanidi-2009.mmt']

    # Set font
    matplotlib.rc('font', family='arial', size = 8)

    fig = plt.figure(figsize = (6.8, 3.4))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)

    ax = [ax1, ax2]
    
    pro_step1 = [10.01, 60.01]
    for j in range(len(pro_step1)):
        for model in models:

            print(model)
            m = myokit.load_model(model)

            v = m.get('membrane.V')
            v.set_binding(None)
            s = myokit.Simulation(m)
            
            # Stabilise the model a steady state by running for 10 seconds
            s.set_constant('membrane.V', - 90.01)
            s.run(10000, log = [])

            # Step to 60 mV
            s.set_constant('membrane.V', pro_step1[j])
            d = s.run(150, log = ['L_type_Ca_current.i_CaL', 'environment.time'])

            tlast = d['environment.time'][-1]
            ical = d['L_type_Ca_current.i_CaL']
            ical_min = min(d['L_type_Ca_current.i_CaL'])
            
            # Step to 5 mV
            s.set_constant('membrane.V', 5.01)
            d = s.run(150, d)

            ical = d['L_type_Ca_current.i_CaL']
            
            if model[0] == 'p':
                lab = 'Priebe 1998'
            else:
                lab = 'Aslanidi 2009b'

            ax[j].plot(d['environment.time'], -1*np.divide(ical, ical_min), \
                label = lab)

            print('-----------')

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

    ax2.axhline(-2.3, xmin = 0.35, xmax = 0.4, color = 'black', ls = '-')
    ax2.axvline(10117, ymin = 0.045, ymax = 0.250, color = 'black', ls = '-')
    ax2.axhline(-1.78, xmin = 0.4, xmax = 0.5, color = 'black', ls = '-')
    ax2.axvline(10150, ymin = 0.150, ymax = 0.250, color = 'black', ls = '-')
    ax2.axhline(-2.0, xmin = 0.5, xmax = 0.6, color = 'black', ls = '-')
    ax2.axvline(10183, ymin = 0.162, ymax = 0.045, color = 'black', ls = '-')
    ax2.axhline(-2.3, xmin = 0.6, xmax = 0.65, color = 'black', ls = '-')

    ax2.text(0.38, 0.259, '60 mV', transform = ax2.transAxes)
    ax2.text(0.51, 0.17, '5 mV', transform = ax2.transAxes)
    ax2.text(0.61, 0.052, '- 90 mV', transform = ax2.transAxes)

    ax1.axvline(tlast, ls = '--', color = 'grey')
    ax2.axvline(tlast, ls = '--', color = 'grey')

    ax1.set_xlabel('Time (ms)')
    ax2.set_xlabel('Time (ms)')

    ax1.set_ylabel('Current (normalized)')
       
    ax1.legend(frameon=False)
    ax2.legend(frameon=False)

    ax1.xaxis.set_minor_locator(MultipleLocator(10))
    ax1.yaxis.set_minor_locator(MultipleLocator(0.05))

    ax2.xaxis.set_minor_locator(MultipleLocator(10))
    ax2.yaxis.set_minor_locator(MultipleLocator(0.1))

    plt.tight_layout()
    plt.savefig('figure17.eps')
    plt.savefig('figure17.pdf')
    plt.close()

plot_ical()




        