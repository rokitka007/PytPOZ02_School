from datetime import datetime
from random import randrange, uniform

from kNowakowska.people.konradzadanietest.Skill import Skill


class PersonException(Exception):
    pass


class Person():

    def __init__(self, name, surname, dateOfBirth, skills =None):
        if skills is None:
            skills = {}
        self.skills = skills
        self.name = name
        self.surname = surname
        self.dateOfBirth = datetime.strptime(dateOfBirth, "%d-%m-%Y")



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

    def defineSkills(self, skills=None, automatic = True):
        if not skills and automatic is True:
            self.skills = {Skill.CHEMISTRY: uniform(0, 1), Skill.BIOLOGY: uniform(0,1), Skill.ENGLISH: uniform(0,1), Skill.HISTORY: uniform(0,1), Skill.MATH: uniform(0,1)}
        elif not skills and automatic is False:
            raise PersonException("Give skills or try automatic")
        else:
            self.skills = skills

    def presentSkills(self):
        print("My skills: \n")
        for k, v in self.skills.items():
            print("{}: {}".format(k.name, v))


