#This script contains classes to update the csv (both append and update data)
#It also has classes to calculate kinetic parameters

import pandas as pd
import numpy as np
import warnings
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

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
        
        screened_columns = [x for x in range(1, no_of_columns-1, 2)] #Last column is median
        screened_data = data.iloc[:,screened_columns]
        
        self.averaged_data = screened_data.median(axis = 1) # no of columns includes the voltage/ time columns as well
        self.xaxis = data.iloc[:,0]

    def activation(self):
        """
        Ouputs the half-voltage activation parameter
        """

        def boltzmann(voltage, vhalf, k):

            voltage = list(map(lambda x: float(x), voltage))
            exponent = np.exp(-np.divide(np.subtract(voltage, vhalf), k))
            return (-1/ (exponent + 1))
        
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
        popt = curve_fit(exponential, self.xaxis, self.averaged_data, p0 = initial_guess)
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


filename = 'Kinetic_protocols/data/recovery.csv'
y = calculate_kinetic_paramters(filename)
answer = y.recovery()
print(answer)    
