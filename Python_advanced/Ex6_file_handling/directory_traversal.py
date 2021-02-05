import os

directories = [file for file in os.listdir("./") if os.path.isfile(file)]

files = [os.path.splitext(file) for file in directories]

file_dict = {}
for file in files:
    extension = file[1]
    file_name = file[0]
    if extension not in file_dict:
        file_dict[extension] = []
    file_dict[extension].append(file_name)

sorted_files = dict(sorted(file_dict.items(), key=lambda x: (x[0], x[1])))

result_list = []
for file_ext, name in sorted_files.items():
    result_list.append(file_ext)
    result_list.extend([f"---{name[i]}{file_ext}" for i in range(len(name))])


desktop_location = os.path.expanduser("~/Desktop/report.txt")
with open(desktop_location, "w") as output_file:
    output_file.writelines("\n".join(result_list))