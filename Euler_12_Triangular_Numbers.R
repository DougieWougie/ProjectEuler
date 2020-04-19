library(numbers)

triangular.number <- function(a) {
    b <- a + 1
    ab = (a * b) / 2
}

factors <- function(number) {
    Sigma((triangular.number(number)), k = 0)
}

num.factors <- 0
i <- 1

while (num.factors < 500) {
    num.factors <- factors(i)
    print(triangular.number(i))
    i <- i + 1
}
