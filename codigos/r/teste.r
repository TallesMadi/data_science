a <- 5
b <- 7
c <- a + b

if (c > 10) {
    d <- 'Sim'
} else {
    d <- 'Não'
}

pow <- function(x, y) {
    result <- x ^ y
    print(paste(result))
}

print(paste("C é maior que 10?", d))
pow(10, 2)

