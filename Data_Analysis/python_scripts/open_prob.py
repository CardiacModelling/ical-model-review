import json
import pandas as pd
import string
import matplotlib.pyplot as plt
import numpy as np

def creating_dictionary():
    """
    This function was initially used to format the dictionary with modle attributes
    """
    column_names = list(pd.read_csv('../AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/Open_prob_all.csv').columns)
    model_names = [column_names[i] for i in range(1, len(column_names), 2)]
    metadata = {}
    for name in model_names:
        metadata[name] = []
        metadata[name].append({
            'species': 'a',
            'cell': 'a',
            'gating': 'a',
            'localisation': 'a', 
            'time_publication': 'a'
        })

    with open('models_metadata.json', 'w') as outfile:
        json.dump(metadata, outfile, indent=4)

class open_prob():

    def __init__(self):
        with open('models_metadata.json') as json_file:
            self.metadata = json.load(json_file)
        
        self.model_names = list(self.metadata.keys())
        self.categories = ['species', 'cell', 'gating', 'localisation', 'time_publication']
        self.species_list = ['mammalian', 'guinea_pig', 'human', 'rat', 'mouse', 'rabbit', 'canine', 'ipsc-cm']
        self.cell_list = ['atrial', 'ventricle', 'san', 'purkinje', 'avn']
        self.gating_list = list(string.ascii_uppercase)[:15]
        #self.gating_list.remove('Q') #Removing Q because Hinch does not have a distinct open_prob
        
        self.data = pd.read_csv('../AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/Open_prob_all.csv')
        self.data = self.data.dropna()
        
    def check_metadata_sensible(self):
        """
        This function merely checks if the category and category attributes are sensible and what we expect 
        """       
        for model in self.model_names:
            # Check species
            if self.metadata[model][0][self.categories[0]] in self.species_list:
                pass
            else:
                raise ValueError("model = " + model + ", category = " + self.categories[0] + ", attribute = " + self.metadata[model][0][self.categories[0]])
            
            # Check cell
            if self.metadata[model][0][self.categories[1]] in self.cell_list:
                pass
            else:
                raise ValueError("model = " + model + ", category = " + self.categories[1] + ", attribute = " + self.metadata[model][0][self.categories[1]])

            # Check gating
            if self.metadata[model][0][self.categories[2]] in self.gating_list:
                pass
            else:
                raise ValueError("model = " + model + ", category = " + self.categories[2] + ", attribute = " + self.metadata[model][0][self.categories[2]])

            # Check localisation
            if  0 < int(self.metadata[model][0][self.categories[3]]) < 13:
                pass
            else:
                raise ValueError("model = " + model + ", category = " + self.categories[3] + ", attribute = " + self.metadata[model][0][self.categories[3]])

            # Check time of publication
            if 1974 < int(self.metadata[model][0][self.categories[4]]) < 2021:
                pass
            else:
                raise ValueError("model = " + model + ", category = " + self.categories[4] + ", attribute = " + self.metadata[model][0][self.categories[4]])        

    def create_category(self, category, category_attribute):
        """
        category: this needs to specify the category of interest e.g., cell, species, etc.
        category_attribute: this tells us the category type of interest e.g., atrial for cell or human for species 
        model_cateogry: Return a list of model names (according to their names in the .csv file open_prob_all)
        """
        model_category = []
        if category == 'time_publication':
            if category_attribute == 1: #for the years 1985 - 1990
                for model in self.model_names:
                    if int(self.metadata[model][0][category]) < 1991:
                        model_category.append(model)
                return model_category        

            elif category_attribute == 2: #for the years 1991 - 2000
                for model in self.model_names:
                    if 1990 < int(self.metadata[model][0][category]) < 2001:
                        model_category.append(model)
                return model_category

            elif category_attribute == 3: #for the years 2001 - 2011
                for model in self.model_names:
                    if 2000 < int(self.metadata[model][0][category]) < 2011:
                        model_category.append(model)
                return model_category

            elif category_attribute == 4: #for the years 2011 - 2020
                for model in self.model_names:
                    if 2010 < int(self.metadata[model][0][category]):
                        model_category.append(model)
                return model_category
        
        else:
            for model in self.model_names:
                if self.metadata[model][0][category] == category_attribute:
                    model_category.append(model)
            return model_category

    def calculate_nrmse(self, category = 0, category_attribute = 0):
        """
        category: this needs to specify the category of interest e.g., cell, species, etc.
        category_attribute: this tells us the category type of interest e.g., atrial for cell or human for species 
        nrmse: Return normalised root mean square error
        """
        if category == 0:
            model_list = self.model_names
        else:
            model_list = self.create_category(category, category_attribute)

        if len(model_list) == 0:
            raise ValueError('No model such that category is %s and attribute is %s' %(category, category_attribute))
        else:
            pass

        index = 0
        for model in model_list:
            if index == 0:
                sum_of_models = self.data[model]
                index += 1
            else:
                sum_of_models = sum_of_models + self.data[model]
            
        average = sum_of_models/len(model_list)
        
        index = 0
        for model in model_list:
            if index == 0:
                diff_of_models = (self.data[model] - average)**2
                index += 1
            else:
                
                diff_of_models += (self.data[model] - average)**2

        average_error = diff_of_models/len(model_list)
        nrmse = pow(average_error.mean(), 0.5)
        
        return nrmse

    def attributes_of_interest_nrmse(self):
        """
        This function calls the specific categories of interest for this paper to calculate nrmse
        """

        for species in self.species_list:
            nrmse = self.calculate_nrmse(self.categories[0], species)
            print('Species: ' + species + ", NRMSE = " + str(nrmse))

        for cell in self.cell_list:
            nrmse = self.calculate_nrmse(self.categories[1], cell)
            print('Cell: ' + cell + ", NRMSE = " + str(nrmse))

        for gating in self.gating_list:
            nrmse = self.calculate_nrmse(self.categories[2], gating)
            print('Gating: ' + gating + ", NRMSE = " + str(nrmse))

        for localisation in range(1, 13):
            nrmse = self.calculate_nrmse(self.categories[3], str(localisation))
            print('Localisation: ' + str(localisation) + ", NRMSE = " + str(nrmse))

        for publication_year_category in range(1, 5):
            nrmse = self.calculate_nrmse(self.categories[4], publication_year_category)
            print('Publication year category : ' + str(publication_year_category) + ", NRMSE = " + str(nrmse))

    def clustering_by_output(self):
            
        time = self.data.iloc[:,0]
        index1 = time[time == 5.0].index.to_numpy()
        index2 = time[time == 20.0].index.to_numpy() 
        
        output1 = []
        output2 = []
        index_cell = []
        index_species = []
        index_localisation = []
        for model in self.model_names:
            output1.append(self.data[model].loc[index1[0]: index1[0] + 5].mean())
            output2.append(self.data[model].loc[index2[0]: index2[0] + 5].mean())
            index_cell.append(self.cell_list.index(self.metadata[model][0]['cell']))
            index_species.append(self.species_list.index(self.metadata[model][0]['species']))
            index_localisation.append(int(self.metadata[model][0]['localisation']))
        
        norm_output1 = [(x - min(output1))/ (max(output1) - min(output1)) for x in output1]
        norm_output2 = [(x - min(output2))/ (max(output2) - min(output2)) for x in output2]
        
        def legend_without_duplicate_labels(ax):
            handles, labels = ax.get_legend_handles_labels()
            unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
            ax.legend(*zip(*unique))
        
        colormap_cell = plt.cm.Set1(np.linspace(0, 1, len(self.cell_list)))
        colormap_species = plt.cm.Set1(np.linspace(0, 1, len(self.species_list)))
        colormap_localisation = plt.cm.Set1(np.linspace(0, 1, 13))
        
        fig, ax1 = plt.subplots()
        plt.xlabel('Average probability at 5-5.5 ms')
        plt.ylabel('Average probability at 50-55.5 ms')
        fig, ax2 = plt.subplots()
        plt.xlabel('Average probability at 5-5.5 ms')
        plt.ylabel('Average probability at 50-55.5 ms')
        fig, ax3 = plt.subplots()
        plt.xlabel('Average probability at 5-5.5 ms')
        plt.ylabel('Average probability at 50-55.5 ms')
        for i in range(len(output1)):
            ax1.scatter(norm_output1[i], norm_output2[i], color = colormap_cell[index_cell[i]], label = self.cell_list[index_cell[i]])
            ax2.scatter(norm_output1[i], norm_output2[i], color = colormap_species[index_species[i]], label = self.species_list[index_species[i]])
            ax3.scatter(norm_output1[i], norm_output2[i], color = colormap_localisation[index_localisation[i]], label = index_localisation[i])

        legend_without_duplicate_labels(ax1)
        legend_without_duplicate_labels(ax2)
        legend_without_duplicate_labels(ax3)
        #plt.xlabel('Average probability at 5-5.5 ms')
        #plt.ylabel('Average probability at 50-55.5 ms')  
        ax1.title.set_text('Scatter Plots: Cell')
        ax2.title.set_text('Scatter Plots: Species')
        ax3.title.set_text('Scatter Plots: Localisation')  
        plt.show()   


open_prob = open_prob()
open_prob.attributes_of_interest_nrmse()
#nrmse = calculate_rmse('time_publication', 4)
#print(nrmse)