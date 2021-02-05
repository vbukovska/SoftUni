import os


def update_file_content(file_path, content):
    with open(file_path, "w") as file:
        file.writelines(content)


def create_file(file_path):
    with open(file_path, "w"):
        pass


def delete_file(file_path):
    try:
        os.remove(file_path)
    except FileNotFoundError:
        print("An error occurred")


def add_to_file(file_path, file_content):
    if not os.path.exists(file_path):
        file = open(file_path, "w")
        file.close()

    with open(file_path, "a") as file:
        file.writelines(file_content + "\n")


def replace_in_file(file_path, old_content, new_content):
    if not os.path.exists(file_path):
        print("An error occurred")
    else:
        with open(file_path, "r+") as file:
            file_lines = [line for line in file.readlines()]
            result = [line.replace(old_content, new_content) for line in file_lines]
        update_file_content(file_path, result)


while True:
    command, *file_data = input("Enter a command:\n").split("-")
    if command == "End":
        break
    file_name = file_data[0]
    if command == "Create":
        create_file(file_name)
    elif command == "Add":
        content = file_data[1]
        add_to_file(file_name, content)
    elif command == "Replace":
        old_string = file_data[1]
        new_string = file_data[2]
        replace_in_file(file_name, old_string, new_string)
    else:
        delete_file(file_name)

