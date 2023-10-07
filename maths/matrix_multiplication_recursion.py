# @Author  : ojas-wani
# @File    : matrix_multiplication_recursion.py
# @Date    : 10/06/2023


"""
Introduction:

This Python script demonstrates matrix multiplication using a recursive algorithm. 
Matrix multiplication is a fundamental operation in linear algebra and computer science.
"""


<<<<<<< HEAD
def matrix_multiply_recursive(matrix_A: list, matrix_B: list) -> list:
    """
    :param matrix_A: Input matrices.
    :param matrix_B: Input matrices where length of matrices is 
                    as same as number of columns matrix_A.
=======
def matrix_multiply_recursive(matrix_a: list, matrix_b: list):
    """
    :param matrix_a: Input matrices.
    :param matrix_b: Input matrices where length of matrices is 
                    as same as number of columns matrix_a.
>>>>>>> origin/master

    """

    # Check if matrices can be multiplied
<<<<<<< HEAD
    if len(matrix_A[0]) != len(matrix_B):
        raise ValueError("Invalid matrix dimensions")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix_B[0]))]
              for _ in range(len(matrix_A))]

    # Recursive multiplication of matrices
    def multiply(i_loop: int, j_loop: int, k_loop: int, matrix_A: list, matrix_B: list, result: list) -> function:
        """
        :param matrix_A: Input matrices.
        :param matrix_B: Input matrices where length of matrices is 
                    as same as number of columns matrix_A.
        :param result: Result matrix
        :param i_loop: Indices used for iteration during multiplication.
        :param j_loop: Indices used for iteration during multiplication.
        :param k_loop: Indices used for iteration during multiplication.
        """

        if i_loop >= len(matrix_A):
            return
        if j_loop >= len(matrix_B[0]):
            return multiply(matrix_A, matrix_B, result, i_loop + 1, 0, 0)
        if k_loop >= len(matrix_B):
            return multiply(matrix_A, matrix_B, result, i_loop, j_loop + 1, 0)
        result[i_loop][j_loop] += matrix_A[i_loop][k_loop] * matrix_B[k_loop][j_loop]
        multiply(matrix_A, matrix_B, result, i_loop, j_loop, k_loop + 1)

    # Perform matrix multiplication
    multiply(matrix_A, matrix_B, result, 0, 0, 0)
=======
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Invalid matrix dimensions")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix_b[0]))]
              for _ in range(len(matrix_a))]

    # Recursive multiplication of matrices
    def multiply(i, j, k, matrix_a, matrix_b, result):
        """
        :param matrix_a: Input matrices.
        :param matrix_b: Input matrices where length of matrices is 
                    as same as number of columns matrix_a.
        :param result: Result matrix
        :param i: Indices used for iteration during multiplication.
        :param j: Indices used for iteration during multiplication.
        :param k: Indices used for iteration during multiplication.
        """

        if i >= len(matrix_a):
            return
        if j >= len(matrix_b[0]):
            return multiply(matrix_a, matrix_b, result, i + 1, 0, 0)
        if k >= len(matrix_b):
            return multiply(matrix_a, matrix_b, result, i, j + 1, 0)
        result[i][j] += matrix_a[i][k] * matrix_b[k][j]
        multiply(matrix_a, matrix_b, result, i, j, k + 1)

    # Perform matrix multiplication
    multiply(matrix_a, matrix_b, result, 0, 0, 0)
>>>>>>> origin/master
    return result


if __name__ == "__main__":

    # Input matrixes
<<<<<<< HEAD
    matrix_A = [
=======
    matrix_a = [
>>>>>>> origin/master
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [13, 14, 15, 16]
    ]
<<<<<<< HEAD
    matrix_B = [
=======
    matrix_b = [
>>>>>>> origin/master
        [5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1],
        [2, 6, 10, 14]
    ]

<<<<<<< HEAD
    result_matrix = matrix_multiply_recursive(matrix_A, matrix_B)
=======
    result_matrix = matrix_multiply_recursive(matrix_a, matrix_b)
>>>>>>> origin/master
    for row in result_matrix:
        print(row)
