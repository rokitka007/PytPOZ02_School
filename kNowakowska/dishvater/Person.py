from datetime import datetime
from Skill import Skill
from random import randrange


class Person:

    def __init__(self, name, surname, dateOfBirth, automatic=True):
        self.name = name
        self.surname = surname
        self.dateOfBirth = datetime.strptime(dateOfBirth, "%d-%m-%Y")
        self.skills = {}
        self.automatic = automatic

    def presentYourself(self):
        print("Hi, I'm {} {} and I'm {} years old".format(self.name, self.surname, self.getAge()))

    def getAge(self):
        now = datetime.now().year
        then = self.dateOfBirth.year
        return now - then

    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname

    def defineSkills(self):
        if self.automatic:
            return Skill.__members__


peter = Person('Piotr', 'Kowalski', '23-04-1986')
print(peter.defineSkills())
