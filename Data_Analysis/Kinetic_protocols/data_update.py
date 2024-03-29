#This script contains classes to update the csv (both append and update data)
#It also has classes to calculate kinetic parameters

import pandas as pd
import numpy as np
import warnings
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import os

class update_csv():
    """
    Updates the existing .csv file as per the latest data
    filename_main : The path to the main file which containes the data for all models from the various protocols 
    filename_new : The path to the new file that contains simulation outputs from models
    """
    def __init__(self, filename_main, filename_new):
        self.existing_data = pd.read_csv(filename_main)
        self.new_data = pd.read_csv(filename_new)
        
    def append_to_csv(self):
        """
        Appends new data into the existing .csv file.
        """
        appended_data = pd.concat([self.existing_data, self.new_data], axis = 1)
        appended_data.to_csv(filename_main, index = False)
        warnings.warn("Add new graphs to .vsz files to show the new data")

    def update_model_output(self):
        """
        Updates existing data in the .csv file.
        """
        warnings.warn("Please ensure that the column names of the new file accurately corresponds to the relevant column names in the exisitng file")
        column_names_new = self.new_data.head()
        column_names_old = self.existing_data.head()
        for column_name in column_names_new:
            if column_name in column_names_old:
                self.existing_data[column_name] = self.new_data[column_name]
        
        self.existing_data.to_csv(filename_main, index = False) 

class calculate_kinetic_paramters():
    """
    Calculates the kinetic parameters required: half-volatge of activation and inactivation, time constant of recovery
    Input file should consist of multiple of 2 columns, wherein the each model has two columns (one for time/ voltage) and the other for normalized current.
    """
    def __init__(self, filename):
        
        data = pd.read_csv(filename)
        no_of_rows = len(data.index)
        no_of_columns = len(data.columns)

        for i in range(no_of_columns):
            if data.iloc[-1, i][0] == '#':
                data = data.drop([no_of_rows - 1])
                break
        
        # no of columns includes the voltage/ time columns as well
        screened_columns = [x for x in range(1, no_of_columns, 2)] 
        self.n_cols = len(screened_columns)
        self.screened_data = data.iloc[:,screened_columns]
        
        self.averaged_data = self.screened_data.median(axis = 1) 
        self.xaxis = data.iloc[:,0]

    def activation(self):
        """
        Ouputs the half-voltage activation parameter
        """
        def boltzmann(voltage, vhalf, k):
            voltage = list(map(lambda x: float(x), voltage))
            exponent = np.exp(-np.divide(np.subtract(voltage, vhalf), k))
            return (-1/ (exponent + 1))

        def find_v_half(current, voltage):
            """
            current: array of normalized IV curve
            voltage: array of the test potentials
            """
            for i in range(len(voltage)):
                if current.iloc[i] > -0.5:
                    continue
                elif current.iloc[i] == -0.5:
                    return voltage.iloc[i]
                else:
                    volt1 = float(voltage.iloc[i-1])
                    volt2 = float(voltage.iloc[i])
                    curr1 = float(current.iloc[i-1])
                    curr2 = float(current.iloc[i])
                    V_half = volt1 + (volt1 - volt2)*(-0.5 - curr1)/(curr1 - curr2)
                    return V_half

        v_half = []
        for i in range(self.n_cols):
            current = self.screened_data.iloc[:,i]
            #print(current)
            v_half.append(find_v_half(current, self.xaxis))
        print('Median: ', np.median(v_half))
        print('Min: ', np.min(v_half))
        print('Max: ', np.max(v_half))
        return 0
        # We only fit to the first half of the activation curve
        no_of_data_points = len(self.averaged_data)
        for i in range(no_of_data_points):
            if self.averaged_data[i+1] > self.averaged_data[i]:
                break
        
        self.averaged_data = self.averaged_data[0:i+1]
        self.xaxis = self.xaxis[0:i+1]

        
        initial_guess = [-10, 10]
        popt, pcov = curve_fit(boltzmann, self.xaxis, self.averaged_data, p0= initial_guess)
        plt.plot(self.xaxis, self.averaged_data, label = 'Average of all models')
        plt.plot(boltzmann(self.xaxis, *initial_guess), label = 'Initial Guess')
        plt.plot(self.xaxis, boltzmann(self.xaxis, *popt), label = 'Best Fit')
        plt.xlabel('Voltage (mV)')
        plt.ylabel('Normalized Current')
        plt.title('Steady State Activation')
        plt.legend()
        plt.savefig('activation_boltzmann_fit.png')
        return popt[0]
        
    def inactivation(self):
        """
        Ouputs the half-voltage inactivation parameter
        """

        def boltzmann(voltage, vhalf, k):

            voltage = list(map(lambda x: float(x), voltage))
            exponent = np.exp(np.divide(np.subtract(voltage, vhalf), k))
            return (1/ (exponent + 1))

        def find_v_half(current, voltage):
            """
            current: array of normalized IV curve
            voltage: array of the test potentials
            """
            for i in range(len(voltage)):
                if current.iloc[i] < 0.5:
                    continue
                elif current.iloc[i] == 0.5:
                    return voltage.iloc[i]
                else:
                    volt1 = float(voltage.iloc[i-1])
                    volt2 = float(voltage.iloc[i])
                    curr1 = float(current.iloc[i-1])
                    curr2 = float(current.iloc[i])
                    V_half = volt1 + (volt1 - volt2)*(0.5 - curr1)/(curr1 - curr2)
                    return V_half

        v_half = []
        for i in range(self.n_cols):
            current = self.screened_data.iloc[:,i]
            #print(current)
            v_half.append(find_v_half(current, self.xaxis))
        print('Median: ', np.median(v_half))
        print('Min: ', np.min(v_half))
        print('Max: ', np.max(v_half))
        return 0

        initial_guess = [-42, 7]
        popt, pcov = curve_fit(boltzmann, self.xaxis, self.averaged_data, p0= initial_guess)
        plt.plot(self.xaxis, self.averaged_data, label = 'Average of all models')
        plt.plot(boltzmann(self.xaxis, *initial_guess), label = 'Initial Guess')
        plt.plot(self.xaxis, boltzmann(self.xaxis, *popt), label = 'Best Fit')
        plt.xlabel('Voltage (mV)')
        plt.ylabel('Normalized Current')
        plt.title('Steady State Inactivation')
        plt.legend()
        plt.savefig('inactivation_boltzmann_fit.png')
        return popt[0]
        
    def recovery(self):
        """
        Ouputs the time constant of recovery from inactivation
        """

        def exponential(time, tau):

            time = list(map(lambda x: float(x), time))
            exponent = np.exp(-np.divide(time, tau))
            return (1 - exponent)
        
        
        initial_guess = [55]
                
        tau = []
        for i in range(self.n_cols):
            current = self.screened_data.iloc[:,i]
            popt = curve_fit(exponential, self.xaxis, current, p0 = initial_guess)
            tau.append(popt[0][0])

        print('Median: ', np.median(tau))
        print('Min: ', np.min(tau))
        print('Max: ', np.max(tau))
        return 0

        plt.plot(self.xaxis, self.averaged_data, label = 'Average of all models')
        plt.plot(exponential(self.xaxis, *initial_guess), label = 'Initial Guess')
        for i in range(len(popt)):
            plt.plot(self.xaxis, exponential(self.xaxis, *popt[i]), label = 'Best Fit: time = ' + str(*popt[i]) + ' (ms)')
        plt.xlabel('Time (ms)')
        plt.ylabel('Normalized Current')
        plt.title('Recovery from Inactivation')
        plt.legend()
        plt.savefig('recovery_exponential_fit.png')
        return popt


filename = 'data/recovery.csv'
y = calculate_kinetic_paramters(filename)
y.recovery()    

def calculate_rmsd():

    def rmsd(arr1, arr2):
        diff = arr1 - arr2
        for i in range(len(diff)): #Remove outlier e.g., hund at last P1
            if abs(diff.loc[i]) > 2:
                diff = diff.drop([i])
        return np.sqrt(diff.pow(2).sum()/len(arr1))

    path = '../calcium_sensitivity/CDI/data'
    files = os.listdir(path)

    insensenitive = []
    mild = []
    strong = []

    for file in files:
        data = pd.read_csv(path + '/' + file)
        no_of_rows = len(data.index)
        no_of_columns = len(data.columns)

        for i in range(no_of_columns):
            if data.iloc[-1, i][0] == '#':
                data = data.drop([no_of_rows - 1])
                break
        
        col1 = data.iloc[:,1]
        col2 = data.iloc[:,-1]
        rmsd_a = rmsd(col1, col2)
        #print(file[:-4], ': RMSD: ', rmsd_a)

        if rmsd_a < 0.1:
            insensenitive.append(file[:-4])
        elif rmsd_a > 0.50:
            strong.append(file[:-4])
        else:
            mild.append(file[:-4])

    print('Insensitive: ', len(insensenitive))
    print(insensenitive)
    print('Mild: ', len(mild))
    print(mild)
    print('Strong: ', len(strong))
    print(strong)

# calculate_rmsd()