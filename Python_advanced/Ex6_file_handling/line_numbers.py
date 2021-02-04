import re


def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            return "".join(file.readlines()).split("\n")
    except FileNotFoundError:
        print("File or file path does not exist!")


def count_characters(list_name):
    count = []
    [count.append(len("".join(line))) for line in list_name]
    return count


file_lines = read_file_content("text.txt")

file_words = [re.findall(r"[a-zA-Z]+", file_line) for file_line in file_lines]
count_letters = count_characters(file_words)

file_punctoation_marks = [re.findall(r"[!?.,'\"-]", file_line) for file_line in file_lines]
count_punctoations = count_characters(file_punctoation_marks)


result_lines = []
for index in range(len(file_lines)):
    result_lines.append(f"Line: {index + 1} {file_lines[index]} ({count_letters[index]})({count_punctoations[index]})")

with open("output.txt", "w") as output_file:
    output_file.writelines("\n".join(result_lines))
