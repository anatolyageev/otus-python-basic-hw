"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    engine: Engine
    cargo: int
    max_cargo: int

    def __init__(self, weight=0, fuel=0, fuel_consumption=0, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def set_engine(self, engine: Engine):
        self.engine = engine

    def load_cargo(self, add_cargo):
        if add_cargo + self.cargo <= self.max_cargo:
            self.cargo += add_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo
