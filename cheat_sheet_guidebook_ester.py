'''
###############################################################
------------Guidebook: Cheat Sheet Guidebook-------------------
###############################################################
###############################################################
'''

###############################################################
#-----------------------Import Modules-------------------------#
###############################################################
import json
import pandas as pd

###############################################################
#-----------------------JSON Functions------------------------#
###############################################################
import json
import pandas as pd

def read_json(file_path):
    '''
    Reads a JSON file and returns its content as a Python dictionary.

    Parameters:
    file_path (str): The path to the JSON file.

    Returns:
    dict: The content of the JSON file.
    '''
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(data, file_path):
    '''
    Writes a Python dictionary to a JSON file.

    Parameters:
    data (dict): The data to write to the JSON file.
    file_path (str): The path to the JSON file.
    '''
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


df_normalizada = pd.json_normalize(df)

###############################################################
#-----------------Sneak peak on type of data------------------#
###############################################################
for col in df.columns:
    print(f"Coluna: {col}")
    print(df[col].unique())
    print("-" * 30)

