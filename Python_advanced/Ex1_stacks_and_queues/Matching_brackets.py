expression = input()

stack = []

for index in range(len(expression)):
    if expression[index] == '(':
        stack.append(index)
    elif expression[index] == ')':
        sub_expr_last_index = index
        sub_expr_start_index = stack.pop()
        print(expression[sub_expr_start_index:sub_expr_last_index + 1])
