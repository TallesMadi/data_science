from pandas import read_csv
from numpy import mean, median, std, round
from scipy import stats
DATAFRAME = read_csv(r"C:\\data_science\\desafios\\deafio_pratico_3\\desafio_pratico_3.csv") 
dataframe_preco = DATAFRAME["Preco_R$"]

def csv_statics(dataframe_value):
    media = mean(dataframe_value)
    mediana = median(dataframe_value)
    moda = stats.mode(dataframe_value, keepdims=True)
    desvio_padrao = std(dataframe_value)
    coefciente_de_variacao = (desvio_padrao / media) * 100
    dictionary = {
        "media": float(media), 
        "mediana": float(mediana), 
        "moda": float(moda.mode[0]), 
        "desvio padrao": float(round(desvio_padrao, 2)), 
        "coeficiente de variacao": float(round(coefciente_de_variacao, 2))
    }
    return dictionary

print(csv_statics(dataframe_preco))

mediana_quantidade = median(DATAFRAME['Quantidade_Vendida'])
i = 0
for index, quantidade in enumerate(DATAFRAME['Quantidade_Vendida']):
    preco_item = DATAFRAME["Preco_R$"][index]
    faturamento = quantidade * preco_item
    if quantidade > mediana_quantidade and preco_item > 200 and faturamento > 6000:
        i += 1

print(f'{i} produtos atenderam ao critério, sendo {(i / len(dataframe_preco)) * 100}% do total de 50 itens')


