########## BIBLIOTECA DPLYR ###############
#rodar a biblioteca
library(dplyr)

#criando uma tabela com valores
tb <- tibble(
    x = 1:4,
    y = c(4, 7, 1, 3),
    z = c(10, 22, 10, 22),
    k = c(TRUE, FALSE, FALSE, TRUE),
    u = c("A", "B", "A", "B")
)

#pedindo pela ordenação dos valores de forma ascendente
tb %>% arrange(z,y)
arrange(tb, z,y)

#pedindo pela ordenação dos valores de forma descendente
tb %>% arrange(desc(z), desc(y))


#selecionar parte do conjunto de dados
tb %>% filter(x>2 | u=="A")

#fatiar linhas
tb %>% slice(1:3)

#selecionar variáveis específicas
tb %>% select(x, y)
#exclusão
tb %>% select(-z)
#intervalo
tb %>% select(y:k)
#por condição
tb %>% select_if(is.numeric)

#transformação de variáveis
tb %>% mutate(x = x * 2, u = factor(u))

#criar variáveis
tb %>% mutate(v = y * z^(x/4))

#gerando estatísticas resumo
tb %>% summarise(x_mean = mean(x), y_median = median(y))

########## BIBLIOTECA GGPLOT2 ###############
########## BIBLIOTECA GGPLOT2 ###############
#rodar a biblioteca
library(ggplot2) #é preciso fazer a instalação
#serão feitos apenas comentários a respeito nesta aula
#Utilize este link: http://r-statistics.co/Top50-Ggplot2-Visualizations-MasterList-R-Code.html
