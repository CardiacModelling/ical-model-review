import json
import pandas as pd
import string


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

def check_metadata_sensible():
    """
    This function merely checks if the category and category attributes are sensible and what we expect 
    """
    with open('models_metadata.json') as json_file:
        metadata = json.load(json_file)

    model_names = list(metadata.keys())
    categories = ['species', 'cell', 'gating', 'localisation', 'time_publication']
    species_list = ['mammalian', 'guinea_pig', 'human', 'rat', 'mouse', 'rabbit', 'canine', 'ipsc-cm']
    cell_list = ['atrial', 'ventricle', 'san', 'purkinje', 'avn']
    gating_list = list(string.ascii_uppercase)[:21]
    
    for model in model_names:
        # Check species
        if metadata[model][0][categories[0]] in species_list:
            pass
        else:
            raise ValueError("model = " + model + ", category = " + categories[0] + ", attribute = " + metadata[model][0][categories[0]])
        
        # Check cell
        if metadata[model][0][categories[1]] in cell_list:
            pass
        else:
            raise ValueError("model = " + model + ", category = " + categories[1] + ", attribute = " + metadata[model][0][categories[1]])

        # Check gating
        if metadata[model][0][categories[2]] in gating_list:
            pass
        else:
            raise ValueError("model = " + model + ", category = " + categories[2] + ", attribute = " + metadata[model][0][categories[2]])

        # Check localisation
        if  0 < int(metadata[model][0][categories[3]]) < 13:
            pass
        else:
            raise ValueError("model = " + model + ", category = " + categories[3] + ", attribute = " + metadata[model][0][categories[3]])

        # Check time of publication
        if 1974 < int(metadata[model][0][categories[4]]) < 2021:
            pass
        else:
            raise ValueError("model = " + model + ", category = " + categories[4] + ", attribute = " + metadata[model][0][categories[4]])        

def create_category(category, category_attribute):
    """
    category: this needs to specify the category of interest e.g., cell, species, etc.
    category_attribute: this tells us the category type of interest e.g., atrial for cell or human for species 
    model_cateogry: Return a list of model names (according to their names in the .csv file open_prob_all)
    """
    with open('models_metadata.json') as json_file:
        metadata = json.load(json_file)

    model_names = list(metadata.keys())

    model_category = []
    if category == 'time_publication':
        if category_attribute == 1: #for the years 1985 - 1990
            for model in model_names:
                if int(metadata[model][0][category]) < 1991:
                    model_category.append(model)
            return model_category        

        elif category_attribute == 2: #for the years 1991 - 2000
            for model in model_names:
                if 1990 < int(metadata[model][0][category]) < 2001:
                    model_category.append(model)
            return model_category

        elif category_attribute == 3: #for the years 2001 - 2011
            for model in model_names:
                if 2000 < int(metadata[model][0][category]) < 2011:
                    model_category.append(model)
            return model_category

        elif category_attribute == 4: #for the years 2011 - 2020
            for model in model_names:
                if 2010 < int(metadata[model][0][category]):
                    model_category.append(model)
            return model_category
    
    else:
        for model in model_names:
            if metadata[model][0][category] == category_attribute:
                model_category.append(model)
        return model_category

def calculate_nrmse(category, category_attribute):
    """
    category: this needs to specify the category of interest e.g., cell, species, etc.
    category_attribute: this tells us the category type of interest e.g., atrial for cell or human for species 
    nrmse: Return normalised root mean square error
    """
    model_list = create_category(category, category_attribute)

    if len(model_list) == 0:
        raise ValueError('No model such that category is %s and attribute is %s' %(category, category_attribute))
    else:
        pass
    data = pd.read_csv('../AP_CaT_Clamp/Open_Prob_AP_CaT_Clamp/Open_prob_all.csv')
    data = data.dropna()
    
    index = 0
    for model in model_list:
        if index == 0:
            sum_of_models = data[model]
            index += 1
        else:
            sum_of_models = sum_of_models + data[model]
        
    average = sum_of_models/len(model_list)
    
    index = 0
    for model in model_list:
        if index == 0:
            diff_of_models = (data[model] - average)**2
            index += 1
        else:
            
            diff_of_models += (data[model] - average)**2

    average_error = diff_of_models/len(model_list)
    nrmse = pow(average_error.mean(), 0.5)
    
    return nrmse

def attributes_of_interest_nrmse():
    """
    This function calls the specific categories of interest for this paper to calculate nrmse
    """
    categories = ['species', 'cell', 'gating', 'localisation', 'time_publication']
    species_list = ['mammalian', 'guinea_pig', 'human', 'rat', 'mouse', 'rabbit', 'canine', 'ipsc-cm']
    cell_list = ['atrial', 'ventricle', 'san', 'purkinje', 'avn']
    gating_list = list(string.ascii_uppercase)[:21] 
    gating_list.remove('Q') #Removing Q because Hinch does not have a distinct open_prob

    for species in species_list:
        nrmse = calculate_nrmse(categories[0], species)
        print('Species: ' + species + ", NRMSE = " + str(nrmse))

    for cell in cell_list:
        nrmse = calculate_nrmse(categories[1], cell)
        print('Cell: ' + cell + ", NRMSE = " + str(nrmse))

    for gating in gating_list:
        nrmse = calculate_nrmse(categories[2], gating)
        print('Gating: ' + gating + ", NRMSE = " + str(nrmse))

    for localisation in range(1, 13):
        nrmse = calculate_nrmse(categories[3], str(localisation))
        print('Localisation: ' + str(localisation) + ", NRMSE = " + str(nrmse))

    for publication_year_category in range(1, 5):
        nrmse = calculate_nrmse(categories[4], publication_year_category)
        print('Publication year category : ' + str(publication_year_category) + ", NRMSE = " + str(nrmse))

attributes_of_interest_nrmse()
#nrmse = calculate_rmse('time_publication', 4)
#print(nrmse)