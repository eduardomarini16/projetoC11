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

# 3) Como a umidade do ar influencia o tamanho médio das áreas queimadas?

# média anual da área queimada e da umidade
annual_data_humidity = dataset.groupby('Year').agg({
    'Burned_Area_Ha': 'mean', 
    'Humidity_Percent': 'mean'
}).reset_index()

correlation_humidity = annual_data_humidity['Burned_Area_Ha'].corr(annual_data_humidity['Humidity_Percent'])
print(f'Correlação entre umidade e tamanho médio das áreas queimadas: {correlation_humidity:.2f}')

plt.scatter(annual_data_humidity['Humidity_Percent'], annual_data_humidity['Burned_Area_Ha'])
plt.xlabel('Umidade do Ar (%)')
plt.ylabel('Tamanho Médio das Áreas Queimadas (Ha)')
plt.title('Relação entre Umidade do Ar e Tamanho Médio das Áreas Queimadas')
plt.show()

# 4) Quais são as causas mais frequentes de incêndios em cada país?

cause_counts = dataset.groupby(['Country', 'Cause']).size().reset_index(name='Count')

most_frequent_cause = cause_counts.loc[cause_counts.groupby('Country')['Count'].idxmax()]
most_frequent_cause = most_frequent_cause.reset_index(drop=True)
print(most_frequent_cause)

# Dados para plotar
countries = most_frequent_cause['Country']
causes = most_frequent_cause['Cause']
counts = most_frequent_cause['Count']

# Plot
plt.figure(figsize=(10,6))
plt.barh(countries, counts, color='orange')
plt.xlabel('Número de Incêndios')
plt.ylabel('País')
plt.title('Causa mais frequente de incêndios por país')

# Adiciona os rótulos das causas na barra
for i, (count, cause) in enumerate(zip(counts, causes)):
    plt.text(count + 5, i, cause, va='center')

plt.gca().invert_yaxis()  # Inverte a ordem do eixo y para mostrar do maior para o menor
plt.show()

