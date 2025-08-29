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
#-----------------------Data Treatment------------------------#
###############################################################
for col in df.columns:
    print(f"Coluna: {col}")
    print(df[col].unique())
    print("-" * 30)

df.duplicated().sum() # numero de entradas duplicadas

df.isna().sum() # numero de entradas vazias por coluna
df.isna().sum().sum() # numero de entradas vazias total

df.describe() # estatisticas descritivas

###############################################################
#-------------------Data Visualization------------------------#
###############################################################
import seaborn as sns
import matplotlib.pyplot as plt

# boxplot para visualizar outliers
sns.boxplot(x=df['coluna_numerica'])

# quartis
Q1 = df['coluna_numerica'].quantile(.25)
Q3 = df['coluna_numerica'].quantile(.75)
IQR = Q3-Q1
limite_inferior = Q1 - 1.5*IQR
limite_superior = Q3 + 1.5*IQR

outliers_index = (df['coluna_numerica'] < limite_inferior) | (df['coluna_numerica'] > limite_superior)
df[outliers_index]['coluna_numerica']
df_sem_outliers = df[~outliers_index]

# Visualizando a distribuição das variáveis numéricas
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.histplot(df['coluna_numerica'], bins=30, kde=True)
plt.title('Distribuição da Coluna Numérica')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()

# Visualizando a relação entre duas variáveis
plt.figure(figsize=(12, 6))
sns.scatterplot(x='coluna_x', y='coluna_y', data=df)
plt.title('Relação entre Coluna X e Coluna Y')
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.show()

