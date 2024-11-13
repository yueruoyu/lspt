# In the previous exercise, you wrote a function that transposed a 3x3 matrix represented by a list of lists.

# Matrix transposes are not limited to 3x3 matrices, or even square matrices. Any matrix can be transposed simply by switching columns with rows.

# Modify your transpose function from the previous exercise so that it works with any MxN matrix with at least one row and one column.

# ExamplesCopy Code
# # All of these examples should print True


def transpose(mat):
    trans_mat = []
    for i in range(len(mat[0])):
        trans_mat.append([row[i] for row in mat])
    return trans_mat


# new_matrix = transpose(matrix)
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)