estatisticas_vetor = function(x) {
    media = mean(x)
    mediana = median(x)
    maior = max(x)
    menor = min(x)
    lista = list(media, mediana, maior, menor)
    result <- lista
}

vetor = c(10, 7, 15, 2, 1, 90, 65)
resultado = estatisticas_vetor(vetor)
print(resultado)