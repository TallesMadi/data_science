dados <- read.csv("C:\\data_science\\codigos\\r\\dataframe\\atlas2010.csv", header = TRUE, sep = ",")

uf_freq = sort(table(dados$uf), decreasing=FALSE)
# print(uf_freq)

# barras
par(mar=c(5, 8, 4, 1))
barplot(
    uf_freq, 
    main="UF por número de cidades em 2010",
    xlab="Frequência",
    horiz=TRUE,
    las=1,
    col="lightblue",
    border="black",
    cex.names=0.7,
    ylab="UF"
)
grid(nx=10, ny=NULL, lty="dotted")

# dispersão
plot(
    dados$mort1, 
    dados$mort5, 
    main="Dispersão entre mortalidade entre um ano e cinco anos",
    xlab="Mortalidade 1",
    ylab="Mortalidade 5"
)

# boxplot
boxplot(
    dados$mort1, 
    dados$mort5, 
    names=c("Mort1", "Mort5"),
    main="Boxplot entre mort1 e mort5",
    ylab="Valor",
    col=c("lightblue", "lightgreen")
)
