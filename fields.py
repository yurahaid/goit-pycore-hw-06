import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
    pass


class Phone(Field):
    def __init__(self, value):
        if not re.match(r"^\d{10}$", value):
            raise ValueError("Phone must contains only 10 digits")
        super().__init__(value)

    pass


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(p)

    def edit_phone(self, old_phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == old_phone:
                self.phones[i] = Phone(new_phone)

                return

    def find_phone(self, to_find_phone):
        for phone in self.phones:
            if phone.value == to_find_phone:
                return phone

        return None

    def get_name(self):
        return self.name.value

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.get_name()] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        del self.data[name]
