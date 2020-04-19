library(gmp)

paths <- function(grid.size) {
    # There are only two available moves, down and right. As the lattice
    # is square the combination of moves must be equal. So the combination
    # nCk is (2n)!/n!n!
    return(factorialZ(2 * grid.size) / (factorialZ(grid.size) * factorialZ(grid.size)))
}

print(paths(20))
