from numpy import mean, median, std
from random import uniform
import matplotlib.pyplot as plt

alturas, pesos, imc, problema_cardiaco = [], [], [], []

for i in range(2000):
    altura_valor = uniform(1.60, 2.0)
    peso_valor = uniform(55, 100)
    alturas.append(altura_valor)
    pesos.append(peso_valor)

for alt, pe in zip(alturas, pesos):
    imc_valor = round(pe / alt ** 2, 2)
    imc.append(imc_valor)

for i in imc:
    if i > 30:
        problema_cardiaco.append('S')
    else:
        problema_cardiaco.append('N')

total_cardiaco, total_saudavel = [], []
for i in range(2000):
    if problema_cardiaco[i] == 'S':
        total_cardiaco.append(imc[i])
    else:
        total_saudavel.append(imc[i])

media_saudavel = mean(total_saudavel)
media_cardiaco = mean(total_cardiaco)
mediana_saudavel = median(total_saudavel)
mediana_cardiaco = median(total_cardiaco)
desvio_padrao_saudavel = std(total_saudavel)
desvio_padrao_cardiaco = std(total_cardiaco)

# plt.hist(imc, bins=25, edgecolor='black')
# plt.axvline(18.5, color='green', linestyle='--', label=f'Abaixo do peso')
# plt.axvline(25, color='yellow', linestyle='--', label=f'Peso normal')
# plt.axvline(30, color='red', linestyle='--', label=f'Sobrepeso')
# plt.xlabel('IMC')
# plt.ylabel('Frequência')
# plt.savefig('hist_imc.png')
# plt.show()
plt.boxplot((total_cardiaco, total_saudavel), tick_labels=['Cárdiaco', 'Saudável'])
plt.ylabel('IMC')
plt.xlabel('Grupo')
plt.title('Comparação do IMC entre grupos')
plt.show()
