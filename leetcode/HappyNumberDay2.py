print('Hello')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('happiness2017.csv')
#print(df['Happiness'])

#print(df[['Happiness']])

dfnp = np.array(df)
print(dfnp)

print(df['Happiness'].mean())

df = df.drop(columns='Country')
df.boxplot(figsize=(5,6), fontsize=14)

