def create_testing_file(file_path, input_lines):
    with open(file_path, "w") as file:
        return file.writelines("\n".join([input_line for input_line in input_lines]))


test_lines = [
    "-I was quick to judge him, but it wasn't his fault.",
    "-Is this some kind of joke?! Is it?",
    "-Quick, hide here. It is safer."
]

create_testing_file("text.txt", test_lines)