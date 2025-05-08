# dataframes
df = data.frame(
    nome = c('Talles', 'Raquel'),
    idade = c(21, 22),
    profissao = c('ti', 'psicóloga')
)
print(df)
print(df$idade)

df$salario = c(50000, 50000)
print(df)
print(mean(df$idade, na.rm = TRUE))

graph = plot(df$idade)
graph_2 = plot(df$idade, df$salario)
# print(graph)
print(graph_2)

dados <- read.csv("C:\\data_science\\codigos\\r\\dataframe\\atlas2010.csv", header = TRUE, sep = ",")
print(dados)
