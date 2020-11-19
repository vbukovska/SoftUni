def add_user(user, side, book):
    for force in book:
        if user in book[force]:
            return book
    if side not in book:
        book[side] = []
    if user not in book[side]:
        book[side].append(user)
    return book


force_book = {}

while True:
    command_line = input()
    if 'Lumpawaroo' in command_line:
        break
    if '|' in command_line:
        force_side, user = command_line.split(' | ')
        force_side = add_user(user, force_side, force_book)
    else:
        user, force_side = command_line.split(' -> ')
        for key in force_book:
            if user in force_book[key]:
                force_book[key].remove(user)
        force_book = add_user(user, force_side, force_book)
        print(f'{user} joins the {force_side} side!')

sorted_book = dict(sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])))
for side in sorted_book:
    side_members = len(sorted_book[side])
    if side_members > 0:
        print(f'Side: {side}, Members: {len(sorted_book[side])}')
        sorted_book[side].sort()
        [print(f'! {sorted_book[side][x]}') for x in range(side_members)]
