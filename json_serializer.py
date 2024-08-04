import json
from entity import AddressBook, Record

def serialize_obj(obj):
    # if isinstance(obj, str):
    #     return str(obj)
    return obj.__dict__

def serialize_to_json(obj, file_path: str):
    with open(file_path, 'w') as file:
        json.dump(obj, file, default=serialize_obj)

def deserialize_from_json(file_path: str):
    with open(file_path, 'r') as file:
        return json.load(file)

def convert_json_to_address_book(json_dict: dict) -> AddressBook:
    book = AddressBook()
    for name, record_dict in json_dict['data'].items():
        name = record_dict['name']['value']
        record = Record(name)

        phones = record_dict['phones']
        for phone in phones:
            record.add_phone(phone['value'])
        
        book.add_record(record)
    
    return book
