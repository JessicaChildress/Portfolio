# Relocated from main.py on 3/22/2023
# these matrices are complete rather than partial knots so while they may make good training data,
# they are not valid submatrices that we can use to search for moves.

''' I WANT TO DELETE THIS FILE'''
# 3x3 matrix 
# Reidemeister Type I move(s) on the unknot:
r1_left_twist_over = [[2, 1, 0],
                      [3, 9, 1],
                      [0, 3, 4]]
# print(r1_left_twist_over)
r1_left_twist_under = [[2, 1, 0],
                       [3, 10, 1],
                       [0, 3, 4]]
r1_left_untwist = [[2, 1, 0],
                   [3, 7, 1],
                   [0, 3, 4]]
r1_right_twist_under = [[0, 2, 1],
                        [2, 9, 4],
                        [3, 4, 0]]
r1_right_twist_over = [[0, 2, 1],
                       [2, 10, 4],
                       [3, 4, 0]]
r1_right_untwist = [[0, 2, 1],
                    [2, 8, 4],
                    [3, 4, 0]]
r1_matrices = [r1_left_twist_over, r1_left_twist_under, r1_left_untwist,
               r1_right_twist_over, r1_right_twist_under, r1_right_untwist]
# print(r1_matrices)