def kwargs_length(**kwargs):
    number_of_inputs = len(kwargs)
    return number_of_inputs


dictionary = {'name': 'Peter', 'age': 25}

print(kwargs_length(**dictionary))