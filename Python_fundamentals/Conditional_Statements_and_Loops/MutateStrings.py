str1 = input()
str2 = input()

new_str, unique_str = '', ''

for i in range(0, len(str1)):
    if str2[i] != str1[i]:
        new_str = str2[0:i+1] + str1[i+1:]
        print(new_str)
        unique_str = new_str
