dados <- read.csv("C:\\data_science\\codigos\\r\\dataframe\\atlas2010.csv", header = TRUE, sep = ",")
ordenado_crescente = dados[order(dados$mort1), ]
ordenado_decrescente = dados[order(dados$mort1, decreasing=TRUE), ]
menor = min(dados$mort1)
maior = max(dados$mort1)
print(menor)
print(maior)
atlas_agregado = aggregate(mort1 ~ uf, data=dados, FUN=mean)
print(atlas_agregado)
atlas_crescente = atlas_agregado[order(atlas_agregado$mort1), ]
print(atlas_crescente)
# print(aggregate(cbind(mort1, mort5) ~ uf, data=dados, FUN=mean))
print(mean(dados$mort1))
print(median(dados$mort1))
print(var(dados$mort1))
print(sd(dados$mort1))
print((sd(dados$mort1) / mean(dados$mort1)) * 100)
print((sd(dados$mort5) / mean(dados$mort5)) * 100)
print(summary(dados$mort1))

k = 2*(nrow(dados) ^ (1/3))
print(k)

library(fdth)

tabela = fdt(dados$mort1, k=36)
# plot(tabela)

h = tabela$breaks[3]

h_valor = as.numeric(sub("h: ", "", h))
print(h_valor)

hist(dados$mort1, breaks=36)