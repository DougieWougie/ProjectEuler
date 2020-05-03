horizontal <-
    problem.matrix[, 1:17] *
    problem.matrix[, 2:18] *
    problem.matrix[, 3:19] *
    problem.matrix[, 4:20]

vertical <-
    problem.matrix[1:17,] *
    problem.matrix[2:18,] *
    problem.matrix[3:19,] *
    problem.matrix[4:20,]

diagonal.ltor <-
    problem.matrix[1:17, 1:17] *
    problem.matrix[2:18, 2:18] *
    problem.matrix[3:19, 3:19] *
    problem.matrix[4:20, 4:20]

diagonal.rto1 <-
    problem.matrix[4:20, 1:17] *
    problem.matrix[3:19, 2:18] *
    problem.matrix[2:18, 3:19] *
    problem.matrix[1:17, 4:20]

print(max(horizontal, vertical, diagonal.ltor, diagonal.rto1))
