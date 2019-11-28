class Car:

    def __init__(self, make, model, year):
        self.odometer = 0
        self.fuel = 70
        self.make = make
        self.model = model
        self.year = year

    def drive(self, distance):
        self.distance = distance
        self.benza_xvatit = False
        if self.fuel * 10 >= self.distance:
            self.benza_xvatit = True
            print("Айда!!!")
            print(self.__add_distance())                # внутри метода Drive
            print(self.__substract_fuel())              # запускает приватные методы
        else:
            print(f"Бензин жетпейт! {self.distance}km")

    def __add_distance(self):
        if self.benza_xvatit == True:
            self.odometer += self.distance
            result = "Odometer: " + str(self.odometer) + "km"
        return result

    def __substract_fuel(self):
        if self.benza_xvatit == True:
            self.fuel -= self.distance / 10
            result = "Fuel: " + str(self.fuel) + "l"
        return result

auto = Car("toyota", "mark2", 1995)
auto.drive(200)
# print(auto._Car__add_distance())              # Прямо
# print(auto._Car__substract_fuel())
# print(dir(auto))




