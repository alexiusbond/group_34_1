class Transport:
    def __init__(self, the_model, the_year, the_color):
        self.model = the_model
        self.year = the_year
        self.color = the_color

    def change_color(self, new_color):
        self.color = new_color
        print(f'{self.model} changed color')


class Plane(Transport):
    def __init__(self, the_model, the_year, the_color):
        # constructor matching
        super().__init__(the_model, the_year, the_color)


class Car(Transport):
    counter = 0
    standart_wheels_number = 5

    # constructor
    def __init__(self, the_model, the_year, the_color, penalties=0):
        # attributes/fields
        super().__init__(the_model, the_year, the_color)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    standart_wheels_number = 12
    def __init__(self, the_model, the_year, the_color, penalties=0, load_capacity=0):
        super().__init__(the_model, the_year, the_color, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg')
        else:
            print(f'Cargo of {type} ({weight} kg) was successfully loaded on {self.model}')


print(f'Car factory produced: {Car.counter}')

bmw_car = Car('BMW X7', 2020, 'Black')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'Red'
bmw_car.change_color('Red')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} NEW COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')

honda_car = Car(the_year=2019, penalties=1200, the_model='Honda Cr-V', the_color='Silver')
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Tokmok')

print(f'Car factory produced: {Car.counter}')
price_for_winter_lastic = 5000
print(f'We need {Car.counter * Car.standart_wheels_number * price_for_winter_lastic} '
      f'soms to change our car on winter lastics')

mig = Plane('Mig 29', 1976, 'Black')
print(f'MODEL: {mig.model} YEAR: {mig.year} COLOR: {mig.color}')

man_truck = Truck('Man 2700', 2009,
                  'Blue', 900, 45000)

print(f'MODEL: {man_truck.model} YEAR: {man_truck.year} COLOR: {man_truck.color} '
      f'PENALTIES: {man_truck.penalties} LOAD CAPACITY: {man_truck.load_capacity} kg')
man_truck.load_cargo(50000, 'Apples')
man_truck.load_cargo(40000, 'Oranges')
man_truck.drive('Batken')

print(Truck.standart_wheels_number)
print(Truck.counter)