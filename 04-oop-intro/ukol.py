import random
class Hello:
    username = 'Teran'
    favorite_number = 2
    def __init__(self, car, book, nmb):
        self.car = car
        self.book = book
        self.nmb = nmb

    def __str__(self):
        return f'({self.car}, {self.book}, {self.nmb})'

    def __eq__(self, other):
        return self.car == other.car

    def __gt__(self, other):
        return self.nmb > other.nmb

    def __add__(self, other):
        return self.nmb + other.nmb

    def __sub__(self, other):
        return self.nmb - other.nmb

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
        return (slovo[:-1])

    def all(self):
        print(f'{self.favorite_number}, {self.username}, {self.car}, {self.book}, {self.nmb}, {self.random_number()}, {self.word()}')

    def only_numbers(self):
        print(f'{self.nmb}, {self.favorite_number}, {self.random_number()}')

class Bye(Hello):
    def __init__(self, car, book, nmb, boom, word, x):
        super().__init__(car, book, nmb)
        self.boom = boom
        self.word = word
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, hodnota):
        self.__x = hodnota

    def __str__(self):
        return f'({self.car}, {self.book}, {self.nmb}, {self.boom}, {self.word}, {self.__x})'

vse = Hello('Mustang', 'Zaklinac', 3)
vse2 = Bye('Kia', 'Krysar', 1, 'booom', Hello.word(), 'Bye')
print(vse)
print(vse2)
vse.all()
vse.only_numbers()
print(type(vse))
print(vse - vse2)
print(vse + vse2)
print(vse == vse2)
print(vse > vse2)
