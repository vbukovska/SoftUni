import re


def read_file_content(file_path):
    try:
        with open(file_path, "r") as file:
            return "".join(file.readlines()).split("\n")
    except FileNotFoundError:
        print("File or file path does not exist!")


characters_to_replace = "-,.!?"

file_lines = read_file_content("text.txt")

even_lines = [file_lines[index] for index in range(len(file_lines)) if index % 2 == 0]

for char in characters_to_replace:
    even_lines = [line.replace(char, "@") for line in even_lines]

# Split to words and reverse.
even_lines_reverced = [re.findall(r"[a-zA-Z@']+", line)[::-1] for line in even_lines]

[print(" ".join(line)) for line in even_lines_reverced]

