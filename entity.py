from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        if value is None:
            raise ValueError
        self.value = value

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f'Field(value = {self.value})'
    

class Name(Field):
    def __str__(self):
        return f'Name(value = {self.value})'


class Phone(Field):
    def __init__(self, phone) -> None:
        if len(phone) < 10:
            raise ValueError
        super().__init__(phone)

    def __str__(self):
        return f'Phone(value = {self.value})'


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f'Record(name = {self.name}, phones = {self.phones})'


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record


# field_one = Field("Ihor")
# print(field_one)

# try:
#     phone = Phone('123')
# except ValueError:
#     phone = Phone('1234567890')

# record = Record("Ihor")
# record.add_phone('1234567890')

# address_book = AddressBook()
# address_book.add_record(record)

# print(address_book)

# # record = Record("Ihor")
# print(record.__dict__)
# print(record.name.__dict__)
