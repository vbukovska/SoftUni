favourite_book = input()
command = input()

searched_books = 0

while command != 'No More Books':
    book = command
    searched_books += 1
    if favourite_book == book:
        exit(print(f'You checked {searched_books-1} books and found it.'))
    command = input()

if command == 'No More Books':
    print(f'The book you search is not here! \n You checked {searched_books} books.')
