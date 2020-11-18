import random
class Hello:
    username = 'Teran'
    favorite_number = 2
    def __init__(self, car, book, nmb):
        self.car = str(car)
        self.book = str(book)
        self.nmb = nmb

    def __str__(self):
        return f'({self.car}, {self.book}, {self.nmb})'

    def __eq__(self, other):
        return self.car == self.book

    def __gt__(self, other):
        return self.favorite_number > self.nmb

    def __add__(self, other):
        return self.favorite_number + self.nmb

    def __sub__(self, other):
        return self.favorite_number - self.nmb

    @staticmethod
    def random_number():
        return random.randint(0, 150)

    @classmethod
    def word(cls):
        slovo = 'Ahoj;ja;jsem;tvurce'
        x = slovo.split(';')
        slovo = ''
        for i in range(0, len(x)):
            slovo += x[i] + ' '
        return (slovo)

    def all(self):
        print(f'{self.favorite_number}, {self.username}, {self.car}, {self.book}, {self.nmb}, {self.random_number()}, {self.word()}')

    def only_numbers(self):
        print(f'{self.nmb}, {self.favorite_number}, {self.random_number()}')

vse = Hello('Mustang', 'Zaklinac', 3)
print(vse)
vse.all()
vse.only_numbers()
print(type(vse))
print(vse - vse)
print(vse + vse)
print(vse == vse)
print(vse > vse)
