import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#beolvasas
df = pd.read_csv("nehezfem_kibocsatas.csv", sep=";", encoding="ANSI", skipinitialspace=True, skiprows=[0])
#vesszok kicserelese pontokra
df.replace(',', '.', regex=True, inplace=True)
#float64-re alakitas
df['Év'] = df['Év'].astype('float64')
df['Arzén'] = df['Arzén'].astype('float64')

print(df.head())
print(df.dtypes)
df = df.iloc[2:]

df["Arzén"].plot(kind='hist', color='#8533ff')
plt.show()
