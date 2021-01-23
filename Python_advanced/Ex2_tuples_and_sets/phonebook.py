class Phonebook:
    def __init__(self):
        self.contacts = {}

    def exists(self, name):
        return name in self.contacts

    def add_contact(self, name, number):
        self.contacts[name] = number

    def update_contact(self, name, contact):
        self.contacts[name].update({name: contact})

    def return_contact(self, name):
        if self.exists(name):
            number = self.contacts[name]
            return f'{name} -> {number}'
        else:
            return f'Contact {name} does not exist.'


contact_book = Phonebook()

while True:
    name, *number = input().split('-')
    if name.isdigit():
        break
    phone_number = number[0]
    if not contact_book.exists(name):
        contact_book.add_contact(name, phone_number)
    else:
        contact_book.update_contact(name, phone_number)

number_of_chechs = int(name)

for _ in range(number_of_chechs):
    contact_name = input()
    print(contact_book.return_contact(contact_name))

