from entity import Record, AddressBook
from json_serializer import serialize_to_json, deserialize_from_json, convert_json_to_address_book
from csv_serializer import serialize_to_csv, deserialize_from_csv

record = Record("Ihor")
record.add_phone('1234567890')

record_two = Record("Stepan")
record_two.add_phone('1234567890')
record_two.add_phone('0987654321')

address_book = AddressBook()
address_book.add_record(record)
address_book.add_record(record_two)

serialize_to_csv(address_book, 'book.csv')

print(deserialize_from_csv('book.csv'))
print(address_book)
# print(address_book)

# serialize_to_json(address_book, 'book.json')

# book_dict = deserialize_from_json('book.json')

# print(address_book)
# print(convert_json_to_address_book(book_dict))

# lst = ['1234567890', '0987654321']
# print(';'.join(lst))

# print('1234567890;0987654321'.split(';'))