from ortools.sat.python import cp_model
from ortools.sat.python.cp_model import CpModel

from data.car import Car
from data.person import Person
from utils.vars_manager import VarsManager

infinity = cp_model.INT32_MAX


class ConstraintInput:
    def __init__(self, model: CpModel, vars: VarsManager, people: list[Person], cars: list[Car]):
        self.model = model
        self.people = people
        self.cars = cars
        self.person_to_car = {(person.id, car.id): vars.new_bool(f"person_{person.id}__car_{car.id}") for person in people for car in cars}
