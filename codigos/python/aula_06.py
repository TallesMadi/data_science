import matplotlib.pyplot as plt
import numpy as np

# Estilo do gráfico
plt.style.use('ggplot')

# Define os valores possíveis (como os lados de um dado)
np.random.seed(1678)
options = np.array([1, 2, 3, 4, 5, 6])

# Gera 1000 valores aleatórios entre 1 e 6
n = 1000
values = np.random.choice(options, size=n)

# Cria dois dicionários:
# - 'contadores' para contar quantas vezes cada número apareceu
# - 'frequencias' para armazenar a frequência relativa ao longo do tempo
contadores = {i: 0 for i in options}
frequencias = {i: [] for i in options}

# Percorre todos os valores gerados
for idx, val in enumerate(values, start=1):
    # Incrementa o contador do número sorteado
    contadores[val] += 1
    
    # Para cada número possível (1 a 6), calcula a frequência relativa:
    # frequência relativa = (quantas vezes apareceu) / (número de observações até agora)
    for num in options:
        frequencias[num].append(contadores[num] / idx)

# Plota as curvas de frequência relativa para cada número
for num in options:
    plt.plot(frequencias[num], label=f'Resultado: {num}')

# Configurações do gráfico
plt.legend(bbox_to_anchor=(1.2, 1), loc='upper center')  # Coloca a legenda fora do gráfico
plt.xlabel('Linha do tempo de observações')
plt.ylabel('Frequência relativa')
plt.title('Evolução das frequências relativas por resultado')
plt.tight_layout()
plt.show()
