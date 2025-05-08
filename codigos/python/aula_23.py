from sympy import * # type: ignore
import numpy as np
from random import uniform
import pandas as pd

alturas = np.random.normal(1.75, 0.3, 2000)
alturas = alturas.tolist()

x1 = symbols('alt_i')
x2 = symbols('aleatorio_i')

peso_i = x1*50 + x2 
peso=[]
imc = []
sexo = []
cardiaco = []

for i in alturas:
    a = float(uniform(-5, 5))
    b = 50*i
    c = a + b
    peso.append(c)

for i, j in zip(alturas, peso):
    resultado = round(j / (i ** 2), 2)
    imc.append(resultado)

for i in range(2000):
    value = uniform(0, 1)
    if value > 50:
        sexo.append('F')
    else:
        sexo.append('M')

    if imc[i] > 40:
        cardiaco.append('S')
    else:
        if 30 > imc[i] < 40:
            cardiaco.append('P')
        else:
            cardiaco.append('N') 

lista_de_dados = alturas, peso, imc, sexo, cardiaco
df = pd.DataFrame(lista_de_dados, index=['Altura', 'Peso', 'IMC', 'Sexo', 'Cardiaco']).T
print(df)