from abc import ABC
from homework_02.exceptions import LowFuelError, \
    NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Not enough fuel to start the vehicle")

    def move(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed <= self.fuel:
            self.fuel -= fuel_needed
        else:
            raise NotEnoughFuel("Not enough fuel to cover the distance")
