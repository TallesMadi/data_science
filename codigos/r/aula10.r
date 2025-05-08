# variáveis
x <- 10
15 -> y
z = 20
print(paste('x = ', x, ', y = ', y, 'e z = ', z))

#vetores
w = c(1, 2, 3)
q = c(4, 5, 6)
r = w + q
print(q[1])
print(r)

w_int = as.integer(w)
print(typeof(w_int))

t = c("A", 1)
print(typeof(t))

# lista
lista_ex = list(10, 'R', TRUE, c(1, 2, 3))
print(lista_ex)
print(lista_ex[[3]])

# Matrizes
matriz_ex = matrix(1:6, nrow=2, ncol=3)
print(matriz_ex)

matriz_ex_2 = matrix(c(10, 20, 30, 40, 50, 60, 70, 80, 90), nrow=3, byrow=TRUE)
print(matriz_ex_2)