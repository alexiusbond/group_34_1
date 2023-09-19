from enum import Enum


class Color(Enum):
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    END = '\033[0m'


class MusicPlayable:  # Mixin
    # def __init__(self):
    #     pass

    def play_music(self, song):
        print(f'Now is playing {song}')

    def stop_music(self):
        print(f'Music stopped')


class Drawable:  # Mixin
    def draw(self, emoji):
        print(emoji)


class SmartPhone(MusicPlayable, Drawable):
    def __init__(self):
        pass


class Car(MusicPlayable, Drawable):
    counter = 0

    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        if type(value) == Color:
            self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'MODEL: {self.__model} YEAR: {self.__year} '
                f'COLOR: {self.__color.value}{self.__color.name}{Color.END.value}')

    def __gt__(self, other):
        return self.__year > other.__year

    def __lt__(self, other):
        return self.__year < other.__year

    def __ge__(self, other):
        return self.__year >= other.__year

    def __le__(self, other):
        return self.__year <= other.__year

    def __eq__(self, other):
        return self.__year == other.__year

    def __ne__(self, other):
        return self.__year != other.__year


class FuelCar(Car):
    __total_fuel = 1000

    @staticmethod
    def get_fuel_type():
        return 'AI - 95'

    @classmethod
    def fill_total_fuel(cls, amount):
        cls.__total_fuel += amount

    @classmethod
    def get_total_fuel(cls):
        return cls.__total_fuel

    def __init__(self, model, year, color, fuel_bank):
        # super().__init__(model, year, color)
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel -= fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by fuel')

    def __str__(self):
        return super().__str__() + f' FUEL BANK: {self.__fuel_bank}'

    def __add__(self, other):
        return self.__fuel_bank + other.__fuel_bank


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    def drive(self):
        print(f'Car {self.model} is driving by electricity')

    def __str__(self):
        return super().__str__() + f' WBATTERY: {self.__battery}'


class HybridCar(ElectricCar, FuelCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        ElectricCar.__init__(self, model, year, color, battery)
        FuelCar.__init__(self, model, year, color, fuel_bank)


print(f'Fuel Car fabric has: {FuelCar.get_total_fuel()} lt.')

some_car = Car('BMW X6', 2020, Color.RED)
print(some_car)

nissan_car = FuelCar('Nissan Patrol', 2009,
                     Color.YELLOW, 80)
print(nissan_car)

tesla_car = ElectricCar('Tesla Model Y', 2023,
                        Color.BLUE, 25000)
print(tesla_car)

toyota_car = HybridCar('Toyota Prius', 2021,
                       Color.GREEN, 45, 10000)
print(toyota_car)
toyota_car.drive()
print(HybridCar.mro())

number_1 = 8
number_2 = 4
print(f'Number one is bigger than Number two: {number_1 > number_2}')
print(f'Number one is smaller than Number two: {number_1 < number_2}')
print(f'Toyota car is better than Nissan car: {toyota_car > nissan_car}')
print(f'Toyota car is the same with Nissan car: {toyota_car == nissan_car}')

# FuelCar.total_fuel -= 100
print(toyota_car + nissan_car)
print(f'Fuel Car fabric has: {FuelCar.get_total_fuel()} lt.')

FuelCar.fill_total_fuel(500)
print(f'Fuel Car fabric has: {FuelCar.get_total_fuel()} lt. ({FuelCar.get_fuel_type()})')

toyota_car.play_music('Song 1')
toyota_car.stop_music()
toyota_car.draw('🚗')

my_phone = SmartPhone()
my_phone.draw('📱')

if tesla_car.model == 'Tesla Model Y':
    print('This car is cool')

if tesla_car.color == Color.BLUE:
    print('This car is beautiful')
