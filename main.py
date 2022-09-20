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

#Coluna categorica
print(base_dados['city'].value_counts(normalize=True) * 100)
for coluna in Colunas_Categoricas:
    Analise = base_dados[coluna].value_counts(normalize=True) * 100
    print(coluna, '\n', Analise, '\n')

# Ajustando os dados
base_dados.iloc[2562,5] = 30
base_dados['floor'] = base_dados['floor'].apply(lambda Registro: 0 if Registro == '-' else Registro)
base_dados['floor'] = pd.to_numeric(base_dados['floor'])

