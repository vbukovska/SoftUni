def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        name_first_letter = name[0]
        if name_first_letter in kwargs:
            result[name] = kwargs[name_first_letter]
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))