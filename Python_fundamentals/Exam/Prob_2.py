import re
number_of_messages = int(input())

# pattern = r"^(\$)[A-Z][a-z]{2,}\1: (\[\d+\]\|){3}$"
# pattern_num = r"\[(\d+)\]\|"
# pattern_tag =
# pattern = r"^(\$)[A-Z][a-z]{2,}\1: (\[(?P<digits>\d+)\]\|){3}$"
pattern = r"^(\$|%)(?P<tag>[A-Z][a-z]{2,})\1: (\[(?P<num_1>\d+)\]\|)(\[(?P<num_2>\d+)\]\|)(\[(?P<num_3>\d+)\]\|)$"
for n in range(number_of_messages):
    messages = input()
    message = re.finditer(pattern, messages)
    message_list = [msg.groupdict() for msg in message]
    if len(message_list) >= 1:
        groups = message_list[0]
        tag = groups['tag']
        char_1 = chr(int(groups['num_1']))
        char_2 = chr(int(groups['num_2']))
        char_3 = chr(int(groups['num_3']))
        decrypted_message = char_1 + char_2 + char_3
        print(f"{tag}: {decrypted_message}")
    else:
        print("Valid message not found!")
