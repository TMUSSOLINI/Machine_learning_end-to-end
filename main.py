import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import warnings

# Configurações
warnings.filterwarnings('ignore')
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_columns', 100)
plt.rcParams['figure.figsize'] = (15, 6)
plt.style.use('seaborn-darkgrid')

base_dados = pd.read_csv('house_data.csv')

# Excluindo colunas
base_dados.drop(columns=['total (R$)', 'fire insurance (R$)'], inplace=True)

#Tipos das colunas
Colunas_Categoricas = base_dados.columns[base_dados.dtypes == object]
Colunas_Numericas = base_dados.columns[base_dados.dtypes != object]
print(Colunas_Numericas, Colunas_Categoricas)
