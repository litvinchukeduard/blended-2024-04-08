import csv 
from entity import AddressBook, Record

def serialize_to_csv(book: AddressBook, file_path: str):
    with open(file_path, 'w') as file:
        fieldnames = ['name', 'phones']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for name, record in book.data.items():
            # record = Record("Ihor") # 1234567890, 0987654321
            phones = [] # ['1234567890', '0987654321']
            for phone_obj in record.phones:
                phones.append(phone_obj.value)
            writer.writerow({'name': record.name.value, 'phones': ';'.join(phones)})

def deserialize_from_csv(file_path: str):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        book = AddressBook()
        for row in reader:
            name = row['name']
            record = Record(name)
            phones = row['phones'].split(';')
            for phone in phones:
                record.add_phone(phone)
            book.add_record(record)
            # print(row['name'], row['phones'])
        return book
