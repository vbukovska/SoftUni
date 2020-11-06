chat = []
while True:
    command_line = input()
    if command_line == 'end':
        break
    command, *messages = command_line.split()
    if command == 'Chat':
        chat.extend(messages)
    elif command == 'Delete':
        erase_message = messages[0]
        if erase_message in chat:
            chat.remove(erase_message)
    elif command == 'Edit':
        message_to_edit = messages[0]
        edited_message = messages[1]
        index_of_message = chat.index(message_to_edit)
        chat[index_of_message] = edited_message
    elif command == 'Pin':
        message_to_move = messages[0]
        chat.remove(message_to_move)
        chat.append(message_to_move)
    else:
        chat.extend(messages)
print('\n'.join(chat))