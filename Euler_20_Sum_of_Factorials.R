library(gmp)
sum.digits <- function(number) {
    return(sum(as.numeric(unlist(strsplit(as.character(number), split = "")))))
}
print((sum.digits(factorialZ(100))))
