library(gmp)

for (i in 1:10000) {
    number.string = as.character(fibnum(i))
    if (nchar(number.string) == 1000) {
        print(i)
        print(number.string)
        break
    }
}
