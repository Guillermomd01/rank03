#friendly way
def matrix_reverse(matrix: list[list[int]]) -> list[list[int]]:
    #here we have to not touch the real matrix so lets create a new one
    new_matrix = []
    for row in matrix:
        #copy the curr row into another variable
        new_row = row.copy()
        #reverse the row
        new_row.reverse()
        #add it to the new matrix
        new_matrix.append(new_row)
    return new_matrix

#for lazy people like me, use list comprhensions
def matrix_reverse(matrix: list[list[int]]) -> list[list[int]]:
    return [row[::-1] for row in matrix]