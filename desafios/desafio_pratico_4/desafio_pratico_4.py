from pandas import read_csv
import matplotlib.pyplot as plt
CSV = read_csv(r'C:\data_science\desafios\desafio_pratico_4\desafio_pratico_4.csv')

soma_pib_idh_baixo = 0
soma_pib_idh_alto = 0
for i, j in enumerate(CSV['IDH']):
    j = j.replace(",", ".")
    if float(j) < 0.75: 
        pib_tratado = CSV['PIB_per_capita'][i].replace('R$ ', '').rstrip('00').replace('.', '').replace(',', '')
        float_pib_tratado = float(pib_tratado)
        soma_pib_idh_baixo += float_pib_tratado
    else:
        pib_tratado = CSV['PIB_per_capita'][i].replace('R$ ', '').rstrip('00').replace('.', '').replace(',', '')
        float_pib_tratado = float(pib_tratado)
        soma_pib_idh_alto += float_pib_tratado

media_pib_idh_baixo = soma_pib_idh_baixo / len(CSV['PIB_per_capita'])
media_pib_idh_alto = soma_pib_idh_alto / len(CSV['PIB_per_capita'])

print(f'R${media_pib_idh_baixo:.2f}')
print(f'R${media_pib_idh_alto:.2f}')

plt.scatter( CSV['Gini'], CSV['PIB_per_capita'], color='blue')
plt.ylabel('PIB per capita')
plt.xlabel('Gini')
plt.title('Gini x PIB')
plt.show()
# plt.savefig('gini_pib.png')
