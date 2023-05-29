# In this file, all possible submatrices that correspond to a "move" are found and returned
import findSubmatrixTest
import submatrix
import performMoves
import numpy as np

'''
* Funciton: find_all_moves()
* This function iterates through all of the submatrices in submatrix.py 
* and stores the following in the possible_moves list:
    - the submatrix that matches
    - horizontal index within matrix
    - vertical index within matrix 
    - index of smat within a family of moves
    - the family of moves where the match was identified (i.e. Reidemeister I)
* Parameters: matrix 
* Returns: NA
'''
def find_all_moves(matrix):
    #GIVEN: 
    # matrix: big matrix
    # family: stores all submatrices of that move type
    # y: vertical index location of top left corner of smat
    # x: horixontal index location of top left corner of smat
    # r: stores the index location of each submatrix in its respective family (family[smat][r]))
    
    possible_moves = []
    for family in submatrix.all_current_families:
        # print("hello from for family")
        for smat in family:
            p = len(smat[0])    # submatrix column size
            q = len(smat)       # submatrix row size
            r = family.index(smat)  # gets index location of each submatrix in its respective family
            for a, x, y in findSubmatrixTest.get_all_desire_submat(matrix, p, q):
                if a == smat:
                    possible_moves.append([a, x, y, r, family])  # a stores submatrix, y stores vertical index, x stores horizontal index
                    # print(a, "found it at top left corner: ", "x =",x, " y =", y)
    perform_all_possible_combos_of_moves(possible_moves, matrix, family, x, y, r)


'''
* This function is currently not being used
* As its name implies, it performs all possible combinations of moves
* However, we have decided to perform moves randomly
'''
def perform_all_possible_combos_of_moves(moves_arr, matrix, family, x, y, r):
    if len(moves_arr) > 0:
        for j in range(len(moves_arr)):
            unknot = performMoves.perform_move(matrix, family, x, y, r) # needs to be a deep copy!!
            unknot = np.array(unknot)
            print(unknot)
            find_all_moves(unknot)