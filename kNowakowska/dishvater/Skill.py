# from enum import Enum
from enum import Enum
from random import random


class Skill(Enum):
    Biology = round(random(), 2)
    Chemistry = round(random(), 2)
    Math = round(random(), 2)
    English = round(random(), 2)
    History = round(random(), 2)


for name in Skill.__members__.items():
    new = {Skill.name: round(random(), 2)}
    print(new)
