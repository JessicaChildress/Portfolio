# this file stores the function that gets all desired submatrices for performing future moves
# Note: it is used by both random and all possible moves functions


'''
* Function: get_all_desired_submat()
* This function iterates over the matrix and finds all of its possible submatrices
* for a desired column (n) and row (m) length. It "yields" this information which is 
* more like a batch return so a for loop is used to iterate over the returned data. 
* The returned data is the submatrix sliced from the matrix
* Parameters: matrix mxn matrix with n columns and m rows
* Returns: submatrix as a slice (needs to be iterated over)
'''
def get_all_desire_submat(mat, n, m):   # n is columns, m is rows
    rows = len(mat)
    cols = len(mat[0])
    for x in range (rows - n + 1):
        for y in range(cols - m + 1):
            yield [row[x:x+n] for row in mat[y:y+m]], x, y
            