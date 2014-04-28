
def transpose_matrix(matrix, asListOfTuples = False):
    if asListOfTuples:
        return zip(*matrix)
    return map(list, zip(*matrix))

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
          
         #Transposed: 
         #[[1, 4, 7], 
         # [2, 5, 8], 
         # [3, 6, 9]]
         
         #Transposed as list of tuples:
         #[(1, 4, 7), 
         # (2, 5, 8), 
         # (3, 6, 9)]
         

assert transpose_matrix(matrix)       == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
assert transpose_matrix(matrix, True) == [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

