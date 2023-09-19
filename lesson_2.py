class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, contact):
        self.__name = name
        self.__age = age
        if (type(contact) == Contact):
            self.__contact = contact
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if (type(new_age) == int and new_age > 0):
            self.__age = new_age
        else:
            raise ValueError('Age attribute must be positive number')

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    @property
    def contact(self):
        return self.__contact

    @contact.setter
    def contact(self, value):
        if (type(value) == Contact):
            self.__contact = value

    def speak(self):
        raise NotImplementedError('Method speak must be implemented')

    def info(self):
        return (f'NAME: {self.__name} AGE: {self.__age} BIRTH YEAR: {2023 - self.__age}\n'
                f'CONTACT INFO: {self.__contact.city}, {self.__contact.street} {self.__contact.number}')


class Cat(Animal):
    def __init__(self, name, age, contact):
        super(Cat, self).__init__(name, age, contact)

    def speak(self):
        print('Myauuu')


class Snake(Animal):
    def __init__(self):
        super(Snake, self).__init__()

class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, commands, contact):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands

    def speak(self):
        print('Gav-gav')

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f' COMMANDS: {self.__commands}'


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact):
        super(FightingDog, self).__init__(name, age, 'Fight', contact)
        self.__wins = wins

    def info(self):
        return super().info() + f' WINS: {self.__wins}'

    def speak(self):
        print('Rrrrr gav')


contact_1 = Contact('Bishkek', 'Chui', 23)

# some_animal = Animal('Anim', 2, contact_1)
# print(some_animal.info())
# some_animal.set_age(4)
# print(some_animal.info())
# print(some_animal.get_name())

dog = Dog('Money', 5, 'Sit', contact_1)
print(dog.commands)
dog.commands = 'Sit, Bark'

f_dog = FightingDog('Fekl', 1, 'Fight', 8,
                    Contact('Osh', 'Masalieva', 4))

cat = Cat('Murka', 5, f_dog.contact)

fish = Fish('Nemo', 9, contact_1)

animals_list = [cat, fish, dog, f_dog]
for animal in animals_list:
    print(animal.info())
    animal.speak()


    