def read_matrix():
    return [[num for num in row.split()] for row in input().split('|')]


matrix = read_matrix()
matrix = matrix[::-1]
print(' '. join([num for row in matrix for num in row]))