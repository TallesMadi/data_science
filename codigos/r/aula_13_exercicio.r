ordenar_filtrar <- function(numeros) {
    # TODO: Ordenar o vetor 'numeros' de forma crescente
    numeros_ordenados <- sort(numeros)

    # TODO: Filtrar apenas os números maiores que 50
    numeros_filtrados <- c()
    for (i in numeros_ordenados) {
        if (i > 50) {
            numeros_filtrados <- c(numeros_filtrados, i)
        }   
    }

    return(list(ordenado = numeros_ordenados, filtrado = numeros_filtrados))
}

vetor = c(100, 15, 70, 30, 50, 20, 90, 130, 120, 80, 10, 4, 11, 14, 60)
print(ordenar_filtrar(vetor))