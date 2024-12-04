class WheeledVehicle:
    def __init__(self,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity
    def range(self):
        return self.fuel_capacity * self.fuel_efficiency

class TireMixin:
    def tires(self, tire_list):
        self.tires = tire_list

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure


class Auto(TireMixin, WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__(50, 25.0)
        self.tires([30, 30, 32, 32])

class Motorcycle(TireMixin, WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__(80, 8.0)
        self.tires([20, 20])

class Catamaran:
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        # ... code omitted ...