class Human :
    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone,
            'address': self.address,
        }

    def call(self, phone_number):
        return f'{self.phone} вызывает абонента {phone_number}'

human_1 = Human('Anna', 'Ponomarenko', 19, '+380686650202', 'Pirogova 12')
human_2 = Human('Sasha', 'Pikul', 25, '+3802347896', 'Ekaterinenskaya 35')
human_3 = Human('Nikoloz', 'Djanashia', 29, '+380686658976', 'Kanatnaya 19')

print(human_1.get_info())
print(human_2.get_info())
print(human_3.get_info())
print(human_1.call('+380686650202'))
