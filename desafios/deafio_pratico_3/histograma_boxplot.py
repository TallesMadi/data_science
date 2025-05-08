import matplotlib.pyplot as plt
from pandas import read_csv

DATAFRAME = read_csv(r"C:\\data_science\\desafios\\deafio_pratico_3\\desafio_pratico_3.csv") 

plt.hist(DATAFRAME["Preco_R$"], bins=7, edgecolor='black')
plt.title('Distribuição de Preços')
plt.xlabel('Preços')
plt.ylabel('Frequência')
plt.grid(True)
plt.savefig(r'C:\\data_science\\desafios\\deafio_pratico_3\\histograma.png')
plt.show()

plt.boxplot(DATAFRAME['Preco_R$'], vert=True, patch_artist=True)
plt.title('Distribuição de Preços')
plt.ylabel('Valores')
plt.grid(True)
plt.savefig(r'C:\\data_science\\desafios\\deafio_pratico_3\\boxplot.png')
plt.show()