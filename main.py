import json
from enum import Enum


class Sounds(Enum):
    dog = "bark"
    cat = "meow"
    cow = "moo"
    rat = "pipi"
    alien = "KILL"


def animal_sound():
    with open('test.json', 'r') as file:
        data = json.load(file)

    animal = data.get("animal", "")

    if animal in Sounds.__members__:
        print(Sounds[animal].value)
    else:
        print("Unknown animal")


animal_sound()
