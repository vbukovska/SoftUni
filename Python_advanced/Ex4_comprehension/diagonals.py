def read_matrix(n):
    # nested comprehension
    result = [[int(num) for num in input().split(', ')] for _ in range(n)]
    return result


n = int(input())
matrix = read_matrix(n)

first_diagonal = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][len(matrix) - i-1] for i in range(len(matrix))]
print(f"First diagonal: {', '.join([str(num) for num in first_diagonal])}. Sum: {sum(first_diagonal)}")
print(f"Second diagonal: {', '.join([str(num) for num in second_diagonal])}. Sum: {sum(second_diagonal)}")
