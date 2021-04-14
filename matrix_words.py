import numpy as np
import math
from wordsolver import WordSearchSolver


def get_string():
    user_string = input("Input string of size N^2 :")
    listed_user_string = list(user_string)
    return listed_user_string


def get_matrix_size(listed_user_string):
    matrix_size = int(math.sqrt(len(listed_user_string)))
    return matrix_size


def get_matrix_string(listed_user_string, matrix_size):
    matrix_from_string = ((np.array(listed_user_string).reshape(matrix_size, matrix_size)))
    return matrix_from_string


def get_words_from_matrix(matrix_from_string):
    new_m = matrix_from_string.tolist()
    wordsearch_solver = WordSearchSolver("words.txt")
    solution = wordsearch_solver.solve(new_m, directions=["E", "W", "N", "S"])
    print(f'Words from your string:{([solution[i][0] for i in range(len(solution))])}')


string = get_string()
matrix_size = get_matrix_size(string)
new_matrix = get_matrix_string(string, matrix_size)
new_matrix2 = get_words_from_matrix(new_matrix)
