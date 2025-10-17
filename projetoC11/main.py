import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Forest_Fires_Dataset__1881-2025_.csv', sep=',')

# print(dataset)

# 2) Há relação entre o aumento da temperatura média e o número de incêndios por ano?

#média da temperatura e o toal de incêndios por ano
annual_data = dataset.groupby('Year').agg({
    'Temperature_C': 'mean',
    'Fires_Count': 'sum'
}).reset_index()

# correlação entre temperatura média e número de incêndios
correlation = annual_data['Temperature_C'].corr(annual_data['Fires_Count'])
print(f'Correlação entre temperatura média e número de incêndios: {correlation:.2f}')

plt.scatter(annual_data['Temperature_C'], annual_data['Fires_Count'])
plt.xlabel('Temperatura Média (°C)')
plt.ylabel('Número de Incêndios')
plt.title('Relação entre Temperatura Média e Número de Incêndios')
plt.show()